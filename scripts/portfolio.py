#!/usr/bin/env python3
"""Portfolio dashboard: one page showing every MakerLine project and the ideas' outcomes.

Scans folders for docs/product/STATUS.md (including repos under a product workspace's 04_repos/) and writes:
  portfolio/index.html   open in any browser (accessible, light/dark)
  portfolio/PORTFOLIO.md same data as text (AI tools can read it)

Usage:  python3 scripts/portfolio.py                     # scans ~/Projects and ~/Documents
        python3 scripts/portfolio.py ~/Code ~/Work       # scan other folders
"""
import datetime as dt
import html
import pathlib
import re
import sys

KIT = pathlib.Path(__file__).resolve().parent.parent
OUT = KIT / "portfolio"
MAX_DEPTH = 4                 # how deep to look for projects under each folder
STALE_DAYS = 14               # flag projects not updated for this long
SKIP_DIRS = {"node_modules", ".git", ".expo", ".next", "Library", ".Trash"}
WORKSPACE_SKIP = {"90_reference", "98_bin", "99_archive"}


def find_status_files(root: pathlib.Path):
    """Yield docs/product/STATUS.md files up to MAX_DEPTH below root (skipping heavy folders)."""
    root = root.expanduser()
    if not root.exists():
        return
    stack = [(root, 0)]
    while stack:
        folder, depth = stack.pop()
        status = folder / "docs" / "product" / "STATUS.md"
        if status.is_file():
            yield status
            continue  # a project folder: don't look inside it for more projects
        if depth >= MAX_DEPTH:
            continue
        try:
            for child in folder.iterdir():
                if child.is_dir() and child.name not in SKIP_DIRS and not child.name.startswith("."):
                    # A product workspace (new-idea references/workspace.md): its bin, archive and reference
                    # copies aren't projects; 04_repos/ costs no depth, so repos under it are still found.
                    if (folder / "04_repos").is_dir() and child.name in WORKSPACE_SKIP:
                        continue
                    stack.append((child, depth if child.name == "04_repos" else depth + 1))
        except PermissionError:
            pass


def parse_status(path: pathlib.Path) -> dict:
    """Pull the useful fields out of a STATUS.md written from the kit template."""
    text = path.read_text(encoding="utf-8", errors="replace")
    project_dir = path.parent.parent.parent
    head = re.search(r"^# Status — (.*?)\s+·\s+updated\s+(\S+)\s+·\s+kit v(\S+)", text, re.M)
    product = head.group(1).strip() if head else project_dir.name
    if product.startswith("<"):
        product = project_dir.name  # template placeholder not filled in yet
    rows = re.findall(r"^\|\s*(\d+[a-z]?|✦|★)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", text, re.M)
    phases = [(n, name, status) for n, name, status in rows]  # ids like 2a, 7b, ✦ stay strings
    done = sum(1 for _, _, s in phases if s.lower().startswith(("done", "skipped")))
    current = next(((n, name, s) for n, name, s in phases if not s.lower().startswith(("done", "skipped"))), None)
    gate = re.search(r"^Evaluation:\s*(.+?)\s*(<!--|$)", text, re.M)
    writing = re.search(r"^Writing:\s*(.+?)\s*(<!--|$)", text, re.M)
    next_step = re.search(r"^Next step:\s*(.*)$", text, re.M)
    blockers = re.search(r"^Blockers:\s*(.*)$", text, re.M)
    updated = dt.datetime.fromtimestamp(path.stat().st_mtime).date()
    costs_file = path.parent / "COSTS.md"
    cost = re.search(r"^Total to date:\s*(\S+)", costs_file.read_text(), re.M) if costs_file.exists() else None
    return {
        "product": product,
        "path": str(project_dir),
        "kit": head.group(3) if head else "?",
        "gate": gate.group(1) if gate else "unknown",
        "done": done,
        "total": len(phases) or 13,
        "current": f"{current[0]}. {current[1]} — {current[2]}" if current else "All phases done",
        "next": (next_step.group(1).strip() if next_step else "") or "—",
        "blockers": (blockers.group(1).strip() if blockers else "") or "—",
        "updated": updated,
        "stale": (dt.date.today() - updated).days > STALE_DAYS,
        "cost": cost.group(1) if cost else "—",
        "writing": writing.group(1).strip() if writing and writing.group(1).strip() not in ("", "–", "-") else "—",
    }


def outcomes_table() -> str:
    """The outcomes table from portfolio/OUTCOMES.md (markdown), if it has real rows."""
    f = KIT / "portfolio" / "OUTCOMES.md"
    if not f.exists():
        return ""
    rows = [l for l in f.read_text().splitlines() if l.startswith("|") and not re.match(r"^\|\s*(Date|---|\s*\|)", l)]
    return "\n".join(rows)


STALE_BADGE = ' <span class="badge warn">stale</span>'


