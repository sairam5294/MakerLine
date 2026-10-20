<p><img src="https://raw.githubusercontent.com/sairam5294/makerline/main/docs/kit/brand/makerline-idea-logo.svg" alt="MakerLine Idea" width="260"></p>

# MakerLine Idea

**Decide if a product idea is worth building, before you write any code.**

MakerLine Idea is the idea stage of [MakerLine](https://github.com/sairam5294/makerline), as its own plugin. Describe your idea and it asks a few short questions, researches who you're up against, and tells you plainly whether it's worth building — and how to make it stronger if it isn't yet. You get an **Idea Pack**: a brief, an evaluation with a scorecard, a competitor analysis, a design direction with clickable wireframes, a draft PRD and a one-pager, all as files in your own folder. It writes no code and sends nothing anywhere except the web searches it runs. When you decide to build, switch to MakerLine.

## Installation

**Claude app:** Customize → Plugins → **Add marketplace** → `sairam5294/makerline` → install **makerline-idea**.

**Claude Code:**
```bash
claude plugin marketplace add sairam5294/makerline
claude plugin install makerline-idea@makerline
```

Don't install **makerline** as well — it already includes everything here, and every skill would appear twice.

## Try it

Connect an empty folder to a new chat, then type:

- *"/makerline-idea:start — Give me everything for this idea: …"* (add *quick* for a fast first look)
- *"I have a new idea: …"* (interview, one round at a time)
- *"Who are my competitors and is my differentiator real?"*
- *"What would it look like?"* (design direction + clickable wireframes)
- *"Make my tool plan — I have Claude and ChatGPT"*

## Commands

| Command | What you get |
|---|---|
| `/start` | Runs the whole Idea Pack in one go, or resumes where you left off |
| `/new-idea` | Discovery interview → `PROJECT_BRIEF.md` + `CLARITY.md` (every open question and what it blocks) |
| `/evaluate-idea` | Honest, constructive evaluation → `EVALUATION.md` + `COMPETITORS.md`: strongest version, reality check, scorecard, differentiator test, path to Go, tools and cost, accessibility and compliance by launch market |
| `/design-direction` | Principles, flows, screens, 2–3 visual directions, clickable wireframes → `DESIGN_DIRECTION.md` + `design/wireframes/` |
| `/write-prd` | Draft PRD → `PRD.md` |
| `/validate-idea` | Kill criteria, interviews, landing page, prototype test → `VALIDATION.md` |
| `/tool-plan` | Which AI tool does which job, from the subscriptions you have → `TOOL_PLAN.md` |
| `/makerline-idea` | The orchestrator: phases, depth (Quick / Standard / Deep), the one-pager and index |

Four agents run inside the evaluation: `market-researcher`, `devils-advocate`, `idea-champion`, `accessibility-strategist`.

## What you end with

`docs/product/ONE_PAGER.md` on top, then the brief, clarity log, evaluation, competitors, design direction, wireframes and draft PRD — all in `docs/product/` and `design/`, checked by a script before you see them. You decide: go, change or stop. When you decide to build, install the full MakerLine.

## What it runs and sends

Reads and writes only `docs/product/` and `design/` in the folder you connect · web searches about your idea's market go to Claude's search tool · one local checker script, no network · no servers of its own, no telemetry, no accounts. Details: [CONNECTORS.md](CONNECTORS.md).

## MCP integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

Everything works standalone. Connect a knowledge base (prior research), Figma (wireframes there) or GitHub (an existing repo) for more.

Generated from MakerLine's `plugin/` by `scripts/build-idea-pack.py` — edit the kit, not this copy.

---

Created by **[Sairam Mogullapalli](https://www.sairammogullapalli.com/)**, Head of Product Design, building products with AI ([GitHub](https://github.com/sairam5294)). MIT licence.
