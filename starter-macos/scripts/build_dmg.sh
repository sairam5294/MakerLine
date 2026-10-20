#!/usr/bin/env bash
# Package dist/<App>.app into a drag-to-Applications disk image (macOS only).
#   python3 setup.py py2app && scripts/build_dmg.sh
#
# Signs the app "ad hoc" (no Apple Developer account needed). macOS will still warn on first
# launch on other Macs — see README → "First launch on another Mac". Notarisation, which
# removes that warning, needs a paid Apple Developer account.
set -euo pipefail
cd "$(dirname "$0")/.."
command -v hdiutil >/dev/null || { echo "hdiutil not found: build the DMG on a Mac."; exit 1; }
NAME="$(python3 -c 'from app.core.config import APP_NAME; print(APP_NAME)')"
APP="dist/$NAME.app"
DMG="dist/$NAME.dmg"
[ -d "$APP" ] || { echo "No $APP yet. Run: python3 setup.py py2app"; exit 1; }

# Ad-hoc signature ("-"): satisfies Apple Silicon's must-be-signed rule; not a developer identity.
codesign --force --deep --sign - "$APP"
codesign --verify --deep --strict "$APP"

STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
cp -R "$APP" "$STAGE/"
ln -s /Applications "$STAGE/Applications"   # so people can drag the app straight in
rm -f "$DMG"
hdiutil create -volname "$NAME" -srcfolder "$STAGE" -ov -format UDZO "$DMG"
echo "✓ $DMG"
