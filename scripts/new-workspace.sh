#!/usr/bin/env bash
# Create a MakerLine product workspace: the standard folder around a product's repo(s).
# Standard: plugin/skills/new-idea/references/workspace.md (the root files are written from its skeletons).
#
#   ./scripts/new-workspace.sh ~/Code_Projects/Lekka                      → core folders + root files + docs-only repo
#   ./scripts/new-workspace.sh ~/Code_Projects/Lekka --name "Lekka" --full → also every numbered folder
#   ./scripts/new-workspace.sh ~/Code_Projects/Lekka --adopt ~/Code/lekka  → preview moving an existing repo in
#   ./scripts/new-workspace.sh ~/Code_Projects/Lekka --adopt ~/Code/lekka --apply   → do it
#
# Safe to re-run: never overwrites a file, never deletes anything. Adopt mode changes nothing without --apply.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
STANDARD="$KIT/plugin/skills/new-idea/references/workspace.md"
usage="Usage: new-workspace.sh <workspace-path> [--name <Name>] [--full] [--adopt <repo-path> [--apply]]"

DEST="${1:?$usage}"; shift
NAME=""; FULL=0; ADOPT=""; APPLY=0
while [ $# -gt 0 ]; do
  case "$1" in
    --name)  NAME="${2:?$usage}"; shift 2 ;;
    --full)  FULL=1; shift ;;
    --adopt) ADOPT="${2:?$usage}"; shift 2 ;;
    --apply) APPLY=1; shift ;;
    *) echo "$usage"; exit 2 ;;
  esac
done
[ -n "$NAME" ] || NAME="$(basename "$DEST")"
slugify() {  # "Café App" → cafe-app (accents dropped, anything else → -)
  python3 -c 'import re,sys,unicodedata as u; s=u.normalize("NFKD",sys.argv[1]).encode("ascii","ignore").decode().lower(); print(re.sub(r"[^a-z0-9]+","-",s).strip("-"))' "$1"
}
SLUG="$(slugify "$NAME")"
[ -n "$SLUG" ] || { echo "Can't make a folder name from '$NAME' — pass --name with letters or digits."; exit 2; }

CORE=(00_inbox 04_repos 98_bin 99_archive)
ALL=(00_inbox 01_research 02_brand 03_design 04_repos 05_qa 06_releases 07_launch 08_ops 90_reference 98_bin 99_archive)

if [ -n "$ADOPT" ]; then
  [ -d "$ADOPT" ] || { echo "No folder at $ADOPT"; exit 1; }
  SRC="$(cd "$ADOPT" && pwd -P)"
  # Resolve the destination through its nearest existing parent (it may not exist yet).
  d="$DEST"; rest=""
  while [ ! -d "$d" ]; do rest="/$(basename "$d")$rest"; d="$(dirname "$d")"; done
  DEST_ABS="$(cd "$d" && pwd -P)$rest"
  case "$DEST_ABS/" in "$SRC"/*) echo "Stopped: the workspace can't be inside the folder you're adopting ($SRC). Pick a folder next to it — nothing changed."; exit 1 ;; esac
  case "$(pwd -P)/" in "$SRC"/*) echo "Stopped: run this from outside $SRC (the folder you're moving) — nothing changed."; exit 1 ;; esac
  REPO_NAME="$(slugify "$(basename "$SRC")")"
  [ -n "$REPO_NAME" ] || { echo "Can't make a folder name from '$(basename "$SRC")' — rename the repo folder first."; exit 2; }
  TARGET="$DEST/04_repos/$REPO_NAME"
  if [ -e "$TARGET" ]; then echo "Stopped: $TARGET already exists — nothing moved."; exit 1; fi
  if [ "$APPLY" = 0 ]; then
    echo "Adopt preview (nothing changed):"
    echo "  create  $DEST with ${CORE[*]} and README.md, AGENTS.md, CLAUDE.md, STATUS.md (missing files only)"
    echo "  move    $SRC → $TARGET"
    echo "Then move loose docs that duplicate repo files to 98_bin/ (after copying to 99_archive/)."
    echo "Run again with --apply to do it."
    exit 0
  fi
  SLUG="$REPO_NAME"
fi

if [ -n "$ADOPT" ]; then  # move first, so a failed move leaves no half-made workspace
  mkdir -p "$DEST/04_repos"
  mv "$SRC" "$TARGET"
  echo "  moved    $SRC → 04_repos/$SLUG"
fi

if [ "$FULL" = 1 ]; then dirs=("${ALL[@]}"); else dirs=("${CORE[@]}"); fi
for d in "${dirs[@]}"; do mkdir -p "$DEST/$d"; done

# Root files from the standard's skeletons; existing files are kept.
python3 - "$STANDARD" "$DEST" "$NAME" "$SLUG" "$(date +%Y-%m-%d)" <<'PY'
import pathlib, re, sys
standard, dest, name, slug, today = sys.argv[1:]
text = pathlib.Path(standard).read_text(encoding="utf-8")
blocks = re.findall(r"<!-- file: (\S+) -->\n```\n(.*?)```\n<!-- end -->", text, re.S)
if not blocks:
    sys.exit(f"No skeletons found in {standard}")
for fname, body in blocks:
    out = pathlib.Path(dest) / fname
    if out.exists():
        print(f"  kept     {fname} (already there)")
        continue
    body = body.replace("{{Name}}", name).replace("{{slug}}", slug).replace("{{date}}", today)
    out.write_text(body, encoding="utf-8")
    print(f"  created  {fname}")
PY

if [ -z "$ADOPT" ]; then
  REPO="$DEST/04_repos/$SLUG"
  mkdir -p "$REPO/docs/product"
  if command -v git >/dev/null && [ ! -d "$REPO/.git" ]; then git -C "$REPO" init -q && echo "  created  04_repos/$SLUG (git, docs only — keep it private)"; fi
fi

echo "✅ Workspace ready: $DEST"
echo "   Next: open 04_repos/$SLUG in Claude Code or Cursor and run /makerline:start (or new-project.sh on it after approval)."
