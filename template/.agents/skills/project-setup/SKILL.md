---
name: project-setup
description: Set up the repo, README and AI tool rules. Covers a proper README, SETUP (clone or download → install → env → run locally → deploy), STRUCTURE (folder tree, where every file goes, rules), a fully commented .env.example, GITHUB (PRs, merge strategy, branch cleanup, experiment branches, previews, deployment retention, storage monitoring), CONTEXT_PACK for tools that can't read the repo, and project-specific rules for every AI tool — .cursor/rules/*.mdc scoped by folder, .claude (CLAUDE.md, project skills), .github (copilot instructions, CODEOWNERS, workflows). Trigger with "set up the repo", "write the README", "cursor rules", "folder structure", "env file", "GitHub rules", or after engineering-docs.
argument-hint: "<one part, e.g. 'cursor rules' or 'README', or nothing for the full setup>"
---

# /project-setup

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Give the repo one shared source of truth that every AI tool reads, plus the files a newcomer needs to clone, run and deploy it.

**Why:** AGENTS.md and `docs/` hold the rules once; each tool's folder (`.claude/`, `.cursor/`, `.github/`) only points to them and adds what that tool needs. So Claude, Cursor, Codex, Copilot and ChatGPT follow the same rules without copies drifting apart.

## Usage

