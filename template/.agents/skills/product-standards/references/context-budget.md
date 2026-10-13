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
