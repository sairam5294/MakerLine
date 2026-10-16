---
name: evaluate-idea
description: Product Kit honest, researched and constructive Idea Evaluation — strongest version of the idea, reality check, scorecard, users and market, competitors with a differentiator test (COMPETITORS.md), strengthening plan with a path to Go, provisional tools and cost, validation tests — refined until the owner approves. Use after discovery or for "evaluate/critique/validate my idea", "who are my competitors?".
---

# Evaluate Idea

Input: `docs/product/PROJECT_BRIEF.md` + `CLARITY.md` (missing → run new-idea first). Quality bar: `examples/example-evaluation.md` (long — open only if unsure).

**Stance: honest coach, not judge.** Tell the truth about weaknesses, then show how to make the idea stronger. A weak idea gets a clear "not like this" *and* the best version worth testing; a valid idea gets a plan to make it better, not a pat on the back.

1. **Research with sources** — reuse `docs/product/research/*.md` first (format: `references/research-cache.md`; sources < 30 days old); search only what's missing and save new findings there. Cover: competitors in four rings (direct, indirect, substitutes, doing nothing) with prices, ratings and review complaints; audience-size inputs; pricing benchmarks; distribution channels; legal/platform constraints. No web → say so and mark estimates as assumptions.
2. **Run three perspectives in parallel** (subagents where available, else in sequence): `market-researcher` (evidence), `devils-advocate` (strongest case against), `idea-champion` (strongest case for, and the best version). Merge; where they disagree, say so and let the evidence decide.
3. **Competitive analysis** — follow `references/competitive-analysis.md` and write `docs/product/COMPETITORS.md`: landscape, leader profiles with mined complaints, job matrix, positioning map, head-to-head, the 5-question differentiator test, "why hasn't anyone done this", wedge and positioning statement.
4. **Score** with `references/scoring-rubric.md`; one line of evidence per score, plus how to raise every score ≤ 6. Feasibility uses `docs/product/OWNER.md`. **Calibrate** with the kit's `portfolio/OUTCOMES.md` (path in OWNER.md; fallback `docs/product/OUTCOMES-snapshot.md`) — say which notes changed a score.
5. **Write** `docs/product/EVALUATION.md` from `references/report-template.md`: verdict and "in one minute" → strongest version → reality check (≥ 3 serious risks; fatal flaws separated, each with a fix) → users and market → competitive summary → differentiation → **strengthening plan with a path to Go** → business → feasibility with provisional tools and cost → validation tests with kill criteria → clarity questions → sources. 2,000–3,000 words; tables over prose; show sizing math; label Evidence / Estimate / Opinion.
6. **Update CLARITY.md**: answered questions move down with their source; new unknowns from research go in with how to find out; assumptions get their test.
7. **Present** in ≤ 15 lines: verdict, what's promising, top 3 risks, top 3 strengthening moves, the cheapest test that could change the verdict, 3–6 questions.
8. **Refine** each round: bump the brief version, update only affected sections (re-research only what changed), add a revision-log row. Re-score only on new facts — never because the owner pushed back; when they push back with a good argument but no evidence, turn it into a test.
9. **Gate** — only the owner approves. Ask them to run `scripts/approve.sh` (types YES; writes STATUS + DECISIONS + commit). Never write `Evaluation: APPROVED` yourself; where there's no shell (Claude app), write it only after the owner's explicit approval in this conversation and quote their words in DECISIONS.md. Log the verdict and accepted risks, then offer design-direction (if not done), validate-idea, or name-product.

Rules: no hype and no cynicism; "unknown + how to find out" beats invented numbers; judge feasibility for this owner's time, skills and budget; always assess distribution; every criticism comes with a fix or a test; never invent competitors, reviews or figures. Learning projects: say if it's a Drop as a business but a Go as learning.