```
/project-setup                    # full setup, phase 7b
/project-setup cursor rules       # only .cursor/rules/
/project-setup env file           # only .env.example
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                     PROJECT SETUP                            │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ STRUCTURE, .env.example, SETUP, README, GITHUB from       │
│    templates/ — real stack, folders, commands, services      │
│  ✓ AI-tool folders: .cursor/rules, .claude, .github, and     │
│    CONTEXT_PACK for tools that can't read the repo           │
│  ✓ Fresh-clone check: install → run → test                   │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Source control: CODEOWNERS, workflows, branch rules live  │
│  + Hosting: preview/production env names and retention       │
│  + Database: real env var names and dashboard paths          │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- Gate: STATUS `Evaluation: APPROVED`; TECH_STACK, DESIGN_SYSTEM (or BRAND), PRD (full) and the engineering docs exist. Phase 7b.
- `TECH_STACK.md`, `docs/ARCHITECTURE.md`, `docs/DATABASE.md`, `docs/CODE_STYLE.md`, `docs/RULES.md`, `BRAND.md` / `DESIGN_SYSTEM.md`, `TOOL_PLAN.md` (if any), and the starter's own files if the project came from a kit starter.
- Templates in `templates/`.
- Use the real stack, folders, commands and services — never generic placeholders.

## Workflow

1. **Read** the inputs above.
2. **Folder structure** → `docs/STRUCTURE.md` (`templates/STRUCTURE.md`): tree with one-line purposes, a "where does X go?" table, naming rules, what must never be created. Before code exists it's a plan — don't create app folders; the starter (`scripts/new-project.sh <path> --web | --starter`) or the first build task does.
3. **Environment** → `.env.example` (`templates/env.example`): every variable, grouped by service, each commented — what, where to get it, public or secret (and why public is safe), environments, required, format. Never a real value; note where production values live.
4. **Setup guide** → `docs/SETUP.md` (`templates/SETUP.md`): prerequisites, get the code (clone, CLI or ZIP — and what ZIP loses), install, env, local DB, run, test, common errors, deploy, rollback — each with the exact command and what "it worked" looks like.
5. **README** → `README.md` (`templates/README.md`): what and for whom, screenshot slot, features, stack, quick start (≤ 5 commands), scripts, links to STRUCTURE, `docs/README.md` and the accessibility statement, contributing, licence.
6. **GitHub rules** → `docs/GITHUB.md` (`templates/GITHUB.md`) + `.github/` from `templates/github/`: `CODEOWNERS`, `copilot-instructions.md` (points to AGENTS.md), `repo-health.yml` (monthly read-only report). Free-tier limits only from the vendors' current pages, dated.
7. **AI tool folders** — one rulebook, thin pointers:
   - `AGENTS.md` stays the shared rulebook (Codex natively, Claude via root `CLAUDE.md` = `@AGENTS.md` + notes, Copilot via `.github/copilot-instructions.md`).
   - `.cursor/rules/`: `project.mdc` (always on: stack, aliases, hard rules, the rule index) + one scoped `.mdc` per area this project has, from `templates/cursor-rules/` (architecture, components, design, data-api, forms-validation, errors-logging, permissions, i18n, dates-time, accessibility, security, testing, ai-features): real globs, one example, an "Enforced by" table (lint / hook / CI / review; "planned" if the config isn't there yet), "never" lines. Link the kit's own rules; don't duplicate them.
   - `.claude/skills/` from `templates/claude-skill/SKILL.template.md` for the 1–3 jobs this project repeats most, with real paths and commands. No CLAUDE.md inside `.claude/`.
   - Other agents: keep the kit's pointers (`GEMINI.md`, `.aider.conf.yml`, `.continue/rules/00-agents-md.md`); tools that read AGENTS.md natively need none (`docs/kit/AGENT-ADAPTERS.md`).
   - `docs/CONTEXT_PACK.md` (`templates/CONTEXT_PACK.md`): ≤ 1 page for tools and people who can't read the repo; regenerate when RULES or BRAND change.
8. **Check:**
   - a fresh clone → follow SETUP.md literally in a clean folder (or the kit's `scripts/new-project.sh` output) and confirm `install → run → test` works
   - every `.mdc` glob matches at least one existing path (`ls` the globs)
   - every env var in code appears in `.env.example` (grep `process.env.` / `Deno.env` / `import.meta.env`)
   - no secret values anywhere
   - branch name and hooks work (`scripts/check-branch.sh`)
9. **Present** in ≤ 10 lines; update `docs/README.md` index, STATUS `7b Project setup: Done`, DECISIONS. Offer `plan-build`.

## Output

| File | Step | Size |
|---|---|---|
| `docs/STRUCTURE.md` | 2 | — |
| `.env.example` | 3 | — |
| `docs/SETUP.md`, `README.md` | 4, 5 | quick start ≤ 5 commands |
| `docs/GITHUB.md` + `.github/` | 6 | — |
| `.cursor/rules/*.mdc`, `.claude/skills/*`, `docs/CONTEXT_PACK.md` | 7 | CONTEXT_PACK ≤ 1 page |
| `GEMINI.md`, `.aider.conf.yml`, `.continue/rules/00-agents-md.md` (kept from the kit template) | 7 | each ≤ 10 lines |

Present in ≤ 10 lines: what was written, what the fresh-clone check found, unverified free-tier limits → CLARITY.

## If connectors available

If **~~source control** is connected:
- Confirm `CODEOWNERS`, the PR template and `repo-health.yml` are picked up, and check branch rules against `docs/GITHUB.md`.

If **~~hosting** is connected:
- Use the real preview/production environment names, deployment retention and where production env values live.

If **~~database** is connected:
- Take the real env var names and dashboard paths for `.env.example` from the project (names only — never values).

## Rules

- Real stack, folders, commands and services — never generic placeholders.
- Never a real secret value anywhere; `.env*` stays git-ignored except `.env.example`.
- One source, thin pointers: tool folders point to AGENTS.md and `docs/`, never copy them.
- Don't create app folders before code exists; the starter or the first build task creates them.
- Free-tier limits come only from the vendors' current pages, dated; otherwise "unverified" + a CLARITY question.
- No badges you can't keep green.

- Keeping it current: `build-feature` updates STRUCTURE and `.env.example`; `quality-review` checks the scoped rules; `standards-refresh` re-checks GITHUB limits.

## Tips

1. Run it once after `engineering-docs`, then rerun single parts (*"cursor rules"*, *"env file"*) as the project grows.
2. Try SETUP.md on a clean folder yourself — if a step needs guessing, the doc is wrong.
3. Hand `docs/CONTEXT_PACK.md` to any tool or person who can't read the repo.

## Related

- Before: `engineering-docs` · After: `plan-build`, `build-feature`
- Reads: `templates/STRUCTURE.md`, `env.example`, `SETUP.md`, `README.md`, `GITHUB.md`, `CONTEXT_PACK.md`, `github/`, `cursor-rules/`, `claude-skill/SKILL.template.md`; `docs/kit/AGENT-ADAPTERS.md`; `scripts/new-project.sh`, `scripts/check-branch.sh`
