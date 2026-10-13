#!/usr/bin/env bash
# PostToolUse hook (Edit|Write|MultiEdit): auto-format the file Claude just changed,
# so formatting never needs a separate AI step (saves tokens and review noise).
# Never fails the edit: any error is ignored.

input="$(cat)"
file="$(printf '%s' "$input" | "$(dirname "$0")/_read-input.sh" tool_input.file_path)"
[ -f "$file" ] || exit 0

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
# Only format file types Prettier understands, and only if the project has Prettier installed.
case "$file" in
  *.ts|*.tsx|*.js|*.jsx|*.mjs|*.json|*.css|*.md|*.yml|*.yaml)
    [ -x node_modules/.bin/prettier ] && node_modules/.bin/prettier --write --log-level silent "$file" >/dev/null 2>&1 ;;
esac
exit 0
