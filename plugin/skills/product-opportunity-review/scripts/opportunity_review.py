#!/usr/bin/env python3
"""Create and render a MakerLine product opportunity review (Python standard library only)."""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import pathlib
import re
import sys
import urllib.parse


REVIEW_FILE = pathlib.Path("docs/product/opportunity/REVIEW.json")
REPORT_FILE = pathlib.Path("docs/product/opportunity/index.html")
STAGES = ("idea", "partial", "prelaunch", "delayed", "live")
DEPTHS = ("quick", "standard", "deep")
MODES = ("first", "refresh")
STATUSES = ("not_started", "in_progress", "blocked", "done", "skipped")
OPTION_TYPES = ("build", "fix", "simplify", "pricing", "distribution", "partnership", "stop")
EVIDENCE = ("none", "weak", "some", "strong")
SOURCE_KINDS = ("official", "independent", "vendor", "community", "repo", "internal")
MARKET_STATUS = ("proposed", "confirmed")
RULE_APPLIES = ("yes", "no", "likely", "unclear")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ROUTES = {
    "idea": [
        ("goal", "Define the idea and goal", "new-idea"),
        ("market", "Research the market", "evaluate-idea"),
        ("evidence", "Test the riskiest assumption", "validate-idea"),
        ("direction", "Choose a design direction", "design-direction"),
        ("access", "Check launch markets and accessibility", "product-opportunity-review"),
        ("decision", "Decide whether to invest", "evaluate-idea"),
    ],
    "partial": [
        ("baseline", "Inspect what is built and planned", "product-opportunity-review"),
        ("goal", "Confirm the goal and remaining investment", "product-opportunity-review"),
        ("market", "Refresh customers and competitors", "evaluate-idea"),
        ("access", "Check launch markets and accessibility", "product-opportunity-review"),
        ("options", "Compare build and non-build options", "product-opportunity-review"),
        ("test", "Test the biggest uncertainty", "validate-idea"),
        ("decision", "Finish, narrow, pivot or stop", "product-opportunity-review"),
    ],
    "prelaunch": [
        ("baseline", "Check what is ready", "ship-checklist"),
        ("market", "Refresh market and positioning", "product-opportunity-review"),
        ("access", "Check launch markets and accessibility", "product-opportunity-review"),
        ("options", "Separate launch essentials from later ideas", "product-opportunity-review"),
        ("decision", "Make the launch decision", "ship-checklist"),
    ],
    "delayed": [
        ("baseline", "Measure remaining work and delay", "product-opportunity-review"),
        ("goal", "Recheck the original goal", "product-opportunity-review"),
        ("market", "Refresh stale market assumptions", "evaluate-idea"),
        ("access", "Check launch markets and accessibility", "product-opportunity-review"),
        ("options", "Compare launch, narrow, pivot and stop", "product-opportunity-review"),
        ("test", "Run a time-boxed demand test", "validate-idea"),
        ("decision", "Make the investment decision", "product-opportunity-review"),
    ],
    "live": [
        ("metrics", "Find the current bottleneck", "post-launch"),
        ("evidence", "Combine usage and customer feedback", "post-launch"),
        ("market", "Refresh the market", "product-opportunity-review"),
        ("access", "Check launch markets and accessibility", "product-opportunity-review"),
        ("options", "Compare improvements", "product-opportunity-review"),
        ("test", "Test the top option", "validate-idea"),
        ("decision", "Decide what to invest in next", "product-opportunity-review"),
        ("roadmap", "Plan the next slice", "plan-build"),
    ],
}


def esc(value: object) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def initial_review(stage: str, product: str, goal: str, markets: list[str], trigger: str, depth: str, mode: str) -> dict:
    today = dt.date.today().isoformat()
    return {
        "schema_version": 1,
        "product": product,
        "stage": stage,
        "depth": depth,
        "mode": mode,
        "trigger": trigger,
        "created": today,
        "updated": today,
        "goal": goal,
        "goal_status": "proposed",
        "launch_markets": markets,
        "markets_status": "proposed",
        "rules": [],
        "decision": "Pending evidence",
        "decision_reason": "The review is in progress.",
        "confidence": "unknown",
        "sources": [],
        "unknowns": [],
        "options": [],
        "next_actions": [],
        "tool_plan": [],
        "steps": [
            {"id": key, "title": title, "skill": skill,
             "status": "in_progress" if i == 0 else "not_started",
             "finding": "", "source_ids": [], "next": ""}
            for i, (key, title, skill) in enumerate(ROUTES[stage])
        ],
    }


