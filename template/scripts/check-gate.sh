#!/usr/bin/env bash
# Approval-gate check for git hooks + CI (covers Cursor, Codex and people, not just Claude).
# Fails if app code changes while docs/product/STATUS.md lacks "Evaluation: APPROVED".
# Same allowlist as .claude/hooks/approval-gate.sh — keep the two in sync.
# Usage: scripts/check-gate.sh [changed files...]   (no args = staged files)
set -euo pipefail

status="docs/product/STATUS.md"
[ -f "$status" ] || exit 0                                  # Not a MakerLine project → skip.
grep -q "Evaluation: APPROVED" "$status" && exit 0          # Approved → nothing to check.

is_allowed() {
  case "$1" in
    docs/*|validation/*|design/*|.agents/*|.claude/*|.cursor/*|.codex/*|.github/*|scripts/*) return 0 ;;
    *.md|.gitignore|.cursorignore|lefthook.yml|.mcp.json|.product-kit-version) return 0 ;;
  esac
  return 1
}

blocked=()
if [ "$#" -gt 0 ]; then
  for f in "$@"; do is_allowed "$f" || blocked+=("$f"); done
else
  # Read staged file names one per line (safe with spaces in names).
  while IFS= read -r f; do [ -n "$f" ] && { is_allowed "$f" || blocked+=("$f"); }; done < <(git diff --cached --name-only)
fi

if [ "${#blocked[@]}" -gt 0 ]; then
  echo "✋ Approval gate: app code changed before the owner approved the evaluation ($status):"
  printf '   %s\n' "${blocked[@]}"
  echo "   Owner: approve with scripts/approve.sh, or record a skip decision in docs/product/DECISIONS.md."
  exit 1
fi
