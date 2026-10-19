#!/usr/bin/env bash
# Delete remote branches that are fully merged into main — after saving a copy.
#
# Why a copy first: deleting a branch on GitHub is hard to undo. The bundle file
# keeps every deleted branch so you can restore one with:
#   git fetch <bundle-file> 'refs/heads/*:refs/heads/restored/*'
#
# Usage: scripts/cleanup-branches.sh [archive-folder]   (default: ../Archive/git-branches)
# Tip: GitHub → Settings → General → "Automatically delete head branches" does this on every merge.
set -euo pipefail

archive="${1:-../Archive/git-branches}"
git fetch --prune origin

merged=()
for ref in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin); do
  name="${ref#origin/}"
  [[ "$name" == "main" || "$name" == "HEAD" || "$name" == "origin" ]] && continue
  if git merge-base --is-ancestor "$ref" origin/main; then merged+=("$name"); fi
done

if [[ ${#merged[@]} -eq 0 ]]; then echo "Nothing to clean: no merged branches."; exit 0; fi

echo "Merged into main (safe to delete):"; printf '  %s\n' "${merged[@]}"

mkdir -p "$archive"
bundle="$archive/merged-branches-$(date +%Y-%m-%d).bundle"
refs=(); for n in "${merged[@]}"; do refs+=("refs/remotes/origin/$n"); done
git bundle create "$bundle" "${refs[@]}" >/dev/null 2>&1
echo "Saved a copy: $bundle"

read -r -p "Delete these ${#merged[@]} branches on GitHub? [y/N] " ok
[[ "$ok" == "y" || "$ok" == "Y" ]] || { echo "Stopped. Nothing deleted."; exit 0; }
git push origin --delete "${merged[@]}"
echo "Done."
