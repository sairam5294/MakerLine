# Kit evals — does evaluate-idea catch what it should?

Each case has a `PROJECT_BRIEF.md` with **planted flaws** and an `expected.md` (hidden from the evaluator) listing what a good evaluation must catch.

## Run
1. For each case, in a fresh session: "Run the evaluate-idea skill on evals/cases/<case>/PROJECT_BRIEF.md. Write the report to evals/runs/<case>/EVALUATION.md. Don't ask me questions — state assumptions." (Don't let it read expected.md.)
2. Grade with `grade.md` → record in `results.md`.
3. Re-run after changing any evaluate-idea file, scoring rubric, report template or the devils-advocate / market-researcher agents. A drop in score = regression.

Pass bar: every case ≥ 80% on the checklist and verdict inside the expected range.
