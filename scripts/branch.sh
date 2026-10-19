#!/usr/bin/env bash
# Creates a branch named by the project convention, dated today:
#   scripts/branch.sh fix "login focus ring"   →  fix/Oct-19-login-focus-ring
#
# Types (pick by the main purpose of the change):
#   feat      new page, section or feature          fix       something broken or wrong
#   content   copy, recommendations, case-study text design    visual or layout polish
#   security  headers, privacy, removing personal data
#   a11y      accessibility fixes                    docs      README, AGENTS.md, guides only
#   test      tests only                             ci        workflows, hooks, checks
#   deps      dependency updates                     refactor  same behaviour, cleaner code
#   perf      speed or size                          chore     housekeeping
#   skill     a kit skill, agent or standard          release   version bump
#   eval      eval cases and blind runs        exp       experiment/spike — never merged, expires in 14 days
set -euo pipefail
TYPE="${1:?Usage: scripts/branch.sh <type> \"<summary>\"   e.g. scripts/branch.sh fix \"login focus ring\"}"
SUMMARY="${2:?Give a short summary in plain words, e.g. \"login focus ring\"}"
HERE="$(cd "$(dirname "$0")" && pwd)"

# Lowercase, keep letters and digits, join with single hyphens, trim the ends.
slug="$(printf '%s' "$SUMMARY" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"
[ -n "$slug" ] || { echo "The summary needs at least one letter or digit."; exit 1; }
name="$TYPE/$(date +%b-%d)-$slug"

"$HERE/check-branch.sh" "$name" || exit 1
git checkout -b "$name"
echo "✔ On branch $name — when done: git push -u origin $name, then open a pull request."
