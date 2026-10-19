#!/usr/bin/env python3
"""Product Kit cockpit: a small local web page that shows your projects and the next prompt to paste.

The chat (Claude, Cursor, Codex) stays the engine. This page only *reads* your projects'
docs/product/ files and tells you what to say next. It never calls an AI API and never
changes a project, except one opt-in action: saving a PITCH.md for a brand-new idea.

Usage:
    python3 scripts/kit-ui.py                          # scans ~/Projects, serves http://127.0.0.1:8765
    python3 scripts/kit-ui.py --projects ~/Code --port 9000
    python3 scripts/kit-ui.py --no-save                # fully read-only: hides the "save PITCH.md" option

Standard library only (no installs). Details: kit-ui/README.md
"""
from __future__ import annotations  # lets the type hints below work on macOS's older Python 3.9

import argparse
import datetime as dt
import html
import http.server
import importlib.util
import pathlib
import re
import secrets
import sys
import urllib.parse

KIT = pathlib.Path(__file__).resolve().parent.parent
STATIC = KIT / "kit-ui"
SKILLS_DIR = KIT / "plugin" / "skills"

# Reuse the portfolio script's folder scan and STATUS.md parsing so the two never disagree
# about approval, next step, blockers or staleness. Its file name has no hyphen, so it can be
# loaded as a module straight from its path.
_spec = importlib.util.spec_from_file_location("portfolio", KIT / "scripts" / "portfolio.py")
portfolio = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(portfolio)

# Only the loopback address. 0.0.0.0 would let anyone on your Wi-Fi read your project docs.
HOST = "127.0.0.1"
MAX_BODY = 20_000          # bytes; the new-idea form is small, so anything bigger is refused
MAX_DOCS = 300             # cap on documents listed per project (keeps huge folders fast)

# Phase id → the skill that runs it. Used for the "or run just this phase" prompt.
PHASE_SKILLS = {
    "1": "new-idea", "2": "evaluate-idea", "2a": "design-direction", "2b": "write-prd",
    "3": "validate-idea", "✦": "start", "★": None, "4": "name-product", "5": "tech-stack",
    "6": "design-system", "7": "write-prd", "7a": "engineering-docs", "—": "tool-plan",
    "7b": "project-setup", "8": "plan-build", "9": "build-feature", "10": "quality-review",
    "11": "test-plan", "12": "ship-checklist", "13": "post-launch",
}
PRE_GATE = {"1", "2", "2a", "2b", "3", "✦"}
SETUP = {"4", "5", "6", "7", "7a", "—", "7b"}
ANYTIME = {"—"}  # the tool-plan row can happen any time, so it never counts as "current"

# Every status a phase can have, with a text label and a shape. Shape + words, never colour
# alone, so the state is clear to colour-blind people and screen-reader users.
STATES = {
    "done": ("Done", "✓"),
    "skipped": ("Skipped", "–"),
    "waiting": ("Waiting for you", "◐"),
    "current": ("Up next", "●"),
    "progress": ("In progress", "●"),
    "todo": ("Not started", "○"),
}


# ---------------------------------------------------------------- reading projects

def esc(value) -> str:
    """Escape text for HTML. Every piece of file content goes through this before it is shown."""
    return html.escape(str(value), quote=True)


def kind_of(status: str) -> str:
    s = status.strip().lower()
    if s.startswith("done"):
        return "done"
    if s.startswith("skipped"):
        return "skipped"
    if s.startswith("waiting"):
        return "waiting"
    if s.startswith("in progress"):
        return "progress"
    return "todo"


ROW_RE = re.compile(r"^\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|", re.M)


def parse_phases(text: str, approved: bool) -> list:
    """All phase rows, including 2a, 2b, ✦, 7a, 7b (portfolio.py only reads numeric ids).

    STATUS.md has no ★ row (approval is the `Evaluation:` line), so one is added after ✦
    to make the gate visible on the timeline.
    """
    phases = []
    for pid, name, status, date, notes in ROW_RE.findall(text):
        if pid in ("#", "") or set(pid) <= {"-", ":"}:
            continue  # header or divider row
        phases.append({"id": pid, "name": name, "status": status or "Not started",
                       "kind": kind_of(status), "date": date, "notes": notes})
    if phases:
        gate = {"id": "★", "name": "Approval (only you can approve)", "status": "Approved" if approved else "Pending",
                "kind": "done" if approved else "waiting", "date": "", "notes": "Evaluation line in STATUS.md"}
        ids = [p["id"] for p in phases]
        after = ids.index("✦") + 1 if "✦" in ids else next((i for i, p in enumerate(ids) if p == "4"), len(ids))
        phases.insert(after, gate)
    # Mark the one phase to work on next. A gate that isn't approved stops everything after it.
    for p in phases:
        if p["id"] in ANYTIME:
            continue
        if p["id"] == "★" and not approved:
            if not any(q["kind"] in ("todo", "progress") for q in phases if q["id"] in PRE_GATE):
                p["kind"] = "current"  # Idea Pack is finished: the next move is the owner's decision
                p["focus"] = True
            break  # nothing after an unapproved gate can be "up next"
        if p["kind"] in ("todo", "progress"):
            if p["kind"] == "todo":
                p["kind"] = "current"
            p["focus"] = True
            break
    return phases


