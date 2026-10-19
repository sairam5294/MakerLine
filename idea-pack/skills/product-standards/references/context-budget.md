# Context & Token Budget

Tokens = cost + quality. A bloated context makes AI tools slower, pricier and sloppier at following rules.

## MUST
- Read only what the task needs: AGENTS.md → HANDOFF.md/STATUS.md → the one task/story → the 1–2 standards files it touches.
- Search before reading: `grep`/`rg` for symbols; read file ranges, not whole large files. Never read `node_modules`, lockfiles, build output, `.expo`, `ios/`/`android/` generated folders, or large media.
- Delegate research and reviews to subagents; they return summaries (≤ 300 words) instead of raw pages/diffs.
- Pass reviewers the diff + one standard file, not the whole repo.
- Don't paste whole files back to the user; show the changed part or a summary.
- Keep living docs short: HANDOFF ≤ 40 lines, STATUS ≤ 60 lines, AGENTS.md ≤ ~120 lines. Move detail into linked files.
- One task per session/branch. When a session gets long or switches topic: run `handoff`, then start fresh (`/clear` in Claude Code, new chat in Cursor/Codex) — cheaper than compacting a long history.

## SHOULD
- Use the smaller/faster model for mechanical work (renames, formatting, simple tests) and the strongest model for planning, evaluation, security review.
- Use ignore files so tools skip generated/heavy files (`.cursorignore`, `.claudeignore`-style deny rules, `.gitignore`).
- Prefer structured outputs (tables, checklists) over prose in docs the AI rereads.
- Cache research: save sources and findings in docs/product so they aren't re-fetched.

## Idea Pack depth (pick before starting; default Standard)
| Mode | Use when | Produces | Research budget | Typical tokens |
|---|---|---|---|---|
| **Quick** | "Is this worth a weekend?" — early or many ideas | v0 brief, CLARITY, short EVALUATION (600–1,500 prose words; sections marked *Quick: optional* in the template may be left out), COMPETITORS lite (`competitive-analysis.md` → Lite), ONE_PAGER. No design direction or PRD | ≤ 8 searches, ≤ 4 page reads (or 6 reads with 4 searches when results carry no snippets) | ~70–100k measured (first run 190k before these fixes) |
| **Standard** | Deciding whether to build | Full pack: + DESIGN_DIRECTION, wireframes (≤ 8 screens), PRD draft | ≤ 15 searches, ≤ 8 page reads (two unused searches buy one extra read when results carry no snippets) | ~120–150k (measured ~214–219k before template trims) |
| **Deep** | Before spending money, pitching or hiring | Standard + all four competitor rings in depth, 12+ screens, Figma, payer research | ≤ 30 searches | ~250k+ |

Baseline before these rules: a blind Standard run (v0.7.0) used ~224k tokens and 72 tool calls.

### Research budget after approval (per phase)
| Phase | Searches | Page reads | How to stay inside it |
|---|---|---|---|
| tool-plan | ≤ 3 | ≤ 3 | one official pricing/limits page per tool the owner has; anything else "unverified" |
| name-product | ≤ 8 | ≤ 4 | one search per name for the top 6; deep checks (store, domain, trademark) only for the top 3 |
| tech-stack | ≤ 4 | ≤ 4 | versions from the package registry (`npm view <pkg> version`, `pip index versions`) — registry lookups don't count as page reads |
| project-setup | ≤ 2 | ≤ 2 | free-tier limits from the vendors' limits pages; a number not on the page → "unverified" |
| design-system, write-prd (full), engineering-docs | 0 | 0 | work from the Idea Pack, research cache and standards |
Unverified facts become CLARITY questions; never quote a limit or price from memory.

