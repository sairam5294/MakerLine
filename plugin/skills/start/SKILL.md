---
name: start
description: Give me everything for my product idea. Covers all of the Idea Pack in one go, all of the setup after approval in one go, or one phase at a time. Trigger with "/makerline:start", "start", "run everything", "run the whole kit", "continue", or "what's next".
argument-hint: "<idea + 'everything' | 'set it all up' | 'build it' | nothing to resume>"
---

# /start

Short entry point to the kit's orchestrator: read `../product-kickoff/SKILL.md` and follow it exactly, choosing the mode from what the owner said.

**Quick** ("quick", "worth a weekend?"): read only `../evaluate-idea/references/quick-run.md` and follow it — it is the whole Quick run in one file; don't open the orchestrator or the phase skills.

## Usage

```
/start                                   # resume: read STATUS.md, say the phase, offer the next step
/start <idea> — give me everything       # full Idea Pack in one go (add "deep" for more)
/start <idea> — quick                    # Quick: one guide (evaluate-idea/references/quick-run.md)
/start set it all up                     # everything after approval, in one go
/start build it                          # plan-build, then one build-feature task per session
```

## Modes

| Owner says | Mode |
|---|---|
| a new idea + "quick" | `../evaluate-idea/references/quick-run.md`: brief → evaluation → one-pager |
| a new idea + "everything" / "all of it" / "the whole pack" (add "deep" for depth) | full Idea Pack in one go: 1 → 2 → 2a → 2b → one-pager |
| "set it all up" / "everything after approval" (STATUS must say APPROVED) | tool-plan → name + brand → stack → design system → full PRD → engineering docs → project setup |
| "build it" / "next task" | plan-build, then one build-feature task per session |
| nothing specific | read STATUS.md, say the current phase in one line, and offer the next step with the one-go option |

## Rules

- Never write `Evaluation: APPROVED` yourself; the owner approves between the Idea Pack and setup.
- Everything else (depth, gate, checks) lives in `../product-kickoff/SKILL.md`; the owner-unavailable path is kickoff step 8 plus `../new-idea/SKILL.md` → Owner unavailable (Quick: quick-run.md step 3 only) — don't improvise.

## Related

- Runs: `product-kickoff` (the orchestrator) and, through it, every phase skill