def scan(root: pathlib.Path) -> list:
    """Every project under root that has docs/product/STATUS.md, newest first."""
    projects, seen = [], set()
    for status in portfolio.find_status_files(root):
        real = status.resolve()
        # A symlinked folder could point outside the projects folder; skip anything that does.
        if real in seen or not real.is_relative_to(root):
            continue
        seen.add(real)
        projects.append(load_project(root, real))
    projects.sort(key=lambda p: p["updated"], reverse=True)
    return projects


def load_project(root: pathlib.Path, status: pathlib.Path) -> dict:
    info = portfolio.parse_status(status)  # gate, next, blockers, updated, stale, cost, kit
    text = status.read_text(encoding="utf-8", errors="replace")
    approved = info["gate"].upper().startswith("APPROVED")
    phases = parse_phases(text, approved)
    project_dir = status.parent.parent.parent
    focus = next((p for p in phases if p.get("focus")), None)
    counted = [p for p in phases if p["id"] not in ANYTIME]
    return {
        **info,
        "id": project_dir.relative_to(root).as_posix(),
        "dir": project_dir,
        "approved": approved,
        "phases": phases,
        "focus": focus,
        "done_count": sum(1 for p in counted if p["kind"] in ("done", "skipped")),
        "total_count": len(counted),
        "waiting": [p for p in phases if p["kind"] == "waiting" and p["id"] != "★"],
        "age": (dt.date.today() - info["updated"]).days,
    }


def safe_path(base: pathlib.Path, rel: str) -> pathlib.Path | None:
    """Resolve rel inside base, or None if it would escape (../, absolute paths, symlinks out)."""
    if not rel or "\x00" in rel:
        return None
    candidate = (base / rel).resolve()
    return candidate if candidate.is_relative_to(base) else None


def find_project(root: pathlib.Path, pid: str):
    """Look a project up by its id (folder path relative to --projects). None = refused."""
    folder = safe_path(root, pid)
    if folder is None:
        return "forbidden"
    status = folder / "docs" / "product" / "STATUS.md"
    if not status.is_file():
        return None
    return load_project(root, status.resolve())


def list_docs(project: dict) -> list:
    docs_dir = project["dir"] / "docs"
    found = []
    for f in sorted(docs_dir.rglob("*.md")):
        if any(part.startswith(".") or part == "node_modules" for part in f.relative_to(docs_dir).parts):
            continue
        if not f.resolve().is_relative_to(project["dir"]):
            continue
        found.append(f.relative_to(project["dir"]).as_posix())
        if len(found) >= MAX_DOCS:
            break
    # docs/product first (the kit's files), then everything else.
    return sorted(found, key=lambda p: (not p.startswith("docs/product/"), p.count("/"), p))


def read_skills() -> list:
    skills = []
    for f in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^description:\s*(.+)$", text, re.M)
        desc = m.group(1).strip().strip('"') if m else ""
        first = re.split(r"(?<=[.!?])\s", desc, maxsplit=1)[0]
        skills.append({"name": f.parent.name, "summary": first})
    return skills


# ---------------------------------------------------------------- the "run next" logic

