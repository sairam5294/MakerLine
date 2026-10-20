---
name: product-kickoff
description: Run the whole MakerLine from one command. Covers idea to launch, phase by phase with approval gates, or in one go ("give me everything for this idea" runs the full Idea Pack; "set it all up" after approval runs naming/brand, stack, design system, full PRD, engineering docs and project setup). Trigger with "I have a new idea", "run the whole kit", "give me everything", "set it all up", "start a project", "kickoff", or "where are we / what's next?".
argument-hint: "<idea, 'give me everything', 'set it all up', 'build it', or nothing to resume>"
---

# /product-kickoff

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run the kit's phases in order. Each phase is a skill in `../<skill>/SKILL.md`; outputs go in `docs/product/`.

## Usage

```
/product-kickoff                                  # resume: find STATUS.md, say the phase, offer the next
/product-kickoff give me everything for <idea>    # full Idea Pack in one go (add "quick" or "deep")
/product-kickoff set it all up                    # after approval: tool-plan → … → project-setup
/product-kickoff build it                         # after setup: plan-build, then one task per session
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                     PRODUCT KICKOFF                          │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ 13 phases, one skill each, outputs in docs/product/       │
│  ✓ Idea Pack (1 → 2b + one-pager) before any code            │
│  ✓ Hard approval gate before phases 4+ (owner only)          │
│  ✓ "Everything" / "set it all up" / "build it" in one go     │
│  ✓ Owner-unavailable path: defaults, never guessed facts     │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Source control: resume from the repo's STATUS and HANDOFF │
│  + Knowledge base: owner profile and prior decisions         │
└──────────────────────────────────────────────────────────────┘
```

## Phases

