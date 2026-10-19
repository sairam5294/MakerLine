---
name: idea-pack
description: Run the whole Idea Pack before any code. Covers discovery questions, an honest and constructive evaluation (strongest version, reality check, competitors and differentiator test, path to Go, tools and cost, accessibility and compliance), design direction with clickable wireframes, a draft PRD and a one-pager. Trigger with "I have an idea", "run the idea pack", "give me everything for this idea", "evaluate my idea", or "who are my competitors?".
argument-hint: "<idea, 'give me everything for this idea', or nothing to resume>"
---

# /idea-pack

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run the Idea Pack phases in order, one at a time. Each phase is a sibling skill (`../<skill>/SKILL.md`); outputs go in `docs/product/` and `design/`.

## Usage

```
/idea-pack                                      # resume: find STATUS.md, say the phase, offer the next
/idea-pack I have an idea: <pitch>              # phase by phase, with a pause after each
/idea-pack give me everything for <idea>        # all phases in one go (add "quick" or "deep")
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                        IDEA PACK                             │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Discovery → evaluation → design direction → draft PRD     │
│  ✓ One-pager + README index, refreshed after every phase     │
│  ✓ Quick / Standard / Deep depth                             │
│  ✓ Checker script before anything is presented               │
│  ✓ Owner decides go / change / stop — no build phases here   │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Knowledge base: prior research and decisions              │
│  + Design: wireframes and directions in Figma                │
└──────────────────────────────────────────────────────────────┘
```

## Phases

| # | Skill | Output | Owner step |
|---|---|---|---|
| 1 | new-idea | PROJECT_BRIEF.md + CLARITY.md | confirms the brief |
| 2 | evaluate-idea | EVALUATION.md + COMPETITORS.md | reads the verdict |
| 2a | design-direction | DESIGN_DIRECTION.md + design/wireframes/ | picks a direction |
| 2b | write-prd (Draft mode) | PRD.md v0.x | reviews |
| 3 | validate-idea (recommended) | VALIDATION.md | runs the tests with real people |
| ✦ | this skill | ONE_PAGER.md + README.md index | decides go / change / stop |

## Inputs

- `docs/product/STATUS.md` — the current phase (none → first run).
- Templates in this skill's folder: `templates/STATUS.md`, `DECISIONS.md`, `COSTS.md`, `ONE_PAGER.md`, `IDEA_PACK_README.md`.
- Owner profile: if there's no `docs/product/OWNER.md`, ask the owner's hours, budget, skills and accounts once and save them there.
- Depth from the owner: Quick, Standard (default) or Deep — `../product-standards/references/context-budget.md`.

## Workflow

1. **Locate the project.** Find `docs/product/STATUS.md`. Found → say the current phase in one line and continue. Not found → create `docs/product/`, copy `templates/STATUS.md`, `templates/DECISIONS.md` and `templates/COSTS.md`, start phase 1.
2. **Pick the depth.** Quick, Standard (default) or Deep — see `../product-standards/references/context-budget.md` for outputs, research budgets and token rules. Suggest Quick for early ideas; say which mode you're using.
3. **Run one phase at a time.** Finish the phase, write its file, get the owner's confirmation, update STATUS.md, offer the next. After 2b write `docs/product/ONE_PAGER.md` and `docs/product/README.md` from `templates/ONE_PAGER.md` and `templates/IDEA_PACK_README.md`; refresh them after later phases.
4. **All in one go** ("give me everything for this idea"): run 1 → 2 → 2a → 2b → one-pager (skip 1 if a brief exists), pausing only for questions that block the next phase. Skip per-phase presentations; present the one-pager with one line per phase.
5. **Owner unavailable:** take the recommended default for every decision, mark it `[Default]` and "default (unconfirmed)" in DECISIONS.md, set those phases to `Waiting for owner`, list the defaults at the top of the one-pager. Facts stay unknown with a question id — never guess them.
6. **Check before presenting.** Run `python3 scripts/check_idea_pack.py <project> --mode <mode>` (this skill's folder) and fix every FAIL. No shell → walk its checks by hand.
7. **Decision.** The owner decides go, change or stop. Record their words in DECISIONS.md.
   - This standalone pack has no build phases: where a skill mentions `scripts/approve.sh`, naming, tech stack, design system or building, that's the full Product Kit (https://github.com/sairam5294/product-kit) — offer it when the owner decides to build.
8. **End each turn** with: produced · one decision needed · next phase.

## Output

| File | What | When |
|---|---|---|
| `docs/product/STATUS.md`, `DECISIONS.md`, `COSTS.md` | project state, decisions (incl. the owner's go / change / stop words), costs | created on first run, updated every phase |
| `docs/product/ONE_PAGER.md` + `README.md` | the Idea Pack summary and index | after 2b, refreshed after later phases |
| each phase's file (table above) | written by that phase's skill | per phase |

End-of-turn line, always:

```
Produced: <files> · Decision needed: <one> · Next: <phase>
```

## If connectors available

If **~~knowledge base** is connected:
- Pull prior research and decisions on the idea before the phases search the web.

If **~~design** is connected:
- design-direction can place the wireframes and visual directions in Figma.

## Rules

- **Honest coach, not judge:** candid about weaknesses; every weakness comes with how to make the idea stronger or a test that would settle it.
- **Accessible worldwide, no discrimination:** apply `../product-standards/references/inclusion.md` whatever the launch market, plus that market's law (`accessibility-law.md`). Not legal advice.
- **Evidence over opinion:** real, linked, dated sources; "unknown + how to find out" beats an invented number.
- **Style:** plain language, 3–5 questions per round with a recommended option for decisions. Keep context lean: load only the files a phase needs.
- **No build phases here:** offer the full Product Kit when the owner decides to build.

## Tips

1. Say *"quick"* for a first look; go Standard once the idea survives it.
2. *"Give me everything for this idea"* gets the whole pack with one pause for blocking questions.
3. Validation (phase 3) is where the pack meets real people — don't skip it before deciding to build.

## Related

- Entry point: `start` · Phases: `new-idea` → `evaluate-idea` → `design-direction` → `write-prd` → `validate-idea` · Anytime: `tool-plan`
- Reads: `templates/*.md`, `scripts/check_idea_pack.py`, `../product-standards/references/context-budget.md`, `inclusion.md`, `accessibility-law.md`