def run_next(project: dict) -> dict:
    """What to paste into Claude next, worked out from the phase table and the approval line."""
    phases, approved = project["phases"], project["approved"]
    open_ids = {p["id"] for p in phases if p["kind"] in ("todo", "current", "progress")}
    focus = project["focus"]
    focus_name = f"{focus['id']} · {focus['name']}" if focus else "nothing left"
    extra = []
    if focus and PHASE_SKILLS.get(focus["id"]) and focus["id"] not in ("✦",):
        extra.append({"label": f"Or run just this phase ({focus['name']})",
                      "text": f"/product-kit:{PHASE_SKILLS[focus['id']]}", "kind": "prompt"})

    if not any(p["kind"] != "current" and p["kind"] != "todo" for p in phases if p["id"] != "★"):
        return {"title": "Start the Idea Pack", "why": "Nothing has run yet. Describe the idea in a sentence or two.",
                "primary": {"label": "Prompt to paste into Claude",
                            "text": "/product-kit:start <describe your idea in one or two sentences> — give me everything",
                            "kind": "prompt"},
                "extra": [], "focus": focus_name}
    if not approved:
        if open_ids & (PRE_GATE - {"3"}):
            return {"title": "Continue the Idea Pack", "why": f"Next up: {focus_name}.",
                    "primary": {"label": "Prompt to paste into Claude", "text": "/product-kit:start — continue", "kind": "prompt"},
                    "extra": extra, "focus": focus_name}
        more = []
        if "3" in open_ids:
            more.append({"label": "Optional, recommended first: test demand with real people",
                         "text": "/product-kit:validate-idea", "kind": "prompt"})
        return {"title": "Your decision: approve, change or park",
                "why": "The Idea Pack is ready. Read ONE_PAGER.md, then decide. Claude can't approve for you — "
                       "that's on purpose. To approve, run this in Terminal inside the project folder:",
                "primary": {"label": "Command to run in Terminal (not in Claude)", "text": "scripts/approve.sh",
                            "kind": "command"},
                "extra": more, "focus": focus_name}
    if open_ids & SETUP:
        all_fresh = all(p["kind"] in ("todo", "current") for p in phases if p["id"] in SETUP)
        text = "/product-kit:start — set it all up" if all_fresh else "/product-kit:start — continue"
        return {"title": "Set it all up", "why": f"Approved. Next up: {focus_name}. Have your name, stack and visual picks ready.",
                "primary": {"label": "Prompt to paste into Claude", "text": text, "kind": "prompt"},
                "extra": extra, "focus": focus_name}
    if open_ids & {"8", "9"}:
        return {"title": "Build it", "why": f"Next up: {focus_name}. One task per session.",
                "primary": {"label": "Prompt to paste into Claude", "text": "/product-kit:start — build it", "kind": "prompt"},
                "extra": extra, "focus": focus_name}
    for pid in ("10", "11", "12"):
        if pid in open_ids:
            return {"title": f"Next: {focus_name}", "why": "Run this in Claude Code, Cursor or Codex inside the project.",
                    "primary": {"label": "Prompt to paste into Claude",
                                "text": f"/product-kit:{PHASE_SKILLS[pid]}", "kind": "prompt"},
                    "extra": [], "focus": focus_name}
    return {"title": "Launched — keep learning", "why": "Every phase is done. Review metrics and feedback weekly.",
            "primary": {"label": "Prompt to paste into Claude", "text": "/product-kit:post-launch", "kind": "prompt"},
            "extra": [], "focus": focus_name}


# ---------------------------------------------------------------- tiny safe markdown → HTML

INLINE_RE = re.compile(
    r"`([^`]+)`"                              # 1 inline code
    r"|\[([^\]]+)\]\(([^)\s]+)\)"             # 2,3 link
    r"|\*\*([^*]+)\*\*"                       # 4 bold
    r"|(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])"  # 5 italic
)


def inline(text: str, link_fn) -> str:
    """Inline markdown. Each piece of text is escaped on its own, so no file can inject HTML."""
    out, pos = [], 0
    for m in INLINE_RE.finditer(text):
        out.append(esc(text[pos:m.start()]))
        if m.group(1) is not None:
            out.append(f"<code>{esc(m.group(1))}</code>")
        elif m.group(2) is not None:
            href = link_fn(m.group(3))
            label = inline(m.group(2), lambda u: None)
            if href:
                rel = ' rel="noopener noreferrer"' if href.startswith("http") else ""
                out.append(f'<a href="{esc(href)}"{rel}>{label}</a>')
            else:
                out.append(f"{label} <span class=\"muted\">({esc(m.group(3))})</span>")
        elif m.group(4) is not None:
            out.append(f"<strong>{inline(m.group(4), link_fn)}</strong>")
        else:
            out.append(f"<em>{inline(m.group(5), link_fn)}</em>")
        pos = m.end()
    out.append(esc(text[pos:]))
    return "".join(out)


