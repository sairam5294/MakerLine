# AI agent adapters

One rulebook (`AGENTS.md`, plus `docs/RULES.md` for this project's rules) for every AI coding tool. A tool that reads `AGENTS.md` natively needs nothing; a tool that doesn't gets a **thin pointer file**, never a copy of the rules. Last verified **2026-10-20** against each tool's official docs.

## Tools

| Tool | Reads `AGENTS.md` natively? | File the kit adds | How to enable | Source |
|---|---|---|---|---|
| Codex (OpenAI) | Yes | — (`.codex/` for agents) | Nothing to do | https://agents.md/ |
| Claude Code | No (reads `CLAUDE.md`) | `CLAUDE.md` → `@AGENTS.md` | Nothing to do | (kit's existing adapter) |
| Cursor | Yes | `.cursor/rules/*.mdc` (scoped rules, written by `project-setup`) | Nothing to do | https://agents.md/ |
| GitHub Copilot | Coding agent: yes | `.github/copilot-instructions.md` (written by `project-setup`) | Nothing to do | https://agents.md/ |
| Gemini CLI | No (`GEMINI.md` by default) | `GEMINI.md` → `@./AGENTS.md` import | Nothing to do. Alternative: `.gemini/settings.json` → `"context": {"fileName": ["AGENTS.md", "GEMINI.md"]}` | https://geminicli.com/docs/cli/gemini-md/ · https://geminicli.com/docs/reference/configuration |
| Aider | No (needs `read:`) | `.aider.conf.yml` → `read: [AGENTS.md]`, `gitignore: false` | Run `aider` from the repo root (it loads `.aider.conf.yml` from the git root) | https://aider.chat/docs/usage/conventions.html · https://aider.chat/docs/config/aider_conf.html |
| Continue | Not documented (docs list only `.continue/rules/`) | `.continue/rules/00-agents-md.md` (always-on pointer) | Nothing to do | https://docs.continue.dev/customize/deep-dives/rules |
| Windsurf (Cascade) | Yes — root = always on, subfolders = scoped to that folder | — | Nothing to do (own rules would go in `.devin/rules/` or `.windsurf/rules/`) | https://docs.devin.ai/desktop/cascade/memories |
| Cline | Yes (also `.clinerules/`, `.cursorrules`, `.windsurfrules`) | — | Toggle in the Rules panel if switched off | https://docs.cline.bot/features/cline-rules |
| Roo Code | Yes, on by default | — | Setting `roo-cline.useAgentRules` (default `true`) | https://roocodeinc.github.io/Roo-Code/features/custom-instructions/ |
| Zed | Yes — but uses only the **first** match of `.rules`, `.cursorrules`, `.windsurfrules`, `.clinerules`, `.github/copilot-instructions.md`, `AGENT.md`, `AGENTS.md`, … | — | See gotcha below | https://zed.dev/docs/ai/rules |
| JetBrains Junie | Yes (root `AGENTS.md`; `.junie/guidelines.md` is legacy) | — | Nothing to do | https://junie.jetbrains.com/docs/guidelines-and-memory.html |
| Kiro (AWS) | Yes — always included, root and subfolders | — | Nothing to do (own steering would go in `.kiro/steering/`) | https://kiro.dev/docs/steering/ |
| Google Antigravity | Yes (also `GEMINI.md`, `.agents/rules/`) | — | Nothing to do | https://www.antigravity.google/docs/rules |
| OpenCode | Yes (falls back to `CLAUDE.md`) | — | Extra files via `instructions` in `opencode.json` | https://opencode.ai/docs/rules/ |
| Amp | Yes (root, parents, subtrees; falls back to `AGENT.md`/`CLAUDE.md`) | — | Nothing to do | https://ampcode.com/docs/customize/agents-md |
| ChatGPT (browser), contractors | Can't read the repo | `docs/CONTEXT_PACK.md` (written by `project-setup`) | Paste it in | — |

## Gotchas

- **Zed** picks one file only. Once `project-setup` writes `.github/copilot-instructions.md`, Zed uses that pointer instead of `AGENTS.md` — the pointer says "follow AGENTS.md", so it still works, but keep it short and current.
- **Antigravity** reads both `AGENTS.md` and `GEMINI.md`; `GEMINI.md` only holds an import line, so nothing is loaded twice.
- **Aider** adds `.aider*` to `.gitignore` by default — `gitignore: false` keeps the shared config committed; `.gitignore` lists Aider's history files instead.
- **Existing projects**: `scripts/upgrade-project.sh` doesn't copy these root files yet — copy `GEMINI.md`, `.aider.conf.yml` and `.continue/rules/00-agents-md.md` from the kit's `template/` by hand.

## Rules

- Never copy rules into an adapter. Add rules to `AGENTS.md` (shared) or `docs/RULES.md` (this project) only.
- An adapter is ≤ 10 lines and says why it exists.
- Add a tool only after checking its current official docs; record the URL and the date here.
- `standards-refresh` re-checks this table; a tool that starts reading `AGENTS.md` natively loses its adapter.
