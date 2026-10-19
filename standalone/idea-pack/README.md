# Idea Pack Plugin

Turn a product idea into everything you need to decide whether to build it — before writing any code. The idea stage of [Product Kit](https://github.com/sairam5294/product-kit), as its own plugin.

## Installation

**Claude app:** Customize → Plugins → **Add marketplace** → `sairam5294/product-kit` → install **idea-pack**.

**Claude Code:**
```bash
claude plugin marketplace add sairam5294/product-kit
claude plugin install idea-pack@product-kit-marketplace
```

Don't install **product-kit** as well — it already includes everything here, and every skill would appear twice.

## Try it

Connect an empty folder to a new chat, then type:

- *"/idea-pack:start — Give me everything for this idea: …"* (add *quick* for a fast first look)
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
| `/idea-pack` | The orchestrator: phases, depth (Quick / Standard / Deep), the one-pager and index |

Four agents run inside the evaluation: `market-researcher`, `devils-advocate`, `idea-champion`, `accessibility-strategist`.

## What you end with

`docs/product/ONE_PAGER.md` on top, then the brief, clarity log, evaluation, competitors, design direction, wireframes and draft PRD — all in `docs/product/` and `design/`, checked by a script before you see them. You decide: go, change or stop. When you decide to build, install the full Product Kit.

## What it runs and sends

Reads and writes only `docs/product/` and `design/` in the folder you connect · web searches about your idea's market go to Claude's search tool · one local checker script, no network · no servers of its own, no telemetry, no accounts. Details: [CONNECTORS.md](CONNECTORS.md).

## MCP integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

Everything works standalone. Connect a knowledge base (prior research), Figma (wireframes there) or GitHub (an existing repo) for more.

Generated from Product Kit's `plugin/` by `scripts/build-idea-pack.py` — edit the kit, not this copy.

---

Created by **[Sairam Mogullapalli](https://github.com/sairam5294)** — UX designer, building products with AI. MIT licence.
