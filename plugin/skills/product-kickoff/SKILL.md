---
name: product-kickoff
description: Runs the whole Product Kit from one command — idea to launch, phase by phase with approval gates, or everything in one go ("give me everything for this idea" runs the full Idea Pack; "set it all up" after approval runs naming/brand, stack, design system, full PRD, engineering docs and project setup). Use for "I have a new idea", "run the whole kit", "give me everything", "set it all up", "start a project", "kickoff", or "where are we / what's next?".
---

# Product Kickoff

Run phases in order, one at a time. Each phase = a skill in the sibling folder `../<skill>/SKILL.md`; outputs go in `docs/product/`.

| # | Skill | Output | Gate |
|---|---|---|---|
| 1 | new-idea | PROJECT_BRIEF.md + CLARITY.md | owner confirms |
| 2 | evaluate-idea | EVALUATION.md + COMPETITORS.md | — |
| 2a | design-direction | DESIGN_DIRECTION.md + design/wireframes/ | owner picks a direction |
| 2b | write-prd (draft) | PRD.md v0.x | owner reviews |
| 3 | validate-idea (recommended) | VALIDATION.md (prototype test uses the wireframes) | results fed into evaluation |
| ✦ | **Idea Pack** | ONE_PAGER.md + README.md index | written after 2b, refreshed each phase |
| ★ | **Approval** | STATUS.md `Evaluation: APPROVED` | **hard gate for 4+** |
| 4 | name-product | NAMING.md + BRAND.md (logo, guidelines, colour, fonts, icons, rules) | owner picks |
| 5 | tech-stack | TECH_STACK.md | owner approves |
| 6 | design-system | DESIGN_SYSTEM.md + tokens (from the chosen direction) | owner approves |
| 7 | write-prd (full) | PRD.md v1.x | owner approves |
| 7a | engineering-docs | docs/ARCHITECTURE · DATABASE · SECURITY · CODE_STYLE · TESTING · RULES · MEMORY + docs/README index | owner confirms |
| 7b | project-setup | README · docs/SETUP · STRUCTURE · GITHUB · CONTEXT_PACK · .env.example · .cursor/rules · .claude/skills · .github | owner confirms |
| 8 | plan-build | PLAN.md | owner approves |
| 9 | build-feature (+ design-qa) | code + tests | checks pass |
| 10 | quality-review | reviews/*.md | no MUST violations |
| 11 | test-plan | TEST_PLAN.md | exit criteria met |
| 12 | ship-checklist | RELEASE.md | checklist done |
| 13 | post-launch | METRICS.md, LESSONS.md | loop weekly |

Phases 1–2b plus the one-pager make the **Idea Pack** (validation, phase 3, then tests it with real people): everything an owner needs to decide — honest verdict, competitors and differentiator, strengthening plan, tools and cost, draft design, draft PRD, open questions — before any code. All of it lives in `docs/` and `design/`, which the approval gate allows.

Anytime: `tool-plan` (which AI tool does which job — offer it at kickoff), `handoff` (end of session), `standards-refresh` (quarterly), `portfolio` (all projects), `ai-feature` (whenever a feature uses AI).

## Procedure
1. Find `docs/product/STATUS.md` (read `HANDOFF.md` too if present). Found → state current phase in one line, continue. Not found → create `docs/product/`, copy `templates/STATUS.md`, `templates/DECISIONS.md` and `templates/COSTS.md` (and the kit's `owner/OWNER.md` if reachable, else ask the owner's profile questions once), start phase 1.
2. Finish one phase, write its file, get owner confirmation, update STATUS.md, then offer the next. After 2b (and after every later phase), write or refresh `docs/product/ONE_PAGER.md` and `docs/product/README.md` from `templates/ONE_PAGER.md` and `templates/IDEA_PACK_README.md`.
   - **Depth:** Quick, Standard (default) or Deep — see `../product-standards/references/context-budget.md` (outputs, research budget, token rules). Suggest Quick for early ideas; say which mode you're using in one line. **Quick runs 1 → 2 → one-pager only** — read only: this file, `../new-idea/SKILL.md` (+ its owner-unavailable path), `../evaluate-idea/SKILL.md`, its `scoring-rubric.md`, `report-template.md`, `competitive-analysis.md` (Lite block), `../product-standards/references/context-budget.md`, and the `accessibility-law.md` rows for the launch markets (grep them): mark 2a and 2b `Skipped (Quick mode)` in STATUS, leave the wireframe/PRD lines out of the one-pager and README, and offer Standard when the owner wants to go further.
   - **Before presenting any Idea Pack:** run `python3 scripts/check_idea_pack.py <project> --mode <mode>` (this skill's folder) and fix every FAIL; a WARN (length) is acceptable if the README says why. No shell → walk its checks by hand.
   - The owner can ask for the whole Idea Pack in one go ("give me everything for this idea"): run 1 → 2 → 2a → 2b → one-pager (skip 1 if a brief already exists), pausing only for questions that block the next phase (CLARITY.md). Skip the per-phase presentations; present the one-pager at the end with one line per phase.
   - **"Set it all up" (after approval):** run tool-plan → 4 name-product (names + brand) → 5 tech-stack → 6 design-system → 7 write-prd (full) → 7a engineering-docs → 7b project-setup in one go. Ask the owner's picks in one round up front (name from the top 3, stack A/B, visual direction if not chosen); anything unanswered takes the recommended option as `[Default]`. Present one summary at the end; then plan-build. Stop before any app code.
   - **"Build it" (after setup):** plan-build, then build-feature task by task — one task per session and branch, quality-review before each merge. Never all tasks in one session.
   - **Owner unavailable** overrides "pause for blocking questions": don't wait — log them in CLARITY and continue on defaults.
   - **Owner unavailable** (scheduled run, "just do it", no reply): take the recommended default for every decision, mark each one `[Default]` in the documents and "default (unconfirmed)" in DECISIONS.md, set those phases to `Waiting for owner` in STATUS, and list the defaults to confirm at the top of the one-pager (≤ 3 there; the rest in DECISIONS.md). Facts stay unknown with a Q-id — never guess them. Presenting with no owner present: point to the one-pager, list the defaults and the next test, stop.
3. Gate: phases 4+ need `Evaluation: APPROVED`, set **only by the owner** (`scripts/approve.sh`, or their explicit words quoted in DECISIONS.md where there's no shell). Re-check STATUS before every build phase. If owner wants to skip: state top 2 risks, obey, log in DECISIONS.md.
4. If goal/audience/scope changes later: update the brief (new version), log it, offer to re-evaluate the changed parts.
5. End each turn with: produced · one decision needed · next phase.

## Which tool for which phase
Phases 1–8 (docs only) work anywhere, incl. Claude Cowork/desktop. Phases 9–12 need a shell and the repo: Claude Code, Cursor or Codex (hooks, `npm run check`, starters). Cowork has no hooks — follow the gate rules yourself.

## Other plugins
If other installed plugins offer similar skills (accessibility review, code review, specs, test strategy, deploy checklists), use the Product Kit skill for kit phases; use complementary ones (ux-copy, research-synthesis, debug, metrics-review) inside phases.

## Style
Owner = senior UX designer, light coding. Plain language, 3–5 questions per round with a recommended option. Honest coach, not judge: candid about weaknesses, and every weakness comes with how to make the idea stronger. Keep context lean: load only the files a phase needs.
