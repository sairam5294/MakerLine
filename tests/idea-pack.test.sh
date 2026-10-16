#!/usr/bin/env bash
# Tests for plugin/skills/product-kickoff/scripts/check_idea_pack.py.
# Builds a tiny passing Idea Pack, then breaks it one way at a time and
# checks the script catches each problem.
set -u
CHECK="$(cd "$(dirname "$0")/.." && pwd)/plugin/skills/product-kickoff/scripts/check_idea_pack.py"
T="$(mktemp -d)"; trap 'rm -rf "$T"' EXIT
pass=0; fail=0
ok()  { pass=$((pass+1)); }
bad() { fail=$((fail+1)); echo "✗ $1"; }

mk_pack() {
  rm -rf "$T/p"; mkdir -p "$T/p/docs/product" "$T/p/design/wireframes"; local d="$T/p/docs/product"
  printf '# Brief\nA brief.\n' > "$d/PROJECT_BRIEF.md"
  printf '# Clarity\n**Readiness:** Evaluation can start\n| ID | Q | Why | Blocks | Type | How | Owner | Default |\n|---|---|---|---|---|---|---|---|\n| Q-01 | Goal? | x | Approval | Decision | ask | Owner | Side income |\n| Q-02 | Volume? | x | Approval | Fact | ask | Owner | None, must be found out |\n' > "$d/CLARITY.md"
  { echo '# Evaluation'; echo '| Dim | Score | Why | Raise it by… |'; echo '## 2. The strongest version'; echo '## 3. Reality check'; echo '## 8. Path to Go'; echo '## 9. Accessibility, inclusion and compliance'; for i in $(seq 1 120); do echo "Plain sentence number $i about the idea and its users today."; done; } > "$d/EVALUATION.md"
  printf '# Competitors\nDoing nothing.\n## Differentiator test\n' > "$d/COMPETITORS.md"
  printf '# One-pager\nShort.\n' > "$d/ONE_PAGER.md"
  printf '# Index\n[One-pager](ONE_PAGER.md) · [web](https://example.com)\n' > "$d/README.md"
  printf '# Design direction\nPrinciples. Accessibility plan.\n| Text | #1F2A37 | #FFFFFF | 14.54:1 |\nContrast checked.\n' > "$d/DESIGN_DIRECTION.md"
  { echo '# PRD'; echo 'Accessibility statement and feedback route.'; for i in 1 2 3 4 5 6; do echo "- Given a $i, when x, then y"; done; } > "$d/PRD.md"
  cat > "$T/p/design/wireframes/index.html" <<'HTML'
<!doctype html><html lang="en"><body>
<section class="screen" id="s-home"><nav aria-label="Main 1"><a href="#s-home-empty">Empty</a></nav>
<label for="f1">Name</label><input id="f1"><div role="alert">Couldn't save. Try again.</div></section>
<section class="screen" id="s-home-empty"><nav aria-label="Main 2"><a href="#s-home">Home</a></nav><button>Add</button></section>
</body></html>
HTML
}
run() { python3 "$CHECK" "$T/p" --mode standard > "$T/out" 2>&1; echo $?; }

mk_pack; [ "$(run)" = 0 ] && ok || { bad "clean pack should pass"; cat "$T/out"; }

expect_fail() { # $1 = name, $2 = grep pattern for the message
  if [ "$(run)" = 1 ] && grep -q "$2" "$T/out"; then ok; else bad "$1"; cat "$T/out"; fi
}
mk_pack; echo 'Hello {{name}}' >> "$T/p/docs/product/PRD.md";            expect_fail "placeholder in doc" "unfilled"
mk_pack; sed -i 's/14.54:1/9.1:1/' "$T/p/docs/product/DESIGN_DIRECTION.md"; expect_fail "wrong contrast claim" "stated 9.1:1"
mk_pack; echo 'Navy #4338CA on white (12:1)' >> "$T/p/docs/product/DESIGN_DIRECTION.md"; expect_fail "wrong prose contrast" "stated 12.0:1"
mk_pack; echo '[V](VALIDATION.md)' >> "$T/p/docs/product/README.md";      expect_fail "broken link" "broken link"
mk_pack; rm "$T/p/docs/product/PRD.md";                                  expect_fail "missing PRD" "missing docs/product/PRD.md"
mk_pack; sed -i 's/Accessibility statement/Statement/' "$T/p/docs/product/PRD.md"; expect_fail "no accessibility statement" "accessibility statement"
mk_pack; sed -i 's/<label for="f1">Name<\/label>//' "$T/p/design/wireframes/index.html"; expect_fail "unlabelled field" "without a label"
mk_pack; sed -i 's/Main 2/Main 1/' "$T/p/design/wireframes/index.html";  expect_fail "duplicate nav label" "repeated <nav>"
mk_pack; sed -i 's/id="s-home-empty"/id="s-list"/; s/#s-home-empty/#s-list/' "$T/p/design/wireframes/index.html"; expect_fail "no empty state" "no empty-state"
mk_pack; sed -i 's/<button>Add<\/button>/<button><\/button>/' "$T/p/design/wireframes/index.html"; expect_fail "unnamed button" "no accessible name"
mk_pack; sed -i 's/<html lang="en">/<html>/' "$T/p/design/wireframes/index.html"; expect_fail "no lang" "no lang"
mk_pack; sed -i 's/#s-home"/#s-gone"/' "$T/p/design/wireframes/index.html"; expect_fail "dead prototype link" "no matching screen"
mk_pack; sed -i 's/None, must be found out/12 orders a week/' "$T/p/docs/product/CLARITY.md"
python3 "$CHECK" "$T/p" > "$T/out"; grep -q "is a fact but has a default" "$T/out" && ok || bad "fact with a default should warn"
mk_pack; rm -r "$T/p/design" "$T/p/docs/product/PRD.md" "$T/p/docs/product/DESIGN_DIRECTION.md"
python3 "$CHECK" "$T/p" --mode quick > "$T/out" && ok || { bad "quick mode needs no PRD/wireframes"; cat "$T/out"; }

echo "idea-pack: $pass passed, $fail failed"
[ "$fail" = 0 ]
