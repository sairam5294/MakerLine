# Product Kit Plugin

**The open-source designer's AI toolkit.** Takes an idea from "I have a new idea" to a shipped web, iOS or Android product — honest evaluation, competitors, design direction, PRD, engineering docs, repo setup, build, review, test, ship — with accessibility (WCAG 2.2 AA, accessible worldwide), UX, security (OWASP 2025) and testing standards built in and enforced. Designed for the Claude desktop app and Claude Code; the same rules travel to Cursor, Codex and Copilot through every project it creates.

Nothing is built until **you** approve the idea: the kit cannot write `Evaluation: APPROVED` itself.

## Installation

**Claude app (desktop or web):** Customize → Plugins → **Add marketplace** → `sairam5294/product-kit` → install **product-kit**. Turn on *Sync automatically* for updates.

**Claude Code:**
```bash
claude plugin marketplace add sairam5294/product-kit
claude plugin install product-kit@product-kit-marketplace
```

Only want the thinking stage? Install **idea-pack** instead (same Idea Pack skills, no build phases). Don't install both — every skill would appear twice.

## Try it

Connect an empty folder to a new chat, then type one of these:

- *"/product-kit:start — Give me everything for this idea: a booking app for small physio clinics"*
- *"/product-kit:start — Give me everything for this idea, quick: …"* (fast first look)
- *"Who are my competitors and what's my real differentiator?"*
- *"Set it all up"* (after you approve: name and brand, stack, design system, full PRD, engineering docs, repo setup)
- *"Make my tool plan — I have Claude, ChatGPT and Cursor"*
- *"Review this branch before I merge"*

…or type `/product-kit:` in any chat to see every skill.

## One command runs the whole kit

| You want | Type |
|---|---|
| The whole Idea Pack at once | `/product-kit:start` + *"Give me everything for this idea: …"* (add *quick* or *deep*) |
| Everything after approval, at once | `/product-kit:start` + *"set it all up"* — asks your picks once (name, stack, look) |
| Build | `/product-kit:start` + *"build it"* — one task per session, each on its own branch |
| Where am I? | `/product-kit:start` |

## Commands

Explicit workflows, in the order the kit runs them. Each works **standalone** (your words, pasted files) and gets **supercharged** with connectors.

### Before approval — the Idea Pack
| Command | What you get |
|---|---|
| `/start` | Runs the whole kit or resumes where you left off |
| `/new-idea` | Discovery interview → `PROJECT_BRIEF.md` + `CLARITY.md` (every open question and what it blocks) |
| `/evaluate-idea` | Honest, constructive evaluation → `EVALUATION.md` + `COMPETITORS.md` (strongest version, reality check, scorecard, differentiator test, path to Go, tools and cost, accessibility and compliance) |
| `/design-direction` | Principles, flows, screen inventory, 2–3 visual directions, clickable wireframes → `DESIGN_DIRECTION.md` + `design/wireframes/` |
| `/write-prd` | Draft PRD (v0) before approval; full PRD (v1) after → `PRD.md` |
| `/validate-idea` | Kill criteria, interviews, landing page, prototype test → `VALIDATION.md` |
| `/tool-plan` | Which AI tool does which job, from the subscriptions you have → `TOOL_PLAN.md` |

### After approval — set up
| Command | What you get |
|---|---|
| `/name-product` | 12–15 contextual names, conflict-checked, then a brand kit (logo, guidelines, colours, fonts, icons, rules) → `NAMING.md` + `BRAND.md` |
| `/tech-stack` | 2–3 stacks with trade-offs and costs → `TECH_STACK.md` (ADR) |
| `/design-system` | Tokens (light + dark, contrast-checked) and component inventory → `design/tokens.json` + `DESIGN_SYSTEM.md` |
| `/engineering-docs` | `docs/ARCHITECTURE`, `DATABASE`, `SECURITY`, `CODE_STYLE`, `TESTING`, `RULES`, `MEMORY`, `LIFECYCLE` + index |
| `/project-setup` | README, `SETUP`, `STRUCTURE`, commented `.env.example`, `GITHUB` rules, `CONTEXT_PACK`, `.cursor/rules`, `.claude` skills, `.github` |
| `/plan-build` | Milestones and small tasks with tests and tool assignment → `PLAN.md` |

