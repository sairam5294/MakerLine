#!/usr/bin/env bash
# Everything CI checks, in one command (MakerLine's pre-push hook and AI tools run this).
#   scripts/check.sh         → lint, format check, types, token drift, contrast, tests
#   scripts/check.sh --fix   → apply ruff fixes + formatting first
# On Linux the AppKit UI tests are skipped; on a Mac they run.
set -euo pipefail
cd "$(dirname "$0")/.."
if [ "${1:-}" = "--fix" ]; then python3 -m ruff check --fix . && python3 -m ruff format .; fi
python3 -m ruff check .
python3 -m ruff format --check .
python3 -m mypy .
python3 scripts/build_tokens.py --check
python3 scripts/check_contrast.py
python3 -m pytest -q