def check(data: dict) -> list[str]:
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return ["schema_version must be 1"]
    stage = data.get("stage")
    if stage not in STAGES:
        errors.append("stage must be idea, partial, prelaunch, delayed, or live")
    if data.get("depth", "standard") not in DEPTHS:
        errors.append("depth must be quick, standard, or deep")
    if data.get("mode", "first") not in MODES:
        errors.append("mode must be first or refresh")
    for field in ("product", "goal", "decision", "decision_reason"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"{field} must be nonempty text")
    if data.get("confidence") not in ("unknown", "weak", "medium", "strong"):
        errors.append("confidence must be unknown, weak, medium, or strong")
    steps = data.get("steps")
    if not isinstance(steps, list) or not steps:
        errors.append("steps must be a nonempty list")
    else:
        ids = set()
        active = 0
        for i, step in enumerate(steps):
            if not isinstance(step, dict):
                errors.append(f"step {i} must be an object")
                continue
            if step.get("status") not in STATUSES:
                errors.append(f"step {i} has an invalid status")
            if step.get("status") == "in_progress":
                active += 1
            if not step.get("id") or step["id"] in ids:
                errors.append(f"step {i} needs a unique id")
            ids.add(step.get("id"))
        if active > 1:
            errors.append("only one step may be in progress")
    for field in ("sources", "unknowns", "options", "next_actions", "tool_plan", "launch_markets"):
        if not isinstance(data.get(field), list):
            errors.append(f"{field} must be a list")
    source_ids = set()
    for i, source in enumerate(data.get("sources", [])):
        if not isinstance(source, dict) or not source.get("id") or not source.get("title") or not source.get("date"):
            errors.append(f"source {i} needs an id, title and checked date")
            continue
        if source["id"] in source_ids:
            errors.append(f"source {source['id']} is duplicated")
        source_ids.add(source["id"])
    for step in data.get("steps", []):
        if not isinstance(step, dict):
            continue
        if step.get("status") in ("done", "skipped") and not str(step.get("finding", "")).strip():
            errors.append(f"completed or skipped step {step.get('id')} needs a finding")
        for sid in step.get("source_ids", []):
            if sid not in source_ids:
                errors.append(f"step {step.get('id')} cites unknown source {sid}")
    for item in data.get("options", []):
        if not isinstance(item, dict):
            errors.append("each option must be an object")
            continue
        name = item.get("name") or "(unnamed)"
        for field in ("name", "value_range", "effort_range", "test"):
            if not str(item.get(field, "")).strip():
                errors.append(f"option {name} needs {field.replace('_', ' ')}")
        if item.get("type") not in OPTION_TYPES:
            errors.append(f"option {name}: type must be one of {', '.join(OPTION_TYPES)}")
        if item.get("evidence") not in EVIDENCE:
            errors.append(f"option {name}: evidence must be one of {', '.join(EVIDENCE)}")
        if item.get("evidence") == "strong" and not item.get("source_ids"):
            errors.append(f"option {name} claims strong evidence without a source")
        for sid in item.get("source_ids", []):
            if sid not in source_ids:
                errors.append(f"option {name} cites unknown source {sid}")
    for i, item in enumerate(data.get("next_actions", [])):
        if not isinstance(item, dict) or not all(str(item.get(f, "")).strip() for f in ("action", "owner", "success_measure")):
            errors.append(f"next action {i + 1} needs an action, an owner and a success measure")
    for i, item in enumerate(data.get("tool_plan", [])):
        if not isinstance(item, dict) or not all(str(item.get(f, "")).strip() for f in ("job", "primary")):
            errors.append(f"tool plan row {i + 1} needs a job and a primary tool")
    for i, item in enumerate(data.get("unknowns", [])):
        if not isinstance(item, dict) or not str(item.get("question", "")).strip():
            errors.append(f"unknown {i + 1} needs a question")
    if data.get("markets_status", "proposed") not in MARKET_STATUS:
        errors.append("markets_status must be proposed or confirmed")
    for i, rule in enumerate(data.get("rules", []) or []):
        if not isinstance(rule, dict) or not all(str(rule.get(f, "")).strip() for f in ("market", "rule", "applies")):
            errors.append(f"rule {i + 1} needs a market, a rule and whether it applies")
            continue
        if rule.get("applies") not in RULE_APPLIES:
            errors.append(f"rule {rule['rule']}: applies must be one of {', '.join(RULE_APPLIES)}")
        for sid in rule.get("source_ids", []):
            if sid not in source_ids:
                errors.append(f"rule {rule['rule']} cites unknown source {sid}")
    for field in ("created", "updated"):
        if data.get(field) and not DATE.match(str(data[field])):
            errors.append(f"{field} must be a YYYY-MM-DD date")
    for source in data.get("sources", []):
        if isinstance(source, dict):
            if source.get("date") and not DATE.match(str(source["date"])):
                errors.append(f"source {source.get('id')}: date must be YYYY-MM-DD")
            if source.get("kind") and source["kind"] not in SOURCE_KINDS:
                errors.append(f"source {source.get('id')}: kind must be one of {', '.join(SOURCE_KINDS)}")
    steps = data.get("steps") if isinstance(data.get("steps"), list) else []
    finished = steps and all(isinstance(s, dict) and s.get("status") in ("done", "skipped") for s in steps)
    if finished:
        if data.get("decision", "").strip().lower() in ("", "pending evidence"):
            errors.append("every step is finished, so record the decision (it still says 'Pending evidence')")
        if not data.get("options") or not data.get("next_actions"):
            errors.append("a finished review needs options and next actions")
    return errors


