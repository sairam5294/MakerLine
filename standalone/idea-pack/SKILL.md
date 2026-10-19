---
name: idea-pack
description: Turn a product idea into an Idea Pack before any code — discovery questions, an honest and constructive evaluation (strongest version, reality check, competitors and differentiator test, path to Go, tools and cost, accessibility and compliance), design direction with clickable wireframes, a draft PRD and a one-pager. Use for "I have an idea", "evaluate my idea", "who are my competitors?", "give me everything for this idea".
---

# Idea Pack

Run the phases in order, one at a time. Each phase is a sibling skill (`../<skill>/SKILL.md`); outputs go in `docs/product/` and `design/`.

| # | Skill | Output | Owner step |
|---|---|---|---|
| 1 | new-idea | PROJECT_BRIEF.md + CLARITY.md | confirms the brief |
| 2 | evaluate-idea | EVALUATION.md + COMPETITORS.md | reads the verdict |
| 2a | design-direction | DESIGN_DIRECTION.md + design/wireframes/ | picks a direction |
| 2b | write-prd (Draft mode) | PRD.md v0.x | reviews |
| 3 | validate-idea (recommended) | VALIDATION.md | runs the tests with real people |
| ✦ | this skill | ONE_PAGER.md + README.md index | decides go / change / stop |

## Procedure
1. Find `docs/product/STATUS.md`. Found → say the current phase in one line and continue. Not found → create `docs/product/`, copy `templates/STATUS.md`, `templates/DECISIONS.md` and `templates/COSTS.md`, start phase 1.
2. **Depth:** Quick, Standard (default) or Deep — see `../product-standards/references/context-budget.md` for outputs, research budgets and token rules. Suggest Quick for early ideas; say which mode you're using.
3. Finish one phase, write its file, get the owner's confirmation, update STATUS.md, offer the next. After 2b write `docs/product/ONE_PAGER.md` and `docs/product/README.md` from `templates/ONE_PAGER.md` and `templates/IDEA_PACK_README.md`; refresh them after later phases.
   - **All in one go** ("give me everything for this idea"): run 1 → 2 → 2a → 2b → one-pager (skip 1 if a brief exists), pausing only for questions that block the next phase. Skip per-phase presentations; present the one-pager with one line per phase.
   - **Owner unavailable:** take the recommended default for every decision, mark it `[Default]` and "default (unconfirmed)" in DECISIONS.md, set those phases to `Waiting for owner`, list the defaults at the top of the one-pager. Facts stay unknown with a question id — never guess them.
4. **Before presenting:** run `python3 scripts/check_idea_pack.py <project> --mode <mode>` (this skill's folder) and fix every FAIL. No shell → walk its checks by hand.
5. **Decision:** the owner decides go, change or stop. Record their words in DECISIONS.md. This standalone pack has no build phases: where a skill mentions `scripts/approve.sh`, naming, tech stack, design system or building, that's the full Product Kit (https://github.com/sairam5294/product-kit) — offer it when the owner decides to build.
6. End each turn with: produced · one decision needed · next phase.

Owner profile: if there's no `docs/product/OWNER.md`, ask the owner's hours, budget, skills and accounts once and save them there.

## Principles
- **Honest coach, not judge:** candid about weaknesses; every weakness comes with how to make the idea stronger or a test that would settle it.
- **Accessible worldwide, no discrimination:** apply `../product-standards/references/inclusion.md` whatever the launch market, plus that market's law (`accessibility-law.md`). Not legal advice.
- **Evidence over opinion:** real, linked, dated sources; "unknown + how to find out" beats an invented number.
- Plain language, 3–5 questions per round with a recommended option for decisions. Keep context lean: load only the files a phase needs.
