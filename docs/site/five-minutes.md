# 5 minutes with MakerLine

Five steps from nothing to a one-page answer about your idea. You need a Claude account and the Claude app (desktop or web) or Claude Code. No terminal and no coding are needed for these steps.

The 5 minutes is your time. Claude's research runs while you wait; a Quick run uses roughly 50,000–70,000 tokens.

## 1. Install the plugin (1 minute)

In the Claude app: **Customize** → **Plugins** → **Add marketplace** → enter `sairam5294/makerline` → find **makerline** (or **makerline-idea**, if you only want the thinking stage) → **Install**.

In Claude Code:

```bash
claude plugin marketplace add sairam5294/makerline
claude plugin install makerline@makerline
```

Install one of the two plugins, not both. [Which one?](index.md#which)

## 2. Connect an empty folder (30 seconds)

Start a new chat and connect a new, empty folder for this idea, for example `Projects/physio-booking`. Everything the kit writes goes into that folder as ordinary files you own: Markdown documents in `docs/product/`, and HTML wireframes in `design/` when you run the Standard depth.

The kit reads and writes only inside the folder you connect. It has no server of its own and collects no analytics.

## 3. Run a Quick Idea Pack (1 minute of your time)

Type the command, the word *quick*, and your idea in two to five sentences:

> /makerline:start — Give me everything for this idea, quick: a booking app for small physio clinics, so patients can rebook their next session from a text message instead of calling the front desk.

With the MakerLine Idea plugin, type `/makerline-idea:start` instead.

The kit may ask a short round of questions. Answer what you know. If you don't know, say *"just do it"*: it picks sensible defaults and marks each one so you can confirm it later. Every unknown is written down in `CLARITY.md` with the decision it blocks, rather than guessed silently.

Quick mode runs discovery, the evaluation and a one-pager. It skips the design direction and the draft PRD; run Standard later for those.

## 4. Read the one-pager (2 minutes)

Open `docs/product/ONE_PAGER.md`. It fits on one page and answers, in this order:

- **The idea in one line**, and the verdict with a confidence level: Go, Go with changes, Pivot, or Drop / Park
- **The problem** and **who it's for first**
- **Up against**: the real competitors, and where you would win or lose
- **Strongest version**: the best honest version of your idea
- **Reality check**: the biggest risks, in plain words
- **How to make it stronger**, and the **next test**: the cheapest thing you could do this week that would change the verdict
- **Decisions needed from you**

Want the reasoning? `EVALUATION.md` has the scorecard, the evidence behind each score with sources, and an accessibility, inclusion and compliance section. In Quick mode the competitors are a short block inside the evaluation; Standard gives them their own file, `COMPETITORS.md`.

## 5. Decide (30 seconds)

You have three good choices:

| If the one-pager says… | Do this |
|---|---|
| The idea is promising but unproven | Run the **next test** it suggests, or say *"validate demand"* for interview questions, a landing page or a prototype test |
| You want to go deeper first | Run `/makerline:start` again with *"give me everything for this idea"* (no *quick*) for the design direction, clickable wireframes and a draft PRD |
| It isn't worth it | Stop. You spent five minutes, not five weeks |

Nothing gets built until **you** approve the evaluation. In the Claude app, say *"I approve the evaluation"* and Claude records your exact words. AI tools cannot approve for you.

## What next

- See what a full Standard run produces: [the ClubSlot case study](case-clubslot.md)
- Set up building with Claude Code, Cursor or Codex: [Getting started](../../GETTING-STARTED.md)
- Every skill and command: [Full overview](../../README.md)