def split_row(line: str) -> list:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def md_to_html(text: str, link_fn) -> str:
    """A deliberately small markdown renderer: headings, paragraphs, lists, quotes, tables, code.

    Raw HTML inside a markdown file is never passed through; it's shown as text. HTML comments
    are dropped because they're notes for AI tools, not for reading.
    """
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = text.splitlines()
    out, para, i = [], [], 0

    def flush():
        if para:
            out.append(f"<p>{inline(' '.join(para), link_fn)}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            out.append('<pre tabindex="0"><code>' + esc("\n".join(code)) + "</code></pre>")
            i += 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*?)\s*#*$", stripped)
        if h:
            flush()
            level = min(len(h.group(1)) + 1, 6)  # the page already has its one h1 (the file name)
            out.append(f"<h{level}>{inline(h.group(2), link_fn)}</h{level}>")
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-{2,}", lines[i + 1].strip()):
            flush()
            head = split_row(stripped)
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(split_row(lines[i]))
                i += 1
            ths = "".join(f'<th scope="col">{inline(c, link_fn)}</th>' for c in head)
            trs = "".join("<tr>" + "".join(f"<td>{inline(c, link_fn)}</td>" for c in r) + "</tr>" for r in body)
            out.append('<div class="scroll" tabindex="0" role="region" aria-label="Table, scrolls sideways">'
                       f"<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>")
            continue
        li = re.match(r"^\s*([-*+]|\d+[.)])\s+(.*)$", line)
        if li:
            flush()
            tag = "ol" if li.group(1)[0].isdigit() else "ul"
            items = []
            while i < len(lines):
                m = re.match(r"^\s*([-*+]|\d+[.)])\s+(.*)$", lines[i])
                if m:
                    items.append(m.group(2))
                elif lines[i].startswith(("  ", "\t")) and lines[i].strip() and items:
                    items[-1] += " " + lines[i].strip()  # wrapped continuation line
                else:
                    break
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(t, link_fn)}</li>" for t in items) + f"</{tag}>")
            continue
        if stripped.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(f"<blockquote><p>{inline(' '.join(quote), link_fn)}</p></blockquote>")
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush()
            out.append("<hr>")
        elif not stripped:
            flush()
        else:
            para.append(stripped)
        i += 1
    flush()
    return "\n".join(out)


# ---------------------------------------------------------------- page building

def layout(title: str, body: str, active: str = "") -> str:
    def nav(href, label, key):
        current = ' aria-current="page"' if key == active else ""
        return f'<li><a href="{href}"{current}>{label}</a></li>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{esc(title)} · Product Kit</title>
<link rel="stylesheet" href="/app.css">
<script src="/app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="top-inner">
    <a class="brand" href="/"><span class="brand-mark" aria-hidden="true">◆</span> Product Kit <span class="brand-sub">cockpit</span></a>
    <nav aria-label="Main">
      <ul>{nav("/", "Projects", "projects")}{nav("/new", "New idea", "new")}{nav("/skills", "Skills", "skills")}</ul>
    </nav>
  </div>
</header>
<main id="main" tabindex="-1">
{body}
</main>
<footer class="foot"><p>Runs only on this computer (127.0.0.1). Reads your files; the chat does the work.</p></footer>
<div id="live" class="sr-only" aria-live="polite" aria-atomic="true"></div>
</body>
</html>"""


def copy_box(cid: str, label: str, text: str, kind: str = "prompt") -> str:
    """A labelled read-only field + Copy button. Works without JavaScript (select and copy)."""
    rows = max(1, min(6, text.count("\n") + 1 + len(text) // 70))
    return f"""<div class="copy copy--{esc(kind)}">
  <label for="{cid}">{esc(label)}</label>
  <div class="copy-row">
    <textarea id="{cid}" readonly rows="{rows}" spellcheck="false">{esc(text)}</textarea>
    <button type="button" class="btn btn--primary js-only" data-copy="{cid}">Copy</button>
  </div>
</div>"""


def gate_badge(p: dict) -> str:
    if p["approved"]:
        return '<span class="badge badge--ok"><span aria-hidden="true">✓</span> Approved</span>'
    return f'<span class="badge badge--wait"><span aria-hidden="true">◐</span> Not approved ({esc(p["gate"])})</span>'


def age_text(p: dict) -> str:
    days = p["age"]
    words = "today" if days <= 0 else ("yesterday" if days == 1 else f"{days} days ago")
    stale = ' <span class="badge badge--warn"><span aria-hidden="true">!</span> Stale</span>' if p["stale"] else ""
    return f'<time datetime="{p["updated"].isoformat()}">{esc(p["updated"])}</time> · {words}{stale}'


def progress(p: dict) -> str:
    return (f'<div class="meter"><progress value="{p["done_count"]}" max="{p["total_count"]}" '
            f'aria-label="{p["done_count"]} of {p["total_count"]} phases done or skipped"></progress>'
            f'<span>{p["done_count"]}/{p["total_count"]} phases</span></div>')


def page_projects(root: pathlib.Path, projects: list) -> str:
    if not projects:
        body = f"""<h1>Projects</h1>
