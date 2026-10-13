---
name: product-kickoff
description: Orchestrates idea-to-launch with approval gates and tracks progress. Use for "I have a new idea", "start a project", "kickoff", or "where are we / what's next?".
---

# Product Kickoff

Run phases in order, one at a time. Each phase = a skill in the sibling folder `../<skill>/SKILL.md`; outputs go in `docs/product/`.

| # | Skill | Output | Gate |
|---|---|---|---|
| 1 | new-idea | PROJECT_BRIEF.md | owner confirms |
| 2 | evaluate-idea | EVALUATION.md | — |
| 3 | validate-idea (recommended) | VALIDATION.md | results fed into evaluation |
| ★ | **Approval** | STATUS.md `Evaluation: APPROVED` | **hard gate for 4+** |
| 4 | name-product | NAMING.md | owner picks |
| 5 | tech-stack | TECH_STACK.md | owner approves |
| 6 | design-system | DESIGN_SYSTEM.md + tokens | owner approves |
| 7 | write-prd | PRD.md | owner approves |
| 8 | plan-build | PLAN.md | owner approves |
| 9 | build-feature (+ design-qa) | code + tests | checks pass |
| 10 | quality-review | reviews/*.md | no MUST violations |
| 11 | test-plan | TEST_PLAN.md | exit criteria met |
| 12 | ship-checklist | RELEASE.md | checklist done |
| 13 | post-launch | METRICS.md, LESSONS.md | loop weekly |

Anytime: `handoff` (end of session), `standards-refresh` (quarterly), `portfolio` (all projects), `ai-feature` (whenever a feature uses AI).

## Procedure
1. Find `docs/product/STATUS.md` (read `HANDOFF.md` too if present). Found → state current phase in one line, continue. Not found → create `docs/product/`, copy `templates/STATUS.md`, `templates/DECISIONS.md` and `templates/COSTS.md` (and the kit's `owner/OWNER.md` if reachable, else ask the owner's profile questions once), start phase 1.
2. Finish one phase, write its file, get owner confirmation, update STATUS.md, then offer the next.
3. Gate: phases 4+ need `Evaluation: APPROVED`, set **only by the owner** (`scripts/approve.sh`, or their explicit words quoted in DECISIONS.md where there's no shell). Re-check STATUS before every build phase. If owner wants to skip: state top 2 risks, obey, log in DECISIONS.md.
4. If goal/audience/scope changes later: update the brief (new version), log it, offer to re-evaluate the changed parts.
5. End each turn with: produced · one decision needed · next phase.

## Which tool for which phase
Phases 1–8 (docs only) work anywhere, incl. Claude Cowork/desktop. Phases 9–12 need a shell and the repo: Claude Code, Cursor or Codex (hooks, `npm run check`, starters). Cowork has no hooks — follow the gate rules yourself.

## Other plugins
If other installed plugins offer similar skills (accessibility review, code review, specs, test strategy, deploy checklists), use the Product Kit skill for kit phases; use complementary ones (ux-copy, research-synthesis, debug, metrics-review) inside phases.

## Style
Owner = senior UX designer, light coding. Plain language, 3–5 questions per round with a recommended option, candid over flattering. Keep context lean: load only the files a phase needs.
