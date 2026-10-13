#!/usr/bin/env bash
# Run several AI tools in parallel without them overwriting each other's files.
# Each task gets its own folder (a git "worktree") on its own branch.
#
#   scripts/worktree.sh new T-07 lesson-player   → creates ../<project>-T-07 on branch feat/T-07-lesson-player
#   scripts/worktree.sh list                     → shows all worktrees
#   scripts/worktree.sh done T-07                → removes the folder (branch stays for the PR)
#
# Worktrees live NEXT TO the project (not inside it) so linters, tests and bundlers in the main
# folder never scan task copies. Open ../<project>-T-07 in Cursor / Codex / Claude Code.
set -euo pipefail
cmd="${1:-list}"
project="$(basename "$(git rev-parse --show-toplevel)")"

case "$cmd" in
  new)
    id="${2:?task id, e.g. T-07}"; name="${3:-task}"
    branch="feat/${id}-${name}"
    dir="../$project-$id"
    git worktree add -b "$branch" "$dir" main
    # Share local env with the main folder; install packages fresh (symlinked node_modules confuse bundlers).
    [ -f .env.local ] && cp .env.local "$dir/.env.local"
    [ -f package.json ] && (cd "$dir" && npm install --silent)
    echo "✅ $dir on $branch — open that folder in your AI tool."
    ;;
  list) git worktree list ;;
  done)
    id="${2:?task id}"
    git worktree remove "../$project-$id"
    echo "Removed ../$project-$id (branch kept — merge it via a pull request)."
    ;;
  *) echo "Usage: worktree.sh new <T-xx> <name> | list | done <T-xx>"; exit 1 ;;
esac
