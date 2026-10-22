#!/usr/bin/env bash
# new-workspace.sh: creates the standard folder, never overwrites, and adopt mode changes nothing without --apply.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
S="$KIT/scripts/new-workspace.sh"

pass=0; fail=0
check() { if eval "$2"; then pass=$((pass+1)); else fail=$((fail+1)); echo "✗ $1"; fi; }

W="$TMP/My App"
bash "$S" "$W" >/dev/null
check "core folders created"                 'for d in 00_inbox 04_repos 98_bin 99_archive; do [ -d "$W/$d" ] || exit 1; done'
check "optional folders not created"         '[ ! -d "$W/01_research" ] && [ ! -d "$W/07_launch" ]'
check "root files written"                   'for f in README.md AGENTS.md CLAUDE.md STATUS.md; do [ -s "$W/$f" ] || exit 1; done'
check "placeholders filled"                  '! grep -q "{{" "$W"/*.md && grep -q "04_repos/my-app/" "$W/AGENTS.md"'
check "CLAUDE.md points to AGENTS.md"        '[ "$(cat "$W/CLAUDE.md")" = "@AGENTS.md" ]'
check "workspace AGENTS.md stays tiny"       '[ "$(wc -l < "$W/AGENTS.md")" -le 15 ]'
check "docs-only repo created"               '[ -d "$W/04_repos/my-app/docs/product" ] && [ -d "$W/04_repos/my-app/.git" ]'

echo "mine" > "$W/README.md"
bash "$S" "$W" --full >/dev/null
check "existing file never overwritten"      '[ "$(cat "$W/README.md")" = "mine" ]'
check "--full adds every numbered folder"    'for d in 01_research 02_brand 03_design 05_qa 06_releases 07_launch 08_ops 90_reference; do [ -d "$W/$d" ] || exit 1; done'

R="$TMP/legacy"; mkdir -p "$R/src"; echo x > "$R/src/a.txt"
W2="$TMP/Legacy"
out="$(bash "$S" "$W2" --adopt "$R")"
check "adopt preview changes nothing"        '[ ! -e "$W2" ] && [ -f "$R/src/a.txt" ] && grep -q "nothing changed" <<<"$out"'
bash "$S" "$W2" --adopt "$R" --apply >/dev/null
check "adopt --apply moves the repo in"      '[ -f "$W2/04_repos/legacy/src/a.txt" ] && [ ! -e "$R" ]'
check "adopt points files at that repo"      'grep -q "04_repos/legacy/" "$W2/AGENTS.md"'

mkdir -p "$R"
check "adopt refuses an occupied target"     '! bash "$S" "$W2" --adopt "$R" --apply >/dev/null 2>&1 && [ -d "$R" ]'

R3="$TMP/self"; mkdir -p "$R3"; echo x > "$R3/a.txt"
check "adopt into itself refused, nothing made"  '! bash "$S" "$R3/ws" --adopt "$R3" --apply >/dev/null 2>&1 && [ "$(ls "$R3")" = "a.txt" ]'
check "adopt from inside the repo refused"       '! (cd "$R3" && bash "$S" "$TMP/ws3" --adopt . --apply >/dev/null 2>&1) && [ ! -e "$TMP/ws3" ]'

R4="$TMP/My Repo"; mkdir -p "$R4"
bash "$S" "$TMP/WS4" --adopt "$R4" --apply >/dev/null
check "adopted folder name has no spaces"         '[ -d "$TMP/WS4/04_repos/my-repo" ]'
bash "$S" "$TMP/Café ☕" >/dev/null
check "accents and symbols make a clean slug"     '[ -d "$TMP/Café ☕/04_repos/cafe" ]'

P="$TMP/scan/Lekka"; mkdir -p "$P/lekka/docs/product" "$P/99_archive/old/docs/product"
cp "$KIT/plugin/skills/product-kickoff/templates/STATUS.md" "$P/lekka/docs/product/"
cp "$KIT/plugin/skills/product-kickoff/templates/STATUS.md" "$P/99_archive/old/docs/product/"
bash "$S" "$P" >/dev/null
cp "$KIT/plugin/skills/product-kickoff/templates/STATUS.md" "$P/04_repos/lekka/docs/product/"
found="$(cd "$KIT" && python3 -c "
import importlib.util,sys
s=importlib.util.spec_from_file_location('p','scripts/portfolio.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
import pathlib; print('\n'.join(str(f) for f in m.find_status_files(pathlib.Path(sys.argv[1]))))" "$TMP/scan")"
check "portfolio finds repo under 04_repos"       'grep -q "04_repos/lekka/docs" <<<"$found"'
check "portfolio still finds a sibling repo"      'grep -q "Lekka/lekka/docs" <<<"$found"'
check "portfolio skips the workspace archive"     '! grep -q "99_archive" <<<"$found"'

echo "workspace: $pass passed, $fail failed"
[ "$fail" = 0 ]
