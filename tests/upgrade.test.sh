#!/usr/bin/env bash
# upgrade-project.sh must never destroy an existing project's own files.
# Scenario: a Python project with its own CI, Cursor rules, pre-commit and a .gitignore that hides .cursor/*.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
P="$TMP/legacy-app"
mkdir -p "$P/.github/workflows" "$P/.cursor/rules" "$P/tests"
printf 'name: My CI\non: [push]\njobs: {}\n' > "$P/.github/workflows/ci.yml"
printf -- '---\ndescription: mine\nalwaysApply: true\n---\nMy rule\n' > "$P/.cursor/rules/testing.mdc"
printf 'repos: []\n' > "$P/.pre-commit-config.yaml"
printf '.cursor/*\n!.cursor/rules/\n' > "$P/.gitignore"
printf 'def test_ok():\n    assert True\n' > "$P/tests/test_ok.py"
git -C "$P" init -q && git -C "$P" -c user.name=t -c user.email=t@t add -A && git -C "$P" -c user.name=t -c user.email=t@t commit -qm init

pass=0; fail=0
check() { if eval "$2"; then pass=$((pass+1)); else fail=$((fail+1)); echo "✗ $1"; fi; }

out="$("$KIT/scripts/upgrade-project.sh" "$P" 2>&1)"
check "preview announces adopt mode"            'grep -q "Adopt mode" <<<"$out"'
check "preview changes nothing"                 '[ -z "$(git -C "$P" status --porcelain)" ]'

out="$("$KIT/scripts/upgrade-project.sh" "$P" --apply 2>&1)"
check "own ci.yml untouched"                    'grep -q "name: My CI" "$P/.github/workflows/ci.yml"'
check "own cursor rule untouched"               'grep -q "My rule" "$P/.cursor/rules/testing.mdc"'
check "kit cursor rules added alongside"        '[ "$(ls "$P/.cursor/rules" | wc -l)" -gt 1 ]'
check "kit scripts added"                       '[ -x "$P/scripts/check-gate.sh" ] && [ -x "$P/scripts/approve.sh" ]'
check "STATUS.md approved by adoption"          'grep -q "^Evaluation: APPROVED (.*adopted" "$P/docs/product/STATUS.md"'
check "phases 1-9 marked done, 10-13 untouched" '[ "$(grep -c "Done (before kit)" "$P/docs/product/STATUS.md")" = 9 ] && grep -q "^| 10 | Review | Not started" "$P/docs/product/STATUS.md"'
check "DECISIONS.md records the adoption"       'grep -q "Adopted into Product Kit" "$P/docs/product/DECISIONS.md"'
check "warns about pre-commit"                  'grep -q "pre-commit/husky" <<<"$out"'
check "warns about git-ignored additions"       'grep -q "git-ignored" <<<"$out" && grep -q ".cursor/agents" <<<"$out"'
check "keep list written with ci.yml + rule"    'grep -qx ".github/workflows/ci.yml" "$P/.product-kit-keep" && grep -qx ".cursor/rules/testing.mdc" "$P/.product-kit-keep"'
check "OWNER.md git-ignored in project"          'grep -qx "docs/product/OWNER.md" "$P/.gitignore"'
check "version stamped"                         '[ "$(cat "$P/.product-kit-version")" != "" ]'
check "gate passes on an adopted project"       '(cd "$P" && echo x > app.py && git add app.py && scripts/check-gate.sh)'

# Second run = normal upgrade mode; kept files must still survive.
out="$("$KIT/scripts/upgrade-project.sh" "$P" --apply 2>&1)"
check "second run is not adopt mode"            '! grep -q "Adopt mode" <<<"$out"'
check "second run keeps own ci.yml"             'grep -q "name: My CI" "$P/.github/workflows/ci.yml"'
check "second run keeps own cursor rule"        'grep -q "My rule" "$P/.cursor/rules/testing.mdc"'

echo "upgrade: $pass passed, $fail failed"
[ "$fail" = 0 ]
