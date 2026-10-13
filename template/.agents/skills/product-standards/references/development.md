# Development Standard

Written for AI-assisted development by a solo builder: optimise for code that an AI and a human can both understand, change safely and debug.

## 1. Working agreement for AI coding agents — MUST

- Read `AGENTS.md`, `docs/product/PROJECT_BRIEF.md`, `docs/product/TECH_STACK.md` and the relevant task in `docs/product/PLAN.md` before writing code.
- Work in small steps: one task → one branch/commit → tests pass → next task. Never make sweeping multi-feature changes in one go.
- Explain the plan in 3–7 bullets before editing more than 3 files.
- Don't add a new dependency without stating why, its size/maintenance status and licence; prefer the platform or existing deps.
- Never invent APIs: check installed package versions and official docs when unsure.
- Never delete or rewrite tests to make them pass; fix the code or explain why the test is wrong.
- Leave the codebase runnable after every step. If something is half-done, say so in `docs/product/STATUS.md`.

## 2. Project structure

- Organise by feature, not by type: `src/features/<feature>/{components,hooks,api,tests}` plus `src/shared/` for truly shared code.
- One component per file; files under ~300 lines; functions do one thing.
- Keep business logic out of UI components (hooks/services), so it can be unit-tested.
- Configuration via environment variables; provide `.env.example` with every key and no real values.

## 3. Code quality

- TypeScript in `strict` mode (web/React Native/Node); Swift with strict concurrency; Kotlin with explicit nullability.
- Lint + format on save and in CI (ESLint + Prettier / SwiftLint / ktlint). Zero warnings policy on new code.
- Names say what things are: `fetchLessonsForChild`, not `getData`. Booleans read as questions: `isLoading`, `hasAccess`.
- Handle every error path explicitly: no empty `catch`; show user-facing messages via a single error-handling helper; log with context.
- No magic numbers or colours — use design tokens and named constants.
- Comments explain *why*, not *what*.

## 4. State & data

- Server state via a cache library (TanStack Query / SWR) — not hand-rolled in global state.
- Local UI state stays local; global state only for truly global concerns (auth session, theme).
- Validate all external data at the boundary with a schema (Zod / Valibot) and share types between client and server.

## 5. Git & review

- `main` is always deployable. Short-lived branches `feat/…`, `fix/…`, `chore/…`.
- Conventional commits: `feat(lessons): add offline download`.
- Every change goes through a PR (even solo) with: what/why, screenshots for UI, test evidence, checklist from `quality-review`.
- CI must pass: typecheck, lint, unit tests, build; e2e smoke on main.

## 6. Documentation

- `README.md`: what it is, how to run, how to test, how to deploy — kept current.
- Decisions go in `docs/product/DECISIONS.md` (date, decision, options considered, why).
- Public functions/APIs get short doc comments; API endpoints documented via OpenAPI or typed routes.

## 7. Dependencies

- Pin versions via lockfile; renovate/dependabot on; review changelogs for majors.
- Prefer well-maintained packages (recent release, many dependents, clear licence: MIT/Apache/BSD). Avoid GPL in closed-source apps unless intended.
