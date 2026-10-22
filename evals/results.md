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
| Quick run with budget caps (unreleased) | Checker clean first time (run 1) / after 1 fix (run 2); verdict Pivot via business lens when no goal stated | 11–12 calls, ~106–109k tokens (from 120k / 19 calls); 4 searches, ≤ 1 fetch |
| Harness baseline: empty agent (2026-10-21) | Replies "ok", no tools | ~78k tokens: the test setup's own instructions and tools. So the kit's own share of a 0.14.0 Quick run ≈ 106k − 78k ≈ 28k (≈ 42k at 0.12.1, if that run had the same baseline). Totals above include this overhead |

## Run 4 — 2026-10-22 · kit 0.14.1 + 0.15.0 changes · pilots and context recovery

Opportunity review pilots (standard depth, each in a fresh agent; harness ≈ 78k included in totals):

| Case | Result | Notes |
|---|---|---|
| RhythmBuddy (live) | **Test before investing more** (medium); check clean | 36 calls, ~137k; 8 searches, 12 fetches (2 blocked); 3 redos. Found: no access/decision step in the live route, shallow check |
| Lekka (half-built, not a MakerLine project) | **Narrow and test** (medium); check clean | 29 calls, ~147k; 8 searches, 8 fetches; 1 redo. Found: no reading list without STATUS.md, no rules field |
| Trust Kit (idea) | **Explore only as a test** (weak); check clean | 34 calls, ~142k; 10 searches, 13 fetches (4 failed); 1 redo. Found: conflicting approval records, no "reused" guidance, markets can't be marked proposed |

All findings fixed in the pilot-fixes PR; the new `check` then caught 4 invalid evidence values in the Trust Kit record.

Context recovery, RhythmBuddy, 10 questions (`context-recovery/README.md`), key written before the runs and kept outside the project:

| Path | Keyword score | Hand grade | Wrong claims | Tokens | Calls |
|---|---|---|---|---|---|
| Folder, before the index | 9/10 | 7/10 (C02, C07 partial: no task or handoff written down; C05 fail: no expiry dates) | 0 | ~104k | 7 |
| Folder, with `CONTEXT_INDEX.md` | 10/10 | 10/10 | 0 | ~100k | 11 |
| Pack only (ChatGPT-style) | 10/10 | 10/10 | 0 | ~95k | 3 |

The keyword scorer passed two answers that said "not recorded", so the README now asks for a hand grade too. The pack run asked for the review's source list and an explanation of the verified commit; both added.
