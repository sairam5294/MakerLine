---
name: plan-build
description: Breaks the PRD into small sequenced tasks with milestones, tests, parallel lanes and tool assignment → PLAN.md. Use for "plan the build", "break down tasks".
---

# Plan Build

1. Read PRD, stack, design system, STATUS, and `docs/ARCHITECTURE.md` + `docs/DATABASE.md` (engineering-docs; if missing, run it first). M1 tasks come from DATABASE.md tables and ARCHITECTURE.md containers.
2. Milestones in `docs/product/PLAN.md`:
   - **M0 Setup** — start from a kit starter (`--starter` Expo / `--web` Next.js) if the stack matches (else: TS strict, lint, tests, CI, env, secrets scan, error tracking); fill AGENTS.md commands.
   - **M1 Foundations** — tokens/base components, navigation, auth, schema + RLS + migrations, analytics.
   - **M2…n Vertical slices** — one user capability end-to-end, riskiest first.
   - **Hardening** — a11y, performance, security, privacy docs. **Release** — store assets, beta, launch.
3. Task format: `T-xx` · title · `US-xx` · acceptance criteria · files/areas · tests · size (S ≤ 2h, M ≤ 1 day; split bigger) · depends on · lane · suggested tool/agent.
4. Mark lanes: tasks with no shared files can run in parallel (separate worktrees — `scripts/worktree.sh`).
5. Owner approves → STATUS Build: current task T-01.

Tool fit: Claude = planning, multi-file features, parallel reviews · Cursor = visual UI iteration · Codex = well-specified independent tasks/tests in parallel.
