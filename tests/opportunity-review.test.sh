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
grep -q '1/7 steps' "$TMP/partial/docs/product/opportunity/index.html"
if grep -q '<script>alert' "$TMP/partial/docs/product/opportunity/index.html"; then echo 'Unsafe HTML'; exit 1; fi

python3 - "$TMP/partial" <<'PY'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1]) / 'docs/product/opportunity/REVIEW.json'
d = json.loads(p.read_text()); d['steps'][0]['source_ids'] = ['MISSING']; p.write_text(json.dumps(d))
PY
if python3 "$KIT/scripts/opportunity_review.py" check "$TMP/partial" >/dev/null 2>&1; then
  echo 'Unknown source was accepted'; exit 1
fi
# Pilot fixes (22 Oct 2026): every route checks launch-market rules; stricter records; tidy rendering.
for stage in idea partial prelaunch delayed live; do
  grep -q '"id": "access"' "$TMP/$stage/docs/product/opportunity/REVIEW.json" || { echo "No access step: $stage"; exit 1; }
done
grep -q '"id": "decision"' "$TMP/live/docs/product/opportunity/REVIEW.json" || { echo 'Live route has no decision step'; exit 1; }
cp "$TMP/live/docs/product/opportunity/REVIEW.json" "$TMP/live.json"
edit_review() {  # $1 = project, $2 = python statements that change d
  python3 -c '
import json, pathlib, sys
p = pathlib.Path(sys.argv[1]) / "docs/product/opportunity/REVIEW.json"
d = json.loads(p.read_text()); exec(sys.argv[2]); p.write_text(json.dumps(d))
' "$1" "$2"
}
expect_fail() {  # $1 = description, $2 = python that edits d
  edit_review "$TMP/live" "$2"
  if python3 "$KIT/scripts/opportunity_review.py" check "$TMP/live" >/dev/null 2>&1; then echo "Accepted: $1"; exit 1; fi
  cp "$TMP/live.json" "$TMP/live/docs/product/opportunity/REVIEW.json"
}
expect_fail 'unknown option type' "d['options']=[{'name':'X','type':'magic','value_range':'v','effort_range':'e','evidence':'some','test':'t'}]"
expect_fail 'unknown evidence level' "d['options']=[{'name':'X','type':'fix','value_range':'v','effort_range':'e','evidence':'lots','test':'t'}]"
expect_fail 'action without owner' "d['next_actions']=[{'action':'Ship','success_measure':'5 users'}]"
expect_fail 'rule with bad applies' "d['rules']=[{'market':'EU','rule':'EAA','applies':'maybe'}]"
expect_fail 'bad source date' "d['sources']=[{'id':'S1','title':'T','date':'22 Oct'}]"
expect_fail 'finished but pending' "[s.update(status='done', finding='ok') for s in d['steps']]"
edit_review "$TMP/live" "d.update(decision='Test before investing.', markets_status='confirmed', launch_markets=['India'], sources=[{'id':'S1','title':'RPwD rules','url':'https://example.com','date':'2026-10-22','kind':'official'}], rules=[{'market':'India','rule':'RPwD Act','applies':'likely','uncertainty':'draft rules','source_ids':['S1']}])"
python3 "$KIT/scripts/opportunity_review.py" render "$TMP/live" >/dev/null 2>&1
html="$TMP/live/docs/product/opportunity/index.html"
if grep -q 'investing\.\.' "$html"; then echo 'Doubled full stop'; exit 1; fi
grep -q 'Launch-market rules <span class="ml-count">1</span>' "$html" && grep -q 'RPwD Act' "$html" && grep -q '>official<' "$html" || { echo 'Rules or source kind missing'; exit 1; }
if grep -q 'owner to confirm' "$html"; then echo 'Confirmed markets shown as proposed'; exit 1; fi
edit_review "$TMP/live" "d['areas']=[{'name':'Customer app','status':'not started','owner':'[Eng]','note':'R3'}]"
python3 "$KIT/scripts/opportunity_review.py" render "$TMP/live" >/dev/null 2>&1
grep -q 'Where each part stands' "$TMP/live/docs/product/opportunity/index.html" || { echo 'Areas table missing'; exit 1; }
expect_fail 'area without status' "d['areas']=[{'name':'Admin'}]"
expect_fail 'overview audience without who' "d['overview']={'what':'x','audience':[{'how':'y'}]}"
expect_fail 'overview text not text' "d['overview']={'what':['x']}"
grep -q '"overview"' "$TMP/idea/docs/product/opportunity/REVIEW.json" || { echo 'init has no overview'; exit 1; }
# The ChatGPT/Codex manifest (plugin/plugin.json) must carry the same version as the Claude one.
python3 - "$KIT" <<'PY'
import json, pathlib, sys
k = pathlib.Path(sys.argv[1])
a = json.loads((k / "plugin/.claude-plugin/plugin.json").read_text())["version"]
b = json.loads((k / "plugin/plugin.json").read_text())["version"]
sys.exit(0 if a == b else f"plugin/plugin.json version {b} != Claude manifest {a}")
PY
# Infographic report (23 Oct 2026): the shared review styles match the kit UI, and the body the kit UI embeds
# stays inside its strict Content-Security-Policy (no inline style or script; SVG attributes are fine).
python3 - "$KIT" "$TMP/live" <<'PY'
import importlib.util, pathlib, re, sys
k, project = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
def block(path):
    css = path.read_text(encoding="utf-8")
    return css[css.index("/* review:start"):css.index("/* review:end */")]
