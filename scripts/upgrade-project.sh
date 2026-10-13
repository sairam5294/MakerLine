#!/usr/bin/env bash
# Upgrade an existing project to the current Product Kit version.
#
#   ./scripts/upgrade-project.sh ~/Projects/my-app           → preview only (nothing changes)
#   ./scripts/upgrade-project.sh ~/Projects/my-app --apply   → apply the upgrade
#
# Two kinds of files:
#   KIT-OWNED  (skills, agents, rules, hooks, kit docs, kit scripts, CI) → replaced with the new version.
#              Old copies are saved in .product-kit-backup/<date>/ first.
#   YOURS      (AGENTS.md, CLAUDE.md, settings, MCP/permissions config, lefthook, .gitignore) → never
#              overwritten. The script shows what the new kit version changed so you (or an AI) can merge.
# Your code, docs/product/ and design/tokens.json are never touched.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?Usage: upgrade-project.sh <project-path> [--apply]}"
APPLY="${2:-}"
NEW="$(sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' "$KIT/plugin/.claude-plugin/plugin.json")"
OLD="$(cat "$DEST/.product-kit-version" 2>/dev/null || echo "unknown")"
T="$KIT/template"

python3 "$KIT/scripts/sync.py" >/dev/null   # make sure template/ is current

KIT_OWNED=(.agents/skills .cursor/agents .cursor/rules .codex/agents .claude/hooks docs/kit
           scripts/check-gate.sh scripts/approve.sh scripts/worktree.sh scripts/setup-github.sh scripts/local-ai.sh
           .github/workflows/ci.yml .github/workflows/ai-review.yml .github/pull_request_template.md .github/dependabot.yml)
YOURS=(AGENTS.md CLAUDE.md .claude/settings.json .codex/config.toml .cursor/permissions.json .cursor/mcp.json
       .mcp.json lefthook.yml .gitignore .cursorignore)

echo "Product Kit upgrade: $OLD → $NEW  ($DEST)"
[ "$APPLY" = "--apply" ] || echo "(preview — run again with --apply to make changes)"

# Warn if the project has uncommitted changes: commit first so the upgrade is easy to review/undo.
if git -C "$DEST" rev-parse >/dev/null 2>&1 && [ -n "$(git -C "$DEST" status --porcelain)" ]; then
  echo "⚠️  Uncommitted changes in the project. Commit them first so you can review/undo the upgrade."
fi

backup="$DEST/.product-kit-backup/$(date +%Y-%m-%d-%H%M)"
echo; echo "KIT-OWNED (replaced):"
for p in "${KIT_OWNED[@]}"; do
  [ -e "$T/$p" ] || continue
  if [ -e "$DEST/$p" ] && diff -rq "$T/$p" "$DEST/$p" >/dev/null 2>&1; then continue; fi  # already current
  echo "  • $p"
  if [ "$APPLY" = "--apply" ]; then
    if [ -e "$DEST/$p" ]; then mkdir -p "$backup/$(dirname "$p")"; cp -R "$DEST/$p" "$backup/$p"; fi
    mkdir -p "$DEST/$(dirname "$p")"
    if [ -d "$T/$p" ]; then mkdir -p "$DEST/$p"; cp -R "$T/$p/." "$DEST/$p/"; else cp "$T/$p" "$DEST/$p"; fi
  fi
done

echo; echo "YOURS (not changed — review these differences and merge what you want):"
for p in "${YOURS[@]}"; do
  [ -e "$T/$p" ] || continue
  if [ ! -e "$DEST/$p" ]; then
    echo "  • $p is new in this kit version"
    [ "$APPLY" = "--apply" ] && { mkdir -p "$DEST/$(dirname "$p")"; cp "$T/$p" "$DEST/$p"; echo "    → added"; }
  elif ! diff -q "$T/$p" "$DEST/$p" >/dev/null; then
    echo "  • $p differs:  diff \"$T/$p\" \"$DEST/$p\""
  fi
done

if [ "$APPLY" = "--apply" ]; then
  chmod +x "$DEST"/.claude/hooks/*.sh "$DEST"/scripts/*.sh 2>/dev/null || true
  echo "$NEW" > "$DEST/.product-kit-version"
  grep -q "^.product-kit-backup/" "$DEST/.gitignore" 2>/dev/null || echo ".product-kit-backup/" >> "$DEST/.gitignore"
  echo; echo "✅ Upgraded to $NEW. Backups: ${backup#$DEST/}. Tip: ask your AI tool"
  echo "   \"merge the Product Kit template changes into AGENTS.md/CLAUDE.md (see upgrade output)\"."
fi