### Build, review, ship
| Command | What you get |
|---|---|
| `/build-feature` | One `PLAN.md` task end-to-end: tests first, code, checks, self-review, commit |
| `/design-qa` | Built screen vs Figma or the design system → fix list |
| `/quality-review` | Parallel accessibility, UX, security, code and test review → one prioritised report |
| `/test-plan` | Criteria → tests, edge cases, devices, screen-reader script → `TEST_PLAN.md` |
| `/ship-checklist` | Pre-launch checklist (web + stores), expert review, rollback → `RELEASE.md` |
| `/post-launch` | Weekly metrics, feedback, retro, lessons fed back into the kit |
| `/ai-feature` | Any AI feature: model choice, prompts, evals, labelling, cost caps → `AI_FEATURE_*.md` |

### Anytime
| Command | What you get |
|---|---|
| `/handoff` | Short session handoff so any tool can continue; updates `docs/MEMORY.md` |
| `/portfolio` | All your projects at a glance, phase and next step |
| `/standards-refresh` | Are the standards still current? (WCAG, OWASP, privacy law, accessibility law, AI models, store rules) |
| `/product-standards` | The rulebook the other skills read |

## Agents

Specialists the skills call in parallel (you can also address them directly):

| Agent | Role |
|---|---|
| `market-researcher` | Evidence: competitors, prices, reviews, audience size, with sources |
| `devils-advocate` | The strongest case against the idea |
| `idea-champion` | The strongest honest case for it, and the best version |
| `accessibility-strategist` | Who the idea excludes; accessibility law by launch market; accessibility as a strength |
| `product-strategist` | Positioning, MVP scope, metrics, monetisation |
| `architect` | Stack, data model, APIs, ADRs |
| `ux-reviewer` · `accessibility-auditor` · `security-reviewer` · `code-reviewer` · `qa-engineer` | The review panel |
| `web-developer` · `mobile-developer` · `backend-developer` | Builders |

## Example workflows

### A new idea, start to one-pager
```
/product-kit:start
Give me everything for this idea: a fair-booking app for shared amenities in gated communities.
```
You answer short question rounds (or say *"just do it"* and get marked defaults). You get a brief, a clarity log, an evaluation with competitors and a path to Go, a design direction with clickable wireframes, a draft PRD and a one-pager — all in `docs/product/` and `design/`.

### Approve, then set everything up
```
I approve the pivot.
/product-kit:start — set it all up
```
The kit asks your picks once (name from the top 3, stack A or B, visual direction), then writes the brand kit, stack ADR, design tokens, full PRD, engineering docs and the repo setup, including rules for Claude, Cursor, Codex and Copilot.

### Build one task
```
/product-kit:start — build it
```
Picks the next `PLAN.md` task, creates a correctly named branch (`feat/Oct-19-booking-form`), writes failing tests, builds, runs the checks, and opens a pull request.

## Standalone + supercharged

| What you can do | Standalone | Supercharged with |
|---|---|---|
| Evaluate an idea | Your pitch and answers | Knowledge base (prior research), analytics (real usage) |
| Design direction and wireframes | HTML wireframes | Figma (build the wireframes and tokens there) |
| Engineering docs and repo setup | Your stack choices | Source control (read the real repo) |
| Build and review | Paste code or a diff | Source control (PR diffs, CI status), hosting (preview deployments) |
| Ship | Checklist | Hosting, database (backups, env), monitoring |

## MCP integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

| Category | Examples | What it enables |
|---|---|---|
| **Source control** | GitHub | PR diffs, CI status, branch rules, the repo itself |
| **Design** | Figma | Wireframes and tokens in Figma; design QA against frames |
| **Hosting** | Vercel | Preview deployments, env vars, rollbacks |
| **Database** | Supabase | Schema, RLS policies, backups |
| **Knowledge base** | Notion | Prior research, specs, decisions |
| **Project tracker** | Linear | Tasks from `PLAN.md` as tickets |
| **Chat** | Slack, Teams | Share the one-pager or a handoff with a team |

## Settings

Your profile lives in the project: `docs/product/OWNER.md` (hours, budget, accounts, AI subscriptions, preferences). The kit asks once and never re-asks. Keep a master copy in the kit repo's `owner/OWNER.md` (git-ignored) so new projects start filled in.

## The full kit

Project templates, safety hooks, CI, git hooks, the Expo and Next.js starters, evals and the docs site live in the repo: https://github.com/sairam5294/product-kit — create a project with `scripts/new-project.sh`. MIT licence.
