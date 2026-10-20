---
name: start
description: Give me everything for my product idea. Covers discovery, evaluation, competitors, design direction with wireframes, draft PRD and one-pager in one go, or the next phase. Trigger with "/makerline-idea:start", "start", "run everything", "give me everything for this idea", or "continue".
argument-hint: "<idea + 'everything' (add 'quick' or 'deep'), or nothing to resume>"
---

# /start

Short entry point: read `../idea-pack/SKILL.md` and follow it, choosing the mode from what the owner said.

**Quick** ("quick", "worth a weekend?"): read only `../evaluate-idea/references/quick-run.md` and follow it — it is the whole Quick run in one file.

## Usage

```
/start                                  # resume: read STATUS.md, say where the project is, offer the next step
/start <idea> — give me everything      # all phases in one go (add "deep" for more)
/start <idea> — quick                   # Quick: one guide (evaluate-idea/references/quick-run.md)
```

## Modes

| Owner says | Mode |
|---|---|
| an idea and "everything" (add "quick" or "deep" for depth) | run all phases in one go |
| nothing specific | read STATUS.md, say where the project is in one line and offer the next step |

## Related

- Runs: `idea-pack` (the orchestrator) and, through it, every phase skill
