# RhythmBuddy × Product Kit

**What it is.** A macOS menu-bar app that keeps a low-interrupt daily wellness rhythm: water, eye breaks, stretching, meals, morning sunlight, a post-lunch walk and a bedtime wind-down. A pixel mascot walks in with a speech bubble; reminders due close together merge into one "health break". Python + PyObjC, ~100 modules, 275 unit tests, accessibility checks, ad-hoc signed `.app` + DMG. It is the grown-up version of HydroBuddy.

**Why it is the first example.** It is an *existing* codebase, so it tests the half of the kit that greenfield projects never touch: `upgrade-project` onto a repo with its own CI, Cursor rules and conventions, then the review skills on code the kit did not write. It is also Python, and the kit's starters are JavaScript, which surfaces every place the standards silently assume Node.

## Kit phases run

| Date | Phase | Result | Notes |
| --- | --- | --- | --- |
| 2026-10-14 | `upgrade-project` preview | Would have overwritten the project's CI and Cursor rules | Led to adopt mode in the kit (v0.6) |
| 2026-10-14 | `upgrade-project --apply` (adopt mode) | 109 files added, 0 code files touched, own CI/rules/pre-commit kept | sairam5294/rhythm_buddy#9 |
| 2026-10-14 | `quality-review` (a11y, security, code, QA reviewers) | **Ready after fixes**: 8 MUST, 15 SHOULD, 6 suggestions | [`docs/product/reviews/2026-10-14-adoption-review.md`](docs/product/reviews/2026-10-14-adoption-review.md) |
| — | `test-plan`, `ship-checklist` | Next | after the MUST fixes |

## What the kit got wrong (feeds LESSONS.md)

1. `upgrade-project` assumed every project was born from `new-project`: it would have replaced a Python project's `ci.yml` with the kit's Node workflow and merged kit rules over hand-written ones. Fixed with adopt mode (never overwrite, `.product-kit-keep`, STATUS approved-by-adoption).
2. The kickoff skill would have seen a shipped v1.0 as "phase 1: discovery". Fixed: adopt mode marks phases 1–9 done.
3. The project's `.gitignore` silently hid three kit-added files, including `.claude/settings.json` (the safety permissions). Fixed: the script now warns about git-ignored additions.
4. Projects committed `docs/product/OWNER.md` (hours, budget, accounts). Fixed: git-ignored in projects, re-copied on upgrade.
5. `AGENTS.md` and `lefthook.yml` are Node-shaped; on a Python project the Commands section had to be rewritten by hand and lefthook is redundant next to pre-commit. Partly fixed: the pre-push check is now stack-aware; the Commands section still needs hand-editing (documented).
6. `quality-review` had no scope rule for a codebase with no diff. Fixed: one line in the skill.

## What the kit got right

The four reviewers found 8 verified MUST-level problems in a project that already had 275 passing tests, its own accessibility checker and a written accessibility statement — including two tests that silently overwrite the developer's real data and a contrast failure in the Preferences captions. Every finding carries a file and line.

## Links

- App repo: https://github.com/sairam5294/rhythm_buddy
- Kit outputs for this project: `docs/product/` in this folder
