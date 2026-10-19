<!-- Template for docs/product/VALIDATION_RESULTS.md: what each validation test actually found, compared with the thresholds and kill criteria set in VALIDATION.md before testing, and how it moved the evaluation. -->
# Validation results — {{name}}

_Updated {{date}} · Plan: `docs/product/VALIDATION.md` · Evaluation: `docs/product/EVALUATION.md` v{{n}}_

<!-- Why a separate file: VALIDATION.md is the plan (written before testing, so the kill
     criteria can't drift). This file is the evidence. Keeping them apart makes it obvious
     if anyone edits a threshold after seeing the numbers. -->

## Summary

| V-id | Assumption | Test | n | Result vs kill criterion | Verdict |
|---|---|---|---|---|---|
| V-01 | A1 | interviews / landing page / prototype / concierge / pre-sale | | e.g. 3 of 8 had the pain (kill: < 4 of 8) | pass / fail / inconclusive |

**Kill criterion hit?** {{No / Yes — V-xx: one plain sentence on what it means. Recommendation: Pivot / Drop.}}

## V-01 — {{test name}}

| Field | Value |
|---|---|
| Date(s) | {{start – end}} |
| What was run | {{exact test: script, page URL, prototype link, offer and price}} |
| Assumption | A{{n}} from VALIDATION.md |
| Sample (n) | {{how many people / visits; where they came from}} |
| Raw numbers | {{counts, not just %: e.g. 1,140 visits → 37 signups (3.2 %)}} |
| Threshold (go) | {{copied from VALIDATION.md, unchanged}} |
| Kill criterion | {{copied from VALIDATION.md, unchanged}} |
| Verdict | pass / fail / inconclusive — {{why, in one line}} |
| What it changes | {{brief / scope / positioning / pricing / nothing}} |

**Themes** (counted across all participants — not the most quotable ones):

| Theme | Participants (count) | Example quote |
|---|---|---|
| | 5 of 8 (P1, P2, P4, P6, P7) | "…" — P4 |

**Surprises / counter-evidence:** {{what didn't fit the hypothesis; include it even if it hurts}}

<!-- Privacy: participants are P1, P2… only. No names, emails, phone numbers, employers
     or anything that identifies a person. Raw notes stay with the owner, outside the repo. -->

## Effect on the evaluation

Applied through evaluate-idea's **Refine** step — only rows backed by a V-id or R-id change.

| Dimension | Old score | New score | Evidence (V-id / R-id) |
|---|---|---|---|
| | | | |

**Verdict:** {{old}} → {{new}} (or unchanged) · EVALUATION.md revision-log row: v{{n}}

## CLARITY updates

| Q-id | Answered by | Answer in one line |
|---|---|---|
| | V-01 | |

## Revision log

| Date | V-ids added | Change |
|---|---|---|
