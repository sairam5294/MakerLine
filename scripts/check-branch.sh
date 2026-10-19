#!/usr/bin/env bash
# Checks that a branch name follows the project convention:
#   <type>/<Mon>-<DD>-<summary-in-kebab-case>      e.g. fix/Oct-19-login-focus-ring
#
# Why: branch names are the changelog you read on GitHub. A type, a date and a
# plain summary tell anyone (you, a contributor, an AI tool) what a branch is for
# without opening it.
#
# Usage: scripts/check-branch.sh [branch]   (default: the current branch)
# Exit 0 = ok. Exit 1 = wrong name (prints how to fix it).
# Exempt: main, HEAD (detached), and bot branches (dependabot/, renovate/).
set -u
BRANCH="${1:-$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo HEAD)}"

# Branch types, by the main purpose of the change. Keep this list short and in
# the same order as AGENTS.md "Branches" so the two never drift.
TYPES="feat|fix|content|design|security|a11y|docs|test|ci|deps|refactor|perf|chore|skill|release|eval"
MONTHS="Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"

case "$BRANCH" in
  main|master|HEAD|dependabot/*|renovate/*) exit 0 ;;
esac

if printf '%s' "$BRANCH" | grep -Eq "^($TYPES)/($MONTHS)-(0[1-9]|[12][0-9]|3[01])-[a-z0-9]+(-[a-z0-9]+)*$"; then
  exit 0
fi

cat >&2 <<EOF
Branch name "$BRANCH" doesn't follow the convention  <type>/<Mon>-<DD>-<summary>
  example:  fix/Oct-19-login-focus-ring
  types:    ${TYPES//|/ · }
  date:     today's month and day (Jan–Dec, two-digit day)
  summary:  3–6 plain words, lowercase, joined with hyphens

Create a correctly named branch with:   scripts/branch.sh <type> "<summary>"
Rename this one with:                   git branch -m "<type>/$(date +%b-%d)-<summary>"
EOF
exit 1
