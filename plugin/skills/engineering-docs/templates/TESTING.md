# Testing — {{product}}

_Updated {{date}} · Standard: `.agents/skills/product-standards/references/testing.md` · Plan per release: `docs/product/TEST_PLAN.md`_

## 1. Test mix and tools
| Layer | Tool | What it covers | Run |
|---|---|---|---|
| Static | TypeScript strict, ESLint (incl. jsx-a11y), Prettier | types, lint, a11y lint | `{{npm run check}}` |
| Unit | {{Vitest / Jest}} | pure logic, hooks, utilities | `{{npm test}}` |
| Integration | {{Testing Library / Supabase local}} | components with state, API + RLS | `{{…}}` |
| End-to-end | {{Playwright / Maestro}} | core flows on real builds | `{{npm run test:e2e}}` |
| Accessibility | axe (in e2e), contrast script, manual screen-reader script | WCAG 2.2 AA | `{{npm run contrast}}` + `TEST_PLAN.md` |
| Performance | Lighthouse CI / device profiling | budgets in `performance.md` | CI |
| Security | gitleaks, `npm audit`, RLS tests, header check | secrets, deps, authz | CI |

## 2. Every user story needs
- A test per acceptance criterion, including the error, empty, offline and permission-denied cases.
- A bug fix starts with a failing test. Tests are never weakened to pass.
- UI stories: an axe pass with no violations and a keyboard path through the flow.

## 3. Test data
- Factories/fixtures in `{{tests/fixtures/}}`; seeded local DB (`DATABASE.md` §4); no real personal data anywhere.
- Two test users (A and B) exist in every suite so cross-user access can be asserted.

## 4. Running locally
- Full check: `{{npm run check}}` · one file: `{{npm test -- path}}` · e2e headed: `{{…}}` · local DB: `{{npx supabase start}}`

## 5. CI expectations
- Every PR: static → unit → integration → e2e → axe/Lighthouse → secret scan; all green before merge. Flaky test = fix or quarantine with an issue, never retry-until-green.

## 6. Manual and assistive-technology testing
- 25-minute screen-reader + keyboard script per release (`TEST_PLAN.md`); a round with 3–5 assistive-tech users before public launch (`test-plan/references/accessibility-user-testing.md`).
- Real devices: {{low-end Android, iPhone, 13″ laptop}}; 200% text; reduced motion; slow network.

## 7. Definition of done (per task)
- [ ] criteria tested · [ ] `check` green · [ ] axe clean · [ ] RLS test for any new table · [ ] evidence in the PR (what changed, how to see it)
