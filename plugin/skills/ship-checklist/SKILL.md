---
name: ship-checklist
description: Product Kit pre-launch checklist (web + App Store/Play) — quality, security, privacy, expert review, stores, monitoring, rollout/rollback → RELEASE.md. Use for "ship", "launch", "release", "submit to app store", "ready to launch?".
---

# Ship Checklist

1. Read STATUS, latest review, TEST_PLAN results, TECH_STACK.
2. Mark each item ✅/❌/N/A with evidence; run what can be verified (tests, build, `npm audit`, gitleaks, header check).
3. Write `docs/product/RELEASE.md` (version, date, results, known issues, rollout, rollback). Any ❌ in a MUST block stops release unless the owner accepts the risk in DECISIONS.md.

**Quality (MUST)** tests green on release build · no P0/P1 · no open MUST review findings · axe clean + manual screen-reader pass + a usability round with 3–5 assistive-tech users (`../test-plan/references/accessibility-user-testing.md`) · performance budgets met on low-end Android.
**Security & privacy (MUST)** audit + secrets scan clean, exposed keys rotated · authz/RLS tests green, admin MFA · headers (web) / obfuscation, debug off (mobile) · privacy policy, terms, data inventory, store privacy labels accurate · account deletion + export work · children's rules met if relevant.
**Expert review (MUST if payments, children's data, health/finance data, or > 10k users)** — send a professional the brief from `references/expert-review.md`; record outcome.
**Operations (MUST)** error tracking with source maps · uptime monitor · billing alerts · backups + tested restore · rollback tested · success-metric events verified in prod.
**Stores** icons, screenshots, copy, support + privacy URLs · age rating / Kids & Families rules · TestFlight/internal test with 5+ real users · staged rollout · minimum-version check.
**Launch** landing/store page live · waitlist notified · in-app feedback · week-1 monitoring owner · post-launch reviews at week 1 and 4 (post-launch skill).
