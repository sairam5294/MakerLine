#!/usr/bin/env bash
# Shared-context checker: a complete project passes; each broken rule fails or warns; packs leave out
# private files and refuse secrets; the recovery scorer counts passes correctly.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
CC="python3 $KIT/scripts/context_check.py"
TPL="$KIT/plugin/skills/handoff/templates"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
pass=0
ok() { pass=$((pass + 1)); }
fail() { echo "FAIL: $1"; exit 1; }

P="$TMP/demo"
mkdir -p "$P/docs/product/opportunity"
cd "$P"
git init -q && git config user.email t@example.com && git config user.name Test
printf '# Rules\nBranches: <type>/<Mon>-<DD>-<summary>.\n' > AGENTS.md
printf '# Status — Demo\nEvaluation: PENDING\n' > docs/product/STATUS.md
printf '# Handoff — 2026-10-20 — Claude\n## Next steps\n1. Interview five users\n' > docs/product/HANDOFF.md
cat > docs/product/DECISIONS.md <<'MD'
| ID | Date | Decision | Options considered | Why | Evidence | Revisit when |
|---|---|---|---|---|---|---|
| D-01 | 2026-10-20 | Narrow to one city | All India | Focus | S1 | After 5 interviews |
MD
cat > docs/product/ASSUMPTIONS.md <<'MD'
| ID | Assumption or risk | Evidence | Confidence | Cost if wrong | Cheapest test | Owner | Review by | Status |
|---|---|---|---|---|---|---|---|---|
| A-01 | Users will pay | none yet | low | 6 weeks | Pre-sale page | Owner | 2026-12-01 | open |
MD
echo '{"product":"Demo","decision":"Test","options":[],"unknowns":[],"next_actions":[]}' > docs/product/opportunity/REVIEW.json
echo 'SECRET=1' > .env
git add -A && git commit -qm init
commit="$(git rev-parse --short HEAD)"
sed -e 's/<product>/Demo/' -e 's/| <name> |/| Demo |/' -e 's/| <idea .*live> |/| partial |/' \
    -e 's/| <the one outcome.*> |/| Decide whether to finish |/' -e 's/| <T-xx.*> |/| none |/' \
    -e 's/| <D-xx.*> |/| D-01 |/' -e 's/| <the exact next step.*> |/| Interview five users |/' \
    -e 's#| <Claude / ChatGPT / Cursor / owner> |#| Claude |#' -e 's/| <who approves and merges> |/| Owner |/' \
    -e "s/| <short commit hash.*> |/| $commit |/" -e 's/| <YYYY-MM-DD> |/| 2026-10-21 |/' \
    -e '/| Build a task |/d' "$TPL/CONTEXT_INDEX.md" > docs/product/CONTEXT_INDEX.md
git add -A && git commit -qm index

# 1. Complete project passes.
out="$($CC check . --today 2026-10-22)" || { echo "$out"; fail "complete project should pass"; }
echo "$out" | grep -q '^PASS' && ok

# 2. Missing index field fails.
cp docs/product/CONTEXT_INDEX.md /tmp/ci.bak.$$
sed -i.b 's/| Next action | Interview five users |/| Next action |  |/' docs/product/CONTEXT_INDEX.md && rm -f docs/product/CONTEXT_INDEX.md.b
if $CC check . --today 2026-10-22 >/dev/null; then fail "empty field should fail"; fi; ok
cp /tmp/ci.bak.$$ docs/product/CONTEXT_INDEX.md

# 3. Index pointing at a missing file fails.
sed -i.b 's#docs/product/ASSUMPTIONS.md, docs/product/opportunity#docs/product/NOPE.md, docs/product/opportunity#' docs/product/CONTEXT_INDEX.md && rm -f docs/product/CONTEXT_INDEX.md.b
$CC check . --today 2026-10-22 | grep -q 'missing file docs/product/NOPE.md' && ok
cp /tmp/ci.bak.$$ docs/product/CONTEXT_INDEX.md

# 4. Expired assumption warns (not fails).
out="$($CC check . --today 2027-01-15)" || fail "expired evidence should only warn"
echo "$out" | grep -q 'A-01 evidence expired' && ok

# 5. Duplicate decision ID fails.
echo '| D-01 | 2026-10-21 | Again | – | – | – | – |' >> docs/product/DECISIONS.md
if $CC check . --today 2026-10-22 >/dev/null; then fail "duplicate ID should fail"; fi; ok
git checkout -q docs/product/DECISIONS.md

# 6. Context changed after the verified commit warns.
echo '- extra' >> docs/product/STATUS.md && git commit -qam 'status change'
$CC check . --today 2026-10-22 | grep -q 'changed after the verified commit' && ok

# 7. Unknown commit fails.
sed -i.b "s/| $commit |/| deadbee |/" docs/product/CONTEXT_INDEX.md && rm -f docs/product/CONTEXT_INDEX.md.b
if $CC check . --today 2026-10-22 >/dev/null; then fail "unknown commit should fail"; fi; ok
cp /tmp/ci.bak.$$ docs/product/CONTEXT_INDEX.md

# 8. Long HANDOFF warns.
seq 1 45 >> docs/product/HANDOFF.md
$CC check . --today 2026-10-22 | grep -q 'HANDOFF.md has' && ok
git checkout -q docs/product/HANDOFF.md

