# Case study: RhythmBuddy

How the kit handled a project it did not create: a shipped macOS app with its own tests, CI and conventions, adopted into the kit and then reviewed.

## The project

RhythmBuddy is a macOS menu-bar app that keeps a low-interrupt daily wellness rhythm: water, eye breaks, stretching, meals, morning sunlight, a post-lunch walk and a bedtime wind-down. A pixel mascot walks in with a speech bubble, and reminders that fall close together merge into one "health break".

| Fact | Detail |
|---|---|
| Stack | Python and PyObjC, about 100 modules |
| Tests before the kit | 275 unit tests, plus the project's own accessibility checker |
| Distribution | Ad-hoc signed `.app` and DMG |
| Kit phases run | Adopt (`upgrade-project`), then `quality-review` |
| Dates | 14 October 2026 |
| Source | [github.com/sairam5294/rhythm_buddy](https://github.com/sairam5294/rhythm_buddy) |

## Why it was a useful test

Most of the kit is written for new projects. RhythmBuddy tested the other half: adding the kit to an existing codebase with its own CI, Cursor rules and conventions, and reviewing code the kit did not write. It is also Python, while the kit's starters are JavaScript, so it showed every place the standards quietly assumed Node.

## What happened

| Step | Result |
|---|---|
| `upgrade-project` preview | Would have overwritten the project's own CI and Cursor rules. This led to the kit's *adopt mode*. |
| `upgrade-project --apply` in adopt mode | 109 kit files added, 0 code files touched; the project's own CI, rules and pre-commit hooks kept |
| `quality-review` with accessibility, security, code and QA reviewers | **Ready after fixes**: 8 MUST, 15 SHOULD, 6 suggestions |
| `test-plan`, `ship-checklist` | Next, after the MUST fixes |

## What the review found

The project already had 275 passing tests, its own accessibility checker and a written accessibility statement. The reviewers still found 8 verified must-fix problems, each with a file and line. Speculative findings were dropped before the report was written. Some examples:

- **Contrast.** Section captions in Preferences measured 3.9:1, below WCAG's 4.5:1 for text.
- **Screen readers.** Edit and delete buttons were glyph-only, with a tooltip but no accessible name. A decorative mascot was announced to VoiceOver.
- **Keyboard focus.** The custom Done, Snooze and Skip buttons had no visible focus indicator.
- **Tests that could not fail.** One test overwrote the developer's real settings and stats files and returned instead of asserting. Another called the live GitHub API and swallowed every error.
- **Supply chain.** Dependencies were unpinned, and CI actions were pinned to movable tags.

The review also recorded what was good: Cocoa-free, well-tested scheduling logic; a contrast table that matched recomputed ratios exactly; Reduce Motion support; atomic file writes; and a single, TLS-verified network call, exactly as the privacy document described.

[Read the full review on GitHub](../../examples/rhythmbuddy/docs/product/reviews/2026-10-14-adoption-review.md)

## What the kit got wrong, and fixed

1. `upgrade-project` assumed every project was created by the kit. On an existing Python app it would have replaced the project's CI and merged kit rules over hand-written ones. **Fixed:** adopt mode never overwrites existing files.
2. The kickoff skill would have treated a shipped v1.0 as "phase 1: discovery". **Fixed:** adopt mode marks the earlier phases as done before the kit.
3. The project's `.gitignore` silently hid three kit-added files, including the safety permissions file. **Fixed:** the script now warns about git-ignored additions.
4. Projects committed the owner's private profile (hours, budget, accounts). **Fixed:** it is git-ignored in every project.
5. Parts of the kit's rules file and git hooks were Node-shaped. **Partly fixed:** the pre-push check is now stack-aware; the Commands section of a Python project still needs editing by hand.
6. `quality-review` had no rule for scoping a review when there is no diff. **Fixed:** one line in the skill.

These fixes shipped in kit version 0.6.0 and are logged in [What the kit got wrong](../../LESSONS.md).

## Takeaway

The kit can be added to a project in any stack without breaking it, and its reviewers find real, line-level problems even in a well-tested app. When the kit's assumptions didn't fit, the run turned them into fixes rather than workarounds.

[Back to case studies](case-studies.md) · [The example files on GitHub](../../examples/rhythmbuddy/README.md)
