#!/usr/bin/env bash
# Build the Claude plugin file from plugin/ so it can be installed in the Claude app (Cowork / desktop).
#   ./scripts/build-plugin.sh            → ../makerline.plugin (next to the kit folder)
#   ./scripts/build-plugin.sh ~/Desktop  → ~/Desktop/makerline.plugin
# Claude Code users don't need this: install from the marketplace instead (see GETTING-STARTED.md).
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="${1:-$KIT/..}"
OUT="$(cd "$OUT_DIR" && pwd)/makerline.plugin"
command -v zip >/dev/null || { echo "zip is required (macOS and Linux have it by default)."; exit 1; }
rm -f "$OUT"
(cd "$KIT/plugin" && zip -qr "$OUT" . -x "*.DS_Store")
echo "✅ Built $OUT"
echo "   Open it in a Claude chat and press Install (replaces any older version)."
