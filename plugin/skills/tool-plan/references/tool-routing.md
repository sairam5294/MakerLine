# Tool routing — default job split

The starting split `tool-plan` adjusts to what the owner has: "Primary" does the job; "fallback" takes over when the primary is unavailable or out of limit. Re-check vendors' current capabilities before relying on any line (`standards-refresh`).

## By phase

| Job | Primary | Fallback | Why |
|---|---|---|---|
| Brainstorming, angles, "what else could this be?" | ChatGPT | Claude (chat) | fast, cheap, divergent; nothing is decided here |
| Naming long-lists, taglines, first-draft copy | ChatGPT | Claude | volume first; Claude (name-product) scores and checks conflicts |
| Quick fact lookups, "what is X" | ChatGPT or Claude with web search | — | either; record anything you'll rely on in `docs/product/research/` |
| Discovery interview, evaluation, competitors, reality check | Claude (Product Kit: new-idea, evaluate-idea) | — | needs the kit's method, sources and the owner's profile |
| Design direction, wireframes, Figma | Claude (design-direction) + Figma | Cursor for small HTML tweaks | follows the kit's accessibility rules |
| Specs: PRD, engineering docs, rules, README | Claude (write-prd, engineering-docs, project-setup) | — | long, consistent, cross-referenced documents |
| Plan and multi-file features | Claude Code | Codex for well-specified independent tasks | reads AGENTS.md, hooks enforce the gate |
| Small edits inside code (rename, style fix, one component) | Cursor or Codex | Claude Code | cheaper per edit, fast in the editor |
| Parallel independent tasks and tests | Codex (separate worktrees) | Claude Code subagents | runs tasks in parallel from PLAN.md |
| Reviews (accessibility, security, code) | Claude (quality-review, parallel agents) | Cursor review for small diffs | multi-angle, against the project's standards |
| Debugging a failing test or build | Claude Code | Cursor | needs the terminal and the logs |
| Summarising your own notes, private drafts | Local model (Ollama) | ChatGPT | free and private; never for evaluation or security |
| Marketing posts, social copy variants | ChatGPT | Claude | volume and tone variants |

## Typical splits

| Owner has | Split |
|---|---|
| **Claude + ChatGPT** (common) | ChatGPT for brainstorming, naming long-lists, quick research and first drafts; Claude for evaluation, specs and docs, then building with Claude Code. |
| **Claude + ChatGPT + Cursor/Codex** | as above, plus Cursor or Codex for small in-code edits and parallel well-specified tasks; Claude Code for multi-file features, reviews and anything touching auth, data or payments. |
| **Claude only** | Claude chat for thinking, Claude Code for building; use the faster model for mechanical work (`context-budget.md`, model routing). |
| **ChatGPT only** | possible for thinking phases with the Idea Pack's CONTEXT_PACK pasted in; switch to an agent that reads the repo before building. |

## Rules that keep the split working

1. **The repo is the memory.** AGENTS.md, `docs/RULES.md`, `docs/MEMORY.md` and `docs/product/` are what every tool reads. Chat history is not.
2. **One owner per document.** The tool that owns a file writes it; others propose changes the owner reviews.
3. **Context out, result back.** A tool that can't read the repo gets `docs/CONTEXT_PACK.md`; its output lands in a named file (`docs/product/research/<topic>.md`, `drafts/<name>.md`) and the owning tool reviews it.
4. **Nothing secret leaves the repo:** no keys, tokens, `.env` contents or users' personal data in any AI tool.
5. **When a limit hits,** switch to that job's fallback, start with HANDOFF.md, and don't redo work that's already in the repo.
