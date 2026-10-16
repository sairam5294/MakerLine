#!/usr/bin/env bash
# Upgrade an existing project to the current Product Kit version.
#
#   ./scripts/upgrade-project.sh ~/Projects/my-app           → preview only (nothing changes)
#   ./scripts/upgrade-project.sh ~/Projects/my-app --apply   → apply the upgrade
#
# ADOPT MODE (automatic when the project has never seen the kit: no .product-kit-version and no
# docs/product/STATUS.md): nothing that already exists is overwritten — your CI, rules and scripts stay;
# only missing kit files are added, and docs/product/STATUS.md is created marked "APPROVED (adopted)"
# so the review, test and ship skills start from where a shipped project actually is.
#
# Two kinds of files:
#   KIT-OWNED  (skills, agents, rules, hooks, kit docs, kit scripts, CI) → replaced with the new version.
#              Old copies are saved in .product-kit-backup/<date>/ first.
#   YOURS      (AGENTS.md, CLAUDE.md, settings, MCP/permissions config, lefthook, .gitignore) → never
#              overwritten. The script shows what the new kit version changed so you (or an AI) can merge.
# Your code, docs/product/ and design/tokens.json are never touched.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?Usage: upgrade-project.sh <project-path> [--apply]}"
APPLY="${2:-}"
NEW="$(sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' "$KIT/plugin/.claude-plugin/plugin.json")"
OLD="$(cat "$DEST/.product-kit-version" 2>/dev/null || echo "unknown")"
T="$KIT/template"
ADOPT=0
[ "$OLD" = "unknown" ] && [ ! -f "$DEST/docs/product/STATUS.md" ] && ADOPT=1

python3 "$KIT/scripts/sync.py" >/dev/null   # make sure template/ is current

KIT_OWNED=(.agents/skills .cursor/agents .cursor/rules .codex/agents .claude/hooks docs/kit
           scripts/check-gate.sh scripts/approve.sh scripts/worktree.sh scripts/setup-github.sh scripts/local-ai.sh
           .github/workflows/ci.yml .github/workflows/ai-review.yml .github/pull_request_template.md .github/dependabot.yml)
YOURS=(AGENTS.md CLAUDE.md .claude/settings.json .codex/config.toml .cursor/permissions.json .cursor/mcp.json
       .mcp.json lefthook.yml .gitignore .cursorignore)

echo "Product Kit upgrade: $OLD → $NEW  ($DEST)"
[ "$ADOPT" = 1 ] && echo "Adopt mode: this project was not created by the kit. Existing files are kept; only missing kit files are added."
[ "$APPLY" = "--apply" ] || echo "(preview — run again with --apply to make changes)"

# Warn if the project has uncommitted changes: commit first so the upgrade is easy to review/undo.
if git -C "$DEST" rev-parse >/dev/null 2>&1 && [ -n "$(git -C "$DEST" status --porcelain)" ]; then
  echo "⚠️  Uncommitted changes in the project. Commit them first so you can review/undo the upgrade."
fi

backup="$DEST/.product-kit-backup/$(date +%Y-%m-%d-%H%M)"
added=(); kept=()
KEEP="$DEST/.product-kit-keep"   # paths an adopted project owns; later upgrades never replace them
if [ "$ADOPT" = 1 ]; then
  echo; echo "KIT FILES (added only where missing — yours are kept):"
  for p in "${KIT_OWNED[@]}"; do
    [ -e "$T/$p" ] || continue
    if [ -d "$T/$p" ]; then
      # Directory: add files that don't exist yet, never replace one that does.
      while IFS= read -r rel; do
        if [ -e "$DEST/$p/$rel" ]; then
          diff -q "$T/$p/$rel" "$DEST/$p/$rel" >/dev/null 2>&1 || { echo "  • $p/$rel  kept yours  (kit version: template/$p/$rel)"; kept+=("$p/$rel"); }
        else
          echo "  • $p/$rel  added"
          [ "$APPLY" = "--apply" ] && { mkdir -p "$DEST/$p/$(dirname "$rel")"; cp "$T/$p/$rel" "$DEST/$p/$rel"; added+=("$p/$rel"); }
        fi
      done < <(cd "$T/$p" && find . -type f | sed 's|^\./||' | sort)
    elif [ -e "$DEST/$p" ]; then
      diff -q "$T/$p" "$DEST/$p" >/dev/null 2>&1 || { echo "  • $p  kept yours  (kit version: template/$p)"; kept+=("$p"); }
    else
      echo "  • $p  added"
      [ "$APPLY" = "--apply" ] && { mkdir -p "$DEST/$(dirname "$p")"; cp "$T/$p" "$DEST/$p"; added+=("$p"); }
    fi
  done
else
  echo; echo "KIT-OWNED (replaced):"
  for p in "${KIT_OWNED[@]}"; do
    [ -e "$T/$p" ] || continue
    if [ -f "$KEEP" ] && grep -qxF "$p" "$KEEP"; then echo "  • $p  kept yours (listed in .product-kit-keep)"; continue; fi
    if [ -e "$DEST/$p" ] && diff -rq "$T/$p" "$DEST/$p" >/dev/null 2>&1; then continue; fi  # already current
    echo "  • $p"
    if [ "$APPLY" = "--apply" ]; then
      if [ -e "$DEST/$p" ]; then mkdir -p "$backup/$(dirname "$p")"; cp -R "$DEST/$p" "$backup/$p"; fi
      mkdir -p "$DEST/$(dirname "$p")"
      if [ -d "$T/$p" ]; then
        mkdir -p "$DEST/$p"
        while IFS= read -r rel; do
          if [ -f "$KEEP" ] && grep -qxF "$p/$rel" "$KEEP"; then continue; fi
          mkdir -p "$DEST/$p/$(dirname "$rel")"; cp "$T/$p/$rel" "$DEST/$p/$rel"
        done < <(cd "$T/$p" && find . -type f | sed 's|^\./||')
      else cp "$T/$p" "$DEST/$p"; fi
    fi
  done
