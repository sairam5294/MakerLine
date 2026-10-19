---
name: product-kickoff
description: Run the whole Product Kit from one command. Covers idea to launch, phase by phase with approval gates, or in one go ("give me everything for this idea" runs the full Idea Pack; "set it all up" after approval runs naming/brand, stack, design system, full PRD, engineering docs and project setup). Trigger with "I have a new idea", "run the whole kit", "give me everything", "set it all up", "start a project", "kickoff", or "where are we / what's next?".
argument-hint: "<idea, 'give me everything', 'set it all up', 'build it', or nothing to resume>"
---

# /product-kickoff

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run the kit's phases in order, one at a time. Each phase is a skill in the sibling folder `../<skill>/SKILL.md`; outputs go in `docs/product/`.

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

**Idea Pack** = phases 1–2b plus the one-pager (validation, phase 3, then tests it with real people). It is everything an owner needs to decide — honest verdict, competitors and differentiator, strengthening plan, tools and cost, draft design, draft PRD, open questions — before any code. All of it lives in `docs/` and `design/`, which the approval gate allows.

**Anytime skills:** `tool-plan` (which AI tool does which job — offer it at kickoff) · `handoff` (end of session) · `standards-refresh` (quarterly) · `portfolio` (all projects) · `ai-feature` (whenever a feature uses AI).

## Inputs

- `docs/product/STATUS.md` (and `HANDOFF.md` if present) — the current phase.
- `templates/*.md` in this skill's folder; `docs/product/OWNER.md` (a kit-repo clone may also have `owner/OWNER.md`; the plugin alone doesn't — then ask once). `portfolio/OUTCOMES.md` exists only in a kit-repo clone; missing → "No calibration data yet".
- Depth from the owner: Quick, Standard (default) or Deep.

## Workflow

1. **Locate the project.** Find `docs/product/STATUS.md` (read `HANDOFF.md` too if present).
   - Found → state the current phase in one line, continue.
   - Not found → create `docs/product/`, copy `templates/STATUS.md`, `templates/DECISIONS.md` and `templates/COSTS.md` (and `owner/OWNER.md` if you're in a kit-repo clone, else ask the owner's profile questions once), start phase 1.
2. **Run one phase at a time.** Finish the phase, write its file, get owner confirmation, update STATUS.md, then offer the next. After 2b (and after every later phase), write or refresh `docs/product/ONE_PAGER.md` and `docs/product/README.md` from `templates/ONE_PAGER.md` and `templates/IDEA_PACK_README.md`.
3. **Pick the depth.** Quick, Standard (default) or Deep — see `../product-standards/references/context-budget.md` (outputs, research budget, token rules). Suggest Quick for early ideas; say which mode you're using in one line.
   - **Quick runs 1 → 2 → one-pager only — this wins over "give me everything" (step 5).** The complete Quick reading list, each read once: this file and `templates/*.md`; `../new-idea/SKILL.md` (+ its owner-unavailable path), `references/question-bank.md`, `brief-template.md`, `clarity-template.md`; `../evaluate-idea/SKILL.md`, `references/scoring-rubric.md`, `report-template-quick.md`, `competitors-lite.md`, `research-cache.md`; `../product-standards/references/context-budget.md`, `inclusion.md`, `accessibility-law-summary.md`. Nothing else.
   - In Quick, mark 2a and 2b `Skipped (Quick mode)` in STATUS, leave the wireframe/PRD lines out of the one-pager and README, and offer Standard when the owner wants to go further.
