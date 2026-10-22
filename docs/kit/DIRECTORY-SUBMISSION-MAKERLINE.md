# Directory submission pack: makerline (the full kit)

The second submission, after **makerline-idea** is listed. Everything about how the portal works, data handling, support, versioning and the checklist is in [`DIRECTORY-SUBMISSION.md`](DIRECTORY-SUBMISSION.md); this page covers only what's different for the full plugin.

_Prepared 2026-10-21. Re-check the portal before submitting: steps and fields change._

## When to submit

Submit **after makerline-idea is live**, not alongside it. Reasons:

- The full plugin writes code and has agents with every tool, so its review is likely slower and stricter. A live, smaller listing first proves the publisher and the docs.
- Feedback from the first review (wording, data answers, prompts) can be applied here before submitting.
- It's one submission per plugin folder: this one is **path `plugin/`, branch `main`**.

## Listing text

The portal reads `plugin/.claude-plugin/plugin.json` (name, description) and `plugin/README.md`. Both are already written; nothing to type.

**Name:** `makerline` · **Author:** Sairam Mogullapalli · **Licence:** MIT

**One line (≤ 80 characters):**
> Know if it's worth building. Then build it right, with accessibility enforced.

**Short (the `plugin.json` description):**
> MakerLine turns a product idea into an honest verdict, real competitors, wireframes and a draft PRD. Once you approve, it helps you build and ship the product, with WCAG 2.2 AA accessibility, security and tests enforced at every step.

## Five example prompts

1. `/makerline:start give me everything for this idea, quick: a booking app for small physio clinics` (the Idea Pack, as in makerline-idea)
2. `set it all up` (after approval: name and brand, stack, design system, full PRD, engineering docs, project setup)
3. `build the next task` (one tested task on its own branch: `build-feature`)
4. `review this pull request for accessibility and security` (`quality-review`: parallel reviewers, one report)
5. `are we ready to launch?` (`ship-checklist` with evidence per item)

Test material for reviewers: the ClubSlot pack (`examples/idea-pack-clubslot/`) for 1, and the RhythmBuddy case study (`docs/site/case-rhythmbuddy.md`) for 4.

## Permissions and what the plugin runs (differs from makerline-idea)

| Component | What it can do | Why |
|---|---|---|
| 26 skills | Instructions only. Read and write the connected folder; the build skills create branches and commit | Idea to launch, phase by phase |
| 8 review and research agents (accessibility-auditor, accessibility-strategist, code-reviewer, devils-advocate, idea-champion, market-researcher, security-reviewer, ux-reviewer) | Read, Grep, Glob, WebSearch, WebFetch; all but one also have Bash (to run tests and checkers) | Reviews and research don't edit files |
| 6 builder agents (architect, backend-developer, mobile-developer, product-strategist, qa-engineer, web-developer) | All tools, including Write, Edit and Bash | They write the docs and code for approved tasks |
| `skills/product-kickoff/scripts/check_idea_pack.py` | Reads the Idea Pack and prints pass, warn or fail; standard library only, no network | Checks documents before the user sees them |
| `.mcp.json` | Six optional remote MCP servers (GitHub, Figma, Vercel, Supabase, Notion, Linear), URLs only | Opt-in connectors |
| Hooks | **None in the plugin bundle** | The approval-gate and safety hooks are files in each project (`.claude/hooks/`), added by `scripts/new-project.sh` or `scripts/upgrade-project.sh` from the repo, so the user can read and change them |

## Safety notes for the reviewer

- **Approval gate.** The builder agents write code only after the owner records approval with `scripts/approve.sh`. No skill writes the `Evaluation: APPROVED` line, and in projects set up from the repo a hook, a git hook and CI block app code until it exists.
- **Branches, not main.** Build tasks work on `<type>/<Mon>-<DD>-<summary>` branches and open pull requests; the kit never asks to push to main or merge.
- **Destructive commands.** In projects, `.claude/hooks/guard-bash.sh` blocks recursive force deletes, force pushes, pushing straight to main, reading `.env` files, printing secrets and destructive database commands; `.claude/settings.json` adds deny rules for secret files. `build-feature` also checks the gate itself: it starts only when STATUS.md says `Evaluation: APPROVED` and the task is in PLAN.md.
- **No secrets, no tracking.** No keys in any file; the kit has no server and collects nothing.
- **Accessibility and security by default.** Every built screen must meet WCAG 2.2 AA; reviews map to OWASP Top 10:2025 and MASVS.

## Screenshots (in addition to makerline-idea's)

| # | What to capture | Alt text |
|---|---|---|
| 9 | `STATUS.md` with "Evaluation: APPROVED" and the phases after it | Project status table: the idea is approved and the setup phases are next |
| 10 | A `build-feature` pull request with the evidence block (tests, axe, screenshots) | Pull request showing passing tests, 0 accessibility issues and before/after screenshots |
| 11 | A `quality-review` report with its verdict and the must-fix table | Review report: "Ready after fixes", with must-fix findings by file and line |
| 12 | The local cockpit (`scripts/kit-ui.py`) listing projects by phase | Local dashboard listing projects, their phase and the next step |

## Checklist (differences only)

- [ ] makerline-idea is live and its review feedback is applied here
- [ ] Portal **Validate** on path `plugin/`: no Blocking findings; read every Policy hold and Warning
- [ ] On a fresh account: install `makerline`, run prompts 1–5 in an empty folder; prompt 3 refuses to write app code before approval
- [ ] Screenshots 9–12 captured with alt text
- [ ] `version` in `plugin/.claude-plugin/plugin.json` raised since the last release
