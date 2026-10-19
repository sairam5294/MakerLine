---
name: new-idea
description: Product Kit discovery interview for a new product idea (problem, goal, audience, alternatives, differentiator, platforms, scope, design, tech, money, naming) → PROJECT_BRIEF.md + CLARITY.md. Use for "new idea/app/project" or capturing requirements.
---

# New Idea — Discovery

Goal: understand the idea well enough to evaluate it honestly, and make every unknown visible instead of guessed.

1. Get the pitch (2–5 sentences); restate it in one line; confirm. First reply: ≤ 150 words of framing (restatement, what you already know, expectations), then the round-1 questions — the questions don't count toward the 150 words, and the restate-and-confirm doesn't count as one of them. Set expectations in one sentence: "Next I'll interview you, then give an honest evaluation with competitors, a strengthening plan, a design direction and a draft PRD."
2. Read `docs/product/OWNER.md` (skills, hours, budget, accounts, preferences). If the project has none, copy the kit's `owner/OWNER.md` (or `owner/OWNER.example.md` if that doesn't exist) to `docs/product/OWNER.md`. Pre-fill from it and the pitch — never re-ask, only list what you already know and let the owner correct it. Ask for missing OWNER fields once — including which AI subscriptions they have (Claude, ChatGPT, Cursor, Codex, Copilot…), used later by `tool-plan` to split the work — as a separate short "About you" block after the round's questions (it doesn't count toward the 3–5), write the answers to the project copy, and offer to save them to the kit's `owner/OWNER.md` for future projects.
3. Interview in 4–6 rounds of 3–5 questions from `references/question-bank.md`, order: problem/goal → users → alternatives & differentiator → scope/platforms → design → technology → business → naming. Typical rounds: (1) problem & goal · (2) users and who pays · (3) alternatives & differentiator · (4) scope, platforms and design · (5) technology and business · (6) naming, only if the owner wants it now. Multiple choice (AskUserQuestion if available); questions marked **open** in the bank (e.g. "describe a real moment") are asked as short free-text questions with an example, never forced into options. Each bank question is tagged **D** (decision) or **F** (fact). **Decisions** (goal, metric, platform, scope, stack, price) get a recommended first option with a one-line trade-off; **facts** about users/market (what they use today, what happened) never do — a "recommended" fact is a leading question. Core questions required; optional ones get a labelled default.
4. In the alternatives round (bank §B2), record the owner's answers as a **hypothesis** (evaluate-idea researches the real landscape; don't argue now). A quick desk check is fine — put findings under "Quick research" in brief §2b, tagged [Research], without judging them.
5. Offer technology suggestions, not just questions: give a provisional recommendation with a one-line reason, based on answers so far (brief §7 "Provisional suggestion"; final choice happens in tech-stack).
6. Make vague answers testable ("everyone" → "who are your first 100 users and where are they?").
7. Capture the owner's unfair advantages (brief §2 "Unfair advantages").
8. Write `docs/product/PROJECT_BRIEF.md` from `references/brief-template.md`; label assumptions. Write `docs/product/CLARITY.md` from `references/clarity-template.md`: every open question with the phase it blocks, its type (decision / fact / assumption), how to find out, and a default only for decisions. Rank the assumptions the idea depends on.
9. Show a 6–8 line summary + the readiness line in the format of CLARITY.md's header, get confirmation, set STATUS Discovery: Done (create `docs/product/STATUS.md` from `../product-kickoff/templates/STATUS.md` if missing), offer evaluate-idea.

**Readiness line** — one format everywhere: "Evaluation can start · {{n}} questions block approval · {{m}} of {{k}} blocking answered". A question is **blocking** if a phase can't sensibly proceed without it and it has no default (facts and assumptions), or the owner must confirm the default before approval (decisions).

**Owner unavailable** (async, scheduled run, or "just make the brief"): send round 1 as a message anyway (`docs/product/INTERVIEW_ROUND1.md` if no chat), then write a **v0** brief from the pitch: tag every line [Pitch], [Default] (recommended option for a decision), [Assumption] or [Research]; leave facts blank with a Q-id. Write CLARITY.md with every unanswered question. Evaluation may start on defaults and is marked provisional; STATUS Discovery stays "Draft — awaiting owner" until they confirm.

No critique in this phase — that's evaluate-idea. Every later skill reads CLARITY.md first and moves answered questions to "Answered" with the source.
