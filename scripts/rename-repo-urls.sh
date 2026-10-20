#!/usr/bin/env bash
# Run ONCE, right after renaming the GitHub repo from product-kit to makerline
# (GitHub → Settings → General → Repository name). It switches every link in the kit:
#   github.com/sairam5294/product-kit      → github.com/sairam5294/makerline
#   sairam5294.github.io/product-kit       → sairam5294.github.io/MakerLine
#   marketplace add sairam5294/product-kit → marketplace add sairam5294/makerline
#
# Why a script: before the rename these new links would 404, so they can't be changed early.
# GitHub redirects the old repo links after the rename, but the docs site's old address
# (…github.io/product-kit) does not redirect — so update the links, merge, and the site moves.
# History files (CHANGELOG, LESSONS, evals, examples) are left as they were written.
#
# Usage: scripts/rename-repo-urls.sh          (preview: lists files that would change)
#        scripts/rename-repo-urls.sh --apply  (makes the change; review with git diff)
set -euo pipefail
cd "$(dirname "$0")/.."

files=$(grep -rIl --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=_site \
  --exclude-dir=evals --exclude-dir=examples --exclude=CHANGELOG.md --exclude=LESSONS.md \
  --exclude=rename-repo-urls.sh -e 'sairam5294/product-kit' -e 'sairam5294.github.io/product-kit' . || true)

if [ -z "$files" ]; then echo "Nothing to change."; exit 0; fi
echo "$files"
[ "${1:-}" = "--apply" ] || { echo; echo "Preview only. Run again with --apply."; exit 0; }

for f in $files; do
  sed -i.bak -e 's#sairam5294\.github\.io/product-kit#sairam5294.github.io/MakerLine#g' \
             -e 's#sairam5294/product-kit#sairam5294/makerline#g' "$f" && rm -f "$f.bak"
done
git remote set-url origin "https://github.com/sairam5294/makerline.git" 2>/dev/null || true
echo "Done. Next: python3 scripts/sync.py && python3 scripts/build-idea-pack.py, run the tests, commit on a branch, open a PR."
