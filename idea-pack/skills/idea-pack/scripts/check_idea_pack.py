#!/usr/bin/env python3
"""Check an Idea Pack for gaps before showing it to the owner.

Why this exists: re-reading every document to self-check costs a lot of tokens
and still misses things (leftover {{placeholders}}, wrong contrast ratios,
broken links). A script checks them in a second and prints only the problems.

Usage:  python3 check_idea_pack.py [project_dir] [--mode quick|standard|deep]
Read-only, standard library only, no network. Exit 1 if any FAIL.
"""
import argparse
import html
import re
import sys
from pathlib import Path

REQUIRED = {
    "quick": ["PROJECT_BRIEF.md", "CLARITY.md", "EVALUATION.md", "COMPETITORS.md", "ONE_PAGER.md", "README.md"],
}
REQUIRED["standard"] = REQUIRED["quick"] + ["DESIGN_DIRECTION.md", "PRD.md"]
REQUIRED["deep"] = REQUIRED["standard"]

# Prose word ranges per mode (tables, code and the sources list don't count).
EVAL_WORDS = {"quick": (600, 1500), "standard": (1500, 3000), "deep": (2500, 4500)}
ONE_PAGER_MAX = 550

# Phrases each document must contain (case-insensitive). Kept loose on purpose:
# they confirm a section exists, not its wording.
MUST_HAVE = {
    "EVALUATION.md": ["strongest version", "reality check", "path to go", "accessibility"],
    "COMPETITORS.md": ["doing nothing", "differentiator test"],
    "CLARITY.md": ["readiness", "decision", "fact"],
    "PRD.md": ["given", "accessibility statement"],
    "DESIGN_DIRECTION.md": ["principle", "accessibility", "contrast"],
}

results = []


def report(level, msg):
    results.append((level, msg))


def prose_words(text):
    """Count words outside tables, code blocks, HTML comments and the Sources section."""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.split(r"\n#+\s*\d*\.?\s*Sources\b", text, flags=re.I)[0]
    lines = [ln for ln in text.splitlines() if not ln.lstrip().startswith("|")]
    return len(re.findall(r"[\w₹$€£%'’-]+", " ".join(lines)))


