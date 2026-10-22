#!/usr/bin/env bash
# Publish a new version of MakerLine after you (or an AI) changed files in plugin/.
#
#   ./scripts/release-kit.sh 0.6.0 "Short note of what changed"
#
# It: checks the version, copies plugin/ into template/, runs the kit tests,
# sets the version, adds a CHANGELOG line, and rebuilds ../makerline.plugin (next to the kit folder).
# Afterwards: reinstall the plugin in Claude, and run upgrade-project.sh on projects you want updated.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
NEW="${1:?Usage: release-kit.sh <new-version e.g. 0.6.0> \"what changed\"}"
NOTE="${2:?Add a short note of what changed, in quotes}"
MANIFEST="$KIT/plugin/.claude-plugin/plugin.json"
OLD="$(sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' "$MANIFEST")"
cd "$KIT"

# 1. Version must look like 1.2.3 and be different from the current one.
[[ "$NEW" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo "Version must look like 0.6.0"; exit 1; }
[ "$NEW" != "$OLD" ] || { echo "Version $NEW is already current — pick a higher one."; exit 1; }

# 2. Copy the source (plugin/) into the project template, then run the kit's own tests.
python3 scripts/sync.py
bash tests/hooks.test.sh
bash tests/upgrade.test.sh
bash tests/idea-pack.test.sh
bash tests/opportunity-review.test.sh
bash tests/context-check.test.sh

# 3. Set the version everywhere it's shown.
sed -i.bak "s/\"version\": *\"$OLD\"/\"version\": \"$NEW\"/" "$MANIFEST" && rm -f "$MANIFEST.bak"
sed -i.bak "s/\"version\": *\"$OLD\"/\"version\": \"$NEW\"/" plugin/plugin.json && rm -f plugin/plugin.json.bak
sed -i.bak "s/^# MakerLine (Claude plugin) v.*/# MakerLine (Claude plugin) v${NEW%.*}/" plugin/README.md && rm -f plugin/README.md.bak
sed -i.bak "s/^# MakerLine v[0-9.]*/# MakerLine v${NEW%.*}/" README.md && rm -f README.md.bak

# 4. Changelog entry at the top (under the title).
today="$(date +%Y-%m-%d)"
python3 - "$NEW" "$today" "$NOTE" <<'PY'
import sys, pathlib
new, today, note = sys.argv[1:4]
p = pathlib.Path("CHANGELOG.md"); t = p.read_text()
marker = "\n## "
i = t.find(marker)
entry = f"\n## {new} — {today}\n{note}\n"
p.write_text(t[:i] + entry + t[i:] if i >= 0 else t + entry)
PY

# 5. Rebuild the Claude plugin files next to the kit folder (full kit + MakerLine Idea).
"$KIT/scripts/build-plugin.sh" >/dev/null
python3 scripts/build-idea-pack.py --zip "$KIT/.." >/dev/null

# 6. Commit if this is a git repo.
if git rev-parse >/dev/null 2>&1; then git add -A && git commit -q -m "MakerLine v$NEW: $NOTE" && echo "✔ committed (push with: git push)"; fi

echo "✅ MakerLine $OLD → $NEW"
echo "Next: 1) open ../makerline.plugin in Claude and install (replaces the old one)"
echo "      2) update projects: ./scripts/upgrade-project.sh ~/Projects/<app>   (preview, then --apply)"