def warnings(data: dict) -> list[str]:
    """Problems worth fixing that shouldn't block rendering."""
    out = []
    cited = set()
    for group in ("steps", "options", "rules"):
        for item in data.get(group, []) or []:
            if isinstance(item, dict):
                cited.update(item.get("source_ids", []))
    for source in data.get("sources", []):
        if isinstance(source, dict) and source.get("id") not in cited:
            out.append(f"source {source.get('id')} isn't cited by any step, option or rule")
        if isinstance(source, dict) and not source.get("kind"):
            out.append(f"source {source.get('id')} has no kind (official, independent, vendor, community, repo, internal)")
    if data.get("launch_markets") and data.get("markets_status", "proposed") == "proposed":
        out.append("launch markets are still proposed; ask the owner to confirm them")
    return out


def _items(values: list, fields: tuple[str, ...], empty: str) -> str:
    if not values:
        return f'<p class="muted">{esc(empty)}</p>'
    rows = []
    for value in values:
        if isinstance(value, dict):
            cells = [f"<td>{esc(', '.join(map(str, value[k])) if isinstance(value.get(k), list) else value.get(k, ''))}</td>" for k in fields]
        else:
            cells = [f"<td>{esc(value)}</td>"]
        rows.append("<tr>" + "".join(cells) + "</tr>")
    heads = "".join(f'<th scope="col">{esc(k.replace("_", " ").title())}</th>' for k in fields)
    return '<div class="scroll" tabindex="0" role="region" aria-label="Scrollable table"><table><thead><tr>' + heads + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>"


def _sources(values: list) -> str:
    if not values:
        return '<p class="muted">No sources recorded.</p>'
    rows = []
    for source in values:
        url = str(source.get("url", ""))
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme in ("https", "http") and parsed.netloc:
            link = f'<a href="{esc(url)}" rel="noopener noreferrer">Open source</a>'
        else:
            link = esc(url)
        rows.append(f'<tr><th scope="row">{esc(source.get("id", ""))}</th><td>{esc(source.get("title", ""))}</td><td>{esc(source.get("kind", ""))}</td><td>{link}</td><td>{esc(source.get("date", ""))}</td></tr>')
    return '<div class="scroll" tabindex="0" role="region" aria-label="Scrollable source table"><table><thead><tr><th scope="col">ID</th><th scope="col">Title</th><th scope="col">Kind</th><th scope="col">Link</th><th scope="col">Checked on</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>'


