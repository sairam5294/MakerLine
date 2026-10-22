# Review record

`docs/product/opportunity/REVIEW.json` is versioned input for `scripts/opportunity_review.py`; the HTML is generated from it. Run `check` before `render`. The generator accepts UTF-8 text and escapes it for HTML. It does not render raw HTML from evidence.

Top-level fields:

- `schema_version`: `1`.
- `product`, `stage`, `depth` (`quick`, `standard`, `deep`), `mode` (`first`, `refresh`), `trigger`, `created`, `updated` (`YYYY-MM-DD`), `goal`, `goal_status`, `launch_markets`, `markets_status` (`proposed` until the owner confirms, then `confirmed`).
- `decision`, `decision_reason`, `confidence`: the answer first; confidence is `unknown`, `weak`, `medium` or `strong`.
- `steps`: route steps with `id`, `title`, `skill`, `status`, `finding`, `source_ids`, `next`. Status is `not_started`, `in_progress`, `blocked`, `done` or `skipped`. A completed step needs a finding. A skipped step explains why in `finding`.
- `sources`: `{id, title, url, date, kind}`. `date` is when you checked it (`YYYY-MM-DD`). `kind` is `official` (law, regulator, platform rules), `independent` (press, analysts, reviews), `vendor` (a company's claims about itself, including competitors' own pages), `community` (forums, social posts), `repo` (a file in this project; put the relative path in `url`) or `internal` (owner's private notes; refer by path, never copy private content). Source IDs cited anywhere must exist, and every source should be cited. Prefer official and primary sources for rules, technology and market claims.
- `rules`: launch-market rules, `{market, rule, applies, uncertainty, source_ids}`. `applies` is `yes`, `no`, `likely` or `unclear`. Not legal advice; escalate uncertain high-stakes questions.
- `unknowns`: `{question, blocks, how_to_answer}`.
- `options`: `{name, type, value_range, effort_range, evidence, test, source_ids}`. Ranges are strings that include units and explicit assumptions. `type` is build, fix, simplify, pricing, distribution, partnership or stop. `evidence` is `none`, `weak`, `some` or `strong`; strong evidence requires a source.
- `next_actions`: `{action, owner, when, success_measure}`; action, owner and success measure are required.
- When every step is `done` or `skipped`, `decision` can't still be "Pending evidence", and `options` and `next_actions` can't be empty.
- `tool_plan`: `{job, primary, fallback, handoff}`. Use only tools the owner has; one owner per output.

Keep public market links in `sources`. Keep private customer evidence in a project-local note and refer to it by file path and anonymised role. Never copy credentials, private participant details, or internal margins into the portable HTML. If a review is shared externally, inspect the HTML before sharing.

Examples:

```json
{"id":"market","title":"Refresh customers and competitors","skill":"evaluate-idea","status":"done","finding":"Two current rivals now offer self-service setup; the opportunity is still untested for small clinics.","source_ids":["S1","S2"],"next":"Interview six clinic managers about switching triggers."}
```

```json
{"name":"Assisted migration","type":"fix","value_range":"Estimate: 10–30 retained customers/year, assuming 20–40% uptake","effort_range":"Estimate: 2–5 person-weeks","evidence":"some","test":"Offer manual migration to five prospects for two weeks","source_ids":["S3"]}
```
