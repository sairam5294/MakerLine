# Monthly kit retro

A 30-minute review the owner runs once a month to decide what the kit changes next. It turns scattered signals (issues, lessons, eval results, token costs) into **three changes**, one LESSONS row and a CHANGELOG plan. It is the kit's own version of the `post-launch` retro.

**When:** first week of each month, after the monthly evals have run (they run on the 3rd; see `evals/RUNBOOK.md`). Skip a month if nothing came in, and write "no retro: no new input" in the log at the bottom.
**Who:** the owner. Claude can prepare the inputs (step 1) so the 30 minutes are spent deciding, not gathering.
**Output:** a filled copy of the template below, saved as `docs/kit/retros/YYYY-MM.md`, plus the LESSONS row and CHANGELOG plan it produces.

## The 30 minutes

| Minutes | Step | What you do |
|---|---|---|
| 0–5 | **Gather** | Fill the Inputs table. Ask Claude: *"Prepare this month's kit retro inputs: open issues since the last retro, new LESSONS.md rows, the latest evals/results.md run and token figures from the last runs. ≤ 300 words."* |
| 5–15 | **Look for patterns** | Group what came in. A theme that appears in two or more inputs (for example an issue and an eval miss about the same skill) beats a one-off. Accessibility barriers and standards drift go first: they are correctness problems, not polish. |
| 15–25 | **Pick three changes** | Exactly three. For each: the problem, the file to change, how you'll know it worked (a test, an eval, a token number). Everything else goes to "Not this month" with one line why. |
| 25–30 | **Record** | Add one LESSONS.md row, write the CHANGELOG plan (next version and one line), label the chosen issues, set a date for the release. |

### Rules
- **Three changes, no more.** A small, finished change beats a big, half-done one. If a change is large, the first step of it counts as the change.
- **Every change names a file and a check.** "Improve evaluation" is not a change; "`evaluate-idea/references/scoring-rubric.md`: add the unknown-fact cap, checked by re-running `community-amenities`" is.
- **Evals don't get weaker.** If a change makes an eval fail, fix the change, not the eval (same rule as tests in AGENTS.md).
- **Watch the always-loaded cost.** If a change adds words to skill or agent descriptions, write the number down. Token savings are a valid change on their own.
- **Close the loop with reporters.** Reply on every issue you picked or parked, with the planned version or the reason.

## Inputs

| Input | Where | What to pull out |
|---|---|---|
| GitHub issues | [Issues](https://github.com/sairam5294/makerline/issues), filter by `created:>YYYY-MM-DD` (last retro date) | Count by label (bug, accessibility, standards, enhancement, rule); the two or three with the most reactions or comments; any accessibility barrier (always reviewed) |
| Lessons | `LESSONS.md` | Rows added since the last retro; any lesson whose "Kit change" is still empty |
| Eval results | `evals/results.md` and `evals/runs/` | Pass or fail per case, misses and severity misses, compared with the previous run |
| Token usage of the last runs | Eval run notes, `KIT_FRICTION.md` files in `examples/`, the Claude usage page, `docs/product/COSTS.md` in projects | Tokens per Idea Pack run by depth (Quick target ~50–70k), tool calls per run, the most expensive file or step |
| Standards | Last `standards-refresh` report (quarterly) and any "Standards drift" issues | Rules now outdated, with source links |
| Directory listing (once published) | Developer portal at claude.ai/directory/manage → the plugin's **Usage** tab | Installs, versions in use, which skills run most, error rates |

## Template

Copy from here into `docs/kit/retros/YYYY-MM.md`.

```markdown
# Kit retro — YYYY-MM

_Date: YYYY-MM-DD · Kit version: 0.x.y · Last retro: YYYY-MM-DD · Time spent: __ min_

## Inputs
| Input | This month | Notes |
|---|---|---|
| Issues opened / closed | __ / __ | bug __ · accessibility __ · standards __ · enhancement __ · rule __ |
| Top issues (link) | #__, #__, #__ | |
| New LESSONS rows | __ | lessons with no kit change yet: __ |
| Evals (latest run, date) | __ pass / __ fail | misses: __ · vs last run: better / same / worse |
| Tokens, last Idea Pack runs | Quick __k · Standard __k · Deep __k | tool calls __ · most expensive step: __ |
| Standards drift | __ | |
| Directory usage (if listed) | installs __ · errors __% | most-used skill: __ |

## Patterns (themes seen in 2+ inputs)
1.
2.
3.

## The three changes
| # | Problem (evidence) | Change (file) | How we'll know it worked | Issue |
|---|---|---|---|---|
| 1 | | | | #__ |
| 2 | | | | #__ |
| 3 | | | | #__ |

## Not this month
| Item | Why it waits | Revisit |
|---|---|---|
| | | |

## LESSONS.md row
| Date | Project | What went wrong / was missing | Kit change (file) | Version |
|---|---|---|---|---|
| YYYY-MM-DD | kit retro YYYY-MM | | | 0.x.y |

## CHANGELOG plan
- Next version: 0.x.y (patch: fixes only · minor: new or changed behaviour)
- One line for CHANGELOG.md:
- Release with: `./scripts/release-kit.sh <version> "<one line>"`
- Target date:

## Follow-ups
- [ ] Reply on every picked or parked issue
- [ ] Re-run the eval case that proves change __
- [ ] Bump `version` in both plugins' `plugin.json` (the directory needs it raised every release)
```

## Retro log

| Month | Three changes | Version | Done? |
|---|---|---|---|
| | | | |
