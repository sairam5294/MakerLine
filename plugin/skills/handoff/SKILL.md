---
name: handoff
description: Save a handoff so any AI tool can continue. A short note of done, in progress, next, decisions and gotchas → HANDOFF.md, plus MEMORY, COSTS, STATUS and DECISIONS updates. Trigger with "handoff", "wrap up", "save progress", "switching tools", or at the end of every session.
argument-hint: "<tool used, or nothing>"
---

# /handoff

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Leave the project in a state any AI tool (Claude, Cursor, Codex) can pick up in one read.

**Why:** `HANDOFF.md` is read at the start of every session, so it must be short and current — a cheap 40 lines beats a long history.

## Usage

```
/handoff                 # end of session
/handoff Cursor          # notes the tool used in the title
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                          HANDOFF                             │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ HANDOFF.md ≤ 40 lines: done, in progress, next, gotchas   │
│  ✓ Long-lived gotchas → docs/MEMORY.md (≤ 60 lines)          │
│  ✓ COSTS.md row if money was spent · STATUS + DECISIONS      │
│  ✓ Workspace 00_inbox/ filed, then archived (never deleted)  │
│  ✓ Commit docs when git is available                         │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Chat: post the handoff summary to the project channel     │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- This session's work: outcomes, half-done items, decisions, failed approaches.
- `docs/product/HANDOFF.md` (overwritten), `docs/MEMORY.md` (if it exists), `docs/product/COSTS.md`, `STATUS.md`, `DECISIONS.md`.
- `docs/product/CONTEXT_INDEX.md` and `ASSUMPTIONS.md` when the project uses the shared context ([shared-context.md](references/shared-context.md)); always when more than one AI tool works on it.
- Ask the owner only if money was spent and the amount isn't visible in the tool.

## Workflow

1. **Overwrite `docs/product/HANDOFF.md`** (≤ 40 lines — it is read at the start of every session, keep it cheap) with this template:

```
# Handoff — <date> — <tool used>
Phase/task: <phase> · <T-xx>   Branch/worktree: <name>
## Done this session
- <outcome, not activity> (files)
## In progress / half-done
- <what, where it stopped, what's broken>
## Next steps (in order)
1.
## Decisions made (also logged in DECISIONS.md)
-
## Gotchas / don't repeat
- <failed approaches, flaky commands, env quirks>
## Verify with
<commands to run, screen to open>
```

2. **Promote to memory.** If `docs/MEMORY.md` exists, move anything long-lived from "Gotchas" and "Decisions" into it (environment quirks, what broke and the fix, do-not-touch areas, conventions) and condense it to ≤ 60 lines.
   - HANDOFF is for this session, MEMORY for every session.
3. **Record costs.** Add a row to `docs/product/COSTS.md` if money was spent this session (e.g. API usage shown by the tool, a new service plan) and update its "Total to date".
4. **Update status.** Update STATUS.md (phase, current task, date, `Writing: –` so the next tool may write); ensure DECISIONS.md has new decisions, each with the next `D-xx` ID and its evidence IDs.
5. **Update the shared context** (more than one AI tool, or the files already exist). Missing files: copy `templates/CONTEXT_INDEX.md` and `templates/ASSUMPTIONS.md` beside this skill into `docs/product/`. Then:
   - fill the index's ten fields (`Next tool` = who picks this up); add new assumptions or risks with an owner and a review-by date;
   - commit the docs (`docs: handoff`), write that commit's short hash in `Verified commit`, then commit the index on its own (`docs: context index`);
   - run `python3 scripts/context_check.py check .` (from a kit clone, or `scripts/context_check.py` beside this skill) and fix every FAIL.
   - If the next tool can't open the folder (ChatGPT in the browser), or TOOL_PLAN uses ChatGPT at all: regenerate the pack at every handoff — `context_check.py pack . --task "<task type>" --tool ChatGPT` — and tell the owner to replace `docs/CONTEXT_PACK.md` in their ChatGPT Project; ChatGPT's answers come back via `00_inbox/`.
6. **Empty the inbox** (repo inside a product workspace, `../../00_inbox/`; [workspace.md](../new-idea/references/workspace.md)). For each file: move what's still useful into its home in the repo, log any decision in DECISIONS.md, then copy the file to `99_archive/YYYY-MM-DD-inbox/` and move it to `98_bin/`. Never delete.
7. **Commit docs** (`docs: handoff`) if git is available and step 5 didn't. Confirm in one line.

## Output

| File | What | Size |
|---|---|---|
| `docs/product/HANDOFF.md` | this session: done, in progress, next, decisions, gotchas, verify | ≤ 40 lines |
| `docs/MEMORY.md` | long-lived quirks, fixes, do-not-touch areas, conventions | ≤ 60 lines |
| `docs/product/COSTS.md` | new row + "Total to date" (only if money was spent) | — |
| `docs/product/STATUS.md`, `DECISIONS.md` | phase, current task, date; new decisions with IDs | — |
| `docs/product/CONTEXT_INDEX.md`, `ASSUMPTIONS.md` | state in ten fields, files per task, privacy tiers; assumptions with review-by dates | short; checked by `context_check.py` |

Confirm to the owner in one line.

## If connectors available

If **~~chat** is connected:
- Post the "Done / Next steps" lines to the project channel when the owner asks; never post secrets or personal data.

## Rules

- Outcomes, not activity: "login works offline" not "worked on login".
- Overwrite HANDOFF.md; never let it grow past 40 lines.
- Every decision in the handoff is also in DECISIONS.md.
- Gotchas record failed approaches so the next tool doesn't repeat them.
- Cite IDs (D-xx, A-xx, S-x) instead of re-explaining; never copy secrets or personal data into any context file or pack.
- Project state lives in these files, never in a tool's built-in memory (Claude, ChatGPT and Cursor memories don't sync).

## Tips

1. Run it before `/clear` or a new chat — cheaper than compacting a long history.
2. "Verify with" should be a command the next session can run in under a minute.
3. If MEMORY.md is near 60 lines, condense rather than append.

## Related

- Before: any phase · After: the next session reads HANDOFF.md first (`AGENTS.md` "Start every session")
- Reads: `../product-standards/references/context-budget.md` (HANDOFF ≤ 40, STATUS ≤ 60 lines), [shared-context.md](references/shared-context.md) (files, IDs, privacy tiers, recovery test), [workspace.md](../new-idea/references/workspace.md) (inbox, archive, bin)
