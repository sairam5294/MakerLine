---
name: evaluate-idea
description: Evaluate my product idea honestly. Covers strongest version, reality check, scorecard, users and market, competitors with a differentiator test, strengthening plan with a path to Go, tools and cost, accessibility and compliance, validation tests → EVALUATION.md + COMPETITORS.md. Trigger with "evaluate my idea", "critique this", "who are my competitors?", "is this worth building?", or after new-idea.
argument-hint: "<idea, or nothing to use docs/product/PROJECT_BRIEF.md>"
---

# /evaluate-idea

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Give the owner an honest, researched verdict on their idea — and the best version of it worth testing.

**Stance: honest coach, not judge.** Tell the truth about weaknesses, then show how to make the idea stronger. A weak idea gets a clear "not like this" *and* the best version worth testing; a valid idea gets a plan to make it better, not a pat on the back.

## Usage

```
/evaluate-idea                       # uses docs/product/PROJECT_BRIEF.md
/evaluate-idea quick                 # Quick depth (see Depth below)
/evaluate-idea who are my competitors?
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                     EVALUATE IDEA                            │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Four perspectives: evidence, critic, champion, access.    │
│  ✓ Competitors in four rings + 5-question differentiator test│
│  ✓ Scorecard with "raise it by…" for every weak score        │
│  ✓ Strengthening plan with a path to Go                      │
│  ✓ Tools and monthly cost · validation tests · clarity log   │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Knowledge base: prior research and decisions              │
│  + Analytics: real usage numbers for an existing product     │
│  + Source control: what already exists in the repo           │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `docs/product/PROJECT_BRIEF.md` and `CLARITY.md`.
  - No brief → run `new-idea` first.
  - Brief but no `CLARITY.md` → create it from `../new-idea/references/clarity-template.md` from the brief's gaps, set STATUS Discovery to `Skipped (brief supplied)`, carry on.
- `docs/product/OWNER.md` for feasibility (missing or blank → use the brief's owner section; log it in DECISIONS.md; calibration = *"No calibration data yet"*).
- STATUS and DECISIONS: create from `../product-kickoff/templates/STATUS.md` and `DECISIONS.md` if missing.
- Owner unavailable or says *"just do it"*: don't ask — take marked defaults (`../new-idea/SKILL.md` → Owner unavailable), log each in DECISIONS.md as *unconfirmed*, list them first in CLARITY.md.
- Depth: **Quick** — follow `references/quick-run.md` instead of this file (whole Quick run in one guide), **Standard** (default) or **Deep** — budgets in `../product-standards/references/context-budget.md`.
- Quality bar: `examples/example-evaluation.md` (long — open only if unsure).

## Workflow

1. **Research with sources.** Reuse `docs/product/research/*.md` first (format: `references/research-cache.md`, sources < 30 days old). Search only what's missing, inside the depth budget, and save new findings there with R-ids. Cover:
   - competitors in four rings (direct, indirect, substitutes, doing nothing) — prices, ratings, review complaints
   - audience-size inputs, pricing benchmarks, distribution channels, legal and platform constraints
   - no web → say so; mark estimates as assumptions.
2. **Run four perspectives in parallel** (subagents where available): `market-researcher` (evidence), `devils-advocate` (strongest case against), `idea-champion` (strongest case for, best version), `accessibility-strategist` (who it excludes, obligations in the launch markets, competitors' accessibility gaps, accessibility as a strength).
   - Quick: all four inline, ≤ 5 lines each; Standard without subagents: ≤ 10 lines each. Inline perspectives are working notes — they feed §2 and §3, they don't get their own section.
   - Merge into report §2 (strongest version, honest ceiling) and §3 (failure modes, "what would have to be true"). Where they disagree, add *"Perspectives disagree on…"* and let the evidence decide.
3. **Competitive analysis.** Follow `references/competitive-analysis.md` → `docs/product/COMPETITORS.md`: landscape, leader profiles with mined complaints, job matrix, positioning map, head-to-head, the 5-question differentiator test, "why hasn't anyone done this", wedge and positioning statement. Quick → `references/competitors-lite.md` instead (don't open the full method).
4. **Score** with `references/scoring-rubric.md`: one line of evidence per score, and "raise it by…" for every score ≤ 6. Score the idea **as briefed**; the strongest version's score is the target. Calibrate with the kit's `portfolio/OUTCOMES.md` (path in OWNER.md) — or write *"No calibration data yet"* without searching.
5. **Write** `docs/product/EVALUATION.md` from `references/report-template.md` (Quick: `references/report-template-quick.md`), in its order: verdict → strongest version → reality check → users and market → competitive summary → differentiation → strengthening plan with a path to Go → business → feasibility, tools and cost → accessibility, inclusion and compliance (`../product-standards/references/accessibility-law-summary.md`; Deep only: grep the launch market's rows in `accessibility-law.md`) → validation tests with kill criteria → clarity questions → sources. Tables over prose; cite R-ids; show sizing maths; label Evidence / Estimate / Opinion. Stay inside the size cap (Standard ≤ 3,000 words incl. tables) — cut prose, not evidence; then run `python3 ../product-kickoff/scripts/check_idea_pack.py . --only EVALUATION.md COMPETITORS.md CLARITY.md` and fix what it flags.
6. **Update `CLARITY.md`.** Answered questions move down with their source; new unknowns get "how to find out"; assumptions get their test.
7. **Present** (≤ 15 lines): verdict · what's promising · top 3 risks · top 3 strengthening moves · the cheapest test that could change the verdict · 3–6 questions.
8. **Refine** each round: bump the brief version, update only affected sections, add a revision-log row. Re-score only on new facts — never because the owner pushed back; a good argument without evidence becomes a test.
   - Never regenerate the whole report: add a *What changed in v{n}* block under the title line (≤ 5 bullets, each citing its trigger — brief version, Q-id, V-id). Results from validate-idea arrive here.
9. **Gate.** Only the owner approves: `scripts/approve.sh` (types YES; writes STATUS + DECISIONS + commit). Never write `Evaluation: APPROVED` yourself; with no shell, write it only after the owner's explicit words in this conversation, quoted in DECISIONS.md. Then offer `design-direction`, `validate-idea` or `name-product`.

## Output

| File | What | Size (Standard) |
|---|---|---|
| `docs/product/EVALUATION.md` | the report, 14 sections | ≤ 3,000 words incl. tables |
| `docs/product/COMPETITORS.md` | landscape, profiles, matrix, map, differentiator test | ≤ 1,200 words |
| `docs/product/research/*.md` | facts with R-ids and sources | — |
| `docs/product/CLARITY.md` | updated open questions and assumptions | ≤ 1,000 words |

**Pivot verdict:** EVALUATION §1 states the verdict as *Pivot* and describes the pivot in §2. Later Idea Pack phases design and spec the *recommended pivot*, labelled "Pivot: …" at the top, with one line on what changes if the owner keeps the brief as written. The owner can switch back at any time.

## If connectors available

If **~~knowledge base** is connected:
- Search prior research, specs and decisions on the topic before searching the web.

If **~~product analytics** is connected (existing product):
- Pull real usage numbers for the problem-severity and retention scores.

If **~~source control** is connected (adopted project):
- Read the README and STATUS to score what already exists, not what's planned.

## Rules

- No hype and no cynicism; every criticism comes with a fix or a test.
- "Unknown + how to find out" beats an invented number; never invent competitors, reviews or figures.
- Judge feasibility for *this* owner's time, skills and budget; always assess distribution.
- Learning or portfolio projects get the second lens in the rubric: say if it's a Drop as a business but a Go as a portfolio or personal tool.

## Tips

1. Say *"quick"* for a first look at several ideas; *"deep"* before spending money.
2. Push back with evidence, not opinion — a good argument becomes a validation test, not a higher score.
3. The strongest version (§2) is the one to approve; the brief is the one that was scored.

## Related

- Before: `new-idea` · After: `design-direction`, `validate-idea`, approval, `name-product`
- Reads: `references/scoring-rubric.md`, `report-template.md` / `report-template-quick.md`, `competitive-analysis.md` / `competitors-lite.md`, `research-cache.md`; `../product-standards/references/context-budget.md`, `accessibility-law-summary.md` (Deep: `accessibility-law.md`), `inclusion.md`
