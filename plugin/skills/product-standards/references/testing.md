# Testing Standard

Goal: confidence to ship every week without manual regression marathons. Test behaviour users care about, not implementation details.

## 1. The test mix (testing trophy)

| Layer | What | Tools (defaults) | Target |
|---|---|---|---|
| Static | Types, lint, a11y lint | TypeScript strict, ESLint, jsx-a11y | 100% of code |
| Unit | Pure logic, utils, hooks | Vitest / Jest; XCTest / Swift Testing; JUnit | Business rules fully covered |
| Integration / component | Components with real children, API handlers with a test DB | Testing Library, MSW, Supertest, Supabase local | Every acceptance criterion |
| End-to-end | Critical user journeys on real build | Playwright (web), Maestro or Detox (mobile) | 3–10 journeys, run on every main build |
| Accessibility | Automated + manual | axe-core, Accessibility Inspector/Scanner, VoiceOver/TalkBack | Every screen |
| Visual | Screenshot diffs of key screens | Playwright screenshots / Chromatic | Key screens in light+dark |
| Security | Deps, secrets, SAST | `npm audit`/OSV, gitleaks, Semgrep/CodeQL | Every PR |
| Performance | Budgets | Lighthouse CI, app startup timing | Every release |

Coverage is a signal, not a goal: aim ≥ 80% on business logic, don't chase 100% on UI glue.

## 2. MUST rules

- Every user story's acceptance criteria map to at least one automated test (write the mapping in the PRD or PR).
- Every bug fix starts with a failing test that reproduces it.
- Never weaken a test to make it pass: no `skip`/`only`/`xit`, deleted assertions or loosened matchers without a linked issue and owner approval.
- Tests are deterministic: no real network, no real time (fake timers), seeded data, no order dependence.
- Query elements the way users find them: by role and label (`getByRole('button', { name: 'Save' })`), not by CSS class or test-id unless unavoidable.
- Test the unhappy paths: validation errors, network failure, empty data, permission denied, slow responses, session expiry.
- Test authorization: user A cannot read or change user B's data (for every resource endpoint).
- E2E runs on at least: Chrome + Safari (WebKit) for web (the starters run WebKit in CI; locally with `PW_WEBKIT=1` after `npx playwright install webkit`); one small Android device + one iPhone for mobile.

## 3. Test-plan template (per feature)

```
Feature: <name>
Risks: <what could go wrong for users / data / money>
Acceptance criteria → tests:
  AC1 … → unit: …; integration: …; e2e: …
Edge cases: empty, max length, unicode/Indic text, RTL (if any), offline, slow 3G, double-tap, back button mid-flow
Accessibility: keyboard, screen reader, 200% text, contrast
Devices/browsers: …
Test data: …
Exit criteria: all MUST tests green, no open P0/P1 bugs
```

## 4. Bug severity

| Severity | Examples | Action |
|---|---|---|
| **P0** | data loss, security hole, crash on launch, payments wrong | stop the release |
| **P1** | core journey blocked for some users, a11y blocker | fix before release |
| **P2** | workaround exists | schedule |
| **P3** | cosmetic | backlog |

## 5. Before every release

- Full e2e suite green on release build; smoke test on a real low-end Android device.
- Manual exploratory session (30 min) on the new feature using the test plan's edge cases.
- Crash-free sessions ≥ 99.5% on the previous release before widening rollout.
