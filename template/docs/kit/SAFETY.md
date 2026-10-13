# Safety settings — what's protected and where

| Risk | Claude Code | Cursor | Codex | Everyone (git/CI) |
|---|---|---|---|---|
| Reading secrets (.env, keys) | `settings.json` deny rules + `guard-bash.sh` | `.cursorignore` + block instructions | sandbox; ask before network | `.gitignore`, gitleaks in pre-commit + CI |
| Recursive delete, force push, push to main | deny rules + `guard-bash.sh` | `permissions.json` block instructions | `approval_policy = "on-request"` | branch protection on GitHub (turn on: Settings → Branches → require PR + CI) |
| Destructive DB commands | deny + hook | block instructions | approval | migrations only via PR |
| Coding before approval | `approval-gate.sh` hook | rule + block instruction | AGENTS.md rule | `scripts/check-gate.sh` in pre-commit + CI |
| AI approving its own work | hook blocks writing `Evaluation: APPROVED` | rule | AGENTS.md rule | owner runs `scripts/approve.sh` (types YES, commits) |
| Messy formatting | `format-edited.sh` | format on save | — | lefthook + CI |

Allowed without asking (Claude/Cursor): tests, lint, typecheck, git status/diff/log. Asked every time: installs, pushes, DB pushes, deploys, store submits.

One-time setup per project: `scripts/setup-github.sh` (repo + branch protection that applies to admins too), then `npx lefthook install`. Install `gitleaks` once with `brew install gitleaks`.
Claude Cowork/desktop runs no hooks, so there the skills follow these rules themselves. Build in Claude Code, Cursor or Codex.

## AI review on pull requests
`.github/workflows/ai-review.yml` runs the kit's quality-review on every PR and comments the findings. Add ONE secret to the GitHub repo: `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`, uses your Pro/Max plan) or `ANTHROPIC_API_KEY` (pay per use). Without a secret it skips itself. Cost control: faster model, 30-turn cap, one run per push (older runs cancelled), drafts and Dependabot PRs skipped.
Codex alternative: if you connect Codex to GitHub, you can also ask it for a review from the PR (see Codex's GitHub integration docs).
