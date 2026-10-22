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
import json
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
    gate = re.search(r"^Evaluation:[ \t]*(.+?)[ \t]*(<!--|$)", text, re.M)
    writing = re.search(r"^Writing:[ \t]*(.+?)[ \t]*(<!--|$)", text, re.M)
    next_step = re.search(r"^Next step:[ \t]*(.*)$", text, re.M)  # [ \t], not \s: an empty field must not swallow the next line
    blockers = re.search(r"^Blockers:[ \t]*(.*)$", text, re.M)
    updated = dt.datetime.fromtimestamp(path.stat().st_mtime).date()
    costs_file = path.parent / "COSTS.md"
    cost = re.search(r"^Total to date:\s*(\S+)", costs_file.read_text(), re.M) if costs_file.exists() else None
    return {
        "what": one_liner(path.parent),
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


def one_liner(docs: pathlib.Path) -> str:
    """What the product is, in one line: ONE_PAGER's "idea in one line", else the opportunity review's overview."""
    pager = docs / "ONE_PAGER.md"
    if pager.is_file():
        m = re.search(r"^\*\*The idea in one line\.\*\*\s*(.+)$", pager.read_text(encoding="utf-8", errors="replace"), re.M)
        if m and "{{" not in m.group(1):
            return m.group(1).strip()
    review = docs / "opportunity" / "REVIEW.json"
    if review.is_file():
        try:
            what = (json.loads(review.read_text(encoding="utf-8")).get("overview") or {}).get("what", "")
            return what.strip() if isinstance(what, str) else ""
        except (ValueError, AttributeError):
            return ""
    return ""


def outcomes_table() -> str:
    """The outcomes table from portfolio/OUTCOMES.md (markdown), if it has real rows."""
    f = KIT / "portfolio" / "OUTCOMES.md"
    if not f.exists():
        return ""
    rows = [l for l in f.read_text().splitlines() if l.startswith("|") and not re.match(r"^\|\s*(Date|---|\s*\|)", l)]
    return "\n".join(rows)


STALE_BADGE = ' <span class="badge warn">stale</span>'
BADGE_STALE = "<span class='badge warn'>stale</span>"
BADGE_BLOCKED = "<span class='badge warn'>blocked</span>"
WHAT_LINE = "<p class='what'>{}</p>"

# Brand: docs/kit/brand/README.md. Every text pair ≥ 4.5:1 and every meaningful graphic ≥ 3:1 in both themes.
PORTFOLIO_CSS = """
:root{--paper:#F6F8FB;--surface:#FFFFFF;--ink:#0F1E33;--muted:#475569;--line:#D5DCE6;--control:#7A869A;--accent:#2337B0;--accent-ink:#FFFFFF;
--tint:#E9EEFC;--ok:#14653F;--ok-tint:#E2F2E9;--wait:#8A4B00;--wait-tint:#FFF3DA;--warn:#B42318;--warn-tint:#FDECEA;--focus:#2337B0;
--shadow:0 18px 40px -24px rgba(15,30,51,.35);--body:"Atkinson Hyperlegible Next","Atkinson Hyperlegible",system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans",sans-serif;
--head:"Bricolage Grotesque",var(--body);--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#0D1522;--surface:#142033;--ink:#E8EEF6;--muted:#A8B5C7;--line:#2B3A51;--control:#7D8AA0;
--accent:#A3B6FF;--accent-ink:#0D1522;--tint:#1B2747;--ok:#7AD9A8;--ok-tint:#123124;--wait:#FFC266;--wait-tint:#2E2410;--warn:#FF9A8F;--warn-tint:#3A1A18;--focus:#A3B6FF;
--shadow:0 18px 40px -24px rgba(0,0,0,.7);color-scheme:dark}}
:root[data-theme="dark"]{--paper:#0D1522;--surface:#142033;--ink:#E8EEF6;--muted:#A8B5C7;--line:#2B3A51;--control:#7D8AA0;--accent:#A3B6FF;--accent-ink:#0D1522;
--tint:#1B2747;--ok:#7AD9A8;--ok-tint:#123124;--wait:#FFC266;--wait-tint:#2E2410;--warn:#FF9A8F;--warn-tint:#3A1A18;--focus:#A3B6FF;--shadow:0 18px 40px -24px rgba(0,0,0,.7);color-scheme:dark}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-padding-top:5rem}
body{margin:0;background:var(--paper);color:var(--ink);font:1rem/1.55 var(--body);-webkit-font-smoothing:antialiased;overflow-wrap:anywhere}
a{color:var(--accent)}:focus-visible{outline:3px solid var(--focus);outline-offset:3px;border-radius:4px}
.skip{position:absolute;left:-999px;top:8px;z-index:40;background:var(--accent);color:var(--accent-ink);padding:.6rem 1rem;border-radius:8px}.skip:focus{left:1rem}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.muted{color:var(--muted);font-size:.85rem;font-weight:400}
h1,h2,h3{font-family:var(--head);letter-spacing:-.015em}
.top{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--surface) 88%,transparent);-webkit-backdrop-filter:saturate(1.4) blur(12px);backdrop-filter:saturate(1.4) blur(12px);border-bottom:1px solid var(--line)}
.top-in{max-width:80rem;margin:0 auto;min-height:4rem;padding:.5rem 1.25rem;display:flex;align-items:center;justify-content:space-between;gap:1rem}
.brand{display:inline-flex;align-items:center;gap:.6rem;font:700 1.05rem/1 var(--head);white-space:nowrap}.brand svg{width:28px;height:28px;border-radius:7px}
.pill{font:600 .7rem/1 var(--mono);letter-spacing:.05em;text-transform:uppercase;color:var(--accent);background:var(--tint);padding:.35rem .55rem;border-radius:99px}
.icon{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:12px;border:1px solid var(--line);background:var(--surface);color:var(--muted);cursor:pointer}
.icon:hover{color:var(--ink);border-color:var(--control)}
.js-only{display:none}.js .js-only{display:inline-grid}
main{display:block;max-width:80rem;margin:0 auto;padding:1.5rem 1.25rem 3rem}
.hero{position:relative;overflow:hidden;border-radius:24px;padding:2rem;background:#0F1E33;color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
.hero::before{content:"";position:absolute;right:-140px;top:-170px;width:480px;height:480px;border-radius:50%;background:radial-gradient(circle,rgba(76,97,219,.6),rgba(76,97,219,0) 65%);pointer-events:none}
.hero::after{content:"";position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(rgba(255,255,255,.08) 1px,transparent 1px);background-size:22px 22px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 70%);mask-image:linear-gradient(90deg,transparent,#000 70%)}
.hero>*{position:relative;z-index:1}
.eyebrow{margin:0 0 .6rem;font:600 .75rem/1.4 var(--mono);letter-spacing:.09em;text-transform:uppercase;color:#A3B6FF}
.hero h1{margin:0 0 .5rem;font-size:clamp(1.9rem,1.3rem + 2.6vw,3rem);line-height:1.05;font-weight:780;letter-spacing:-.025em}
.tick{display:block;width:min(12rem,45%);height:auto;margin:0 0 1.25rem}
.stats{list-style:none;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:.75rem;margin:0;padding:0}
.stats li{padding:.9rem 1rem;border-radius:14px;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14)}
.stats strong{display:block;font:780 2rem/1 var(--head);letter-spacing:-.03em}.stats span{font-size:.88rem;color:#C9D3F6}
.bar{position:sticky;top:4.25rem;z-index:10;display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin:1rem 0;padding:.5rem;background:color-mix(in srgb,var(--surface) 92%,transparent);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border:1px solid var(--line);border-radius:14px}
.bar[hidden]{display:none}
.filters{display:flex;flex-wrap:wrap;gap:.35rem}
.filters button{font:600 .92rem var(--body);min-height:44px;padding:0 1rem;border-radius:10px;border:1px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer}
.filters button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.filters button span{font-family:var(--mono);font-size:.8rem;opacity:.85;margin-left:.35rem}
.bar input{flex:1 1 14rem;min-height:44px;padding:0 .9rem;border-radius:10px;border:1px solid var(--control);background:var(--surface);color:var(--ink);font:inherit}
.count{margin:0 .25rem;font-size:.9rem;color:var(--muted)}
.cards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,22rem),1fr));gap:1rem}
.card{display:flex;flex-direction:column;gap:.75rem;padding:1.25rem;background:var(--surface);border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow)}
.card[hidden]{display:none}
.card.attn{border-color:var(--warn);box-shadow:inset 0 4px 0 var(--warn),var(--shadow)}
.card-head{display:flex;gap:.9rem;align-items:center}
.card h2{margin:0;font-size:1.2rem;line-height:1.25}
.card .what{margin:0;font-size:.98rem;line-height:1.5;padding:.7rem .85rem;border-radius:12px;background:var(--tint)}
.card .path{display:block;margin-top:.1rem;font:.78rem/1.4 var(--mono);color:var(--muted)}
.ring{width:56px;height:56px;flex:none}.ring .t{fill:none;stroke:var(--tint);stroke-width:7}.ring .f{fill:none;stroke:var(--accent);stroke-width:7;stroke-linecap:round}
.ring text{fill:var(--ink);font:700 12.5px var(--body)}
.badges{display:flex;flex-wrap:wrap;gap:.4rem}
.badge{display:inline-flex;align-items:center;gap:.3em;padding:.15rem .6rem;border-radius:99px;font-size:.8rem;font-weight:700;white-space:nowrap}
.badge.ok{background:var(--ok-tint);color:var(--ok)}.badge.wait{background:var(--wait-tint);color:var(--wait)}.badge.warn{background:var(--warn-tint);color:var(--warn)}.badge.plain{background:var(--tint);color:var(--accent)}
.facts{display:grid;gap:.55rem;margin:0}
.facts div{display:grid;grid-template-columns:7.5rem minmax(0,1fr);gap:.5rem}
.facts dt{font-size:.75rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);padding-top:.15rem}
.facts dd{margin:0;font-size:.95rem}
.facts .blocker dd{color:var(--warn);font-weight:700}
.card-foot{display:flex;flex-wrap:wrap;gap:.4rem 1rem;margin-top:auto;padding-top:.75rem;border-top:1px solid var(--line);font-size:.85rem;color:var(--muted)}
.empty{padding:1.25rem;border:1.5px dashed var(--control);border-radius:14px;color:var(--muted)}
section.block{margin-top:1.5rem;background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:1.25rem 1.5rem}
section.block h2{margin:0 0 .75rem;font-size:1.3rem}
details>summary{min-height:44px;padding:.55rem 0;font-weight:700;cursor:pointer}
.wrap{overflow-x:auto;border:1px solid var(--line);border-radius:12px;margin-top:.5rem}
table{border-collapse:collapse;width:100%;min-width:900px;font-size:.9rem}
caption{text-align:left;font-weight:700;padding:.6rem .8rem}
th,td{border-top:1px solid var(--line);padding:.6rem .8rem;text-align:left;vertical-align:top}
thead th{background:var(--tint);font-size:.78rem;letter-spacing:.02em;white-space:nowrap}
progress{accent-color:var(--accent);width:5rem}
footer{max-width:80rem;margin:0 auto;padding:0 1.25rem 2.5rem;color:var(--muted);font-size:.85rem}
@media (max-width:60rem){.stats{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:36rem){.hero{padding:1.5rem 1.15rem;border-radius:18px}.stats{grid-template-columns:repeat(2,minmax(0,1fr))}.pill{display:none}main{padding-inline:1rem}.facts div{grid-template-columns:1fr;gap:0}.bar{position:static}}
@media (prefers-reduced-motion:no-preference){.filters button,.icon{transition:background-color .15s,color .15s}}
@media (forced-colors:active){.badge,.pill{border:1px solid CanvasText}}
@media print{.top,.bar,.skip{display:none!important}.hero{background:none;color:#000;border:1px solid #999}.hero::before,.hero::after{display:none}.stats span{color:#333}.card{box-shadow:none;break-inside:avoid}}
"""

PORTFOLIO_JS = """
document.documentElement.classList.add('js');
(function () {
  var root = document.documentElement, btn = document.getElementById('theme');
  function dark() { return root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; }
  function label() { btn.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme'); }
  try { var saved = localStorage.getItem('ml-theme'); if (saved) root.dataset.theme = saved; } catch (e) {}
  btn.addEventListener('click', function () { root.dataset.theme = dark() ? 'light' : 'dark'; try { localStorage.setItem('ml-theme', root.dataset.theme); } catch (e) {} label(); });
  label();
  var bar = document.getElementById('bar'), cards = [].slice.call(document.querySelectorAll('.card')), q = document.getElementById('q');
  if (!cards.length) return;
  bar.hidden = false;
  var buttons = [].slice.call(bar.querySelectorAll('.filters button')), mode = 'all';
  buttons.forEach(function (b) {
    var n = b.dataset.f === 'all' ? cards.length : cards.filter(function (c) { return c.dataset[b.dataset.f] === '1'; }).length;
    var s = document.createElement('span'); s.textContent = n; b.append(s);
    b.addEventListener('click', function () { mode = b.dataset.f; buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b); }); apply(); });
  });
  q.addEventListener('input', apply);
  function apply() {
    var t = q.value.trim().toLowerCase(), shown = 0;
    cards.forEach(function (c) { var ok = (mode === 'all' || c.dataset[mode] === '1') && (!t || c.textContent.toLowerCase().indexOf(t) > -1); c.hidden = !ok; shown += ok; });
    document.getElementById('count').textContent = shown + ' of ' + cards.length + ' shown';
  }
  apply();
})();
"""


def _ring(done: int, total: int) -> str:
    circ = 2 * 3.14159 * 23
    filled = circ * done / total if total else 0
    pct = round(100 * done / total) if total else 0
    return (f"<svg class='ring' viewBox='0 0 56 56' aria-hidden='true' focusable='false'><circle class='t' cx='28' cy='28' r='23'/>"
            f"<circle class='f' cx='28' cy='28' r='23' stroke-dasharray='{filled:.1f} {circ:.1f}' transform='rotate(-90 28 28)'/>"
            f"<text x='28' y='32.5' text-anchor='middle'>{pct}%</text></svg>")


def render_html(projects, outcomes_md) -> str:
    def esc(x):
        return html.escape(str(x))

    def approved(p):
        return "APPROVED" in p["gate"]

    def attention(p):
        return p["stale"] or p["blockers"] != "—"

    cards = "".join(
        f"<li class='card{' attn' if attention(p) else ''}' data-approved='{int(approved(p))}' data-waiting='{int(not approved(p))}' data-attention='{int(attention(p))}'>"
        f"<div class='card-head'>{_ring(p['done'], p['total'])}<div><h2>{esc(p['product'])}</h2><span class='path'>{esc(p['path'])}</span></div></div>"
        f"{WHAT_LINE.format(esc(p['what'])) if p.get('what') else ''}"
        f"<div class='badges'><span class='badge {'ok' if approved(p) else 'wait'}'>Gate: {esc(p['gate'])}</span>"
        f"<span class='badge plain'>{p['done']} of {p['total']} phases</span>"
        f"{BADGE_STALE if p['stale'] else ''}{BADGE_BLOCKED if p['blockers'] != '—' else ''}</div>"
        f"<dl class='facts'><div><dt>Now</dt><dd>{esc(p['current'])}</dd></div><div><dt>Next step</dt><dd>{esc(p['next'])}</dd></div>"
        f"<div><dt>Writing</dt><dd>{esc(p['writing'])}</dd></div>"
        f"<div class='{'blocker' if p['blockers'] != '—' else ''}'><dt>Blockers</dt><dd>{esc(p['blockers'])}</dd></div></dl>"
        f"<p class='card-foot'><span>Updated {esc(p['updated'])}</span><span>Cost {esc(p['cost'])}</span><span>Kit v{esc(p['kit'])}</span></p></li>"
        for p in projects
    )
    cards_html = f"<ul class='cards' aria-label='Projects'>{cards}</ul>" if projects else \
        "<p class='empty'>No projects found. Create one with scripts/new-project.sh, or pass the folders to scan.</p>"
    body_rows = "".join(
        f"<tr><th scope='row'>{esc(p['product'])}<br><span class='muted'>{esc(p['path'])}</span></th>"
        f"<td><span class='badge {'ok' if approved(p) else 'wait'}'>{esc(p['gate'])}</span></td>"
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
    n = len(projects)
    n_ok = sum(approved(p) for p in projects)
    n_attn = sum(attention(p) for p in projects)
    avg = round(100 * sum(p["done"] / p["total"] for p in projects if p["total"]) / n) if n else 0
    mark = ("<svg viewBox='0 0 64 64' aria-hidden='true' focusable='false'><rect width='64' height='64' rx='14' fill='#2337B0'/>"
            "<path d='M15 44V20l10.5 14L36 20v24h14' fill='none' stroke='#fff' stroke-width='7' stroke-linecap='round' stroke-linejoin='round'/></svg>")
    theme_icon = ("<svg width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' aria-hidden='true' focusable='false'>"
                  "<circle cx='12' cy='12' r='9'/><path d='M12 3a9 9 0 0 1 0 18z' fill='currentColor'/></svg>")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark"><title>Product portfolio · MakerLine</title>
<style>{PORTFOLIO_CSS}</style></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="top-in"><span class="brand">{mark}MakerLine <span class="pill">Portfolio</span></span>
<button type="button" class="icon js-only" id="theme" aria-label="Switch theme" title="Switch theme">{theme_icon}</button></div></header>
<main id="main" tabindex="-1">
<section class="hero" aria-labelledby="title">
<p class="eyebrow">Generated {dt.datetime.now():%Y-%m-%d %H:%M} · scripts/portfolio.py</p>
<h1 id="title">Product portfolio</h1>
<svg class="tick" viewBox="0 0 240 24" aria-hidden="true" focusable="false"><path transform="translate(0 2)" d="M2 10H200L208 17L226 3" fill="none" stroke="#A3B6FF" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>
<ul class="stats" aria-label="Portfolio at a glance">
<li><strong>{n}</strong><span>project(s)</span></li><li><strong>{n_ok}</strong><span>approved</span></li><li><strong>{n - n_ok}</strong><span>awaiting a decision</span></li>
<li><strong>{n_attn}</strong><span>need attention (stale or blocked)</span></li><li><strong>{avg}%</strong><span>average progress</span></li></ul>
</section>
<div class="bar" id="bar" hidden>
<div class="filters" role="group" aria-label="Show projects"><button type="button" data-f="all" aria-pressed="true">All</button><button type="button" data-f="attention" aria-pressed="false">Needs attention</button><button type="button" data-f="approved" aria-pressed="false">Approved</button><button type="button" data-f="waiting" aria-pressed="false">Awaiting decision</button></div>
<label class="sr-only" for="q">Find a project</label><input id="q" type="search" placeholder="Find a project" autocomplete="off">
<p class="count" id="count" aria-live="polite"></p></div>
{cards_html}
<section class="block" aria-labelledby="cmp-h"><h2 id="cmp-h">Compare in a table</h2>
<details><summary>Projects table ({n})</summary>
<div class="wrap" tabindex="0" role="region" aria-label="Projects table, scrolls sideways">
<table><caption>Projects</caption>
<thead><tr><th scope="col">Project</th><th scope="col">Approval gate</th><th scope="col">Progress</th><th scope="col">Current phase</th>
<th scope="col">Next step</th><th scope="col">Writing</th><th scope="col">Blockers</th><th scope="col">Updated</th><th scope="col">Cost to date</th><th scope="col">Kit</th></tr></thead>
<tbody>{body_rows}</tbody></table></div></details></section>
<section class="block" aria-labelledby="out-h"><h2 id="out-h">Idea outcomes</h2>
<p class="muted">What happened to each idea after its verdict. Feeds evaluate-idea calibration.</p>
<div class="wrap" tabindex="0" role="region" aria-label="Idea outcomes table, scrolls sideways">
<table><caption>Idea outcomes (feeds evaluate-idea calibration)</caption>
<thead><tr><th scope="col">Date</th><th scope="col">Project</th><th scope="col">Verdict at approval</th><th scope="col">Kill criteria</th>
<th scope="col">What happened</th><th scope="col">Metric vs target</th><th scope="col">Total cost</th><th scope="col">Lesson</th></tr></thead>
<tbody>{outcome_rows}</tbody></table></div></section>
</main>
<footer><p>MakerLine · the portfolio reports each approval gate; only the owner changes it.</p></footer>
<script>{PORTFOLIO_JS}</script>
</body></html>"""


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
