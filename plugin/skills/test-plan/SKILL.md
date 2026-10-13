---
name: test-plan
description: Product Kit test strategy for a feature/release — map criteria to tests, edge cases, devices, write missing tests, report vs exit criteria → TEST_PLAN.md. Use for "test plan", "write tests", "QA this".
---

# Test Plan

1. Read the stories, TECH_STACK test tools, `../product-standards/references/testing.md`.
2. Write/update `docs/product/TEST_PLAN.md` (template in testing.md): risks · AC→test map · edge cases (empty, long/Indic text, offline, slow network, double submit, back mid-flow, session expiry, permission denied) · a11y checks · device matrix · data · exit criteria.
3. Find gaps (untested ACs, unhappy paths, authz tests); write missing tests; run; fix or report.
4. Give a ≤ 30-min manual script for screen readers / real devices. Before launch (and on the prototype), plan a round with real assistive-tech users: `references/accessibility-user-testing.md`.
5. Report: pass/fail per exit criterion, bugs P0–P3, ship / fix-first.