<div class="empty"><p>No projects found in <code>{esc(root)}</code>.</p>
<p>A project is any folder with <code>docs/product/STATUS.md</code>. Start one from <a href="/new">New idea</a>,
or point this page at another folder: <code>python3 scripts/kit-ui.py --projects ~/Code</code>.</p></div>"""
        return layout("Projects", body, "projects")
    waiting = sum(1 for p in projects if not p["approved"] and p["focus"] and p["focus"]["id"] == "★")
    stale = sum(1 for p in projects if p["stale"])
    summary = [f"{len(projects)} project{'s' if len(projects) != 1 else ''}"]
    if waiting:
        summary.append(f"{waiting} waiting for your approval")
    if stale:
        summary.append(f"{stale} stale (no update in {portfolio.STALE_DAYS}+ days)")
    cards = []
    for p in projects:
        q = urllib.parse.quote(p["id"])
        focus = f'{esc(p["focus"]["id"])} · {esc(p["focus"]["name"])}' if p["focus"] else "All phases done"
        cards.append(f"""<li class="card">
  <h2><a href="/project?id={q}">{esc(p["product"])}</a></h2>
  <p class="muted path">{esc(p["id"])}</p>
  {progress(p)}
  <dl>
    <div><dt>Current phase</dt><dd>{focus}</dd></div>
    <div><dt>Approval</dt><dd>{gate_badge(p)}</dd></div>
    <div><dt>Next step</dt><dd>{esc(p["next"])}</dd></div>
    <div><dt>Last updated</dt><dd>{age_text(p)}</dd></div>
  </dl>
</li>""")
    body = f"""<h1>Projects</h1>
<p class="lede">{esc(" · ".join(summary))}. Scanning <code>{esc(root)}</code>.</p>
<ul class="cards" role="list">{"".join(cards)}</ul>"""
    return layout("Projects", body, "projects")


def page_project(p: dict) -> str:
    q = urllib.parse.quote(p["id"])
    nxt = run_next(p)
    steps = []
    for ph in p["phases"]:
        label, icon = STATES[ph["kind"]]
        cur = ' aria-current="step"' if ph.get("focus") else ""
        meta = " · ".join(x for x in (esc(ph["date"]), inline(ph["notes"], lambda u: None)) if x)
        steps.append(f"""<li class="step step--{ph['kind']}"{cur}>
  <span class="step-icon" aria-hidden="true">{icon}</span>
  <div class="step-body"><p class="step-title"><span class="step-id">{esc(ph["id"])}</span> {esc(ph["name"])}
  <span class="step-state">{label}</span></p>{f'<p class="step-meta">{meta}</p>' if meta else ""}</div>
</li>""")
    timeline = (f'<ol class="timeline">{"".join(steps)}</ol>' if steps
                else '<p class="empty">No phase table found in STATUS.md.</p>')

    docs = list_docs(p)
    doc_items = "".join(
        f'<li><a href="/doc?id={q}&amp;file={urllib.parse.quote(d)}">{esc(d.removeprefix("docs/product/"))}</a></li>'
        for d in docs) or "<li>No markdown documents yet.</li>"

    extras = "".join(copy_box(f"extra-{i}", e["label"], e["text"], e["kind"]) for i, e in enumerate(nxt["extra"]))
    waiting = ""
    if p["waiting"]:
        names = ", ".join(f'{w["id"]} {w["name"]}' for w in p["waiting"])
        waiting = f'<p class="note"><span aria-hidden="true">◐</span> Waiting for your review: {esc(names)}.</p>'
    body = f"""<p class="crumbs"><a href="/">Projects</a> <span aria-hidden="true">/</span> {esc(p["product"])}</p>
<h1>{esc(p["product"])}</h1>
<p class="lede">{gate_badge(p)} · updated {age_text(p)} · kit v{esc(p["kit"])}</p>
<div class="detail">
  <section class="panel run" aria-labelledby="run-h">
    <h2 id="run-h">Run next</h2>
    <p class="run-title">{esc(nxt["title"])}</p>
    <p>{esc(nxt["why"])}</p>
    {copy_box("open-folder", "1. Open Claude (Code, Cursor or Codex) in this folder", str(p["dir"]), "path")}
    {copy_box("next-prompt", "2. " + nxt["primary"]["label"], nxt["primary"]["text"], nxt["primary"]["kind"])}
    {extras}
    {waiting}
    <dl class="facts">
      <div><dt>Next step (from STATUS.md)</dt><dd>{esc(p["next"])}</dd></div>
      <div><dt>Blockers</dt><dd>{esc(p["blockers"])}</dd></div>
      <div><dt>Cost to date</dt><dd>{esc(p["cost"])}</dd></div>
    </dl>
  </section>
  <section class="panel" aria-labelledby="tl-h">
    <h2 id="tl-h">Phases</h2>
    {progress(p)}
    {timeline}
  </section>
  <section class="panel" aria-labelledby="docs-h">
    <h2 id="docs-h">Documents</h2>
    <ul class="doclist">{doc_items}</ul>
  </section>