### Token rules for the Idea Pack (MUST)
1. **Research once, cite everywhere.** Facts go to `docs/product/research/<topic>.md` with IDs (R1, R2…); other documents cite the ID instead of repeating the fact.
2. **One home per fact.** Competitor detail lives in COMPETITORS; EVALUATION §6 summarises it in ≤ 150 words of prose (tables excluded; §7 differentiation is separate). The PRD links personas, flows and screens by ID instead of copying them. ONE_PAGER ≤ 500 words.
3. **Search before you read.** A search snippet with the figure and date is enough to cite. Open a page only for numbers or quotes you need; prefer round-up and comparison pages that cover several competitors in one read. If search returns bare links (no snippets), trade two unused searches for one extra page read. Stop a competitor ring when two sources agree. A fact the budget can't reach becomes a CLARITY question, not a guess.
4. **Copy templates, don't read them.** `cp` the template into place, read only its HOW TO FILL notes and one example block, then fill it section by section with targeted edits. Exception: the wireframe template is read once in full (its CSS kit and script contract are needed to fill it) — never twice.
5. **Write once, check with a script.** Write each document in one pass from your notes. Don't re-read your own output — run `check_idea_pack.py` (idea-pack/scripts) and fix only what it flags.
6. **Small subagent briefs.** Give each perspective agent the brief plus the one reference it needs and the research file; replies ≤ 300 words. Agents read the research cache before searching, and their own search caps count **inside** the mode's budget. No subagents available → play the perspectives inline: ≤ 5 lines each in Quick, ≤ 10 in Standard, full in Deep.

## Which doc to load for which task (after engineering-docs)
| Task touches | Load | Don't load |
|---|---|---|
| any task | AGENTS.md · docs/RULES.md · docs/MEMORY.md · HANDOFF/STATUS · the PLAN task · its PRD stories | the whole PRD, DESIGN_SYSTEM, EVALUATION |
| a table, migration, policy | docs/DATABASE.md (that table's block) | ARCHITECTURE |
| a new flow, service, integration | docs/ARCHITECTURE.md §4–5 | DATABASE |
| first task in a repo, or a style question | docs/CODE_STYLE.md | — |
| tests | docs/TESTING.md | — |
| a review | the diff + docs/SECURITY.md or CODE_STYLE.md + one standard | the repo |

## Cost reference (measured on kit evals, Sept 2026)
| Activity | Typical tokens | How to keep it down |
|---|---|---|
| Discovery interview (new-idea) | ~80k | Pre-fill from the pitch; short first reply |
| Full evaluation with web research | ~110–120k | Reuse `docs/product/research/`; refinement rounds re-research only what changed |
| Quality review of one feature branch | ~100k | Review the diff, not the repo; one standard file per reviewer |
| Build one S/M task | 30–150k | One task per session; `handoff` then start fresh |

## Model routing
- Agents declare their model: checklist/research agents (`market-researcher`, `qa-engineer`, `accessibility-auditor`, `ux-reviewer`) use a faster model (`sonnet` in Claude, medium reasoning in Codex); judgement-heavy ones (`devils-advocate`, `architect`, `security-reviewer`, builders) inherit the strongest.
- Cursor copies always `inherit` (Cursor uses its own model names) — pick the model in Cursor's chat.
- Mechanical edits (renames, formatting, copy tweaks) → fastest model; evaluations, architecture, security → strongest.

## Local models (Ollama on your Mac) — free and private, but weaker
Good for: summarising your own interview notes, first-draft translations for a native speaker to fix, renaming/boilerplate, reading long logs. Not for: evaluation, architecture, security review, anything customer-facing without review.
- Quick use: `ollama run <model> "Summarise these notes into themes:" < notes.md` (pick a model that fits your RAM; check `ollama list`).
- Codex with a local model: `codex --oss` (or `ollama launch codex`); use a model with a ≥ 64k context window. Keep a separate Codex profile in `~/.codex/` so your normal setup is unchanged.
- Claude and Cursor use cloud models; keep them for judgement-heavy work.
- Never paste secrets or users' personal data into any model, local or cloud, without a reason and consent.
