# Eval results

## Run 1 — 2026-09-27 · kit v0.2.0 · evaluate-idea (blind: evaluator never saw expected.md)

| Case | Verdict (expected) | Score | Universal checklist | Planted flaws caught | Result |
|---|---|---|---|---|---|
| kids-devotional | Pivot (Go w/ changes · Pivot) ✅ | 4.1 | 10/10 | 6/6: ads/analytics vs kids rules, DPDP/COPPA, child chat + photo/DOB, film-song + Suno rights, scope vs 80 h, 5k subs vs benchmarks (Kutuki ₹399, YouTube) | **Pass** |
| ai-todo | Pivot, Drop as written, Go as learning (Drop · Pivot) ✅ | 3.45 | 10/10 | 6/6: "everyone", crowded (Todoist, TickTick, free built-ins, ChatGPT), no differentiation, scope, 1M users vs budget, AI cost with free model | **Pass** |
| community-amenities | Pivot (Go w/ changes · Pivot) ✅ | 4.25 | 10/10 | 6/6: "no competitors" disproved (Mygate, ADDA, NoBrokerHood…), scope clash, RWA sales cycle, payment-aggregator rules, pricing/target, owner's contacts → pilot | **Pass** |

Hallucinations spotted: none in spot checks; unverifiable inputs were labelled as such (good).

## What the evals changed in the kit
- `examples/` folder was referenced but missing → added a golden example (ai-todo report).
- Reports ran ~4,000–4,500 words (~6k tokens) → added a 1,500–2,500-word target to keep reruns and refinement rounds cheaper.
- Cost reference: one full evaluation ≈ 110–120k tokens and ~5 minutes with web research. Refinement rounds should re-research only what changed.

## Run 2 — 2026-09-28 · kit v0.3.0 · quality-review + new-idea

| Case | Result | Notes |
|---|---|---|
| review-planted-bugs | **Pass — 11/11 planted issues found, 0 invented** | 2 severity misses: PostgREST filter injection and missing loading/empty/error states rated SHOULD (standards say MUST). → Added a severity rule to quality-review. Also found a real extra bug not planted: deleted row never removed from the list. |
| new-idea-pitch | **Pass — 10/11** | Pre-filled answers confirmed, not re-asked; provisional tech suggestion given; first-100 users and unfair advantage probed. Misses: first reply too long; "recommended" options on factual questions (leading questions). → new-idea now recommends only on decisions and keeps the first reply ≤ 150 words. |

## Run 3 — 2026-10-20 · kit v0.11.0 → 0.12.0 · blind (runner never saw expected.md)

| Case | Result | Notes |
|---|---|---|
| review-planted-bugs | **Pass — 11/11, 0 invented** | console.log of email rated MUST (key: SHOULD) — acceptable, privacy MUST. 8 tool calls, ~111k tokens |
| ontario-clinic-booking (evaluate-idea, Standard) | **Pass — 7/7, verdict Pivot (in range)** | AODA customer service vs web standard split by staff size, PHIPA agent agreement, older-patient wedge tested with the 5-question test. EVALUATION 2,952 words (cap 3,000). 34 calls, ~149k tokens |
| Quick Idea Pack, flatmates app (0.11.0) | Checker clean after 3 trims; verdict Pivot | 30 calls, ~157k tokens |
| Same, after trims (0.12.0) | **Checker clean first time**; verdict Pivot | 24 calls, ~146k tokens |
| Trust Kit, Quick → Standard continue (0.12.0) | Checker clean; gate untouched | 32 calls, ~161k tokens, 0 new searches (research reused) |
| Same, one-file Quick guide (0.12.1) | **Checker clean first time**; verdict Pivot (Low) | 19 calls, ~120k tokens (from 157k / 30 calls at 0.11.0); 7 searches, 4 reads |
