---
name: product-standards
description: Product Kit quality rulebook — accessibility (WCAG 2.2 AA, iOS/Android), UX, development, testing, backend, security (OWASP 2025, MASVS), privacy, performance, mobile, AI features. Use when designing, building, reviewing or testing anything.
---

# Product Standards

Definition of done. Load **only** the reference files the task touches:

| Area | File |
|---|---|
| Accessibility | references/accessibility.md |
| Accessibility law by market (AODA, ADA, 508, EAA, UK, India…) | references/accessibility-law.md |
| UX, states, copy | references/ux.md |
| Code, git, deps | references/development.md |
| Tests | references/testing.md |
| API, DB, ops | references/backend.md |
| Security | references/security.md |
| Privacy, children, payments | references/privacy.md |
| Speed budgets | references/performance.md |
| iOS/Android, stores | references/mobile.md |
| AI features, AI content | references/ai.md |
| Context/token budget, local models | references/context-budget.md |

MUST = always. SHOULD = default; skipping needs a reason in DECISIONS.md. Report findings as MUST-violation / SHOULD-gap / Suggestion with location + fix. Versions tracked in VERSIONS.md.

**Always (no file needed):** no secrets in code/logs/client · every control has an accessible name and works with keyboard/screen reader · contrast ≥ 4.5:1 (3:1 large text, UI boundaries) · targets ≥ 44pt/48dp · loading/empty/error/offline/success states · server-side authorization + schema validation + parameterized queries · tests for every acceptance criterion · minimum personal data.
