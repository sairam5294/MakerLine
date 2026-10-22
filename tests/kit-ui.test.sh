#!/usr/bin/env bash
# kit-ui must serve its pages, refuse paths outside --projects, escape file content,
# and listen on 127.0.0.1 only.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
PID=""
cleanup() { [ -n "$PID" ] && kill "$PID" 2>/dev/null; wait "$PID" 2>/dev/null || true; rm -rf "$TMP"; }
trap cleanup EXIT

# Sample project: Idea Pack waiting for approval, plus a doc with hostile HTML and a secret outside.
P="$TMP/projects/sample-app"
mkdir -p "$P/docs/product"
cat > "$P/docs/product/STATUS.md" <<'EOF'
# Status — Sample App  ·  updated 2026-10-19  ·  kit v0.11

Evaluation: PENDING   <!-- owner only -->

| # | Phase | Status | Date | Notes |
|---|---|---|---|---|
| 1 | Discovery | Done | 2026-10-18 | |
| 2 | Evaluation | Waiting for owner | 2026-10-19 | verdict Go |
| 2a | Design direction | Done | 2026-10-19 | |
| 2b | PRD draft | Done | 2026-10-19 | |
| 3 | Validation | Skipped | | quick look |
| ✦ | Idea Pack | Waiting for owner | 2026-10-19 | |
| 4 | Naming | Not started | | |
| 13 | Post-launch | Not started | | |

Next step: owner reads ONE_PAGER.md
Blockers:
EOF
printf '# One pager\n\n<script>alert(1)</script>\n\n[bad](javascript:alert(1)) [ok](STATUS.md)\n' > "$P/docs/product/ONE_PAGER.md"
python3 "$KIT/scripts/opportunity_review.py" init "$P" --stage partial --product 'Sample App' --goal 'Decide whether to finish' >/dev/null
python3 - "$P" <<'PY'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1]) / 'docs/product/opportunity/REVIEW.json'
d = json.loads(p.read_text()); d['decision_reason'] = '<script>alert(1)</script>'
p.write_text(json.dumps(d))
PY
echo "TOP-SECRET" > "$TMP/secret.md"

PORT=$(python3 -c 'import socket; s=socket.socket(); s.bind(("127.0.0.1",0)); print(s.getsockname()[1]); s.close()')
python3 "$KIT/scripts/kit-ui.py" --projects "$TMP/projects" --port "$PORT" 2>"$TMP/server.log" &
PID=$!
B="http://127.0.0.1:$PORT"
for _ in $(seq 1 50); do curl -s -o /dev/null "$B/" && break; sleep 0.1; done

pass=0; fail=0
check() { if eval "$2"; then pass=$((pass+1)); else fail=$((fail+1)); echo "✗ $1"; fi; }
code() { curl -s -o /dev/null -w '%{http_code}' "$@"; }
# Fetch first, then grep: `curl | grep -q` is flaky under pipefail (grep exits early, curl gets SIGPIPE).
has() { local body; body="$(curl -s "${@:2}")"; grep -q -- "$1" <<<"$body"; }

check "projects page 200"                  '[ "$(code "$B/")" = 200 ]'
check "projects page lists the sample"     'has "Sample App" "$B/"'
check "project page 200"                   '[ "$(code "$B/project?id=sample-app")" = 200 ]'
check "project links opportunity review"  'has "Open the interactive review" "$B/project?id=sample-app"'
check "opportunity page 200"               '[ "$(code "$B/opportunity?id=sample-app")" = 200 ]'
check "opportunity shows progress"         'has "0/7 steps" "$B/opportunity?id=sample-app"'
check "opportunity escapes HTML"           '! has "<script>alert" "$B/opportunity?id=sample-app"'
check "approval is the next move"          'has "scripts/approve.sh" "$B/project?id=sample-app"'
check "timeline shows lettered phases"     'has "Design direction" "$B/project?id=sample-app"'
check "doc page 200"                       '[ "$(code "$B/doc?id=sample-app&file=docs/product/ONE_PAGER.md")" = 200 ]'
check "doc HTML is escaped"                '! has "<script>alert" "$B/doc?id=sample-app&file=docs/product/ONE_PAGER.md"'
check "javascript: links not linked"       '! has "href=\"javascript" "$B/doc?id=sample-app&file=docs/product/ONE_PAGER.md"'
check "new idea page 200"                  '[ "$(code "$B/new")" = 200 ]'
check "skills page 200"                    '[ "$(code "$B/skills")" = 200 ]'
check "skills lists start"                 'has "/makerline:start" "$B/skills"'
check "css served"                         '[ "$(code "$B/app.css")" = 200 ]'
check "CSP header set"                     'has "Content-Security-Policy: default-src" -I "$B/"'
check "unknown page 404"                   '[ "$(code "$B/nope")" = 404 ]'

