---
name: build-feature
description: Implements one PLAN.md task end-to-end — plan, tests, code, checks, self-review, commit, STATUS update. Use for "build", "implement", "next task", "start T-xx".
---

# Build Feature

1. Load only: AGENTS.md, `docs/RULES.md`, `docs/MEMORY.md`, HANDOFF.md/STATUS.md, the task in PLAN.md, its stories in PRD.md, the engineering doc the task touches (`docs/ARCHITECTURE.md` for a new container or flow, `docs/DATABASE.md` for any table, `docs/CODE_STYLE.md` on your first task) and standards files the task touches (`../product-standards/references/`). Use search (grep) instead of reading whole large files.
2. State scope in 3–7 bullets; ask only if blocked.
3. Branch: `scripts/branch.sh feat "<T-xx summary>"` → `feat/<Mon>-<DD>-<summary>` (or the task's worktree).
4. Write failing tests for acceptance criteria incl. unhappy paths.
5. Implement in small steps: tokens + existing components, all UI states, a11y props, server-side validation + authorization. Comment the *why* of non-obvious code (owner is learning).
6. Run `npm run check` (or typecheck + lint + test + build). Fix; never weaken tests.
7. Self-review: ACs tested · a11y (names, focus, contrast via tokens, targets, text scaling) · all states · authz/validation/no secrets · no unrecorded deps · no debug leftovers · copy clear and localisable.
8. UI task with a Figma frame → run design-qa.
9. Evidence: what changed, how to see it, test results. Commit `feat(scope): … (T-xx, US-xx)`; tick PLAN; update STATUS. A new table or migration → update `docs/DATABASE.md`; a new container, service or cross-cutting rule → `docs/ARCHITECTURE.md`.