def luminance(hex6):
    def ch(c):
        c = int(c, 16) / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = hex6[0:2], hex6[2:4], hex6[4:6]
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = sorted([luminance(a), luminance(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def expand(h):
    h = h.lstrip("#")
    return "".join(c * 2 for c in h) if len(h) == 3 else h


NAMED = {"white": "ffffff", "black": "000000"}
COLOUR = r"(#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|\bwhite\b|\bblack\b)"
RATIO = r"(\d+(?:\.\d+)?)\s*:\s*1"


def hexval(c):
    c = c.lower()
    return NAMED.get(c) or expand(c)


def check_pair(name, a, b, stated, line):
    actual = contrast(hexval(a), hexval(b))
    short = line.strip()[:80]
    if abs(actual - stated) > 0.3:
        report("FAIL", f"{name}: stated {stated}:1 but {a} on {b} is {actual:.2f}:1 → {short}")
    elif actual < 4.5 and not re.search(r"large|non-text|icon|border|3:1|fail|✗|decor", line, re.I):
        report("WARN", f"{name}: {a} on {b} is {actual:.2f}:1 (< 4.5:1 for body text) → {short}")


def check_contrast_claims(name, text):
    """Recompute stated contrast ratios. Two shapes are checked:
    'X on Y (n:1)' in prose, and table rows holding exactly two colours and one ratio."""
    for ln in text.splitlines():
        if ln.lstrip().startswith("|"):
            cols = re.findall(COLOUR, ln)
            ratios = re.findall(RATIO, ln)
            if len(cols) == 2 and len(ratios) == 1:
                check_pair(name, cols[0], cols[1], float(ratios[0]), ln)
            continue
        pat = COLOUR + r"\s*(?:text\s*)?(?:on|over|/|vs\.?)\s*" + COLOUR + r"[^0-9#]{0,20}" + RATIO
        for m in re.finditer(pat, ln, re.I):
            check_pair(name, m.group(1), m.group(2), float(m.group(3)), ln)


def check_wireframes(path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    if "HOW TO FILL" in raw:
        report("WARN", "wireframes: template instructions comment still present — delete it")
    body = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    n_ph = len(re.findall(r"(?<![$=])\{\{", body))
    if n_ph:
        report("FAIL", f"wireframes: {n_ph} unfilled {{{{placeholders}}}}")
    if re.search(r"lorem ipsum", body, re.I):
        report("FAIL", "wireframes: lorem ipsum found — use real content")
    if not re.search(r"<html[^>]*\blang=", body):
        report("FAIL", "wireframes: <html> has no lang attribute")
    screens = re.findall(r'<section[^>]*class="[^"]*screen[^"]*"[^>]*id="([^"]+)"', body)
    screens += re.findall(r'<section[^>]*id="([^"]+)"[^>]*class="[^"]*screen', body)
    screens = sorted(set(screens))
    report("INFO", f"wireframes: {len(screens)} screens")
    if not any("empty" in s for s in screens):
        report("FAIL", "wireframes: no empty-state screen (id containing 'empty')")
    if 'role="alert"' not in body and "error" not in " ".join(screens):
        report("FAIL", "wireframes: no error state (role=\"alert\" or a screen id containing 'error')")
    ids = set(re.findall(r'\bid="([^"]+)"', body))
    for target in set(re.findall(r'href="#([^"?]+)"', body)):
        if target not in ids:
            report("FAIL", f"wireframes: link to #{target} has no matching screen")
    for inp in re.findall(r"<(?:input|select|textarea)\b[^>]*>", body):
        if re.search(r'type="(hidden|submit|button)"', inp):
            continue
        m = re.search(r'\bid="([^"]+)"', inp)
        labelled = m and re.search(rf'<label[^>]*for="{re.escape(m.group(1))}"', body)
        if not labelled and "aria-label" not in inp and "aria-labelledby" not in inp:
            report("FAIL", f"wireframes: form field without a label → {inp[:70]}")
    navs = re.findall(r'<nav[^>]*aria-label="([^"]*)"', body)
    dupes = {n for n in navs if navs.count(n) > 1}
    if dupes:
        report("FAIL", f"wireframes: repeated <nav> labels {sorted(dupes)} — make each unique")
    for m in re.finditer(r"<(button|a)\b([^>]*)>(.*?)</\1>", body, flags=re.S):
        text = html.unescape(re.sub(r"<[^>]+>", "", m.group(3))).strip()
        if not text and "aria-label" not in m.group(2):
            report("FAIL", f"wireframes: <{m.group(1)}> with no accessible name → {m.group(0)[:70]}")
    # Inclusion checks (product-standards references/inclusion.md)
    labels = [html.unescape(re.sub(r"<[^>]+>", "", x)).strip().lower() for x in re.findall(r"<label[^>]*>(.*?)</label>", body, flags=re.S)]
    if any("first name" in x for x in labels) and any("last name" in x or "surname" in x for x in labels):
        report("WARN", "wireframes: separate first/last name fields — prefer one 'Full name' field (inclusion.md §4)")
    for x in labels:
        if re.search(r"\b(gender|sex|religion|caste|ethnicity|marital|title)\b", x) and "optional" not in x:
            report("WARN", f"wireframes: '{x[:40]}' looks required — make it optional with 'prefer not to say', or drop it (inclusion.md §4)")
    if re.search(r'<span[^>]*class="chip"[^>]*onclick', body):
        report("FAIL", "wireframes: clickable span chips — use <button class=\"chip\" aria-pressed>")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project", nargs="?", default=".")
    ap.add_argument("--mode", choices=["quick", "standard", "deep"], default="standard")
    a = ap.parse_args()
    root = Path(a.project)
    docs = root / "docs" / "product"
    if not docs.is_dir():
        print(f"No docs/product folder in {root.resolve()}")
        return 1

    for f in REQUIRED[a.mode]:
        if not (docs / f).exists():
            report("FAIL", f"missing docs/product/{f} ({a.mode} mode)")

    for f in sorted(docs.glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        body = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
        n = len(re.findall(r"(?<![$=])\{\{", body))  # ignore GitHub Actions ${{ }} and JSX style={{ }}
        if n:
            report("FAIL", f"{f.name}: {n} unfilled {{{{placeholders}}}}")
        if re.search(r"lorem ipsum", body, re.I):
            report("FAIL", f"{f.name}: lorem ipsum")
        for phrase in MUST_HAVE.get(f.name, []):
            if phrase not in body.lower():
                report("FAIL", f"{f.name}: no section mentioning '{phrase}'")
        check_contrast_claims(f.name, body)
        for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", body):
            if re.match(r"[a-z]+:", target):
                continue  # external link
            if not (f.parent / target).exists():
                report("FAIL", f"{f.name}: broken link → {target}")

    caps = {
        "EVALUATION.md": {"quick": 2000, "standard": 3000, "deep": 4500},
        "COMPETITORS.md": {"quick": 600, "standard": 1200, "deep": 2000},
        "DESIGN_DIRECTION.md": {"quick": 10**9, "standard": 1500, "deep": 2500},
        "PRD.md": {"quick": 10**9, "standard": 2000, "deep": 3000},
        "CLARITY.md": {"quick": 800, "standard": 1000, "deep": 1500},
    }
    for name, by_mode in caps.items():
        f = docs / name
        if f.exists():
            total = len(re.findall(r"[\w₹$€£%'’-]+", re.sub(r"<!--.*?-->", " ", f.read_text(encoding="utf-8"), flags=re.S)))
            cap = by_mode[a.mode]
            if total > cap and not (name == "PRD.md" and "v1." in f.read_text(encoding="utf-8")[:400]):
                report("WARN", f"{name}: {total} words incl. tables (cap {cap} for {a.mode}) — every later phase re-reads it")
    ev = docs / "EVALUATION.md"
    if ev.exists():
        w = prose_words(ev.read_text(encoding="utf-8"))
        lo, hi = EVAL_WORDS[a.mode]
        lvl = "WARN" if not lo <= w <= hi else "INFO"
        report(lvl, f"EVALUATION.md: {w} prose words (target {lo}–{hi} for {a.mode})")
        t = ev.read_text(encoding="utf-8").lower()
        if "raise it by" not in t:
            report("FAIL", "EVALUATION.md: scorecard has no 'Raise it by…' column")
    op = docs / "ONE_PAGER.md"
    if op.exists():
        w = prose_words(op.read_text(encoding="utf-8"))
        if w > ONE_PAGER_MAX:
            report("WARN", f"ONE_PAGER.md: {w} words (max {ONE_PAGER_MAX})")
    cl = docs / "CLARITY.md"
    if cl.exists():
        rows = [r for r in cl.read_text(encoding="utf-8").splitlines() if re.match(r"\|\s*Q-\d+", r)]
        report("INFO", f"CLARITY.md: {len(rows)} open questions")
        for r in rows:
            cells = [c.strip() for c in r.strip("|").split("|")]
            typ = " ".join(cells).lower()
            if "fact" in typ and re.search(r"\|\s*fact\s*\|", r, re.I):
                default = cells[-1].lower() if cells else ""
                if default and not re.search(r"none|must be found|unknown|—|-$", default):
                    report("WARN", f"CLARITY.md: {cells[0]} is a fact but has a default ('{cells[-1][:40]}') — facts are found out, not assumed")
    prd = docs / "PRD.md"
    if prd.exists() and a.mode != "quick":
        g = len(re.findall(r"\bGiven\b", prd.read_text(encoding="utf-8")))
        if g < 6:
            report("FAIL", f"PRD.md: only {g} Given/When/Then criteria (need ≥ 6)")

    wf = root / "design" / "wireframes" / "index.html"
    if a.mode != "quick":
        if wf.exists():
            check_wireframes(wf)
        else:
            report("FAIL", "missing design/wireframes/index.html")

    order = {"FAIL": 0, "WARN": 1, "INFO": 2}
    for lvl, msg in sorted(results, key=lambda r: order[r[0]]):
        print(f"{lvl:4}  {msg}")
    fails = sum(1 for lvl, _ in results if lvl == "FAIL")
    warns = sum(1 for lvl, _ in results if lvl == "WARN")
    print(f"\nIdea Pack check ({a.mode}): {fails} fail · {warns} warn")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