</div>"""
    return layout(p["product"], body, "projects")


def page_doc(p: dict, rel: str, path: pathlib.Path) -> str:
    q = urllib.parse.quote(p["id"])
    base_dir = path.parent

    def link_fn(url: str):
        if re.match(r"^https?://", url, re.I):
            return url
        if re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I) or url.startswith(("//", "#")):
            return None  # other schemes (javascript:, data:, file:) are never linked
        # Relative links to other .md files in the same project open in this viewer; anything
        # pointing outside the project is shown as plain text instead of a link.
        target = (base_dir / url.split("#", 1)[0]).resolve()
        if target.suffix.lower() != ".md" or not target.is_relative_to(p["dir"]):
            return None
        return f"/doc?id={q}&file={urllib.parse.quote(target.relative_to(p['dir']).as_posix())}"

    rendered = md_to_html(path.read_text(encoding="utf-8", errors="replace"), link_fn)
    body = f"""<p class="crumbs"><a href="/">Projects</a> <span aria-hidden="true">/</span>
<a href="/project?id={q}">{esc(p["product"])}</a> <span aria-hidden="true">/</span> {esc(rel)}</p>
<h1>{esc(path.name)}</h1>
<p class="muted">{esc(rel)} · read-only view. Edit it in your editor or ask Claude.</p>
<article class="doc panel">{rendered}</article>"""
    return layout(path.name, body, "projects")


DEPTHS = {"quick": "Quick", "standard": "Standard", "deep": "Deep"}
PLATFORMS = ["Web", "iOS", "Android", "macOS", "Not sure yet"]
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,59}$")


def build_idea_prompt(form: dict, saved_rel: str | None = None) -> str:
    depth = form.get("depth", "standard")
    bits = []
    if saved_rel:
        bits.append(f"/product-kit:start — my idea is in {saved_rel}/docs/product/PITCH.md — give me everything")
    else:
        bits.append(f"/product-kit:start {form.get('pitch', '').strip()} — give me everything")
    if depth in ("quick", "deep"):
        bits[0] += f" ({depth})"
    if form.get("markets", "").strip():
        bits.append(f"Launch markets: {form['markets'].strip()}.")
    if form.get("platforms"):
        bits.append(f"Platforms: {', '.join(form['platforms'])}.")
    return "\n".join(bits)


def page_new(form: dict, errors: dict, result: dict, token: str, can_save: bool) -> str:
    def err(name):
        return f'<p class="field-error" id="{name}-err"><span aria-hidden="true">!</span> {esc(errors[name])}</p>' if name in errors else ""

    def described(name, hint_id=None):
        ids = [x for x in (hint_id, f"{name}-err" if name in errors else None) if x]
        inv = ' aria-invalid="true"' if name in errors else ""
        return (f' aria-describedby="{" ".join(ids)}"' if ids else "") + inv

    summary = ""
    if errors:
        items = "".join(f'<li><a href="#{k}">{esc(v)}</a></li>' for k, v in errors.items())
        summary = f'<div class="error-summary" role="alert" tabindex="-1" id="error-summary"><h2>Please fix {len(errors)} thing{"s" if len(errors) > 1 else ""}</h2><ul>{items}</ul></div>'
    depth = form.get("depth", "standard")
    radios = "".join(
        f'<label class="choice"><input type="radio" name="depth" value="{k}"{" checked" if k == depth else ""}> '
        f'<span><strong>{v}</strong> <span class="muted">{hint}</span></span></label>'
        for (k, v), hint in zip(DEPTHS.items(), ("first look, ~50–70k tokens", "recommended default", "more research, more tokens")))
    chosen = form.get("platforms", [])
    boxes = "".join(
        f'<label class="choice"><input type="checkbox" name="platforms" value="{esc(x)}"{" checked" if x in chosen else ""}> {esc(x)}</label>'
        for x in PLATFORMS)
    save_block = ""
    if can_save:
        save_block = f"""<fieldset>
  <legend>Save (optional)</legend>
  <label class="choice"><input type="checkbox" name="save" value="yes"{" checked" if form.get("save") else ""}
    aria-describedby="save-hint"> Save PITCH.md into a new project folder</label>
  <p class="hint" id="save-hint">Off by default. Writes only <code>&lt;folder&gt;/docs/product/PITCH.md</code> inside your projects folder, and never overwrites.</p>
  <label for="folder">Folder name <span class="muted">(only if saving)</span></label>
  <p class="hint" id="folder-hint">Lowercase letters, numbers and dashes, e.g. <code>plant-swap</code>.</p>
  <input id="folder" name="folder" type="text" autocomplete="off" value="{esc(form.get("folder", ""))}"{described("folder", "folder-hint")}>
  {err("folder")}
</fieldset>"""
    out = ""
    if result:
        saved = f'<p class="note note--ok"><span aria-hidden="true">✓</span> Saved {esc(result["saved"])}</p>' if result.get("saved") else ""
        out = f"""<section class="panel run" aria-labelledby="out-h" id="result" tabindex="-1">
  <h2 id="out-h">Your prompt is ready</h2>
  {saved}
  {copy_box("idea-prompt", "Prompt to paste into Claude", result["prompt"])}
  <p class="hint">Nothing was sent anywhere. Paste this in Claude Code (or Cursor/Codex) opened in the project folder.</p>
