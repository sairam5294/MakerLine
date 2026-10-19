---
name: new-idea
description: Turn a new idea into a clear brief. Interviews the owner about a new product idea (problem, goal, audience, alternatives, differentiator, platforms, scope, design, tech, money, naming) and make every unknown visible instead of guessed → PROJECT_BRIEF.md + CLARITY.md. Trigger with "new idea", "new app", "new project", "I have an idea", or when capturing requirements.
argument-hint: "<the idea in 2–5 sentences, or nothing to be asked for it>"
---

# /new-idea

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Understand the idea well enough to evaluate it honestly, and make every unknown visible instead of guessed.

**Why:** evaluation is only as good as the brief; a question logged in CLARITY.md beats an assumption buried in prose.

## Usage

```
/new-idea                                  # asks for the pitch first
/new-idea A menu-bar app that reminds remote workers to stretch…
/new-idea just make the brief              # owner-unavailable path (v0 brief from the pitch)
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                        NEW IDEA                              │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Pitch → one-line restatement → confirm                    │
│  ✓ 4–6 rounds of 3–5 questions from the question bank        │
│  ✓ Decisions get a recommended option; facts never do        │
│  ✓ Provisional tech suggestion · unfair advantages           │
│  ✓ PROJECT_BRIEF.md + CLARITY.md with a readiness line       │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Knowledge base: prior notes, decks and research on the    │
│    idea pre-fill the brief instead of being re-asked         │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- The pitch (2–5 sentences) from the owner.
- `docs/product/OWNER.md` (skills, hours, budget, accounts, preferences). None → copy the kit's `owner/OWNER.md` (or `owner/OWNER.example.md` if that doesn't exist) to `docs/product/OWNER.md`.
- `references/question-bank.md` (questions, C/O and D/F tags), `references/brief-template.md`, `references/clarity-template.md`.
- No gate: this is the first phase.

## Workflow

1. **Get the pitch.** 2–5 sentences; restate it in one line; confirm. Set expectations in one sentence: "Next I'll interview you, then give an honest evaluation with competitors, a strengthening plan, a design direction and a draft PRD."
   - First reply: ≤ 150 words of framing (restatement, what you already know, expectations), then the round-1 questions — the questions don't count toward the 150 words, and the restate-and-confirm doesn't count as one of them.
2. **Read OWNER.md and pre-fill.** Pre-fill from it and the pitch — never re-ask, only list what you already know and let the owner correct it.
   - Ask for missing OWNER fields once — including which AI subscriptions they have (Claude, ChatGPT, Cursor, Codex, Copilot…), used later by `tool-plan` to split the work — as a separate short "About you" block after the round's questions (it doesn't count toward the 3–5).
   - Write the answers to the project copy, and offer to save them to the kit's `owner/OWNER.md` for future projects.
3. **Interview in 4–6 rounds of 3–5 questions** from `references/question-bank.md`, in this order: problem/goal → users → alternatives & differentiator → scope/platforms → design → technology → business → naming.
   - Typical rounds: (1) problem & goal · (2) users and who pays · (3) alternatives & differentiator · (4) scope, platforms and design · (5) technology and business · (6) naming, only if the owner wants it now.
   - Multiple choice (AskUserQuestion if available); questions marked **open** in the bank (e.g. "describe a real moment") are asked as short free-text questions with an example, never forced into options.
   - Each bank question is tagged **D** (decision) or **F** (fact). **Decisions** (goal, metric, platform, scope, stack, price) get a recommended first option with a one-line trade-off; **facts** about users/market (what they use today, what happened) never do — a "recommended" fact is a leading question. Core questions required; optional ones get a labelled default.
4. **Alternatives round (bank §B2).** Record the owner's answers as a **hypothesis** (evaluate-idea researches the real landscape; don't argue now). A quick desk check is fine — put findings under "Quick research" in brief §2b, tagged [Research], without judging them.
5. **Offer technology suggestions, not just questions.** Give a provisional recommendation with a one-line reason, based on answers so far (brief §7 "Provisional suggestion"; final choice happens in tech-stack).
6. **Make vague answers testable** ("everyone" → "who are your first 100 users and where are they?"). Use the follow-up patterns in the bank.
7. **Capture the owner's unfair advantages** (brief §2 "Unfair advantages").
8. **Write the documents.** `docs/product/PROJECT_BRIEF.md` from `references/brief-template.md`; label assumptions. `docs/product/CLARITY.md` from `references/clarity-template.md`: every open question with the phase it blocks, its type (decision / fact / assumption), how to find out, and a default only for decisions. Rank the assumptions the idea depends on.
9. **Present and close.** Show a 6–8 line summary + the readiness line in the format of CLARITY.md's header, get confirmation, set STATUS Discovery: Done (create `docs/product/STATUS.md` from `../product-kickoff/templates/STATUS.md` if missing), offer evaluate-idea.

### Owner unavailable

Applies when the run is async, scheduled, or the owner says "just make the brief":
- Send round 1 as a message anyway (`docs/product/INTERVIEW_ROUND1.md` if no chat). With no chat at all, `INTERVIEW_ROUND1.md` replaces the first reply (same content: restatement, what you know, the questions).
- Write a **v0** brief from the pitch: tag every line [Pitch], [Default] (recommended option for a decision), [Assumption] or [Research]; leave facts blank with a Q-id.
- Write CLARITY.md with every unanswered question. Evaluation may start on defaults and is marked provisional; STATUS Discovery stays `Waiting for owner` until they confirm.

## Output

| File | What | Size |
|---|---|---|
| `docs/product/PROJECT_BRIEF.md` | the brief, assumptions labelled, §2 unfair advantages, §2b quick research, §7 provisional tech suggestion | per `brief-template.md` |
| `docs/product/CLARITY.md` | every open question: phase it blocks, type, how to find out, default (decisions only); ranked assumptions | per `clarity-template.md` |
| `docs/product/OWNER.md` | owner profile (created or completed) | — |
| `docs/product/STATUS.md` | Discovery: Done (or `Waiting for owner`) | — |

Presentation to the owner (6–8 lines + the readiness line):

```
Evaluation can start · {{n}} questions block approval · {{m}} of {{k}} blocking answered
```

A question is **blocking** if a phase can't sensibly proceed without it and it has no default (facts and assumptions), or the owner must confirm the default before approval (decisions). Use this one readiness format everywhere.

## If connectors available

If **~~knowledge base** is connected:
- Search prior notes, decks and research on the idea and pre-fill the brief from them; list what you found and let the owner correct it, instead of re-asking.

## Rules

- **No critique in this phase** — that's evaluate-idea.
- Never re-ask what OWNER.md or the pitch already answers; list it and let the owner correct it.
- Facts never get a recommended answer; decisions always get one with a one-line trade-off.
- Open questions are asked as free text with an example, never forced into options.
- Every later skill reads CLARITY.md first and moves answered questions to "Answered" with the source.

## Tips

1. Give the pitch as a real moment ("last Tuesday my mum couldn't…") — open questions get better answers than feature lists.
2. "I don't know yet" is a fine answer for a fact; it becomes a CLARITY question with how to find out.
3. Share your AI subscriptions in the "About you" block once — `tool-plan` uses them later.

## Related

- Before: `product-kickoff` / `start` · After: `evaluate-idea`
- Reads: `references/question-bank.md`, `brief-template.md`, `clarity-template.md`; `../product-kickoff/templates/STATUS.md`; the kit's `owner/OWNER.md`
