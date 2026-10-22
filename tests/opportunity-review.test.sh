#!/usr/bin/env bash
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

for stage in idea partial prelaunch delayed live; do
  project="$TMP/$stage"
  python3 "$KIT/scripts/opportunity_review.py" init "$project" --stage "$stage" --product "<Demo $stage>" --goal 'Improve the outcome' --market Ontario >/dev/null
  python3 "$KIT/scripts/opportunity_review.py" check "$project" >/dev/null
  report="$project/docs/product/opportunity/index.html"
  test -s "$report"
  grep -q 'Workflow and progress' "$report"
  grep -q '&lt;Demo' "$report"
  if grep -q '<Demo' "$report"; then echo "Unescaped product name: $stage"; exit 1; fi
  if python3 "$KIT/scripts/opportunity_review.py" init "$project" --stage "$stage" --product Again >/dev/null 2>&1; then
    echo "Existing review was overwritten: $stage"; exit 1
  fi
done

python3 - "$TMP/partial" <<'PY'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1]) / 'docs/product/opportunity/REVIEW.json'
d = json.loads(p.read_text())
d['steps'][0]['status'] = 'done'
d['steps'][0]['finding'] = 'The prototype works for one workflow.'
d['steps'][1]['status'] = 'in_progress'
d['decision_reason'] = '<script>alert(1)</script>'
d['sources'] = [{'id': 'S1', 'title': 'Pilot', 'url': 'https://example.com', 'date': '2026-10-22'}]
d['steps'][0]['source_ids'] = ['S1']
p.write_text(json.dumps(d))
PY
python3 "$KIT/scripts/opportunity_review.py" render "$TMP/partial" >/dev/null
grep -q '1/6 steps' "$TMP/partial/docs/product/opportunity/index.html"
if grep -q '<script>alert' "$TMP/partial/docs/product/opportunity/index.html"; then echo 'Unsafe HTML'; exit 1; fi

python3 - "$TMP/partial" <<'PY'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1]) / 'docs/product/opportunity/REVIEW.json'
d = json.loads(p.read_text()); d['steps'][0]['source_ids'] = ['MISSING']; p.write_text(json.dumps(d))
PY
if python3 "$KIT/scripts/opportunity_review.py" check "$TMP/partial" >/dev/null 2>&1; then
  echo 'Unknown source was accepted'; exit 1
fi
# The ChatGPT/Codex manifest (plugin/plugin.json) must carry the same version as the Claude one.
python3 - "$KIT" <<'PY'
import json, pathlib, sys
k = pathlib.Path(sys.argv[1])
a = json.loads((k / "plugin/.claude-plugin/plugin.json").read_text())["version"]
b = json.loads((k / "plugin/plugin.json").read_text())["version"]
sys.exit(0 if a == b else f"plugin/plugin.json version {b} != Claude manifest {a}")
PY
echo 'opportunity-review: five routes, no overwrite, safe rendering, progress, source and manifest-version checks passed'
