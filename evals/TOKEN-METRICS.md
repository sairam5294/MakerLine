# Token metrics and strategy

What a MakerLine run costs, measured, and how the kit keeps that cost down without losing quality. Every number below comes from a real run in this repo's test setup. Raw rows live in `results.md`.

_Last measured 2026-10-22 · kit 0.14.1 plus the 0.15.0 changes · model: Claude (Opus class), same setup for every row._

## How to read the numbers

- **Total** is what the run used, end to end.
- **Harness** is what an empty run uses in the same setup before MakerLine does anything: about **78,000 tokens** (the app's own instructions and tools; measured 2026-10-21, re-measured monthly by the evals task).
- **MakerLine's share** = total − harness. That's the part the kit controls.
- **Quality comes first.** A saving only counts if the run still passes its check (checker clean, recovery score held, no new wrong claims).
- One run per row unless stated: treat differences under ~10% as noise.

## Measured runs

| Run | What it did | Total | MakerLine's share | Tool calls | Time | Quality |
|---|---|---|---|---|---|---|
| Quick Idea Pack, 0.11.0 | brief → one-pager | 157k | ~79k | 30 | — | checker clean after 3 trims |
| Quick Idea Pack, 0.14.0 | same, after budget caps | 106k | **~28k** | 12 | — | checker clean first time |
| Opportunity review, Lekka (half-built) | standard depth, 8 searches, 8 fetches | 147k | ~69k | 29 | 3.4 min | check clean |
| Opportunity review, Trust Kit (idea) | standard, 10 searches, 13 fetches (4 failed) | 142k | ~64k | 34 | 13.2 min | check clean |
| Opportunity review, RhythmBuddy (live) | standard, 8 searches, 12 fetches (2 blocked) | 137k | ~59k | 36 | 13.3 min | check clean |
| Opportunity review, Tindi (3 apps, 2 repos, ~68k words of docs) | standard, 7 searches, 13 fetches | 175k | ~97k | 43 | 6.1 min | check clean, no warnings |
| Context recovery, before the index | fresh tool, folder only, 10 questions | 104k | ~26k | 7 | 50 s | 7/10 by hand |
| Context recovery, with the index | same, with `CONTEXT_INDEX.md` | 100k | **~22k** | 11 | 48 s | **10/10** |
| Context recovery, pack only | browser-style tool, one 3,200-word pack | 95k | **~17k** | 3 | 41 s | **10/10** |
| Context recovery, Tindi with the index | two repos, per-app rows, section anchors | 114k | ~36k | 16 | 84 s | 9/10 by hand, 0 wrong claims |

**What this shows**

1. **The shared context makes recovery more accurate, not just cheaper.** With the index or the pack, a fresh tool got all ten answers right. Without them it got seven, because the active task, the expiry dates and the last session weren't written down anywhere. The index also cut the share by about 15%, and the pack by about 35%.
2. **A standard opportunity review costs about 60–70k of MakerLine's share**, roughly twice a Quick Idea Pack. Web pages are most of it: each fetch costs tokens, and blocked or failing pages also cost minutes (two runs lost about 10 minutes waiting on pages that never opened).
3. **Bigger products cost more, but not in proportion.** Tindi has 10–20 times RhythmBuddy's documentation; its review cost about 1.3 times as much in total (1.6 times MakerLine's share), and a task pack holds 2–7% of the docs because the index points at sections (`SCALE.md`).
4. **Reuse is the biggest lever.** Trust Kit reused its Idea Pack research and still spent 10 searches checking what had changed. A refresh should open only sources older than their review-by date.

## Strategy

| Lever | Rule | Where it lives | Status |
|---|---|---|---|
| Index first | Read `AGENTS.md` → `CONTEXT_INDEX.md` → your task's row only | handoff skill, `shared-context.md`, `context-budget.md` | Shipped (0.15.0) |
| Pack for browser tools | Send ChatGPT one generated pack, not the repo | `context_check.py pack` | Shipped (0.15.0) |
| Research once, cite by ID | Facts get IDs (S1, A-01, D-01); later runs cite the ID | `context-budget.md` rule 1, review record | Shipped |
| Evidence expiry | Re-open a source only after its review-by date | `ASSUMPTIONS.md`, review `sources` dates | Shipped (0.15.0) |
| Fetch budget for reviews | Standard review: ≤ 10 searches, ≤ 6 page reads; skip a page that doesn't open on the first try and use the kit's own reference with its date | review SKILL.md | **Proposed** — target share ≤ 50k |
| Model routing | Fast model for filling records and summaries; strongest for the decision | `context-budget.md` §5 | Shipped; not yet measured |
| Quality guard | No saving counts if the checker, recovery score or wrong-claim count gets worse | this file, `context-recovery/README.md` | Shipped |

**Targets for the next measurement (proposed, not yet met)**

| Run | Now (share) | Target |
|---|---|---|
| Quick Idea Pack | ~28k | hold, ≤ 30k |
| Opportunity review, standard | ~59–69k | ≤ 50k, same check result |
| Context recovery with index or pack | ~17–22k | ≤ 20k, 10/10, 0 wrong claims |

## What to record per run

`evals/results.md`, one row per run: date · kit version · model · task · total tokens · harness baseline · MakerLine's share · tool calls · searches · page reads (failed) · files read · time · redos · quality result · **cost per accepted decision** (share ÷ decisions the owner accepted; filled in once the owner accepts or rejects the recommendation).

## Limits of these numbers

- One run per row, one model, one test setup. Your Claude app's harness differs, so compare shares, not totals.
- The cockpit doesn't track tokens yet; these come from the agent runner's usage report.
- ChatGPT and Cursor runs haven't been measured yet (owner action; see `context-recovery/README.md`).
