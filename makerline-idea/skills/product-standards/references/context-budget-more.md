# Context & Token Budget — after approval

The second half of `context-budget.md`; read only from `tool-plan` onwards.

## 1. Which doc to load for which task (after engineering-docs)
| Task touches | Load | Don't load |
|---|---|---|
| any task | AGENTS.md · docs/RULES.md · docs/MEMORY.md · HANDOFF/STATUS · the PLAN task · its PRD stories | the whole PRD, DESIGN_SYSTEM, EVALUATION |
| a table, migration, policy | docs/DATABASE.md (that table's block) | ARCHITECTURE |
| a new flow, service, integration | docs/ARCHITECTURE.md §4–5 | DATABASE |
| first task in a repo, or a style question | docs/CODE_STYLE.md | — |
| tests | docs/TESTING.md | — |
| a review | the diff + docs/SECURITY.md or CODE_STYLE.md + one standard | the repo |

## 2. Research budget after approval (per phase)
| Phase | Searches | Page reads | How to stay inside it |
|---|---|---|---|
| tool-plan | ≤ 3 | ≤ 3 | one official pricing/limits page per tool the owner has; anything else "unverified" |
| name-product | ≤ 8 | ≤ 4 | one search per name for the top 6; deep checks (store, domain, trademark) only for the top 3 |
| tech-stack | ≤ 4 | ≤ 4 | versions from the package registry (`npm view <pkg> version`, `pip index versions`) — registry lookups don't count as page reads |
| project-setup | ≤ 2 | ≤ 2 | free-tier limits from the vendors' limits pages; a number not on the page → "unverified" |
| design-system, write-prd (full), engineering-docs | 0 | 0 | work from the Idea Pack, research cache and standards |
Unverified facts become CLARITY questions; never quote a limit or price from memory.

## 3. Cost reference (measured on kit evals, Sept 2026)
| Activity | Typical tokens | How to keep it down |
|---|---|---|
| Discovery interview (new-idea) | ~80k | Pre-fill from the pitch; short first reply |
| Full evaluation with web research | ~110–120k | Reuse `docs/product/research/`; refinement rounds re-research only what changed |
| Quality review of one feature branch | ~100k | Review the diff, not the repo; one standard file per reviewer |
| Build one S/M task | 30–150k | One task per session; `handoff` then start fresh |

## 4. Model routing (agents and tools)
- Agents declare their model: checklist/research agents (`market-researcher`, `qa-engineer`, `accessibility-auditor`, `ux-reviewer`) use a faster model (`sonnet` in Claude, medium reasoning in Codex); judgement-heavy ones (`devils-advocate`, `architect`, `security-reviewer`, builders) inherit the strongest.
- Cursor copies always `inherit` (Cursor uses its own model names) — pick the model in Cursor's chat.
- Mechanical edits (renames, formatting, copy tweaks) → fastest model; evaluations, architecture, security → strongest.

## 5. Local models (Ollama on your Mac) — free and private, but weaker
Good for: summarising your own interview notes, first-draft translations for a native speaker to fix, renaming/boilerplate, reading long logs. Not for: evaluation, architecture, security review, anything customer-facing without review.
- Quick use: `ollama run <model> "Summarise these notes into themes:" < notes.md` (pick a model that fits your RAM; check `ollama list`).
- Codex with a local model: `codex --oss` (or `ollama launch codex`); use a model with a ≥ 64k context window. Keep a separate Codex profile in `~/.codex/` so your normal setup is unchanged.
- Claude and Cursor use cloud models; keep them for judgement-heavy work.
- Never paste secrets or users' personal data into any model, local or cloud, without a reason and consent.
