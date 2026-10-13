---
name: evaluate-idea
description: Product Kit honest, researched Idea Evaluation Report (verdict, scorecard, critique, user base, market size, competitors, value add, improvements, validation test) with refinement rounds until owner approves. Use after discovery or for "evaluate/critique/validate my idea".
---

# Evaluate Idea

Input: `docs/product/PROJECT_BRIEF.md` (missing → run new-idea first). Quality bar: `examples/example-evaluation.md` (long — open only if unsure).

1. **Research with sources** — first reuse `docs/product/research/*.md` (format: `references/research-cache.md`; sources < 30 days old); only search what's missing, then save new findings there (topic, date, URL, fact). Web search: competitors + substitutes (incl. YouTube/WhatsApp/doing nothing) with ratings, prices, top review complaints; audience-size inputs; pricing benchmarks; legal/platform constraints. With subagents: run `market-researcher` and `devils-advocate` in parallel and merge their summaries. No web → say so, mark estimates as assumptions.
2. **Score** with `references/scoring-rubric.md`; each score gets one line of evidence. Feasibility uses `docs/product/OWNER.md`. **Calibrate**: read the kit's `portfolio/OUTCOMES.md` (path in OWNER.md; fallback `docs/product/OUTCOMES-snapshot.md`) and apply its calibration notes — say which ones changed a score.
3. **Critique first**: ≥ 3 serious risks before any Go; separate fatal flaws from manageable risks.
4. **Write** `docs/product/EVALUATION.md` from `references/report-template.md`. Aim for 1,500–2,500 words — tables over prose, detail in an appendix; show sizing math; label Evidence / Estimate / Opinion; sources at the end.
5. **Present** in ≤ 15 lines: verdict, top 3 risks, top 3 improvements, cheapest validation test + kill criteria, 3–6 refinement questions.
6. **Refine** each round: bump brief version, update only affected sections (re-research only what changed), add revision-log row. Re-score only on new facts — never because the owner pushed back.
7. **Gate** — only the owner approves. Ask them to run `scripts/approve.sh` (types YES; writes STATUS + DECISIONS + commit). Never write `Evaluation: APPROVED` yourself; where there's no shell (Claude Cowork/desktop), write it only after the owner's explicit approval in this conversation and quote their words in DECISIONS.md. Log verdict + accepted risks, then offer validate-idea (if not done) or name-product.

Rules: no hype; "unknown + how to find out" beats invented numbers; judge feasibility for this owner's time/skills/budget; always assess distribution; every criticism comes with a fix or test. Learning projects: say if it's a Drop as a business but a Go as learning.