def render_html(projects, outcomes_md) -> str:
    def esc(x):
        return html.escape(str(x))

    body_rows = "".join(
        f"<tr><th scope='row'>{esc(p['product'])}<br><span class='muted'>{esc(p['path'])}</span></th>"
        f"<td><span class='badge {'ok' if 'APPROVED' in p['gate'] else 'wait'}'>{esc(p['gate'])}</span></td>"
        f"<td><progress value='{p['done']}' max='{p['total']}' aria-label='{p['done']} of {p['total']} phases done'></progress> "
        f"{p['done']}/{p['total']}</td>"
        f"<td>{esc(p['current'])}</td><td>{esc(p['next'])}</td><td>{esc(p['writing'])}</td><td>{esc(p['blockers'])}</td>"
        f"<td>{esc(p['updated'])}{STALE_BADGE if p['stale'] else ''}</td>"
        f"<td>{esc(p['cost'])}</td><td>v{esc(p['kit'])}</td></tr>"
        for p in projects
    ) or "<tr><td colspan='10'>No projects found. Create one with scripts/new-project.sh.</td></tr>"
    outcome_rows = "".join(
        "<tr>" + "".join(f"<td>{esc(c.strip())}</td>" for c in r.strip("|").split("|")) + "</tr>"
        for r in outcomes_md.splitlines()
    ) or "<tr><td colspan='8'>No outcomes logged yet (post-launch adds them).</td></tr>"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Product portfolio</title>
<style>
  :root {{ --bg:#fff; --fg:#16161a; --muted:#5c5c66; --line:#c4c4cc; --ok:#1e7a46; --wait:#8a4b00; --warn:#b42318; color-scheme: light dark; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --bg:#16161a; --fg:#f7f7f8; --muted:#c4c4cc; --line:#5c5c66; --ok:#6fd39a; --wait:#ffc266; --warn:#ff8a80; }} }}
  body {{ background:var(--bg); color:var(--fg); font:16px/1.5 system-ui, sans-serif; margin:0; padding:24px; }}
  h1 {{ margin-top:0 }} .muted {{ color:var(--muted); font-size:13px; font-weight:400 }}
  .wrap {{ overflow-x:auto }} table {{ border-collapse:collapse; width:100%; min-width:900px; margin-bottom:32px }}
  caption {{ text-align:left; font-weight:600; padding:8px 0 }}
  th, td {{ border-bottom:1px solid var(--line); padding:10px 8px; text-align:left; vertical-align:top }}
  .badge {{ border:2px solid currentColor; border-radius:999px; padding:0 8px; font-size:13px; white-space:nowrap }}
  .ok {{ color:var(--ok) }} .wait {{ color:var(--wait) }} .warn {{ color:var(--warn) }}
  :focus-visible {{ outline:3px solid var(--fg); outline-offset:2px }}
</style></head>
<body><main>
<h1>Product portfolio</h1>
<p class="muted">Generated {dt.datetime.now():%Y-%m-%d %H:%M} by scripts/portfolio.py · {len(projects)} project(s)</p>
<div class="wrap" tabindex="0" role="region" aria-label="Projects table, scrolls sideways">
<table><caption>Projects</caption>
<thead><tr><th scope="col">Project</th><th scope="col">Approval gate</th><th scope="col">Progress</th><th scope="col">Current phase</th>
<th scope="col">Next step</th><th scope="col">Writing</th><th scope="col">Blockers</th><th scope="col">Updated</th><th scope="col">Cost to date</th><th scope="col">Kit</th></tr></thead>
<tbody>{body_rows}</tbody></table></div>
<div class="wrap" tabindex="0" role="region" aria-label="Idea outcomes table, scrolls sideways">
<table><caption>Idea outcomes (feeds evaluate-idea calibration)</caption>
<thead><tr><th scope="col">Date</th><th scope="col">Project</th><th scope="col">Verdict at approval</th><th scope="col">Kill criteria</th>
<th scope="col">What happened</th><th scope="col">Metric vs target</th><th scope="col">Total cost</th><th scope="col">Lesson</th></tr></thead>
<tbody>{outcome_rows}</tbody></table></div>
</main></body></html>"""


def render_md(projects) -> str:
    lines = ["# Portfolio", f"_Generated {dt.date.today()}_", "",
             "| Project | Gate | Done | Current phase | Next step | Writing | Updated | Cost | Kit |", "|---|---|---|---|---|---|---|---|---|"]
    for p in projects:
        lines.append(f"| {p['product']} | {p['gate']} | {p['done']}/{p['total']} | {p['current']} | {p['next']} | {p['writing']} | "
                     f"{p['updated']}{' ⚠️ stale' if p['stale'] else ''} | {p['cost']} | v{p['kit']} |")
    return "\n".join(lines) + "\n"


def main():
    roots = [pathlib.Path(a) for a in sys.argv[1:]] or [pathlib.Path("~/Projects"), pathlib.Path("~/Documents")]
    seen, projects = set(), []
    for root in roots:
        for f in find_status_files(root):
            if f.parent.parent.parent == KIT / "template":
                continue  # the kit's own template isn't a project
            key = f.resolve()
            if key not in seen:
                seen.add(key)
                projects.append(parse_status(f))
    projects.sort(key=lambda p: p["updated"], reverse=True)
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(render_html(projects, outcomes_table()), encoding="utf-8")
    (OUT / "PORTFOLIO.md").write_text(render_md(projects), encoding="utf-8")
    print(f"✔ {len(projects)} project(s) → portfolio/index.html and portfolio/PORTFOLIO.md")


if __name__ == "__main__":
    main()