def _sentence(text: str) -> str:
    text = str(text).strip()
    return text if text.endswith((".", "!", "?")) else text + "."


def render_body(data: dict) -> str:
    errors = check(data)
    if errors:
        raise ValueError("Invalid review: " + "; ".join(errors))
    steps = data["steps"]
    done = sum(s["status"] in ("done", "skipped") for s in steps)
    current = next((s for s in steps if s["status"] in ("in_progress", "blocked", "not_started")), None)
    route = " → ".join(s["title"] for s in steps)
    step_html = []
    for i, step in enumerate(steps, 1):
        status = step["status"].replace("_", " ")
        prompt = f"{data['product']}, opportunity review step “{step['title']}”: use the {step['skill']} skill. Read docs/product/opportunity/REVIEW.json, record this step's finding and sources there, then regenerate the HTML report."
        step_html.append(f'''<li class="review-step review-step--{esc(step["status"])}">
<details{' open' if step is current else ''}><summary><span class="step-id">{i}.</span> {esc(step['title'])} <span class="step-state">{esc(status)}</span></summary>
<div class="review-step-body"><p><strong>Skill:</strong> <code>{esc(step['skill'])}</code></p>
<p><strong>Finding:</strong> {esc(step.get('finding') or 'Not recorded yet.')}</p>
<p><strong>Next:</strong> {esc(step.get('next') or 'Complete this step and record its finding.')}</p>
<p><strong>Sources:</strong> {esc(', '.join(step.get('source_ids', [])) or 'None recorded')}</p>
<label for="review-prompt-{i}">Example prompt</label><textarea id="review-prompt-{i}" readonly rows="3">{esc(prompt)}</textarea></div></details></li>''')
    return f'''<div class="review">
<p class="eyebrow">Product opportunity review · {esc(data['stage'])} · updated {esc(data.get('updated', ''))}</p>
<h1>{esc(data['product'])}: what to do next</h1>
<p class="muted">How to read this: start with the recommendation, then open each workflow step for its finding and next move. “Unknown” means evidence is still needed.</p>
<p class="lede"><strong>Current recommendation:</strong> {esc(_sentence(data['decision']))} {esc(data['decision_reason'])}</p>
<p><strong>Confidence:</strong> {esc(data['confidence'])} · <strong>Goal:</strong> {esc(data['goal'])} ({esc(data.get('goal_status', 'proposed'))})</p>
<p><strong>Review scope:</strong> {esc(data.get('depth', 'standard'))} · {esc(data.get('mode', 'first'))} run</p>
<p><strong>Launch markets:</strong> {esc(', '.join(data['launch_markets']) or 'Not supplied; market-specific rules remain open.')}{esc(' (proposed; owner to confirm)' if data['launch_markets'] and data.get('markets_status', 'proposed') == 'proposed' else '')}</p>
<p><strong>Review trigger:</strong> {esc(data.get('trigger', 'Not recorded'))}</p>
<nav class="review-nav" aria-label="Review sections"><a href="#workflow">Workflow</a><a href="#options">Options</a><a href="#actions">Action plan</a><a href="#tools">AI tools</a><a href="#evidence">Evidence</a></nav>
<section class="panel" id="workflow" aria-labelledby="workflow-h"><h2 id="workflow-h">Workflow and progress</h2>
<p>{esc(route)}</p><div class="meter"><progress value="{done}" max="{len(steps)}" aria-label="{done} of {len(steps)} review steps done or skipped"></progress><span>{done}/{len(steps)} steps</span></div>
<p><strong>Now:</strong> {esc(current['title'] if current else 'Review complete')}. {esc(current.get('next', '') if current else '')}</p>
<ol class="review-steps">{''.join(step_html)}</ol></section>
<section class="panel" id="options" aria-labelledby="options-h"><h2 id="options-h">Options to compare</h2>
<p class="muted">Value, effort and evidence are estimates until a source or test confirms them. Include non-build options.</p>
{_items(data['options'], ('name', 'type', 'value_range', 'effort_range', 'evidence', 'test', 'source_ids'), 'Options have not been assessed yet.')}</section>
<section class="panel" id="actions" aria-labelledby="actions-h"><h2 id="actions-h">Next actions</h2>
{_items(data['next_actions'], ('action', 'owner', 'when', 'success_measure'), 'Actions will appear as the review progresses.')}</section>
<section class="panel" id="tools" aria-labelledby="tools-h"><h2 id="tools-h">Working across AI tools</h2>
<p class="muted">One tool owns each output. Give a new tool the source files and the latest handoff before it continues.</p>
{_items(data['tool_plan'], ('job', 'primary', 'fallback', 'handoff'), 'Run tool-plan to assign primary and fallback tools.')}</section>
<section class="panel" id="evidence" aria-labelledby="evidence-h"><h2 id="evidence-h">Evidence and open questions</h2>
<details><summary>Launch-market rules ({len(data.get('rules') or [])})</summary><p class="muted">Not legal advice. WCAG conformance alone doesn't mean legal compliance.</p>{_items(data.get('rules') or [], ('market', 'rule', 'applies', 'uncertainty', 'source_ids'), 'No rules recorded yet.')}</details>
<details><summary>Sources ({len(data['sources'])})</summary>{_sources(data['sources'])}</details>
<details><summary>Unknowns ({len(data['unknowns'])})</summary>{_items(data['unknowns'], ('question', 'blocks', 'how_to_answer'), 'No unknowns recorded.')}</details></section>
<p class="muted">The saved REVIEW.json is the review record. Regenerate this page after each update; the HTML shows that saved state.</p>
</div>'''


