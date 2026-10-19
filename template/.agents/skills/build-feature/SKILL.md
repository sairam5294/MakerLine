---
name: build-feature
description: Build the next task with tests first. Covers scope, branch, failing tests, code, checks, self-review, evidence, commit and STATUS update. Trigger with "build", "implement", "next task", "start T-xx", or after plan-build.
argument-hint: "<T-xx, or nothing for the current task in STATUS.md>"
---

# /build-feature

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Take one task from `docs/product/PLAN.md` from branch to commit, with tests first and the app runnable at the end.

**Why:** one task per branch, proven by tests and self-reviewed against the kit standards, is how a non-coder owner can trust what was built.

## Usage

```
/build-feature                       # the current task in STATUS.md
/build-feature T-04                  # a specific task
/build-feature next task
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                      BUILD FEATURE                           │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Minimal context load (task, stories, touched docs)        │
│  ✓ Branch per task · failing tests first · small steps       │
│  ✓ Checks: typecheck + lint + test + build, never weakened   │
│  ✓ Self-review: ACs, a11y, states, authz, secrets, deps      │
│  ✓ Evidence, conventional commit, PLAN tick, STATUS update   │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Source control: open the PR with evidence attached        │
│  + Project tracker: move the ticket as the task progresses   │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

Load only these (use search / grep instead of reading whole large files):

- `AGENTS.md`, `docs/RULES.md`, `docs/MEMORY.md`, `HANDOFF.md` / `STATUS.md`.
- The task in `PLAN.md` and its stories in `PRD.md`.
- The engineering doc the task touches: `docs/ARCHITECTURE.md` for a new container or flow, `docs/DATABASE.md` for any table, `docs/CODE_STYLE.md` on your first task.
- The standards files the task touches (`../product-standards/references/`).
- Gate: STATUS.md says `Evaluation: APPROVED` and the task is in PLAN.md.
- Ask the owner only if blocked.

## Workflow

1. **Load context** — only the inputs above; grep rather than read large files whole.
2. **State scope** in 3–7 bullets; ask only if blocked.
3. **Branch:** `scripts/branch.sh feat "<T-xx summary>"` → `feat/<Mon>-<DD>-<summary>` (or the task's worktree).
4. **Write failing tests** for the acceptance criteria, including unhappy paths.
5. **Implement in small steps:** tokens + existing components, all UI states, a11y props, server-side validation + authorization.
   - Comment the *why* of non-obvious code (the owner is learning).
6. **Run checks:** `npm run check` (or typecheck + lint + test + build). Fix; never weaken tests.
7. **Self-review** against the checklist below.
8. **Design QA:** a UI task with a Figma frame → run `design-qa`.
9. **Evidence and commit:** what changed, how to see it, test results. Commit `feat(scope): … (T-xx, US-xx)`; tick PLAN; update STATUS.
   - Keep the docs in step (table below).

### Self-review checklist

| Area | Check |
|---|---|
| ACs | every acceptance criterion tested |
| a11y | names, focus, contrast via tokens, targets, text scaling |
| states | all UI states (loading, empty, error, offline, success) |
| security | authz / validation / no secrets |
| deps | no unrecorded dependencies |
| hygiene | no debug leftovers |
| copy | clear and localisable |

### Docs to update with the change

| Change | Update |
|---|---|
| new table or migration | `docs/DATABASE.md` |
| new folder | `docs/STRUCTURE.md` |
| new env variable | `.env.example` (with its comment) and `docs/SETUP.md` |
| new container, service or cross-cutting rule | `docs/ARCHITECTURE.md` |

## Output

| File | What |
|---|---|
| branch `feat/<Mon>-<DD>-<summary>` | the task, committed as `feat(scope): … (T-xx, US-xx)` |
| `docs/product/PLAN.md` | task ticked |
| `docs/product/STATUS.md` | current task advanced |
| `docs/*.md`, `.env.example` | kept in step per the table above |

Present to the owner (≤ 8 lines): what changed · how to see it (command or screen) · test results · anything deferred.

## If connectors available

If **~~source control** is connected:
- Push the branch and open a PR with the evidence (what changed, how to see it, test results) as the description.
- Push or open a PR only when the owner asks in chat.

If **~~project tracker** is connected:
- Move the task's ticket to in-progress on branch, to review on commit; link the branch / PR on the ticket.

## Rules

- One task per branch; keep the app runnable after every task.
- Tests first; bug fixes start with a failing test; never weaken tests.
- Design tokens and existing components only — no raw colours.
- Server-side validation + authorization on every write; no secrets in code, logs or client bundles.
- Ask before adding a dependency and record why in `docs/product/DECISIONS.md`; verify APIs against real docs, never invent package names.
- Ask before anything irreversible.

## Tips

1. If scope grows past the task, stop and add a new T-xx to PLAN.md rather than stretching the branch.
2. Run the checks before the self-review — a red build hides review findings.
3. Hand well-specified sibling tasks to Codex in their own worktree while this one is in progress.

## Related

- Before: `plan-build` · Alongside: `design-qa` · After: `quality-review`, `test-plan`, `handoff`
- Reads: `AGENTS.md`, `docs/RULES.md`, `docs/MEMORY.md`, `docs/ARCHITECTURE.md`, `docs/DATABASE.md`, `docs/CODE_STYLE.md`, `../product-standards/references/*`; `scripts/branch.sh`