# 9. Pack: includes task files, summarises REVIEW.json, leaves out private, records commit.
$CC pack . --task strategy --tool ChatGPT --today 2026-10-22 >/dev/null
grep -q 'Created 2026-10-22 for \*\*ChatGPT\*\*' docs/CONTEXT_PACK.md && ok
grep -q '## docs/product/ASSUMPTIONS.md' docs/product/../CONTEXT_PACK.md && ok
grep -q -- "- Decision: Test" docs/CONTEXT_PACK.md && ok
if grep -q 'SECRET=1' docs/CONTEXT_PACK.md; then fail ".env leaked into pack"; fi; ok

# 10. Pack: --public-only keeps only public files (STATUS is public in the template).
$CC pack . --task strategy --tool ChatGPT --public-only >/dev/null
grep -q '## docs/product/STATUS.md' docs/CONTEXT_PACK.md && ! grep -q '## docs/product/DECISIONS.md' docs/CONTEXT_PACK.md && ok

# 11. Pack refuses a secret-looking value.
echo 'api_key = sk-abcdefghijklmnopqrstuvwxyz123456' >> docs/product/HANDOFF.md
if $CC pack . --task strategy --tool ChatGPT >/dev/null; then fail "secret should block the pack"; fi; ok
git checkout -q docs/product/HANDOFF.md

# 12. Unknown task fails with the list of tasks.
$CC pack . --task nonsense --tool ChatGPT | grep -q 'Choose one of' && ok

# 12b. Pack to an absolute path outside the project works.
mkdir -p "$TMP/out"; $CC pack . --task strategy --tool ChatGPT --out "$TMP/out/pack.md" >/dev/null && test -s "$TMP/out/pack.md" && ok

# 13. Score: 1 pass, 1 missing, 1 wrong claim.
cat > key.json <<'J'
{"cases":[
 {"id":"C01","scenario":"s","must_include":["Demo",["partial","half-built"]]},
 {"id":"C02","scenario":"s","must_include":["T-09"]},
 {"id":"C03","scenario":"s","must_include":["D-01"],"must_not_include":["approved for build"]}
]}
J
printf '## C01\nDemo is half-built.\n## C02\nNo task.\n## C03\nD-01, approved for build.\n' > answers.md
out="$($CC score answers.md key.json || true)"
echo "$out" | grep -q '1/3 passed' && echo "$out" | grep -q 'missing: T-09' && echo "$out" | grep -q 'wrong: approved for build' && ok

# 14. Scale: a section anchor packs only that section; a missing section fails the check.
printf '# Big doc\n## Intro\nintro text\n## Payments\npay rules here\n### Refunds\nrefund rule\n## Other\nother text\n' > docs/product/BIG.md
cp docs/product/CONTEXT_INDEX.md /tmp/ci2.bak.$$
printf '| Payments | docs/product/BIG.md#payments, docs/product/DECISIONS.md#D-01 | big doc section only |\n' > /tmp/row.$$
python3 -c "import sys;p='docs/product/CONTEXT_INDEX.md';t=open(p).read();r=open(sys.argv[1]).read();t=t.replace('| Review |',r+'| Review |',1);open(p,'w').write(t)" /tmp/row.$$
git add -A && git commit -qm big
$CC pack . --task payments --tool ChatGPT >/dev/null
grep -q 'refund rule' docs/CONTEXT_PACK.md && ! grep -q 'other text' docs/CONTEXT_PACK.md && grep -q 'Narrow to one city' docs/CONTEXT_PACK.md && ok
sed -i.b 's/BIG.md#payments/BIG.md#shipping/' docs/product/CONTEXT_INDEX.md && rm -f docs/product/CONTEXT_INDEX.md.b
$CC check . --today 2026-10-22 | grep -q 'section #shipping' && ok

# 15. Scale: related repos are checked for existence and drift.
cp /tmp/ci2.bak.$$ docs/product/CONTEXT_INDEX.md
R="$TMP/docs-repo"; mkdir -p "$R" && git -C "$R" init -q && git -C "$R" -c user.email=t@e -c user.name=T commit -q --allow-empty -m one
rc="$(git -C "$R" rev-parse --short HEAD)"
printf '\n## Related repos\n\n| Repo | Path | Verified commit |\n|---|---|---|\n| Product docs | ../docs-repo | %s |\n' "$rc" >> docs/product/CONTEXT_INDEX.md
out="$($CC check . --today 2026-10-22)" || { echo "$out"; fail "current related repo should pass"; }
echo x > "$R/new.md" && git -C "$R" add -A && git -C "$R" -c user.email=t@e -c user.name=T commit -qm two
$CC check . --today 2026-10-22 | grep -q "related repo 'Product docs' has 1 changed file" && ok
sed -i.b 's#| ../docs-repo |#| ../nowhere |#' docs/product/CONTEXT_INDEX.md && rm -f docs/product/CONTEXT_INDEX.md.b
if $CC check . --today 2026-10-22 >/dev/null; then fail "missing related repo should fail"; fi; ok
cp /tmp/ci2.bak.$$ docs/product/CONTEXT_INDEX.md; rm -f /tmp/ci2.bak.$$ /tmp/row.$$

rm -f /tmp/ci.bak.$$
echo "context-check: $pass checks passed"
