# AGENTS.md

Rules for every AI agent in this repo (Claude via CLAUDE.md, Cursor, Codex). Keep this file short; details live in linked files.

## Start every session
1. Read `docs/product/HANDOFF.md` (if present), `docs/product/STATUS.md` and `docs/product/OWNER.md` (who you're building with: skills, time, budget, tools).
2. Read only the files the current task needs (see `.agents/skills/product-standards/references/context-budget.md`).
3. End every session with the `handoff` skill.

## Workflow
new-idea → evaluate-idea → design-direction → write-prd (draft) → validate-idea → **owner approval** → name-product → tech-stack → design-system → write-prd (full) → plan-build → build-feature (+ design-qa) → quality-review → test-plan → ship-checklist → post-launch.
Anytime: `handoff`, `portfolio`, `ai-feature` (any AI feature), `standards-refresh`.
Skills live in `.agents/skills/<name>/SKILL.md`. Outputs live in `docs/product/`. Design tokens: `design/tokens.json` → `npm run tokens`.

- No stack choice, scaffolding or app code until STATUS.md says `Evaluation: APPROVED`. Only the owner approves (`scripts/approve.sh`) — never write that line yourself. (Enforced by a Claude Code hook, git hooks and CI.)
- Log decisions in `docs/product/DECISIONS.md`. Update STATUS.md after each phase/task.

## Definition of done (details: `.agents/skills/product-standards/references/`)
- WCAG 2.2 AA: accessible names, keyboard/screen-reader operable, contrast ≥ 4.5:1, targets ≥ 44pt/48dp, text scales to 200%. Accessibility statement + barrier-feedback route from first release; accessible worldwide and non-discriminatory by default (`inclusion.md`), plus the accessibility law of each launch market (`accessibility-law.md`: AODA, ADA, EAA, RPwD…).
- Every screen: loading, empty, error, offline, success states. Design tokens only — no raw colours.
- Server-side authorization + RLS on every user-data table; schema-validated input; parameterized queries.
- No secrets in code, logs or client bundles; only `.env.example` is committed.
- Every acceptance criterion has a test; bug fixes start with a failing test; never weaken tests.
- Minimum personal data; children's data needs verifiable parental consent.
- AI features follow `ai.md`: server-side calls, evals before launch, labelled AI content, user control, cost caps.
- `npm run check` passes before saying "done".

## How to work
- One `PLAN.md` task per branch (`feat/T-xx-name`); parallel tools use separate worktrees (`scripts/worktree.sh`).
- State a short plan before editing more than 3 files. Keep the app runnable after every task.
- Follow `docs/product/TECH_STACK.md`; ask before adding a dependency and record why. Verify APIs against real docs; never invent package names.
- Comment the *why* of non-obvious code in plain English — the owner is a senior UX designer learning to code.
- Ask before anything irreversible: deleting data, force-push, production settings, paid services.

## Commands (same names in both kit starters — update if your stack differs)
- Install: `npm install` · Run: `npm run dev` · Check everything: `npm run check`
- Tests: `npm test` · Web e2e + axe: `npm run build:web && npm run test:e2e` · Contrast: `npm run contrast`
- Expo app: add packages with `npx expo install`, never plain npm (`docs/kit/expo-rules.md`). Next.js: read `docs/kit/nextjs-rules.md`.
- DB: `npx supabase start` · migrations in `supabase/migrations/`
