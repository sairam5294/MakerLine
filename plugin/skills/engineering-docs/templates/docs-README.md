# Docs — {{product}}

_Updated {{date}} · Read `../AGENTS.md` first, then `RULES.md` and `MEMORY.md`, then only the doc the task needs._

| Doc | What it answers | Lives in | Keep current via |
|---|---|---|---|
| **PRD** | What we're building and why, story by story | `product/PRD.md` | write-prd |
| **DESIGN** | Tokens, components, states, accessibility of the UI | `product/DESIGN_SYSTEM.md` · `../design/tokens.json` | design-system, design-qa |
| **ARCHITECTURE** | How the parts fit, the core request path, cross-cutting rules | `ARCHITECTURE.md` | engineering-docs, build-feature |
| **DATABASE** | Entities, tables, RLS policies, personal data, migrations | `DATABASE.md` | every migration |
| **SECURITY** | Threat model, OWASP controls, secrets, auth, privacy, incidents | `SECURITY.md` | quality-review, ship-checklist |
| **CODE_STYLE** | Versions, folders, naming, patterns, comments, review checklist | `CODE_STYLE.md` | build-feature |
| **TESTING** | Test mix, what every story needs, commands, CI, manual and AT testing | `TESTING.md` | test-plan |
| **RULES** | Standing rules: tokens, security, AI, accessibility, branches, never-do | `RULES.md` | standards-refresh |
| **TASKS** | Milestones and tasks, who/what builds each, status | `product/PLAN.md` · `product/STATUS.md` | plan-build, build-feature |
| **LIFECYCLE** | Stages, exit criteria, growth plan, upgrade triggers | `LIFECYCLE.md` | post-launch |
| **SETUP** | Clone or download → install → env → run → deploy | `SETUP.md` · `../.env.example` | project-setup |
| **STRUCTURE** | Folder tree, where every file goes, naming | `STRUCTURE.md` | project-setup, build-feature |
| **GITHUB** | PRs, merge strategy, branches, previews, retention, storage | `GITHUB.md` | project-setup |
| **BRAND** | Name, logo and guidelines, colours, fonts, icons, rules | `product/BRAND.md` · `../design/brand/` | name-product |
| **TOOLS** | Which AI tool does which job, handoffs, limits | `product/TOOL_PLAN.md` · `CONTEXT_PACK.md` | tool-plan |
| **MEMORY** | Long-lived facts: environment, conventions, what broke before, do-not-touch | `MEMORY.md` | handoff |
| **AGENTS** | Rules for every AI tool in this repo | `../AGENTS.md` (root `../CLAUDE.md` imports it; Cursor `../.cursor/rules/project.mdc`, Copilot `../.github/copilot-instructions.md`) | kit upgrades |

Also here: `product/` (brief, clarity log, evaluation, competitors, design direction, validation, naming, tech stack ADR, test plan, release, reviews, handoff, decisions, costs) · `kit/` (starter rules) · `../design/wireframes/` (clickable low-fi screens).
