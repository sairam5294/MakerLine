---
name: quality-review
description: Product Kit review (WCAG 2.2, OWASP 2025, kit standards) — parallel multi-angle review (accessibility, UX, security, code, tests) of a branch/PR/screen → one prioritised findings report. Use for "review", "audit", "is it ready?", before merge or release.
---

# Quality Review

1. Scope: diff/branch/files/screens + stories implemented. Reviewers also get `docs/SECURITY.md` (security reviewer) and `docs/CODE_STYLE.md` (code reviewer) when they exist; a finding that changes a rule updates that doc. Prefer the diff (`git diff main...`) over whole files. Adopted project with no diff (STATUS.md says "adopted"): scope = the boot-path modules the project's own README/STATUS lists, plus `tests/`, config and workflows; sample large files by code path instead of reading them whole.
2. Run applicable reviewers in parallel (subagents) or in sequence; skip non-applicable ones and say so:
   accessibility-auditor → accessibility.md · ux-reviewer → ux.md + design system · security-reviewer → security/privacy/backend.md · code-reviewer → development/performance/mobile.md · qa-engineer → testing.md. Diff touches AI calls/prompts → security-reviewer + ux-reviewer also get ai.md.
   Pass each reviewer only the diff + its one standard file (saves tokens).
3. Verify each finding against the code; drop speculative ones; dedupe. Severity: breaking any standards MUST (incl. injection, missing UI states, secrets, authz, a11y AA) = MUST-violation — never downgrade because code is unused or "small".
4. Write `docs/product/reviews/YYYY-MM-DD-<scope>.md`: verdict (Ready / Ready after fixes / Not ready) · table severity (MUST / SHOULD / Suggestion) · area · file:line · problem · fix · short "what's good".
5. Offer to fix MUSTs now; SHOULDs become PLAN tasks.