def render_standalone(data: dict, css: str) -> str:
    body = render_body(data)
    # CSS is kit-controlled; all review fields are HTML-escaped above. No script, CDN or network needed.
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><title>{esc(data['product'])} · opportunity review · MakerLine</title><style>{css}</style></head><body><a class="skip" href="#main">Skip to content</a><main id="main" tabindex="-1">{body}</main><footer class="foot"><p>Generated by MakerLine. Evidence and recommendations are dated; verify them before acting.</p></footer></body></html>'''


def read_review(project: pathlib.Path) -> dict:
    path = safe_review_path(project, REVIEW_FILE)
    return json.loads(path.read_text(encoding="utf-8"))


def safe_review_path(project: pathlib.Path, rel: pathlib.Path) -> pathlib.Path:
    root = project.resolve()
    path = (root / rel).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Review path points outside the project")
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    ini = sub.add_parser("init", help="create an initial stage-aware review; never overwrites")
    ini.add_argument("project", type=pathlib.Path)
    ini.add_argument("--stage", choices=STAGES, required=True)
    ini.add_argument("--product", required=True)
    ini.add_argument("--goal", default="Goal to confirm")
    ini.add_argument("--market", action="append", default=[])
    ini.add_argument("--trigger", default="Review what to do next")
    ini.add_argument("--depth", choices=DEPTHS, default="standard")
    ini.add_argument("--mode", choices=MODES, default="first")
    for name in ("check", "render"):
        sub.add_parser(name).add_argument("project", type=pathlib.Path)
    args = ap.parse_args()
    project = args.project.expanduser().resolve()
    path = safe_review_path(project, REVIEW_FILE)
    if args.command == "init":
        if path.exists():
            print(f"Review already exists: {path}", file=sys.stderr)
            return 2
        path.parent.mkdir(parents=True, exist_ok=True)
        data = initial_review(args.stage, args.product, args.goal, args.market, args.trigger, args.depth, args.mode)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        data = read_review(project)
    errors = check(data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 2
    for warning in warnings(data):
        print(f"Warning: {warning}", file=sys.stderr)
    if args.command in ("init", "render"):
        css = (pathlib.Path(__file__).resolve().parent.parent / "assets" / "report.css").read_text(encoding="utf-8")
        report = safe_review_path(project, REPORT_FILE)
        report.write_text(render_standalone(data, css), encoding="utf-8")
        print(report)
    else:
        print("Review valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
