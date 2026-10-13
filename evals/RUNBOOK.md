# Running the kit evals

Cheap monthly set (~180k tokens): `review-planted-bugs`, `new-idea-pitch`.
Quarterly full set adds one evaluate-idea case (~120k tokens each): `ai-todo` (rotate `kids-devotional`, `community-amenities`).

Rules that keep evals honest:
1. **Runner never sees `expected.md`.** Run each case in a fresh subagent/session with only the skill files + the case input.
2. **Grader is separate.** After the run, a second pass compares the output with `expected.md` and `grade.md`.
3. Write outputs to `evals/runs/<YYYY-MM>/<case>/`, append a row to `results.md` (date, kit version, model, score, misses).
4. A score drop vs the last run = regression → open an issue / fix the skill, then re-run that case.

Manual run (Claude Code in the kit folder): "Run the monthly kit evals following evals/RUNBOOK.md."
