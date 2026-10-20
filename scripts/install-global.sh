#!/usr/bin/env bash
# Install MakerLine skills and agents at USER level (available in every project).
# Usage: ./scripts/install-global.sh claude|cursor|codex [more...]
#   claude -> ~/.claude/skills + ~/.claude/agents (Claude Code CLI; Cowork/desktop should use the .plugin file instead)
#   cursor -> ~/.cursor/skills + ~/.cursor/agents
#   codex  -> ~/.agents/skills + ~/.codex/agents (TOML)
# Note: Cursor also reads ~/.claude/* and ~/.agents/skills, so installing several targets can show duplicate
# skills in Cursor. Per-project install (new-project.sh) avoids this and is recommended.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$KIT/scripts/sync.py" >/dev/null
for target in "$@"; do
  case "$target" in
    claude) mkdir -p ~/.claude/skills ~/.claude/agents
            cp -R "$KIT/plugin/skills/." ~/.claude/skills/; cp "$KIT/plugin/agents/"*.md ~/.claude/agents/ ;;
    cursor) mkdir -p ~/.cursor/skills ~/.cursor/agents
            cp -R "$KIT/plugin/skills/." ~/.cursor/skills/; cp "$KIT/plugin/agents/"*.md ~/.cursor/agents/ ;;
    codex)  mkdir -p ~/.agents/skills ~/.codex/agents
            cp -R "$KIT/plugin/skills/." ~/.agents/skills/; cp "$KIT/template/.codex/agents/"*.toml ~/.codex/agents/ ;;
    *) echo "Unknown target: $target (use claude, cursor or codex)"; exit 1 ;;
  esac
  echo "✅ Installed for $target"
done
