---
name: handoff
description: Writes a short session handoff (done, in progress, next, decisions, gotchas) so any AI tool can continue. Use at the end of a session or for "handoff", "wrap up", "save progress", "switching tools".
---

# Handoff

Overwrite `docs/product/HANDOFF.md` (≤ 40 lines — it is read at the start of every session, keep it cheap):

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

Then: add a row to `docs/product/COSTS.md` if money was spent this session (e.g. API usage shown by the tool, a new service plan) and update its "Total to date"; update STATUS.md (phase, current task, date), ensure DECISIONS.md has new decisions, commit docs (`docs: handoff`) if git is available. Confirm in one line.
