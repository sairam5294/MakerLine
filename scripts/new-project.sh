#!/usr/bin/env bash
# Create (or upgrade) a project from MakerLine.
#
#   ./scripts/new-project.sh ~/Projects/my-app            → rules, skills, agents, safety, CI (any stack)
#   ./scripts/new-project.sh ~/Projects/my-app --starter  → the above + tested Expo/Supabase app (iOS/Android/web)
#   ./scripts/new-project.sh ~/Projects/my-site --web     → the above + tested Next.js site (landing page, SEO, waitlist)
#
# Safe to re-run on an existing project: it never overwrites files you already have.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?Usage: new-project.sh <path> [--starter | --web]}"
STARTER="${2:-}"
VERSION="$(sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' "$KIT/plugin/.claude-plugin/plugin.json")"

python3 "$KIT/scripts/sync.py" >/dev/null          # make sure template/ matches plugin/
mkdir -p "$DEST"

# Copy only files that don't exist yet (never overwrite the user's work).
copy_missing() {  # copy_missing <from-dir> <to-dir>
  if command -v rsync >/dev/null; then
    rsync -a --ignore-existing --exclude node_modules "$1/" "$2/"
  else
    (cd "$1" && find . -path ./node_modules -prune -o -type f -print) | while read -r f; do
      [ -e "$2/$f" ] || { mkdir -p "$2/$(dirname "$f")"; cp -p "$1/$f" "$2/$f"; }
    done
  fi
}
copy_missing "$KIT/template" "$DEST"

if [ "$STARTER" = "--starter" ]; then
  copy_missing "$KIT/starter" "$DEST"
  # Enable Expo's official Claude plugin in the project settings (merges, doesn't overwrite).
  python3 - "$DEST/.claude/settings.json" "$KIT/scripts/starter-claude-plugins.json" <<'PY'
import json, sys
dest, extra = sys.argv[1], sys.argv[2]
d = json.load(open(dest)); e = json.load(open(extra))
d.setdefault("enabledPlugins", {}).update(e.get("enabledPlugins", {}))
json.dump(d, open(dest, "w"), indent=2)
PY
elif [ "$STARTER" = "--web" ]; then
  copy_missing "$KIT/starter-web" "$DEST"
fi

cd "$DEST"
# Record which kit version this project started from (helps when upgrading later).
sed -i.bak "s/kit v<version>/kit v$VERSION/" docs/product/STATUS.md 2>/dev/null && rm -f docs/product/STATUS.md.bak
echo "$VERSION" > .product-kit-version
# Owner profile + cross-project outcomes: snapshots the skills can read inside this project.
if [ ! -f docs/product/OWNER.md ]; then
  if [ -f "$KIT/owner/OWNER.md" ]; then cp "$KIT/owner/OWNER.md" docs/product/OWNER.md
  else cp "$KIT/owner/OWNER.example.md" docs/product/OWNER.md; echo "ℹ No owner/OWNER.md in the kit yet — copied the example. Fill in docs/product/OWNER.md (or owner/OWNER.md in the kit for all future projects)."; fi
fi
cp "$KIT/portfolio/OUTCOMES.md" docs/product/OUTCOMES-snapshot.md
chmod +x .claude/hooks/*.sh scripts/*.sh 2>/dev/null || true
# New repo → first commit contains the scaffold, so the approval gate only checks YOUR later changes.
if [ ! -d .git ] && command -v git >/dev/null; then
  git init -q -b main
  git add -A && git commit -q --no-verify -m "chore: scaffold from MakerLine v$VERSION" \
    || echo "   (Couldn't make the first commit — set git user.name/user.email, then commit.)"
fi

echo "✅ Project ready at $DEST (MakerLine v$VERSION)"
[ -n "$STARTER" ] && echo "   Next: cd \"$DEST\" && npm install && cp .env.example .env.local && npx lefthook install"
echo "   Then open it in Claude, Cursor or Codex and say: \"I have a new idea\"."
