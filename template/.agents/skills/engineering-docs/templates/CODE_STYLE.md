# Code style — {{product}}

_Updated {{date}} · Standard: `.agents/skills/product-standards/references/development.md` · Enforced by: lint + format on commit, `{{npm run check}}` before "done"._

## 1. Languages and versions
| Layer | Language / framework | Version | Notes |
|---|---|---|---|
| App | {{TypeScript strict / Expo SDK n / Next.js n}} | | |
| Server | | | |
| Database | {{Postgres n}} | | |

## 2. Folder and naming
- Feature folders (`features/<name>/` with screen, components, hooks, api, tests together); shared UI only in `components/`.
- Files: `kebab-case.ts`; components `PascalCase.tsx`; hooks `use-thing.ts`; tests next to code as `*.test.ts(x)`; e2e in `tests/e2e/`.
- Names say what, not how: `bookingsForDay()` not `getData2()`. One term per concept, the same as the PRD glossary.

## 3. Components and state
- Design-system components and tokens only (`docs/product/DESIGN_SYSTEM.md`); no raw colours, sizes or fonts in feature code.
- Every screen renders all seven states (loading, empty, error, offline, success, permission denied, partial) — prefer one `<StateView>` pattern.
- Server state via {{TanStack Query / SWR}}; local UI state in the component; global state only for {{auth, settings}}.
- Forms: schema-validated ({{zod}}) on client *and* server; labels, errors and `autocomplete` per accessibility standard.

## 4. Errors and logging
- Throw typed errors; map to plain-language user messages in one place; never swallow errors silently.
- Log with {{logger}}: event name + ids, never personal data or secrets.

## 5. Accessibility in code
- Accessible name on every control; roles and states for custom widgets (APG patterns); focus management on route change and after actions; live region for status; `allowFontScaling` never disabled; targets ≥ 44pt / 48dp.

## 6. Comments and docs
- Comment the **why** of non-obvious code in plain English — the owner is a senior UX designer learning to code. No commented-out code.
- A public function gets a one-line doc comment; a module with rules gets a top comment pointing at the doc that holds them.

## 7. Dependencies
- Ask before adding one; record why in `docs/product/DECISIONS.md`. Expo: `npx expo install`. Verify the package name on the registry (no AI-invented packages). Prefer the platform or an existing dep over a new one.

## 8. Git
- Branches `<type>/<Mon>-<DD>-<summary>` (`scripts/branch.sh`); commits `type(scope): what (T-xx, US-xx)`; one task per PR; PR says what changed, why, how to test.

## 9. Commands
- Install `{{…}}` · Run `{{…}}` · Check everything `{{…}}` · Fix formatting `{{…}}` · Typecheck `{{…}}`

## 10. Review checklist (every PR)
- [ ] Acceptance criteria tested · [ ] five states · [ ] a11y props and focus · [ ] server-side authz + validation · [ ] no secrets, no personal data in logs · [ ] no new dep without a decision · [ ] copy is plain and localisable · [ ] "why" comments where needed