</section>"""
    body = f"""<h1>New idea</h1>
<p class="lede">Fill this in and get the exact prompt to start the Idea Pack. This page doesn't call any AI.</p>
{summary}
{out}
<form class="panel form" method="post" action="/new" novalidate>
  <input type="hidden" name="token" value="{esc(token)}">
  <label for="pitch">Your idea, in a sentence or two</label>
  <p class="hint" id="pitch-hint">Who it's for and what problem it solves. Plain words are fine.</p>
  <textarea id="pitch" name="pitch" rows="4"{described("pitch", "pitch-hint")}>{esc(form.get("pitch", ""))}</textarea>
  {err("pitch")}
  <fieldset><legend>Depth</legend>{radios}</fieldset>
  <label for="markets">Launch markets</label>
  <p class="hint" id="markets-hint">Countries or regions, e.g. India, Canada. Sets which accessibility laws apply.</p>
  <input id="markets" name="markets" type="text" autocomplete="off" value="{esc(form.get("markets", ""))}"{described("markets", "markets-hint")}>
  {err("markets")}
  <fieldset><legend>Platforms</legend>{boxes}</fieldset>
  {save_block}
  <button type="submit" class="btn btn--primary">Make my prompt</button>
</form>"""
    return layout("New idea", body, "new")


def page_skills(skills: list) -> str:
    rows = "".join(
        f'<li class="skill"><h2><code>/product-kit:{esc(s["name"])}</code></h2><p>{esc(s["summary"])}</p></li>'
        for s in skills) or "<li>No skills found in plugin/skills.</li>"
    body = f"""<h1>Skills</h1>
