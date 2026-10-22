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
# "Product at a glance": the same pieces as ONE_PAGER's "idea in one line", filled from the brief and evaluation.
OVERVIEW_TEXT = ("what", "problem", "solution", "outcome", "value_add", "success_measure")
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
        "overview": {key: "" for key in OVERVIEW_TEXT} | {"audience": []},
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
    for i, area in enumerate(data.get("areas", []) or []):
        if not isinstance(area, dict) or not all(str(area.get(f, "")).strip() for f in ("name", "status")):
            errors.append(f"area {i + 1} needs a name and a status")
    overview = data.get("overview")
    if overview is not None:
        if not isinstance(overview, dict):
            errors.append("overview must be an object")
        else:
            for key in OVERVIEW_TEXT:
                if key in overview and not isinstance(overview[key], str):
                    errors.append(f"overview {key} must be text")
            audience = overview.get("audience", [])
            if not isinstance(audience, list) or not all(isinstance(a, dict) and str(a.get("who", "")).strip() for a in audience):
                errors.append("overview audience must be a list of {who, how}")
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


CONFIDENCE_LEVEL = {"unknown": 0, "weak": 1, "medium": 2, "strong": 3}
EVIDENCE_LEVEL = {"none": 0, "weak": 1, "some": 2, "strong": 3}
STEP_ICON = {"done": "✓", "skipped": "–", "blocked": "!"}
MARK_SVG = ('<svg class="ml-mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect width="64" height="64" rx="14" fill="#2337B0"/>'
            '<path d="M15 44V20l10.5 14L36 20v24h14" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
TICK_SVG = ('<svg class="ml-tick" viewBox="0 0 240 24" aria-hidden="true" focusable="false"><path transform="translate(0 2)" '
            'd="M2 10H200L208 17L226 3" fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def _items(values: list, fields: tuple[str, ...], empty: str) -> str:
    if not values:
        return f'<p class="ml-empty">{esc(empty)}</p>'
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
        return '<p class="ml-empty">No sources recorded.</p>'
    rows = []
    for source in values:
        url = str(source.get("url", ""))
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme in ("https", "http") and parsed.netloc:
            link = f'<a href="{esc(url)}" rel="noopener noreferrer">Open source</a>'
        else:
            link = esc(url)
        kind = source.get("kind", "")
        kind_html = f'<span class="ml-kind">{esc(kind)}</span>' if kind else ""
        rows.append(f'<tr><th scope="row">{esc(source.get("id", ""))}</th><td>{esc(source.get("title", ""))}</td><td>{kind_html}</td><td>{link}</td><td>{esc(source.get("date", ""))}</td></tr>')
    return '<div class="scroll" tabindex="0" role="region" aria-label="Scrollable source table"><table><thead><tr><th scope="col">ID</th><th scope="col">Title</th><th scope="col">Kind</th><th scope="col">Link</th><th scope="col">Checked on</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>'


def _areas(data: dict) -> str:
    """Products with several apps, repos or teams show where each part stands."""
    areas = data.get("areas") or []
    if not areas:
        return ""
    return ('<section class="panel ml-section" id="areas" aria-labelledby="areas-h"><h2 id="areas-h">Where each part stands</h2>'
            + _items(areas, ("name", "status", "owner", "note"), "") + "</section>\n")


def _sentence(text: str) -> str:
    text = str(text).strip()
    return text if text.endswith((".", "!", "?")) else text + "."


def _level(value: str, levels: dict, label: str) -> str:
    """Three-segment meter: the word carries the meaning, the segments only reinforce it."""
    n = levels.get(value, 0)
    segs = "".join(f'<i class="{"on" if i < n else "off"}"></i>' for i in range(3))
    return (f'<p class="ml-level ml-level--{n}"><span class="ml-segs" aria-hidden="true">{segs}</span>'
            f'<span>{esc(label)}: <strong>{esc(value)}</strong></span></p>')


def _ring(done: int, total: int) -> str:
    """Progress ring drawn with SVG attributes (no inline style, so the kit UI's strict CSP allows it)."""
    circ = 2 * 3.14159 * 26
    filled = circ * done / total if total else 0
    pct = round(100 * done / total) if total else 0
    return (f'<svg class="ml-ring" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
            f'<circle cx="32" cy="32" r="26" class="ml-ring-track"/>'
            f'<circle cx="32" cy="32" r="26" class="ml-ring-fill" stroke-dasharray="{filled:.1f} {circ:.1f}" transform="rotate(-90 32 32)"/>'
            f'<text x="32" y="37" text-anchor="middle">{pct}%</text></svg>')


def _kind_bar(sources: list) -> str:
    """Stacked bar of source kinds; the legend carries the counts in words."""
    counts: dict[str, int] = {}
    for source in sources:
        if isinstance(source, dict):
            kind = source.get("kind") or "unlabelled"
            counts[kind] = counts.get(kind, 0) + 1
    total = sum(counts.values())
    if not total:
        return ""
    order = [k for k in (*SOURCE_KINDS, "unlabelled") if k in counts]
    x, rects = 0.0, []
    for kind in order:
        w = 100 * counts[kind] / total
        rects.append(f'<rect class="ml-k-{esc(kind)}" x="{x:.2f}" y="0" width="{w:.2f}" height="10"/>')
        x += w
    legend = "".join(f'<li><svg viewBox="0 0 10 10" aria-hidden="true" focusable="false"><rect class="ml-k-{esc(k)}" width="10" height="10" rx="2"/></svg>'
                     f'{esc(k)} <strong>{counts[k]}</strong></li>' for k in order)
    plural = "s" if total != 1 else ""
    return (f'<div class="ml-kinds"><p class="ml-label">Evidence mix · {total} source{plural}</p>'
            f'<svg class="ml-kind-bar" viewBox="0 0 100 10" preserveAspectRatio="none" aria-hidden="true" focusable="false">{"".join(rects)}</svg>'
            f'<ul class="ml-kind-legend">{legend}</ul></div>')


def _options(options: list) -> str:
    if not options:
        return '<p class="ml-empty">Options have not been assessed yet.</p>'
    cards = []
    for o in options:
        src = ", ".join(o.get("source_ids", [])) or "none yet"
        cards.append(
            f'<li class="ml-option"><p class="ml-option-type">{esc(o.get("type", ""))}</p><h3>{esc(o.get("name", ""))}</h3>'
            f'<dl class="ml-option-facts"><div><dt>Value</dt><dd>{esc(o.get("value_range", ""))}</dd></div>'
            f'<div><dt>Effort</dt><dd>{esc(o.get("effort_range", ""))}</dd></div></dl>'
            f'{_level(o.get("evidence", "none"), EVIDENCE_LEVEL, "Evidence")}'
            f'<p class="ml-option-test"><strong>Cheapest test:</strong> {esc(o.get("test", ""))}</p>'
            f'<p class="ml-option-src">Sources: {esc(src)}</p></li>')
    return '<ul class="ml-options">' + "".join(cards) + "</ul>"


def _glance(data: dict) -> str:
    """Product at a glance: what it is, the idea (problem → solution → outcome), goal, value add, who it helps."""
    o = data.get("overview") if isinstance(data.get("overview"), dict) else {}
    missing = "Not recorded yet."

    def txt(key: str) -> str:
        return esc(o.get(key) or missing)

    people = o.get("audience") or []
    people_html = "".join(
        f'<li><span class="ml-av" aria-hidden="true">{i}</span><span><strong>{esc(a.get("who", ""))}</strong>{esc(a.get("how", "") or missing)}</span></li>'
        for i, a in enumerate(people, 1)) or f'<li class="ml-muted-row">{missing} Add who it helps and how.</li>'
    filled = any(str(o.get(k, "")).strip() for k in OVERVIEW_TEXT) or people
    hint = "" if filled else ('<p class="ml-hint">Fill <code>overview</code> in REVIEW.json from the brief, evaluation and one-pager, '
                              'then render again. Write “Not decided yet” rather than guessing.</p>')
    return f'''<section class="panel ml-section ml-glance" id="glance" aria-labelledby="glance-h"><h2 id="glance-h">Product at a glance</h2>
{hint}<p class="ml-what">{txt("what")}</p>
<ol class="ml-idea" aria-label="The idea"><li><span class="ml-k">Problem today</span><p>{txt("problem")}</p></li>
<li><span class="ml-k">What it does</span><p>{txt("solution")}</p></li><li><span class="ml-k">Outcome for users</span><p>{txt("outcome")}</p></li></ol>
<div class="ml-glance-grid"><article class="ml-card ml-card--goal"><span class="ml-k">Goal</span><p class="ml-big">{esc(data["goal"])}</p>
<p>{esc(data.get("goal_status", "proposed"))} · measured by {txt("success_measure")}</p></article>
<article class="ml-card ml-card--value"><span class="ml-k">Value add</span><p class="ml-big">{txt("value_add")}</p></article>
<article class="ml-card ml-card--who"><span class="ml-k">Who it helps, and how</span><ul class="ml-people">{people_html}</ul></article></div>
</section>'''


def _steps(data: dict, steps: list, current) -> str:
    out = []
    for i, step in enumerate(steps, 1):
        status = step["status"].replace("_", " ")
        prompt = (f"{data['product']}, opportunity review step “{step['title']}”: use the {step['skill']} skill. "
                  "Read docs/product/opportunity/REVIEW.json, record this step's finding and sources there, then regenerate the HTML report.")
        icon = STEP_ICON.get(step["status"], str(i))
        is_open = " open" if step is current else ""
        out.append(
            f'<li class="review-step review-step--{esc(step["status"])}"><span class="ml-step-icon" aria-hidden="true">{esc(icon)}</span>'
            f'<details{is_open}><summary><span class="step-id">{i}.</span> {esc(step["title"])} <span class="step-state">{esc(status)}</span></summary>'
            f'<div class="review-step-body"><p><strong>Skill:</strong> <code>{esc(step["skill"])}</code></p>'
            f'<p><strong>Finding:</strong> {esc(step.get("finding") or "Not recorded yet.")}</p>'
            f'<p><strong>Next:</strong> {esc(step.get("next") or "Complete this step and record its finding.")}</p>'
            f'<p><strong>Sources:</strong> {esc(", ".join(step.get("source_ids", [])) or "None recorded")}</p>'
            f'<label for="review-prompt-{i}">Example prompt</label><div class="ml-copy">'
            f'<textarea id="review-prompt-{i}" readonly rows="3">{esc(prompt)}</textarea>'
            f'<button type="button" class="btn js-only" data-copy="review-prompt-{i}">Copy</button></div></div></details></li>')
    return "".join(out)


def render_body(data: dict) -> str:
    errors = check(data)
    if errors:
        raise ValueError("Invalid review: " + "; ".join(errors))
    steps = data["steps"]
    total = len(steps)
    done = sum(s["status"] in ("done", "skipped") for s in steps)
    current = next((s for s in steps if s["status"] in ("in_progress", "blocked", "not_started")), None)
    now = esc(current["title"] if current else "Review complete")
    now_next = esc(current.get("next", "") if current else "")
    markets = ", ".join(data["launch_markets"]) or "Not supplied; market-specific rules remain open."
    proposed = " (proposed; owner to confirm)" if data["launch_markets"] and data.get("markets_status", "proposed") == "proposed" else ""
    route = "".join(f'<li class="ml-route-seg ml-route-seg--{esc(s["status"])}"></li>' for s in steps)
    rules = data.get("rules") or []
    areas_link = '<a href="#areas">Parts</a>' if data.get("areas") else ""
    return f'''<div class="review">
<section class="ml-hero" aria-labelledby="review-h">
<p class="eyebrow">Product opportunity review · {esc(data["stage"])} · updated {esc(data.get("updated", ""))}</p>
<h1 id="review-h">{esc(data["product"])}: what to do next</h1>{TICK_SVG}
<div class="ml-verdict"><p class="ml-label">Current recommendation</p>
<p class="ml-decision">{esc(_sentence(data["decision"]))}</p>
<p class="ml-reason">{esc(data["decision_reason"])}</p>
{_level(data["confidence"], CONFIDENCE_LEVEL, "Confidence")}</div>
<dl class="ml-meta">
<div><dt>Launch markets</dt><dd>{esc(markets)}{esc(proposed)}</dd></div>
<div><dt>Review scope</dt><dd>{esc(data.get("depth", "standard"))} · {esc(data.get("mode", "first"))} run</dd></div>
<div><dt>Review trigger</dt><dd>{esc(data.get("trigger", "Not recorded"))}</dd></div>
</dl></section>
<ul class="ml-stats" aria-label="Review at a glance">
<li class="ml-stat ml-stat--ring">{_ring(done, total)}<span><strong>{done} of {total}</strong><span>steps done · now: {now}</span></span></li>
<li class="ml-stat"><strong>{len(data["options"])}</strong><span>options compared</span></li>
<li class="ml-stat"><strong>{len(data["sources"])}</strong><span>sources checked</span></li>
<li class="ml-stat"><strong>{len(data["unknowns"])}</strong><span>open questions</span></li>
</ul>
<p class="muted ml-howto">How to read this: start with the recommendation, then open each workflow step for its finding and next move. “Unknown” means evidence is still needed.</p>
<nav class="review-nav" aria-label="Review sections"><a href="#glance">At a glance</a><a href="#workflow">Workflow</a>{areas_link}<a href="#options">Options</a><a href="#actions">Action plan</a><a href="#tools">AI tools</a><a href="#evidence">Evidence</a></nav>
{_glance(data)}
<section class="panel ml-section" id="workflow" aria-labelledby="workflow-h"><h2 id="workflow-h">Workflow and progress</h2>
<ol class="ml-route" aria-hidden="true">{route}</ol>
<div class="meter"><progress value="{done}" max="{total}" aria-label="{done} of {total} review steps done or skipped"></progress><span>{done}/{total} steps</span></div>
<p><strong>Now:</strong> {now}. {now_next}</p>
<ol class="review-steps">{_steps(data, steps, current)}</ol></section>
{_areas(data)}<section class="panel ml-section" id="options" aria-labelledby="options-h"><h2 id="options-h">Options to compare</h2>
<p class="muted">Value, effort and evidence are estimates until a source or test confirms them. Include non-build options.</p>
{_options(data["options"])}</section>
<section class="panel ml-section" id="actions" aria-labelledby="actions-h"><h2 id="actions-h">Next actions</h2>
{_items(data["next_actions"], ("action", "owner", "when", "success_measure"), "Actions will appear as the review progresses.")}</section>
<section class="panel ml-section" id="tools" aria-labelledby="tools-h"><h2 id="tools-h">Working across AI tools</h2>
<p class="muted">One tool owns each output. Give a new tool the source files and the latest handoff before it continues.</p>
{_items(data["tool_plan"], ("job", "primary", "fallback", "handoff"), "Run tool-plan to assign primary and fallback tools.")}</section>
<section class="panel ml-section" id="evidence" aria-labelledby="evidence-h"><h2 id="evidence-h">Evidence and open questions</h2>
{_kind_bar(data["sources"])}
<details><summary>Launch-market rules ({len(rules)})</summary><p class="muted">Not legal advice. WCAG conformance alone doesn't mean legal compliance.</p>{_items(rules, ("market", "rule", "applies", "uncertainty", "source_ids"), "No rules recorded yet.")}</details>
<details><summary>Sources ({len(data["sources"])})</summary>{_sources(data["sources"])}</details>
<details><summary>Unknowns ({len(data["unknowns"])})</summary>{_items(data["unknowns"], ("question", "blocks", "how_to_answer"), "No unknowns recorded.")}</details></section>
<p class="muted">The saved REVIEW.json is the review record. Regenerate this page after each update; the HTML shows that saved state.</p>
</div>'''


# Only the offline report runs this; the kit UI uses its own app.js (same data-copy contract).
STANDALONE_SCRIPT = """
document.documentElement.classList.add('js');
(function () {
  var root = document.documentElement, btn = document.getElementById('ml-theme');
  function dark() { return root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; }
  function label() { btn.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme'); }
  try { var saved = localStorage.getItem('ml-theme'); if (saved) root.dataset.theme = saved; } catch (e) {}
  btn.addEventListener('click', function () { root.dataset.theme = dark() ? 'light' : 'dark'; try { localStorage.setItem('ml-theme', root.dataset.theme); } catch (e) {} label(); });
  label();
  document.getElementById('ml-print').addEventListener('click', function () {
    var shut = [].slice.call(document.querySelectorAll('details:not([open])'));
    shut.forEach(function (d) { d.open = true; }); window.print(); shut.forEach(function (d) { d.open = false; });
  });
  var live = document.getElementById('ml-live');
  document.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-copy]'); if (!b) return;
    var f = document.getElementById(b.getAttribute('data-copy'));
    function say(ok) {
      live.textContent = ''; live.textContent = ok ? 'Prompt copied.' : 'The prompt is selected: press Ctrl+C or Command+C.';
      if (ok) { b.textContent = 'Copied'; setTimeout(function () { b.textContent = 'Copy'; }, 1500); }
    }
    if (navigator.clipboard) navigator.clipboard.writeText(f.value).then(function () { say(true); }, function () { f.select(); say(false); });
    else { f.select(); say(false); }
  });
  var links = [].slice.call(document.querySelectorAll('.review-nav a'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) { if (a.hash === '#' + en.target.id) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    links.forEach(function (a) { var s = document.getElementById(a.hash.slice(1)); if (s) io.observe(s); });
  }
})();
"""

ICON_PRINT = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" focusable="false">'
              '<path d="M6 9V3h12v6M6 18H4v-7h16v7h-2M8 14h8v7H8z"/></svg>')
ICON_THEME = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" focusable="false">'
              '<circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor"/></svg>')