fi

echo; echo "YOURS (not changed — review these differences and merge what you want):"
for p in "${YOURS[@]}"; do
  [ -e "$T/$p" ] || continue
  if [ ! -e "$DEST/$p" ]; then
    echo "  • $p is new in this kit version"
    [ "$APPLY" = "--apply" ] && { mkdir -p "$DEST/$(dirname "$p")"; cp "$T/$p" "$DEST/$p"; added+=("$p"); echo "    → added"; }
  elif ! diff -q "$T/$p" "$DEST/$p" >/dev/null; then
    echo "  • $p differs:  diff \"$T/$p\" \"$DEST/$p\""
  fi
done

# Adopt mode: the project shipped (or at least was built) before the kit, so record that honestly.
if [ "$ADOPT" = 1 ]; then
  echo; echo "PROJECT DOCS (adopt mode):"
  today="$(date +%Y-%m-%d)"
  name="$(basename "$DEST")"
  echo "  • docs/product/STATUS.md  created: Evaluation: APPROVED (adopted $today), phases 1–9 marked done before the kit"
  echo "  • docs/product/DECISIONS.md, COSTS.md, OWNER.md  added if missing"
  if [ "$APPLY" = "--apply" ]; then
    mkdir -p "$DEST/docs/product"
    tpl="$KIT/plugin/skills/product-kickoff/templates"
    sed -e "s/<product>/$name/" -e "s/<YYYY-MM-DD>/$today/" -e "s/<version>/$NEW/" \
        -e "s/^Evaluation: PENDING.*/Evaluation: APPROVED ($today — adopted: built and shipped before the kit; discovery\/evaluation not run)/" \
        -e "s/^| \([1-9][ab]*\) | \(.*\) | Not started | | \(.*\)|$/| \1 | \2 | Done (before kit) | $today | \3|/" \
        "$tpl/STATUS.md" > "$DEST/docs/product/STATUS.md"
    [ -f "$DEST/docs/product/DECISIONS.md" ] || cp "$tpl/DECISIONS.md" "$DEST/docs/product/DECISIONS.md"
    printf '| %s | Adopted into Product Kit %s: existing code, CI and rules kept; kit skills, agents and hooks added | — | Owner decision | — |\n' "$today" "$NEW" >> "$DEST/docs/product/DECISIONS.md"
    [ -f "$DEST/docs/product/COSTS.md" ] || cp "$tpl/COSTS.md" "$DEST/docs/product/COSTS.md"
    if [ ! -f "$DEST/docs/product/OWNER.md" ]; then
      if [ -f "$KIT/owner/OWNER.md" ]; then cp "$KIT/owner/OWNER.md" "$DEST/docs/product/OWNER.md"; else cp "$KIT/owner/OWNER.example.md" "$DEST/docs/product/OWNER.md"; fi
    fi
  fi
  echo; echo "THINGS TO KNOW:"
  [ -f "$DEST/.pre-commit-config.yaml" ] || [ -d "$DEST/.husky" ] && echo "  ⚠️  This project already has a git-hook manager (pre-commit/husky). 'lefthook install' would take over .git/hooks — keep one, or add scripts/check-gate.sh to the existing one."
  [ -f "$DEST/package.json" ] || echo "  ℹ  Not a Node project: the kit's lefthook.yml runs scripts/check.sh if you add one (or pytest when present); its template CI is Node-specific, so your own CI stays in charge."
fi

if [ "$APPLY" = "--apply" ]; then
  # Anything the kit added that git will silently ignore is worth knowing about.
  if git -C "$DEST" rev-parse >/dev/null 2>&1 && [ "${#added[@]}" -gt 0 ]; then
    ignored="$(cd "$DEST" && git check-ignore "${added[@]}" 2>/dev/null || true)"
    [ -z "$ignored" ] || { echo; echo "  ⚠️  git-ignored by this project's .gitignore (add exceptions if you want them committed):"; printf '     %s\n' $ignored; }
  fi
  if [ "$ADOPT" = 1 ] && [ "${#kept[@]}" -gt 0 ]; then
    printf '%s\n' "${kept[@]}" > "$KEEP"
    echo; echo "  ℹ  Kept files are listed in .product-kit-keep; future upgrades leave them alone (delete a line to let the kit manage that file)."
  fi
  chmod +x "$DEST"/.claude/hooks/*.sh "$DEST"/scripts/*.sh 2>/dev/null || true
  echo "$NEW" > "$DEST/.product-kit-version"
  grep -q "^.product-kit-backup/" "$DEST/.gitignore" 2>/dev/null || echo ".product-kit-backup/" >> "$DEST/.gitignore"
  grep -q "^docs/product/OWNER.md" "$DEST/.gitignore" 2>/dev/null || printf '# Your personal profile — copied in by the kit, never committed\ndocs/product/OWNER.md\n' >> "$DEST/.gitignore"
  # Refresh the profile from the kit (it is git-ignored in projects, so this is the only way it travels).
  [ -f "$KIT/owner/OWNER.md" ] && cp "$KIT/owner/OWNER.md" "$DEST/docs/product/OWNER.md" 2>/dev/null || true
  echo; echo "✅ Upgraded to $NEW. Backups: ${backup#$DEST/}. Tip: ask your AI tool"
  echo "   \"merge the Product Kit template changes into AGENTS.md/CLAUDE.md (see upgrade output)\"."
fi
