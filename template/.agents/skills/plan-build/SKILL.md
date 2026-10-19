---
name: plan-build
description: Break the PRD into small sequenced tasks with milestones, acceptance criteria, tests, parallel lanes and tool assignment → PLAN.md. Trigger with "plan the build", "break down tasks", "what do we build first?", or after engineering-docs.
argument-hint: "<milestone or feature to plan, or nothing to plan the whole PRD>"
---

# /plan-build

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Turn the PRD and engineering docs into `docs/product/PLAN.md`: small, sequenced, testable tasks that any AI tool can pick up one at a time.

**Why:** a task small enough to finish in a day, with its tests named up front, is the unit that keeps the app runnable and the owner in control.

## Usage

```
/plan-build                          # plan the whole PRD
/plan-build M2 offline playback      # plan or re-plan one milestone / slice
/plan-build break down tasks
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                       PLAN BUILD                             │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Milestones M0 Setup → M1 Foundations → M2…n slices        │
│    → Hardening → Release                                     │
│  ✓ T-xx tasks with criteria, tests, size, dependencies       │
│  ✓ Parallel lanes for tasks with no shared files             │
│  ✓ Suggested tool per task (Claude / Cursor / Codex)         │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Project tracker: tasks become tickets, lanes become cycles│
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `docs/product/PRD.md`, `TECH_STACK.md`, `DESIGN_SYSTEM.md`, `STATUS.md`.
- `docs/ARCHITECTURE.md` + `docs/DATABASE.md` (from engineering-docs; if missing, run it first).
- Gate: STATUS.md says `Evaluation: APPROVED` — no planning of app code before that.
- Ask the owner only what the PRD leaves open (scope of the first slice, which tools they will use).

## Workflow

1. **Read the docs.** PRD, stack, design system, STATUS, and `docs/ARCHITECTURE.md` + `docs/DATABASE.md` (engineering-docs; if missing, run it first).
   - M1 tasks come from DATABASE.md tables and ARCHITECTURE.md containers.
2. **Lay out milestones** in `docs/product/PLAN.md`:
   - **M0 Setup** — start from a kit starter (`--starter` Expo / `--web` Next.js) if the stack matches (else: TS strict, lint, tests, CI, env, secrets scan, error tracking); fill AGENTS.md commands.
   - **M1 Foundations** — tokens/base components, navigation, auth, schema + RLS + migrations, analytics.
   - **M2…n Vertical slices** — one user capability end-to-end, riskiest first.
   - **Hardening** — a11y, performance, security, privacy docs. **Release** — store assets, beta, launch.
3. **Write each task** in the task format (table below). Size S ≤ 2h, M ≤ 1 day; split anything bigger.
4. **Mark lanes.** Tasks with no shared files can run in parallel (separate worktrees — `scripts/worktree.sh`).
5. **Assign tools** with the tool-fit guide below; one suggested tool/agent per task.
6. **Owner approves** the plan → STATUS Build: current task T-01.

### Task format

| Field | Content |
|---|---|
| `T-xx` | task id |
| title | one line |
| `US-xx` | the user story it implements |
| acceptance criteria | testable statements |
| files/areas | what it touches |
| tests | which tests prove the criteria |
| size | S ≤ 2h, M ≤ 1 day; split bigger |
| depends on | prior tasks |
| lane | parallel lane |
| suggested tool/agent | from the tool-fit guide |

### Tool fit

| Tool | Best for |
|---|---|
| Claude | planning, multi-file features, parallel reviews |
| Cursor | visual UI iteration |
| Codex | well-specified independent tasks/tests in parallel |

## Output

| File | What | Size |
|---|---|---|
| `docs/product/PLAN.md` | milestones, T-xx tasks, lanes, tool assignment | one line per field; keep it scannable |
| `docs/product/STATUS.md` | Build: current task T-01 (after owner approval) | — |

Present to the owner (≤ 10 lines): milestones · number of tasks per milestone · the first three tasks · which lanes can run in parallel · what you need them to decide.

## If connectors available

If **~~project tracker** is connected:
- Create one ticket per T-xx with its acceptance criteria and dependencies, grouped by milestone; link ticket ids back in PLAN.md.
- Write tickets only when the owner asks in chat; reading the tracker first is fine.

## Rules

- No stack choice, scaffolding or app code until STATUS.md says `Evaluation: APPROVED`.
- One PLAN.md task per branch; keep the app runnable after every task.
- Riskiest vertical slice first; every task names its tests before any code.
- Size S ≤ 2h, M ≤ 1 day — split bigger tasks instead of estimating them.
- Record plan-shaping decisions in `docs/product/DECISIONS.md`.

## Tips

1. Start M2 with the slice you are least sure you can build — it de-risks the whole plan.
2. Give Codex the independent, well-specified tasks and keep the UI iteration in Cursor.
3. Re-run `/plan-build` for one milestone when the PRD changes; don't rewrite the whole plan.

## Related

- Before: `engineering-docs` (needs `docs/ARCHITECTURE.md` + `docs/DATABASE.md`) · After: `build-feature`, `design-qa`
- Reads: `docs/product/PRD.md`, `TECH_STACK.md`, `DESIGN_SYSTEM.md`, `STATUS.md`, `docs/ARCHITECTURE.md`, `docs/DATABASE.md`; `scripts/worktree.sh`