if block(k / "plugin/skills/product-opportunity-review/assets/report.css") != block(k / "kit-ui/app.css"):
    sys.exit("review:start…review:end differs between report.css and kit-ui/app.css")
assets = k / "plugin/skills/product-opportunity-review/assets"
def part(path, start, end):
    t = path.read_text(encoding="utf-8")
    return t[t.index(start):t.index(end)]
if part(assets / "ui.css", "/* ml-ui:start", "/* ml-ui:end */") != part(k / "kit-ui/app.css", "/* ml-ui:start", "/* ml-ui:end */"):
    sys.exit("ml-ui block differs between assets/ui.css and kit-ui/app.css")
js = (assets / "ui.js").read_text(encoding="utf-8")
if js not in (k / "kit-ui/app.js").read_text(encoding="utf-8"):
    sys.exit("kit-ui/app.js doesn't carry the same assets/ui.js")
spec = importlib.util.spec_from_file_location("r", k / "plugin/skills/product-opportunity-review/scripts/opportunity_review.py")
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
body = r.render_body(r.read_review(project))
if re.search(r"<script|\sstyle=|\son[a-z]+=", body):
    sys.exit("review body has inline script, style or event handler (blocked by the kit UI's CSP)")
for needle in ("ml-hero", "Current recommendation", "ml-ring", "ml-route", "review-nav", "Product at a glance", "Who it helps, and how", 'class="ml-acc"', 'data-acc="open"', 'id="step-'):
    if needle not in body:
        sys.exit(f"review body is missing {needle}")
PY
html="$TMP/live/docs/product/opportunity/index.html"
grep -q 'Evidence mix · 1 source' "$html" || { echo 'Evidence mix bar missing'; exit 1; }
grep -q 'Confidence: <strong>unknown</strong>' "$html" || { echo 'Confidence meter missing'; exit 1; }
if grep -Eq '(src|href)="https?://[^"]*\.(css|js)' "$html"; then echo 'Report loads a CDN file'; exit 1; fi
grep -q 'window.mlUI' "$html" && grep -q 'ml-drawer' "$html" || { echo 'Shared table/accordion UI not bundled'; exit 1; }
echo 'opportunity-review: five routes with access checks, strict records, rules table, no overwrite, safe rendering, progress, source, manifest-version, shared-style and CSP checks passed'
