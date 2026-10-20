---
name: post-launch
description: Review how the launched product is doing. Covers weekly metrics review, feedback synthesis, retros, next priorities and lessons fed back into the kit → METRICS.md, COSTS.md, LESSONS.md, OUTCOMES.md row. Trigger with "how is it doing", "metrics review", "user feedback", "retro", "what next after launch", or weekly after ship-checklist.
argument-hint: "<weekly | retro | outcome | end, or nothing for the weekly review>"
---

# /post-launch

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Turn a launched product into evidence: what the numbers and users say, what to do next, and what the kit should learn.

**Why:** a launch without a loop drifts. Decide with evidence — persevere, iterate, or pivot — tied back to the EVALUATION kill criteria.

## Usage

```
/post-launch                 # weekly review (15 min) → METRICS.md
/post-launch retro           # every 2–4 weeks → LESSONS.md
/post-launch outcome         # weeks 4, 12 or when parked → portfolio/OUTCOMES.md
/post-launch end             # project end / major milestone → kit improvements
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                       POST-LAUNCH                            │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Weekly metrics vs last week and target, > 20% flagged     │
│  ✓ Feedback themes with counts and quotes                    │
│  ✓ Monthly cost vs success metric                            │
│  ✓ Retro → LESSONS.md · outcome row → OUTCOMES.md            │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Product analytics: metrics pulled, not asked for          │
│  + Monitoring: crash-free % and performance from the source  │
│  + Chat: feedback threads and a posted weekly summary        │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `docs/product/METRICS.md` (last week's row), `EVALUATION.md` (success metric, kill criteria), `PLAN.md`.
- Numbers: from analytics/Sentry/stores via MCP if connected, else ask the owner for them.
- Monthly: the owner's bills (AI tools, hosting, stores).
- Feedback sources: store reviews, support, interviews.

## Workflow

1. **Weekly review (15 min)** → append to `docs/product/METRICS.md`.
   - Pull the success metric + inputs: activation, retention D1/D7/D30, conversion, crash-free %, performance.
   - Compare to last week and target; flag changes > 20%; one-line hypothesis each.
2. **Synthesize new feedback** (store reviews, support, interviews): themes, counts, quotes.
3. **Monthly costs.** Ask the owner for the month's bills (AI tools, hosting, stores) → `docs/product/COSTS.md`; compare cost vs the success metric (cost per active user / per paying user).
4. **Decide.** Output 3 findings · 1–3 actions → PLAN.md tasks. Decide with evidence: persevere, iterate, or pivot — tie back to EVALUATION kill criteria.
5. **Retro (every 2–4 weeks)** → `docs/product/LESSONS.md`: what worked · what didn't · what we'll change · kit improvements (skill/rule/standard that was wrong or missing).
6. **Outcome log (weeks 4, 12 and when parked).** Add/update this project's row in the kit's `portfolio/OUTCOMES.md`: verdict & score at approval vs what happened, metric vs target, total cost from COSTS.md. When a pattern repeats across projects, add a calibration note for evaluate-idea.
7. **Project end / major milestone.** List kit improvements as concrete edits (file + change) for the MakerLine repo's `LESSONS.md` and CHANGELOG.

## Output

| File | What | Cadence |
|---|---|---|
| `docs/product/METRICS.md` | weekly row: metrics, deltas, hypotheses, feedback themes | weekly |
| `docs/product/COSTS.md` | month's bills, cost per active / paying user | monthly |
| `docs/product/PLAN.md` | 1–3 new tasks from the findings | weekly |
| `docs/product/LESSONS.md` | retro: worked · didn't · change · kit improvements | every 2–4 weeks |
| `portfolio/OUTCOMES.md` (kit) | this project's outcome row, calibration notes | weeks 4, 12, parked |

Present to the owner (≤ 8 lines):

```
Metric vs target: <value> (<delta> vs last week)
Findings: 1. … 2. … 3. …
Actions → PLAN: 1. … 2. …
Decision: persevere / iterate / pivot — because <kill criterion>
```

## If connectors available

If **~~product analytics** is connected:
- Pull activation, retention D1/D7/D30 and conversion directly; ask the owner only for what it lacks.

If **~~monitoring** is connected:
- Read crash-free % and performance for the week; link the top new error in the findings.

If **~~chat** is connected:
- Scan feedback/support channels for the week's themes; post the ≤ 8-line summary where the owner asks.

## Rules

- Flag any metric change > 20% with a one-line hypothesis — never a bare number.
- Every finding leads to an action in PLAN.md or an explicit "watch".
- Persevere / iterate / pivot is decided against EVALUATION kill criteria, not mood.
- Kit improvements are concrete edits (file + change), not "improve the docs".

## Tips

1. Keep the weekly review to 15 minutes; depth belongs in the retro.
2. Count feedback themes — three users saying the same thing beats one loud one.
3. Log costs monthly even when they are zero; the trend is the point.

## Related

- Before: `ship-checklist` · Anytime: `handoff`, `portfolio`
- Reads: `docs/product/EVALUATION.md` (kill criteria), `METRICS.md`, `COSTS.md`, `PLAN.md`; writes `portfolio/OUTCOMES.md` for `evaluate-idea` calibration