| # | Skill | Output | Gate |
|---|---|---|---|
| 1 | new-idea | PROJECT_BRIEF + CLARITY | owner confirms |
| 2 | evaluate-idea | EVALUATION + COMPETITORS | — |
| 2a | design-direction | DESIGN_DIRECTION + design/wireframes/ | owner picks a direction |
| 2b | write-prd (draft) | PRD v0.x | owner reviews |
| 3 | validate-idea (recommended) | VALIDATION (+ VALIDATION_RESULTS) | results feed the evaluation |
| ✦ | **Idea Pack** | ONE_PAGER + README index | after 2b, refreshed each phase |
| ★ | **Approval** | STATUS `Evaluation: APPROVED` | **hard gate for 4+** |
| 4 | name-product | NAMING + BRAND | owner picks |
| 5 | tech-stack | TECH_STACK | owner approves |
| 6 | design-system | DESIGN_SYSTEM + tokens | owner approves |
| 7 | write-prd (full) | PRD v1.x | owner approves |
| 7a | engineering-docs | docs/ARCHITECTURE, DATABASE, SECURITY, CODE_STYLE, TESTING, RULES, MEMORY, LIFECYCLE | owner confirms |
| 7b | project-setup | README, SETUP, STRUCTURE, GITHUB, CONTEXT_PACK, .env.example, AI-tool rules | owner confirms |
| 8 | plan-build | PLAN | owner approves |
| 9 | build-feature (+ design-qa) | code + tests + PR evidence | checks pass |
| 10 | quality-review | reviews/*.md | no MUST violations |
| 11 | test-plan | TEST_PLAN | exit criteria met |
| 12 | ship-checklist | RELEASE | checklist done |
| 13 | post-launch | METRICS, LESSONS | weekly |

The **Idea Pack** (1–2b + one-pager) is everything the owner needs to decide before any code; it lives in `docs/` and `design/`, which the gate allows. **Anytime:** `tool-plan` (offer at kickoff) · `handoff` · `standards-refresh` · `portfolio` · `ai-feature`.

## Inputs

- `docs/product/STATUS.md` (+ `HANDOFF.md`) — the current phase. Never scan other docs to find it.
- `templates/*.md` here; `docs/product/OWNER.md` (a kit-repo clone may also have `owner/OWNER.md` and `portfolio/OUTCOMES.md`; the plugin alone has neither).
- Depth: Quick, Standard (default) or Deep.

## Workflow

1. **Locate the project.** STATUS.md found → say the phase in one line, continue. Not found → create `docs/product/`, copy `templates/STATUS.md`, `DECISIONS.md`, `COSTS.md`; OWNER.md from the kit clone, else ask the profile questions once (owner unavailable → build it from the brief, fields *unconfirmed*); start phase 1.
2. **One phase at a time.** Finish it, write its file, get confirmation, update STATUS, offer the next. After 2b and every later phase, refresh `ONE_PAGER.md` and `README.md` from `templates/ONE_PAGER.md` and `IDEA_PACK_README.md`.
3. **Pick the depth** (`../product-standards/references/context-budget.md`); suggest Quick for early ideas; say the mode in one line.
   - **Quick = follow `../evaluate-idea/references/quick-run.md` only** (brief → evaluation → one-pager, one guide instead of eight files). It wins over "give me everything".
   - **Quick → Standard:** keep the Quick EVALUATION and Lite COMPETITORS (say so in the README); expand only if the owner asks.
4. **Check before presenting.** `python3 scripts/check_idea_pack.py <project> --mode <mode>` (this folder); fix every FAIL; a length WARN is fine if the README says why. No shell → walk its checks by hand.
5. **"Give me everything."** Standard/Deep: 1 → 2 → 2a → 2b → one-pager (skip 1 if a brief exists), pausing only for questions that block the next phase. Present the one-pager with one line per phase.
6. **"Set it all up"** (after approval): tool-plan → 4 → 5 → 6 → 7 (full PRD) → 7a → 7b in one go. Ask the picks in one round up front (name from the top 3, stack A/B, visual direction); unanswered → recommended option as `[Default]`. One summary at the end; stop before app code.
7. **"Build it"** (after setup): plan-build, then build-feature — one task per session and branch, quality-review before each merge.
8. **Owner unavailable** (scheduled run, "just do it", no reply): don't pause. Recommended default for every decision, marked `[Default]` and "default (unconfirmed)" in DECISIONS; those phases `Waiting for owner`; ≤ 3 defaults in the one-pager's *Defaults to confirm* line. Facts stay unknown with a Q-id — never guess. Details: `../new-idea/SKILL.md` → Owner unavailable.
9. **Gate.** Phases 4+ need `Evaluation: APPROVED`, set **only by the owner** (`scripts/approve.sh`, or their explicit words quoted in DECISIONS where there's no shell). Re-check before every build phase. Owner insists on skipping → state the top 2 risks, obey, log it.
10. **Changes later.** Goal/audience/scope changes → new brief version, log it, offer to re-evaluate. Any doc re-run updates only affected sections, adds a *What changed in v{n}* block (≤ 5 bullets citing brief version, Q-id or V-id) and a revision-log row. The one-pager just gets a new date.
11. **End each turn:** `Produced: <files> · Decision needed: <one> · Next: <phase>`.

## Output

| File | What | When |
|---|---|---|
| `docs/product/STATUS.md`, `DECISIONS.md`, `COSTS.md` | state, decisions, costs | first run; every phase |
| `docs/product/ONE_PAGER.md` + `README.md` | Idea Pack summary and index | after 2b; every later phase |
| each phase's file | by that phase's skill | per phase |

## If connectors available

If **~~source control** is connected: read STATUS.md and HANDOFF.md from the repo to resume.

If **~~knowledge base** is connected: pull the owner profile and prior decisions instead of re-asking.

## Rules

- Never write `Evaluation: APPROVED` yourself.
- Phases 1–8 (docs) work anywhere, incl. the Claude app. Phases 9–12 need a shell and the repo (Claude Code, Cursor, Codex); without hooks, follow the gate yourself.
- Overlapping plugins: the MakerLine skill wins for kit phases; complementary skills (ux-copy, research-synthesis, debug, metrics-review) are welcome inside phases.
- Owner = senior UX designer, light coding: plain language, 3–5 questions per round with a recommended option. Honest coach, not judge — every weakness comes with how to make the idea stronger.

## Tips

1. Say *"quick"* for a first look; go Standard once the idea survives.
2. *"Give me everything for this idea"* gets the whole Idea Pack with one pause for blocking questions.
3. Have your name, stack and visual picks ready before *"set it all up"*.

## Related

- Entry point: `start` · Phases: the table above · Anytime: `tool-plan`, `handoff`, `standards-refresh`, `portfolio`, `ai-feature`
- Reads: `templates/*.md`, `scripts/check_idea_pack.py`, `../product-standards/references/context-budget.md`, `accessibility-law-summary.md` (Deep and ship: `accessibility-law.md`)
