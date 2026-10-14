# Product Kit v0.6

**The open-source designer's AI toolkit.** One setup that takes an idea from "I have a new idea" to a shipped web / iOS / Android product, and works the same way in **Claude**, **Cursor** and **Codex**. Built by a designer with light coding skills, for designers and solo makers who build with AI. The rules are enforced by checks, not just written down.

> **New here? Read [GETTING-STARTED.md](GETTING-STARTED.md)** — how to run it and how to update it, step by step.

**Why it exists.** AI tools write working code fast, but they forget accessibility, UX heuristics, security, tests and honest evaluation unless you remind them every session, in every tool. Product Kit packages that know-how as skills, agents, standards, hooks and CI so every tool you use starts thinking like a senior product designer.

**What you get**
- A 13-phase workflow from discovery interview to post-launch retro, with an approval gate AI tools cannot bypass
- 20 skills and 12 specialist agents (strategist, UX reviewer, accessibility auditor, security reviewer, QA, devil's advocate…)
- Standards for accessibility (WCAG 2.2 AA), UX, security, testing, backend and AI features — split into small files so only the relevant ones load
- Two tested starters: Expo + Supabase (iOS / Android / web) and Next.js (landing page + waitlist), both with axe, Lighthouse and contrast tests
- Safety hooks, git hooks and GitHub Actions that block dangerous commands, leaked secrets and code before approval
- One design-token source for Figma and code, plus evals that check the skills still catch planted flaws

Licensed under [MIT](LICENSE). Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## What's inside

```
product-kit/
├── plugin/        THE SOURCE — edit only here (20 skills, 12 agents, standards). Installs into Claude.
├── template/      Copied into every project: AGENTS.md, safety settings, CI, git hooks, MCP, Cursor/Codex adapters
├── starter/       Tested Expo (iOS/Android/Web) + Supabase app: i18n (en/te/hi), Sentry, PostHog
├── starter-web/   Tested Next.js site: landing page + waitlist (nonce CSP, rate limit, optional Turnstile), AI harness with evals; Lighthouse 1.0/1.0/1.0
├── design/        tokens.json (single source for Figma + code) + build-tokens.mjs · Figma library: https://www.figma.com/community/file/1692097443572763844/product-kit-design-system
├── owner/         OWNER.example.md → copy to OWNER.md (git-ignored): your profile, copied into every project
├── portfolio/     OUTCOMES.md (idea outcomes) + generated dashboard (index.html)
├── evals/         Sample cases with planted flaws + RUNBOOK (runs monthly on your Mac)
├── scripts/       new-project · upgrade-project · release-kit · build-plugin · portfolio · setup-github · sync · install-global
├── .github/       Kit CI: keeps template in sync, tests both starters
├── CHANGELOG.md   What changed per version
└── LESSONS.md     What the kit got wrong, fed back after each project
```

## Workflow

| # | Skill | Output (`docs/product/`) |
|---|---|---|
| 0 | **product-kickoff**: say "I have a new idea" | runs everything below, tracks `STATUS.md` |
| 1 | new-idea: discovery interview | PROJECT_BRIEF.md |
| 2 | evaluate-idea: researched, honest report; refine until you say "approved" | EVALUATION.md |
| 3 | validate-idea: kill criteria, interviews, landing page, prototype test | VALIDATION.md |
| ★ | **Approval gate**: no app code before `Evaluation: APPROVED` (enforced) | STATUS.md |
| 4–8 | name-product · tech-stack · design-system · write-prd · plan-build | NAMING · TECH_STACK · DESIGN_SYSTEM · PRD · PLAN |
| 9 | build-feature (+ design-qa against Figma) | code + tests |
| 10–12 | quality-review · test-plan · ship-checklist (incl. expert review) | reviews/ · TEST_PLAN · RELEASE |
| 13 | post-launch: weekly metrics, feedback, retros → LESSONS | METRICS · LESSONS |
| any | handoff (end of every session) · portfolio (all projects) · ai-feature (any AI feature) · standards-refresh (quarterly) | HANDOFF.md · AI_FEATURE_*.md |

## What enforces the rules

| Layer | Catches | Works for |
|---|---|---|
| Claude Code hooks + permissions | code before approval, AI self-approval, `rm -rf`, force-push, push to main, reading `.env` secrets, destructive DB commands; auto-formats edits | Claude Code |
| `permissions.json` + `.cursorignore` | secrets and risky commands | Cursor |
| `.codex/config.toml` | sandboxed writes, no network without asking | Codex |
| lefthook git hooks | approval gate, leaked secrets, lint, format; no direct push to main; full check before push | every tool |
| AI review on every PR (`ai-review.yml`) | kit quality-review posted as a PR comment (needs one Claude secret) | every tool |
| GitHub Actions CI (actions pinned to SHAs) | gate, secret scan, typecheck, lint, tests, dependency audit, axe on Chrome + Safari engines, Lighthouse, RLS database tests | every tool |
| Starter tests | colour contrast (light + dark), token drift, accessible components, translations, sign-in validation, session storage, privacy scrubbing | every tool |
| Kit tests (`tests/hooks.test.sh`, actionlint) | the safety hooks block/allow exactly what they promise; workflow files are valid | the kit itself |

## Setup (once)

```bash
git clone https://github.com/sairam5294/product-kit ~/Documents/product-kit
cd ~/Documents/product-kit
brew install gh gitleaks                                   # GitHub CLI + secret scanning; Node 22+ required
claude plugin marketplace add sairam5294/product-kit       # Claude Code
claude plugin install product-kit@product-kit-marketplace
./scripts/build-plugin.sh                                  # Claude app instead: open ../product-kit.plugin → Install
cp owner/OWNER.example.md owner/OWNER.md                   # your profile (git-ignored); fill in hours, budget, accounts
```
Full walkthrough, including Cursor and Codex: [GETTING-STARTED.md](GETTING-STARTED.md).

Where the rules are enforced: Claude Code, Cursor and Codex get hooks, git hooks and CI. **Claude Cowork/desktop has no hooks**, so there the skills follow the gate rules themselves. Use Cowork for phases 1–8 (docs) and Claude Code, Cursor or Codex for building.
Scheduled in Claude: a quarterly standards check (1 Jan, 1 Apr, 1 Jul, 1 Oct) and monthly evals on your Mac (3rd of each month).

## Start a project

```bash
./scripts/new-project.sh ~/Projects/my-app             # any stack: rules, skills, agents, safety, CI
./scripts/new-project.sh ~/Projects/my-app --starter   # + tested Expo + Supabase app (iOS/Android/web)
./scripts/new-project.sh ~/Projects/my-site --web      # + tested Next.js site (landing page, SEO, waitlist)
cd ~/Projects/my-app && scripts/setup-github.sh        # private GitHub repo + push + protect main (needs: brew install gh)
npx lefthook install                                   # git hooks (after setup-github)
```

Then say **"I have a new idea"** in Claude, Cursor or Codex. After the evaluation, **you** approve with `scripts/approve.sh`. AI tools can't approve for you.

Keep projects current when the kit improves: `./scripts/upgrade-project.sh ~/Projects/my-app` (preview) → add `--apply`. The same command adopts a project built before the kit, in any stack, without overwriting anything it already has.
See everything at once: `python3 scripts/portfolio.py` → open `portfolio/index.html`.

GitHub Free can't protect `main` on private repos. setup-github.sh tells you if so, and the `no-push-to-main` git hook covers it locally. The kit repo itself uses the same idea: run `git config core.hooksPath .githooks` once per clone, and pushes to `main` are refused — work on `update/<date>-<topic>` branches and merge through pull requests.

## Using the three tools together

- **Claude**: discovery, evaluation, planning, multi-file features, parallel reviews.
- **Cursor**: visual UI iteration with live preview.
- **Codex**: well-defined independent tasks in parallel (tests, endpoints).
- Give each tool its own task folder: `scripts/worktree.sh new T-07 lesson-player`, which creates `../my-app-T-07`.
- End every session with **handoff**, so the next tool picks up exactly where you stopped.

## Token-saving design

- Always-loaded text (skill + agent descriptions + AGENTS.md) stays around 2,300 tokens for 20 skills and 12 agents. v0.1 used ~3,000 for 13 skills.
- Checklist agents run on a faster model; research is cached in `docs/product/research/`; drafts can use a free local model (`scripts/local-ai.sh`).
- Skills load their detail only when used. Standards are split into 10 files, and only the relevant ones are read.
- Subagents return summaries of 300 words or less. Reviewers get the diff plus one standard file.
- Formatting is done by hooks, not by the AI.
- `.cursorignore` and deny rules keep secrets and generated folders out of context.
- Full rules: `plugin/skills/product-standards/references/context-budget.md`.

## Changing the kit
Edit files in `plugin/`, then `./scripts/release-kit.sh <new-version> "what changed"` (sync + tests + version + CHANGELOG + rebuild plugin + commit). Reinstall the plugin in Claude, then `./scripts/upgrade-project.sh <project>` for projects you want updated. Details: GETTING-STARTED.md → Part 3.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for ground rules, [SECURITY.md](SECURITY.md) to report a vulnerability, and [LESSONS.md](LESSONS.md) for what the kit has got wrong so far. Issue templates cover bugs, rule proposals and new skills or adapters.

## Other plugins
You also have design / engineering / product-management plugins. The kit's versions win for kit phases (see `template/docs/kit/PLUGIN-OVERLAP.md`); complementary skills like ux-copy and research-synthesis are used inside phases.
