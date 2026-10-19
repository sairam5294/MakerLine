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
2. **Folder structure** → `docs/STRUCTURE.md` from `templates/STRUCTURE.md`: the tree to two or three levels with a one-line purpose per folder, a "where does X go?" table (component, screen/route, API call, hook, store, type, constant, string, test, migration, asset, doc), naming rules, and what must never be created (e.g. a second `utils/`, files over ~300 lines without a reason).
   - Before any code exists, STRUCTURE.md is the plan: don't create app folders now — the starter (`scripts/new-project.sh <path> --web | --starter`, which keeps existing files) or the first build task creates them. Only `design/brand/` and `docs/` exist at this point.
3. **Environment** → `.env.example` from `templates/env.example`: every variable the stack uses, grouped by service, each with inline comments — what it is, where to get it (dashboard path), public or secret (and why a public one is safe), which environments need it, required or optional, example format. Never a real value. `.env*` stays git-ignored except `.env.example`. Note where production values live (Vercel/Supabase/EAS dashboards, GitHub Actions secrets).
4. **Setup guide** → `docs/SETUP.md` from `templates/SETUP.md`: prerequisites with version-check commands; get the code (git clone, GitHub CLI, or Download ZIP — and what ZIP loses: no git history, no hooks until `git init`); install; env; local database; run; test; common errors and fixes; deploy (preview and production for this stack); rollback. Each step has the exact command and what "it worked" looks like.
5. **README** → `README.md` from `templates/README.md`: what it is and who it's for, screenshot slot, features, tech stack, quick start (5 commands max, linking SETUP for detail), scripts table, folder summary (link STRUCTURE), docs index (link `docs/README.md`), accessibility statement link, contributing (branch convention), licence. Plain language, no badges you can't keep green.
6. **GitHub rules** → `docs/GITHUB.md` from `templates/GITHUB.md`, plus `.github/` files from `templates/github/`: PR template (already in the kit template), `CODEOWNERS`, `copilot-instructions.md` (points to AGENTS.md), workflow `repo-health.yml` (monthly, read-only report: repo size, Actions storage, stale branches, open PR age). Fill free-tier limits only from the vendors' current pages, with the date checked; a number not on the page is "unverified" with a CLARITY question.
7. **AI tool folders** (one source, thin pointers):
   - `AGENTS.md` stays the shared rulebook (Codex reads it natively; Claude via CLAUDE.md; Copilot via `.github/copilot-instructions.md`).
   - `.cursor/rules/`: write `project.mdc` (always applied: stack in one line, import aliases, hard rules with their enforcement, and the **rule index** table of every scoped rule and the globs it attaches to) and one scoped `.mdc` per area that exists in this project, from `templates/cursor-rules/`: architecture, components, design, data-api, forms-validation, errors-logging, permissions, i18n, dates-time, accessibility, security, testing, ai-features. Each: frontmatter `description` + `globs` for the real folders, the project's actual patterns with one short example, an "Enforced by" table (lint / hook / CI / review only — a rule whose lint config doesn't exist yet says "planned — first build task"), and "never" lines. Skip areas the project doesn't have. Don't duplicate the kit's own rules (`product-workflow`, `security-backend`, `testing`, `ui-accessibility-ux`) — link them.
   - Claude: the root `CLAUDE.md` stays `@AGENTS.md` + Claude notes (Claude Code reads it from the repo root; don't put a CLAUDE.md inside `.claude/`). `.claude/` holds `settings.json`, `hooks/` and project skills — add project skills in `.claude/skills/` from `templates/claude-skill/SKILL.template.md` for the 1–3 jobs this project repeats most (e.g. "add a screen", "add a table + RLS + migration", "add a translated string") — each a short step list using this project's real paths and commands.
   - Other agents: keep the kit's thin pointers (`GEMINI.md`, `.aider.conf.yml`, `.continue/rules/00-agents-md.md`) and add none for tools that read AGENTS.md natively — table and gotchas (Zed reads only the first rules file it finds) in `docs/kit/AGENT-ADAPTERS.md`. Never copy rules into them.
   - `docs/CONTEXT_PACK.md` from `templates/CONTEXT_PACK.md`: ≤ 1 page for tools that can't read the repo (ChatGPT in the browser, a contractor): the product in 5 lines, stack, rules that matter, terminology, where answers must go back. Regenerate when RULES or BRAND change.
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

### Keeping it current

- `build-feature` updates STRUCTURE and `.env.example` when it adds a folder or variable.
- `quality-review` checks code against the scoped rules.
- `standards-refresh` re-checks `GITHUB.md` limits.

## Tips

1. Run it once after `engineering-docs`, then rerun single parts (*"cursor rules"*, *"env file"*) as the project grows.
2. Try SETUP.md on a clean folder yourself — if a step needs guessing, the doc is wrong.
3. Hand `docs/CONTEXT_PACK.md` to any tool or person who can't read the repo.

## Related

- Before: `engineering-docs` · After: `plan-build`, `build-feature`
- Reads: `templates/STRUCTURE.md`, `env.example`, `SETUP.md`, `README.md`, `GITHUB.md`, `CONTEXT_PACK.md`, `github/`, `cursor-rules/`, `claude-skill/SKILL.template.md`; `docs/kit/AGENT-ADAPTERS.md`; `scripts/new-project.sh`, `scripts/check-branch.sh`