4. **Check before presenting any Idea Pack.** Run `python3 scripts/check_idea_pack.py <project> --mode <mode>` (this skill's folder) and fix every FAIL; a WARN (length) is acceptable if the README says why. No shell → walk its checks by hand.
5. **"Give me everything for this idea" (whole Idea Pack in one go).** Standard/Deep: run 1 → 2 → 2a → 2b → one-pager (Quick: step 3) (skip 1 if a brief already exists), pausing only for questions that block the next phase (CLARITY.md). Skip the per-phase presentations; present the one-pager at the end with one line per phase.
6. **"Set it all up" (after approval).** Run tool-plan → 4 name-product (names + brand) → 5 tech-stack → 6 design-system → 7 write-prd (full) → 7a engineering-docs → 7b project-setup in one go.
   - Ask the owner's picks in one round up front (name from the top 3, stack A/B, visual direction if not chosen); anything unanswered takes the recommended option as `[Default]`.
   - Present one summary at the end; then plan-build. Stop before any app code.
7. **"Build it" (after setup).** plan-build, then build-feature task by task — one task per session and branch, quality-review before each merge. Never all tasks in one session.
8. **Owner unavailable** (scheduled run, "just do it", no reply). Don't pause for blocking questions; log them in CLARITY and continue.
   - Take the recommended default for every decision; mark each one `[Default]` in the documents and "default (unconfirmed)" in DECISIONS.md; set those phases to `Waiting for owner` in STATUS.
   - List the defaults to confirm at the top of the one-pager (≤ 3 there; the rest in DECISIONS.md). Facts stay unknown with a Q-id — never guess them.
   - Presenting with no owner present: point to the one-pager, list the defaults and the next test, stop.
9. **Gate.** Phases 4+ need `Evaluation: APPROVED`, set **only by the owner** (`scripts/approve.sh`, or their explicit words quoted in DECISIONS.md where there's no shell). Re-check STATUS before every build phase. If the owner wants to skip: state the top 2 risks, obey, log in DECISIONS.md.
10. **Changes later.** If goal/audience/scope changes: update the brief (new version), log it, offer to re-evaluate the changed parts.
11. **End each turn** with: produced · one decision needed · next phase.

## Output

| File | What | When |
|---|---|---|
| `docs/product/STATUS.md`, `DECISIONS.md`, `COSTS.md` | project state, decisions, costs | first run; updated every phase |
| `docs/product/ONE_PAGER.md` + `README.md` | Idea Pack summary and index | after 2b; refreshed every later phase |
| each phase's file (table above) | by that phase's skill | per phase |

End-of-turn line, always:

```
Produced: <files> · Decision needed: <one> · Next: <phase>
```

## If connectors available

If **~~source control** is connected (adopted or existing project):
- Read STATUS.md and HANDOFF.md from the repo to resume at the right phase.

If **~~knowledge base** is connected:
- Pull the owner profile and prior decisions instead of re-asking the profile questions.

## Rules

- **Gate:** never write `Evaluation: APPROVED` yourself; only the owner sets it. Re-check STATUS before every build phase.
- **Which tool for which phase:** phases 1–8 (docs only) work anywhere, incl. Claude Cowork/desktop. Phases 9–12 need a shell and the repo: Claude Code, Cursor or Codex (hooks, `npm run check`, starters). Cowork has no hooks — follow the gate rules yourself.
- **Other plugins:** if other installed plugins offer similar skills (accessibility review, code review, specs, test strategy, deploy checklists), use the Product Kit skill for kit phases; use complementary ones (ux-copy, research-synthesis, debug, metrics-review) inside phases.
- **Style:** owner = senior UX designer, light coding. Plain language, 3–5 questions per round with a recommended option. Honest coach, not judge: candid about weaknesses, and every weakness comes with how to make the idea stronger.
- **Context:** keep it lean — load only the files a phase needs.

## Tips

1. Say *"quick"* for a first look at an idea; go Standard once it survives.
2. *"Give me everything for this idea"* gets the whole Idea Pack with one pause for blocking questions.
3. After approval, *"set it all up"* does the whole setup in one go — have your name, stack and visual picks ready.

## Related

- Entry point: `start` · Phases: the skills in the table above, in order · Anytime: `tool-plan`, `handoff`, `standards-refresh`, `portfolio`, `ai-feature`
- Reads: `templates/*.md`, `scripts/check_idea_pack.py`, `../product-standards/references/context-budget.md`, `accessibility-law.md`
