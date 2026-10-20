#!/usr/bin/env bash
# PreToolUse hook (Edit|Write|MultiEdit) — the MakerLine approval gate, for Claude Code.
#  1. Until docs/product/STATUS.md says "Evaluation: APPROVED", only planning/docs/config files may be
#     edited — not app code.
#  2. The AI may never write "Evaluation: APPROVED" itself: only the owner approves, with
#     scripts/approve.sh. (Stops an agent from approving its own work.)
# Exit 0 = allow. Exit 2 = block (stderr is shown to Claude so it can explain to the owner).
# Same allowlist as scripts/check-gate.sh (git hook + CI) — keep the two in sync.

input="$(cat)"
read_field() { printf '%s' "$input" | "$(dirname "$0")/_read-input.sh" "$1"; }

file="$(read_field tool_input.file_path)"
[ -z "$file" ] && exit 0
root="${CLAUDE_PROJECT_DIR:-$(pwd)}"
rel="${file#"$root"/}"
status="$root/docs/product/STATUS.md"

# --- Rule 2: no self-approval -------------------------------------------------------------
if [ "$rel" = "docs/product/STATUS.md" ]; then
  new_text="$(read_field tool_input.content)$(read_field tool_input.new_string)"
  if printf '%s' "$new_text" | grep -q "Evaluation: APPROVED" && ! grep -q "Evaluation: APPROVED" "$status" 2>/dev/null; then
    echo "Blocked: only the owner can approve the evaluation. Ask them to run: scripts/approve.sh" >&2
    exit 2
  fi
  exit 0
fi

# --- Rule 1: app code only after approval --------------------------------------------------
case "$rel" in
  docs/*|validation/*|design/*|.agents/*|.claude/*|.cursor/*|.codex/*|.github/*|scripts/*) exit 0 ;;
  *.md|.gitignore|.cursorignore|lefthook.yml|.mcp.json|.product-kit-version) exit 0 ;;
esac
[ -f "$status" ] || exit 0                        # Not a MakerLine project → don't block.
grep -q "Evaluation: APPROVED" "$status" && exit 0

echo "Blocked by the MakerLine approval gate: '$rel' is app code, but the owner hasn't approved the evaluation yet (docs/product/STATUS.md). Finish evaluate-idea; the owner approves with scripts/approve.sh. Landing pages for validation go in a separate project or the validation/ folder." >&2
exit 2