def render_standalone(data: dict, css: str) -> str:
    body = render_body(data)
    # CSS and script are kit-controlled; all review fields are HTML-escaped above. No CDN or network needed,
    # and the page reads fine without the script (it only adds the theme switch, print and copy buttons).
    title = f"{esc(data['product'])} · opportunity review · MakerLine"
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><title>{title}</title><style>{css}</style></head><body><a class="skip" href="#main">Skip to content</a>
<header class="ml-top"><div class="ml-top-inner"><span class="ml-brand">{MARK_SVG}<strong>MakerLine</strong><span class="ml-pill">Opportunity review</span></span>
<span class="ml-actions"><button type="button" class="ml-icon js-only" id="ml-print" aria-label="Print or save as PDF" title="Print or save as PDF">{ICON_PRINT}</button><button type="button" class="ml-icon js-only" id="ml-theme" aria-label="Switch theme" title="Switch theme">{ICON_THEME}</button></span></div></header>
<main id="main" tabindex="-1">{body}</main><footer class="foot"><p>Generated by MakerLine. Evidence and recommendations are dated; verify them before acting.</p></footer>
<div id="ml-live" class="sr-only" aria-live="polite" aria-atomic="true"></div><script>{STANDALONE_SCRIPT}</script></body></html>'''


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
