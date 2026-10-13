#!/usr/bin/env bash
# Free, private helpers using a local model (Ollama) on your Mac. Nothing leaves your computer.
# Quality is lower than Claude/Cursor/Codex — use for drafts, then review.
#
#   scripts/local-ai.sh summarise docs/research/interview-3.md   → themes, pains, quotes
#   scripts/local-ai.sh translate te src/i18n/en.ts              → Telugu draft for a native speaker to fix
#   scripts/local-ai.sh ask "Explain this error" < error.log
#
# Model: set LOCAL_MODEL (default: first model from `ollama list`).
set -euo pipefail
command -v ollama >/dev/null || { echo "Install Ollama first: https://ollama.com"; exit 1; }
MODEL="${LOCAL_MODEL:-$(ollama list | awk 'NR==2{print $1}')}"
[ -n "$MODEL" ] || { echo "No local model found. Try: ollama pull llama3.2"; exit 1; }

case "${1:-}" in
  summarise|summarize)
    file="${2:?file to summarise}"
    ollama run "$MODEL" "Summarise these user interview notes for a product designer. Output: 1) top themes with how many mentions, 2) pains in the user's own words (quotes), 3) current workarounds, 4) surprises. Do not invent anything not in the notes.

$(cat "$file")" ;;
  translate)
    lang="${2:?language code, e.g. te or hi}"; file="${3:?file}"
    ollama run "$MODEL" "Translate only the user-facing string values in this file into language code '$lang'. Keep keys, code, and {{placeholders}} exactly. Mark the output as a DRAFT for native-speaker review.

$(cat "$file")" ;;
  ask)
    ollama run "$MODEL" "${2:?question}

$(cat)" ;;
  *) sed -n '2,10p' "$0"; exit 1 ;;
esac