refused() { c="$(code "$@")"; [ "$c" = 403 ] || [ "$c" = 404 ]; }
check "doc traversal refused"              'refused "$B/doc?id=sample-app&file=../../../secret.md"'
check "encoded traversal refused"          'refused "$B/doc?id=sample-app&file=..%2F..%2F..%2Fsecret.md"'
check "project traversal refused"          'refused "$B/project?id=../"'
check "opportunity traversal refused"      'refused "$B/opportunity?id=../"'
check "absolute path refused"              'refused "$B/doc?id=sample-app&file=$TMP/secret.md"'
check "non-markdown refused"               'refused "$B/doc?id=sample-app&file=../../../../etc/passwd"'
check "secret never leaks"                 '! has TOP-SECRET "$B/doc?id=sample-app&file=../../../secret.md"'
check "foreign Host header refused"        '[ "$(code -H "Host: evil.example" "$B/")" = 403 ]'

# New idea form: needs the per-run token; with it, the prompt comes back and nothing is written.
NEWPAGE="$(curl -s "$B/new")"
TOKEN="$(sed -n 's/.*name="token" value="\([^"]*\)".*/\1/p' <<<"$NEWPAGE")"
check "form without token refused"         '[ "$(code -d "pitch=An app for plant swaps" "$B/new")" = 403 ]'
check "form makes a prompt"                'has "give me everything (quick)" -d "token=$TOKEN&pitch=An+app+for+plant+swaps&depth=quick" "$B/new"'
check "form wrote nothing by default"      '[ "$(find "$TMP/projects" -name PITCH.md | wc -l)" -eq 0 ]'
check "empty pitch shows error summary"   'has "id=\"error-summary\"" -d "token=$TOKEN&pitch=" "$B/new"'
check "error page title starts Error:"    'has "<title>Error: New idea" -d "token=$TOKEN&pitch=" "$B/new"'
check "error summary not role=alert"      '! has "role=\"alert\"" -d "token=$TOKEN&pitch=" "$B/new"'
check "pitch marked required"             'has "aria-required=\"true\"" "$B/new"'
check "save rejects traversal folder"      '[ "$(code -d "token=$TOKEN&pitch=An+app+for+plant+swaps&save=yes&folder=../evil" "$B/new")" = 400 ] && [ ! -e "$TMP/evil" ]'
check "save writes PITCH.md when ticked"   '[ "$(code -d "token=$TOKEN&pitch=An+app+for+plant+swaps&save=yes&folder=plant-swap" "$B/new")" = 200 ] && [ -f "$TMP/projects/plant-swap/docs/product/PITCH.md" ]'
check "save never overwrites"              '[ "$(code -d "token=$TOKEN&pitch=Another+idea+entirely&save=yes&folder=plant-swap" "$B/new")" = 400 ]'

# Listening address: must be 127.0.0.1, never 0.0.0.0 / all interfaces.
listen_lines() {
  if command -v lsof >/dev/null; then lsof -nP -a -p "$PID" -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null | tail -n +2
  else
    hex=$(printf '%04X' "$PORT")
    awk -v h=":$hex" '$2 ~ h"$" && $4=="0A" {print $2}' /proc/net/tcp /proc/net/tcp6 2>/dev/null
  fi
}
L="$(listen_lines)"
check "server is listening"                '[ -n "$L" ]'
check "bound to 127.0.0.1"                 'grep -Eq "127\.0\.0\.1:$PORT|0100007F:" <<<"$L"'
check "not bound to 0.0.0.0 or *"          '! grep -Eq "(0\.0\.0\.0|\*|\[::\]):$PORT|00000000:" <<<"$L"'
OTHER_IP="$(hostname -I 2>/dev/null | awk '{print $1}' || true)"
if [ -n "$OTHER_IP" ] && [ "$OTHER_IP" != "127.0.0.1" ]; then
  check "unreachable on $OTHER_IP"         '! curl -s -m 2 -o /dev/null "http://$OTHER_IP:$PORT/"'
fi

# Browsers send the page's real Origin on form posts only if the referrer policy allows it ("no-referrer"
# makes Chrome send "Origin: null" and every save is refused). Keep it same-origin.
HDRS="$(curl -s -D - -o /dev/null "$B/new")"
check "referrer policy lets the browser send its origin" 'grep -qi "^referrer-policy: same-origin" <<<"$HDRS"'
TOKEN="$(grep -o 'name="token" value="[^"]*"' <<<"$NEWPAGE" | sed 's/.*value="//; s/"$//')"
check "a same-origin form post is accepted" '[ "$(code -X POST -H "Origin: $B" --data-urlencode "token=$TOKEN" --data-urlencode "pitch=A booking app" --data-urlencode depth=quick "$B/new")" = 200 ]'
echo "kit-ui: $pass passed, $fail failed"
[ "$fail" -eq 0 ]