<p class="lede">{len(skills)} skills in <code>plugin/skills</code>. Type any of these in Claude. Most people only need <code>/product-kit:start</code>.</p>
<ul class="skills" role="list">{rows}</ul>"""
    return layout("Skills", body, "skills")


def page_error(code: int, message: str) -> str:
    return layout(f"{code}", f'<h1>{code}</h1><p class="lede">{esc(message)}</p><p><a href="/">Back to projects</a></p>')


# ---------------------------------------------------------------- the server

def make_handler(root: pathlib.Path, port: int, can_save: bool):
    token = secrets.token_urlsafe(24)  # stops other web pages from submitting the form (CSRF)
    allowed_hosts = {f"127.0.0.1:{port}", f"localhost:{port}"}

    class Handler(http.server.BaseHTTPRequestHandler):
        server_version = "kit-ui"
        sys_version = ""

        def send(self, code: int, body: str | bytes, ctype: str = "text/html; charset=utf-8"):
            data = body.encode("utf-8") if isinstance(body, str) else body
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            # The browser may only load our own files: no CDNs, no inline scripts, no frames.
            self.send_header("Content-Security-Policy",
                             "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; "
                             "form-action 'self'; frame-ancestors 'none'; base-uri 'none'; object-src 'none'")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(data)

        def host_ok(self) -> bool:
            # A web page elsewhere can't trick the browser into reading this server through
            # another domain name (a "DNS rebinding" attack) because only these hosts are accepted.
            return self.headers.get("Host", "") in allowed_hosts

        def do_HEAD(self):
            self.do_GET()

        def do_GET(self):
            if not self.host_ok():
                return self.send(403, page_error(403, "Wrong host. Open http://127.0.0.1:%d/" % port))
            url = urllib.parse.urlsplit(self.path)
            qs = urllib.parse.parse_qs(url.query)
            route = url.path
            try:
                if route == "/":
                    return self.send(200, page_projects(root, scan(root)))
                if route in ("/app.css", "/app.js"):
                    ctype = "text/css; charset=utf-8" if route.endswith(".css") else "text/javascript; charset=utf-8"
                    return self.send(200, (STATIC / route[1:]).read_bytes(), ctype)
                if route == "/project":
                    p = find_project(root, qs.get("id", [""])[0])
                    if p == "forbidden":
                        return self.send(403, page_error(403, "That folder is outside your projects folder."))
                    if p is None:
                        return self.send(404, page_error(404, "No project with a docs/product/STATUS.md there."))
                    return self.send(200, page_project(p))
                if route == "/doc":
                    p = find_project(root, qs.get("id", [""])[0])
                    if p == "forbidden":
                        return self.send(403, page_error(403, "That folder is outside your projects folder."))
                    if p is None:
                        return self.send(404, page_error(404, "Project not found."))
                    rel = qs.get("file", [""])[0]
                    path = safe_path(p["dir"], rel)
                    if path is None:
                        return self.send(403, page_error(403, "That file is outside the project."))
                    if path.suffix.lower() != ".md" or not path.is_file():
                        return self.send(404, page_error(404, "Only markdown documents inside the project can be shown."))
                    return self.send(200, page_doc(p, path.relative_to(p["dir"]).as_posix(), path))
                if route == "/new":
                    return self.send(200, page_new({"depth": "standard"}, {}, {}, token, can_save))
                if route == "/skills":
                    return self.send(200, page_skills(read_skills()))
                return self.send(404, page_error(404, "Page not found."))
            except Exception as exc:  # show a calm error page instead of a dropped connection
                self.log_error("error: %r", exc)
                return self.send(500, page_error(500, "Something went wrong reading that. Details are in the terminal."))

        def do_POST(self):
            if not self.host_ok():
                return self.send(403, page_error(403, "Wrong host."))
            if urllib.parse.urlsplit(self.path).path != "/new":
                return self.send(404, page_error(404, "Page not found."))
            origin = self.headers.get("Origin")
            if origin and origin.removeprefix("http://") not in allowed_hosts:
                return self.send(403, page_error(403, "Form came from another site."))
            length = int(self.headers.get("Content-Length") or 0)
            if length > MAX_BODY:
                return self.send(413, page_error(413, "That's too long."))
            data = urllib.parse.parse_qs(self.rfile.read(length).decode("utf-8", "replace"))
            if not secrets.compare_digest(data.get("token", [""])[0], token):
                return self.send(403, page_error(403, "This form expired. Reload the New idea page and try again."))
            form = {
                "pitch": data.get("pitch", [""])[0].strip(),
                "depth": data.get("depth", ["standard"])[0] if data.get("depth", [""])[0] in DEPTHS else "standard",
                "markets": data.get("markets", [""])[0].strip(),
                "platforms": [x for x in data.get("platforms", []) if x in PLATFORMS],
                "save": can_save and data.get("save", [""])[0] == "yes",
                "folder": data.get("folder", [""])[0].strip(),
            }
            errors = {}
            if len(form["pitch"]) < 10:
                errors["pitch"] = "Describe your idea in at least a short sentence (10+ characters)."
            elif len(form["pitch"]) > 2000:
                errors["pitch"] = "Keep the pitch under 2,000 characters; Claude will ask for detail."
            if len(form["markets"]) > 200:
                errors["markets"] = "Keep launch markets under 200 characters."
            target = None
            if form["save"]:
                if not SLUG_RE.match(form["folder"]):
                    errors["folder"] = "Folder name: lowercase letters, numbers and dashes only, starting with a letter or number."
                else:
                    target = safe_path(root, form["folder"])
                    if target is None:
                        errors["folder"] = "That folder would be outside your projects folder."
                    elif (target / "docs" / "product" / "PITCH.md").exists():
                        errors["folder"] = "That folder already has a PITCH.md. Pick another name (nothing is overwritten)."
            if errors:
                return self.send(400, page_new(form, errors, {}, token, can_save))
            result = {}
            if target is not None:
                pitch_file = target / "docs" / "product" / "PITCH.md"
                pitch_file.parent.mkdir(parents=True, exist_ok=True)
                pitch_file.write_text(
                    f"# Pitch\n\n_Saved {dt.date.today()} from the Product Kit cockpit._\n\n{form['pitch']}\n\n"
                    f"- Depth: {DEPTHS[form['depth']]}\n- Launch markets: {form['markets'] or 'not set'}\n"
                    f"- Platforms: {', '.join(form['platforms']) or 'not set'}\n", encoding="utf-8")
                result["saved"] = pitch_file.relative_to(root).as_posix()
                result["prompt"] = build_idea_prompt(form, form["folder"])
            else:
                result["prompt"] = build_idea_prompt(form)
            return self.send(200, page_new(form, {}, result, token, can_save))

        def log_message(self, fmt, *args):
            sys.stderr.write("kit-ui: " + (fmt % args) + "\n")

    return Handler


def main():
    ap = argparse.ArgumentParser(description="Local Product Kit cockpit (read-only by default).")
    ap.add_argument("--projects", default="~/Projects", help="folder that holds your projects (default ~/Projects)")
    ap.add_argument("--port", type=int, default=8765, help="port on 127.0.0.1 (default 8765)")
    ap.add_argument("--no-save", action="store_true", help="hide the 'save PITCH.md' option: never write anything")
    args = ap.parse_args()
    root = pathlib.Path(args.projects).expanduser().resolve()
    if not root.is_dir():
        sys.exit(f"Projects folder not found: {root}  (use --projects <folder>)")
    server = http.server.ThreadingHTTPServer((HOST, args.port), make_handler(root, args.port, not args.no_save))
    print(f"Product Kit cockpit → http://{HOST}:{args.port}/   (projects: {root})  ·  Ctrl+C to stop", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
