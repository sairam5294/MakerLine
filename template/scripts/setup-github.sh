#!/usr/bin/env bash
# One-time GitHub setup for a Product Kit project (or the kit itself).
#   1. creates a PRIVATE GitHub repo from this folder and pushes it
#   2. protects `main`: changes must come through a pull request with green CI
#
# Needs the GitHub CLI:  brew install gh && gh auth login
# Usage (inside the project folder):  scripts/setup-github.sh [repo-name] [--public]
#
# Note: GitHub only allows branch protection on PRIVATE repos with a paid plan (Pro/Team).
# On GitHub Free the script still works; it tells you, and the local pre-push hook
# (lefthook: "no-push-to-main") remains your guard.
set -euo pipefail

command -v gh >/dev/null || { echo "Install the GitHub CLI first: brew install gh && gh auth login"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "Log in first: gh auth login"; exit 1; }

name="${1:-$(basename "$PWD")}"
visibility="--private"
[ "${2:-}" = "--public" ] && visibility="--public"

# 1. Create the repo (skip if this folder already has a GitHub remote).
if ! git remote get-url origin >/dev/null 2>&1; then
  git branch -M main
  gh repo create "$name" "$visibility" --source=. --remote=origin
fi
# --no-verify: this first push of main is intentional (the pre-push hook blocks later ones).
git push --no-verify -u origin main
repo="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
echo "✅ Repo: https://github.com/$repo"

# 2. Protect main. Check names = the `name:` of each job in .github/workflows/*.yml.
checks="${REQUIRED_CHECKS:-\"Approval gate\", \"Secret scan\", \"Typecheck · lint · tests\"}"
protection='{
  "required_status_checks": { "strict": true, "contexts": ['"$checks"'] },
  "enforce_admins": true,
  "required_pull_request_reviews": { "required_approving_review_count": 0 },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_linear_history": true
}'
if echo "$protection" | gh api -X PUT "repos/$repo/branches/main/protection" --input - >/dev/null 2>&1; then
  echo "✅ main is protected for everyone, including you and your AI tools: pull request + green CI required, no force-push, no deletion."
else
  echo "⚠️  Couldn't protect main (GitHub Free doesn't allow it on private repos)."
  echo "    Options: GitHub Pro (about US\$4/month), or rely on the local pre-push hook: npx lefthook install"
fi

# 3. Turn on free security features where available.
gh api -X PUT "repos/$repo/vulnerability-alerts" >/dev/null 2>&1 && echo "✅ Dependabot alerts on" || true
gh api -X PUT "repos/$repo/automated-security-fixes" >/dev/null 2>&1 && echo "✅ Dependabot security fixes on" || true

echo "Next: open a branch, push it, and create a pull request — CI will run on it."
