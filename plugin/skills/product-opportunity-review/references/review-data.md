# Review record

`docs/product/opportunity/REVIEW.json` is versioned input for `scripts/opportunity_review.py`; the HTML is generated from it. Run `check` before `render`. The generator accepts UTF-8 text and escapes it for HTML. It does not render raw HTML from evidence.

Top-level fields:

- `schema_version`: `1`.
- `product`, `stage`, `depth` (`quick`, `standard`, `deep`), `mode` (`first`, `refresh`), `trigger`, `created`, `updated`, `goal`, `goal_status`, `launch_markets`.
- `decision`, `decision_reason`, `confidence`: the answer first; confidence is `unknown`, `weak`, `medium` or `strong`.
- `steps`: route steps with `id`, `title`, `skill`, `status`, `finding`, `source_ids`, `next`. Status is `not_started`, `in_progress`, `blocked`, `done` or `skipped`. A completed step needs a finding. A skipped step explains why in `finding`.
- `sources`: `{id, title, url, date}`. Source IDs cited by steps must exist. Prefer official and primary sources for rules, technology and market claims.
- `unknowns`: `{question, blocks, how_to_answer}`.
- `options`: `{name, type, value_range, effort_range, evidence, test, source_ids}`. Ranges are strings that include units and explicit assumptions. `type` can be build, fix, simplify, pricing, distribution, partnership, or stop. Strong evidence requires a source.
- `next_actions`: `{action, owner, when, success_measure}`.
- `tool_plan`: `{job, primary, fallback, handoff}`. Use only tools the owner has; one owner per output.

Keep public market links in `sources`. Keep private customer evidence in a project-local note and refer to it by file path and anonymised role. Never copy credentials, private participant details, or internal margins into the portable HTML. If a review is shared externally, inspect the HTML before sharing.

Examples:

```json
{"id":"market","title":"Refresh customers and competitors","skill":"evaluate-idea","status":"done","finding":"Two current rivals now offer self-service setup; the opportunity is still untested for small clinics.","source_ids":["S1","S2"],"next":"Interview six clinic managers about switching triggers."}
```

```json
{"name":"Assisted migration","type":"fix","value_range":"Estimate: 10–30 retained customers/year, assuming 20–40% uptake","effort_range":"Estimate: 2–5 person-weeks","evidence":"some","test":"Offer manual migration to five prospects for two weeks","source_ids":["S3"]}
```
