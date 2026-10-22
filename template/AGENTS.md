# AGENTS.md

Rules for every AI agent in this repo — Claude (via CLAUDE.md), Cursor (`.cursor/rules/`, index in `project.mdc`), Codex (reads this file), GitHub Copilot (`.github/copilot-instructions.md`), and tools that can't read the repo such as ChatGPT (paste `docs/CONTEXT_PACK.md`). One rulebook; each tool's folder only points here. Keep this file short; details live in linked files.
Other tools (Gemini CLI, Aider, Continue, Windsurf, Cline, Roo, Zed, Junie, Kiro, Antigravity, OpenCode, Amp): native or thin pointer — see `docs/kit/AGENT-ADAPTERS.md`.

## Start every session
1. Read `docs/product/HANDOFF.md` (if present), `docs/product/STATUS.md` and `docs/product/OWNER.md` (who you're building with: skills, time, budget, tools). If STATUS `Writing:` names another tool on your branch, stop and ask; otherwise set it to you.
2. Read only the files the current task needs (see `.agents/skills/product-standards/references/context-budget.md`).
3. End every session with the `handoff` skill (it also updates `docs/MEMORY.md`, the project's long-lived memory).
4. In a product workspace (this repo under `04_repos/`): outputs with no home yet go to `../../00_inbox/`; never read the workspace's `02_brand/`, `03_design/`, `05_qa/`, `06_releases/`, `90_reference/`, `98_bin/` or `99_archive/` unless the task names a file there.

## Workflow
new-idea → evaluate-idea → design-direction → write-prd (draft) → validate-idea → **owner approval** → name-product → tech-stack → design-system → write-prd (full) → engineering-docs → project-setup → plan-build → build-feature (+ design-qa) → quality-review → test-plan → ship-checklist → post-launch.
Anytime: `tool-plan` (which AI tool does which job), `handoff`, `portfolio`, `ai-feature` (any AI feature), `standards-refresh`.
Skills live in `.agents/skills/<name>/SKILL.md`. Outputs live in `docs/product/`; engineering docs (architecture, database, security, code style, testing, rules, memory) in `docs/` — index: `docs/README.md`. Design tokens: `design/tokens.json` → `npm run tokens`.

- No stack choice, scaffolding or app code until STATUS.md says `Evaluation: APPROVED`. Only the owner approves (`scripts/approve.sh`) — never write that line yourself. (Enforced by a Claude Code hook, git hooks and CI.)
- Log decisions in `docs/product/DECISIONS.md`. Update STATUS.md after each phase/task.

## Definition of done (details: `.agents/skills/product-standards/references/`; unfamiliar terms: `glossary.md` there)
- WCAG 2.2 AA: accessible names, keyboard/screen-reader operable, contrast ≥ 4.5:1, targets ≥ 44 CSS px (web) / 44 pt (iOS) / 48 dp (Android) — the starters use 48 as one safe value, text scales to 200%. Accessibility statement + barrier-feedback route from first release; accessible worldwide and non-discriminatory by default (`inclusion.md`), plus the accessibility law of each launch market (`accessibility-law.md`: AODA, ADA, EAA, RPwD…).
- Every screen: loading, empty, error, offline, success, permission-denied and partial states. Design tokens only — no raw colours.
- Server-side authorization + RLS on every user-data table; schema-validated input; parameterized queries.
- No secrets in code, logs or client bundles; only `.env.example` is committed.
- Every acceptance criterion has a test; bug fixes start with a failing test; never weaken tests.
- Minimum personal data; children's data needs verifiable parental consent.
- AI features follow `ai.md`: server-side calls, evals before launch, labelled AI content, user control, cost caps.
- `npm run check` passes before saying "done".

## How to work
- One `PLAN.md` task per branch; parallel tools use separate worktrees (`scripts/worktree.sh`).
- Keep every session inside the token budget (`context-budget.md`): read only what the task needs, search before reading, one task per session, reviewers get the diff + one standard file, run `handoff` then start fresh when the topic changes.
- Security and AI rules are not optional: `security.md` (OWASP 2025, secrets, authz), `ai.md` (server-side calls, evals, labelling, cost caps). `docs/RULES.md` lists the ones that apply to this project.
- State a short plan before editing more than 3 files. Keep the app runnable after every task.
- Follow `docs/product/TECH_STACK.md`; ask before adding a dependency and record why. Verify APIs against real docs; never invent package names.
- Comment the *why* of non-obvious code in plain English — the owner is a senior UX designer learning to code.
- Ask before anything irreversible: deleting data, force-push, production settings, paid services.

## Branches
Name every branch `<type>/<Mon>-<DD>-<summary>` — e.g. `fix/Oct-19-login-focus-ring` — made with `scripts/branch.sh fix "login focus ring"`; the pre-push hook and CI reject other names. Type = the main purpose of the change:
`feat` new page/section/feature · `fix` something broken · `content` copy, recommendations, case-study text · `design` visual or layout polish · `security` headers, privacy, removing personal data · `a11y` accessibility · `docs` README/AGENTS.md/guides only · `test` tests only · `ci` workflows, hooks, checks · `deps` dependency updates · `refactor` same behaviour, cleaner code · `perf` speed or size · `chore` housekeeping · `skill` a kit skill, agent or standard · `release` version bump · `eval` eval cases and blind runs · `exp` experiments/spikes (never merged directly; expire after 14 days).
Every pull request says what changed and why; bots (Dependabot) keep their own names.

## Commands (same names in both kit starters — update if your stack differs)
- Install: `npm install` · Run: `npm run dev` · Check everything: `npm run check`
- Tests: `npm test` · Web e2e + axe: `npm run build:web && npm run test:e2e` · Contrast: `npm run contrast`
- Expo app: add packages with `npx expo install`, never plain npm (`docs/kit/expo-rules.md`). Next.js: read `docs/kit/nextjs-rules.md`.
- DB: `npx supabase start` · migrations in `supabase/migrations/`
