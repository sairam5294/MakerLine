---
name: quality-review
description: Review a branch, PR, diff or screen against the kit standards (WCAG 2.2, OWASP 2025) — parallel accessibility, UX, security, code and test reviewers, verified findings, one prioritised report with a verdict → docs/product/reviews/. Trigger with "review", "audit", "is it ready?", before merge or release, or after build-feature.
argument-hint: "<branch, PR, files or screen to review; nothing = diff against main>"
---

# /quality-review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run five specialist reviews on the same change and hand the owner one verified, prioritised findings report with a Ready / Not ready verdict.

**Why:** each reviewer sees the diff plus one standard, so nothing is missed for lack of context and nothing is invented for lack of code.

## Usage

```
/quality-review                      # git diff main... on the current branch
/quality-review PR #12
/quality-review Settings screen      # a screen plus its stories
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                      QUALITY REVIEW                          │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Five reviewers: accessibility, UX, security, code, QA     │
│  ✓ Each gets only the diff + its one standard file           │
│  ✓ Findings verified against code, deduped, severity-rated   │
│  ✓ One report: verdict · MUST / SHOULD / Suggestion table    │
│  ✓ Offer to fix MUSTs now; SHOULDs become PLAN tasks         │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Source control: read the PR diff, post findings as review │
│  + Project tracker: SHOULDs filed as tasks                   │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- Scope: diff / branch / files / screens + the stories implemented. Prefer the diff (`git diff main...`) over whole files.
- Adopted project with no diff (STATUS.md says "adopted"): scope = the boot-path modules the project's own README/STATUS lists, plus `tests/`, config and workflows; sample large files by code path instead of reading them whole.
- `docs/SECURITY.md` (security reviewer) and `docs/CODE_STYLE.md` (code reviewer) when they exist.
- Standards: `../product-standards/references/*.md` (one file per reviewer, table below).
- Ask the owner only for the scope if it isn't clear from STATUS.md or the branch.

## Workflow

1. **Set the scope.** Diff/branch/files/screens + stories implemented; prefer `git diff main...`. Adopted project with no diff → boot-path modules, `tests/`, config and workflows, sampled by code path.
   - Reviewers also get `docs/SECURITY.md` (security) and `docs/CODE_STYLE.md` (code) when they exist; a finding that changes a rule updates that doc.
2. **Run the applicable reviewers** in parallel (subagents) or in sequence; skip non-applicable ones and say so.
   - Pass each reviewer only the diff + its one standard file (saves tokens).
   - Diff touches AI calls/prompts → security-reviewer + ux-reviewer also get `ai.md`.
3. **Verify each finding** against the code; drop speculative ones; dedupe.
   - Severity: breaking any standards MUST (incl. injection, missing UI states, secrets, authz, a11y AA) = MUST-violation — never downgrade because code is unused or "small".
4. **Write the report** `docs/product/reviews/YYYY-MM-DD-<scope>.md` (shape below).
5. **Offer to fix MUSTs now;** SHOULDs become PLAN tasks.

### Reviewers and their standard

| Reviewer | Standard file (`../product-standards/references/`) |
|---|---|
| accessibility-auditor | `accessibility.md` |
| ux-reviewer | `ux.md` + design system |
| security-reviewer | `security.md`, `privacy.md`, `backend.md` |
| code-reviewer | `development.md`, `performance.md`, `mobile.md` |
| qa-engineer | `testing.md` |
| (AI in the diff) | security-reviewer + ux-reviewer also get `ai.md` |

## Output

| File | What |
|---|---|
| `docs/product/reviews/YYYY-MM-DD-<scope>.md` | verdict (Ready / Ready after fixes / Not ready) · findings table · short "what's good" |
| `docs/SECURITY.md`, `docs/CODE_STYLE.md` | updated when a finding changes a rule |

Findings table columns: severity (MUST / SHOULD / Suggestion) · area · file:line · problem · fix.

Present to the owner (≤ 10 lines): verdict · count per severity · the MUSTs · offer to fix them now · SHOULDs to be added to PLAN.

## If connectors available

If **~~source control** is connected:
- Read the PR diff and existing review comments as the scope; post the findings as a PR review only when the owner asks in chat.

If **~~project tracker** is connected:
- File SHOULDs as PLAN tasks / tickets linked to the review file, on request.

## Rules

- A MUST violation is a MUST violation — never downgrade because code is unused or "small".
- Every finding is verified against the code; speculative findings are dropped, duplicates merged.
- Each reviewer gets the diff + one standard file only; skipped reviewers are named in the report.
- A finding that changes a project rule updates `docs/SECURITY.md` or `docs/CODE_STYLE.md`.

## Tips

1. Review per branch, not per milestone — small diffs get sharper findings.
2. Say *"security only"* or *"a11y only"* for a focused pass on a hot spot.
3. Keep the "what's good" section — it tells the owner which patterns to repeat.

## Related

- Before: `build-feature`, `design-qa` · After: `test-plan`, `ship-checklist`
- Reads: `../product-standards/references/accessibility.md`, `ux.md`, `security.md`, `privacy.md`, `backend.md`, `development.md`, `performance.md`, `mobile.md`, `testing.md`, `ai.md`; `docs/SECURITY.md`, `docs/CODE_STYLE.md`
