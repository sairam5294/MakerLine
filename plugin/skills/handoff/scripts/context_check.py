#!/usr/bin/env python3
"""Shared project context for every AI tool: check it, export it, and score a recovery test.

Python standard library only. Run from a MakerLine kit clone or beside the handoff skill:

    python3 context_check.py check <project-root>           # health check before a tool starts work
    python3 context_check.py pack <project-root> --task "Strategy" --tool ChatGPT
                                                             # portable, permission-safe export
    python3 context_check.py score <answers.md> <key.json>  # score a context-recovery test

The contract these commands enforce is described in ../references/shared-context.md.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys

INDEX = pathlib.Path("docs/product/CONTEXT_INDEX.md")
HANDOFF = pathlib.Path("docs/product/HANDOFF.md")
STATUS = pathlib.Path("docs/product/STATUS.md")
DECISIONS = pathlib.Path("docs/product/DECISIONS.md")
ASSUMPTIONS = pathlib.Path("docs/product/ASSUMPTIONS.md")
PACK = pathlib.Path("docs/CONTEXT_PACK.md")

# Header fields every context index must fill in. "Verified commit" lets the next tool
# notice that the files changed after the last handoff.
REQUIRED_FIELDS = (
    "Product", "Stage", "Objective", "Active task", "Current decision",
    "Next action", "Next tool", "Owner", "Verified commit", "Updated",
)
TIERS = ("public", "project", "private")
LIMITS = {HANDOFF: 40, STATUS: 60}
CONFIDENCE = ("low", "medium", "high")

# Patterns that must never travel in a context pack. Deliberately broad: a false alarm
# costs a minute, a leaked key costs much more.
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}"),
    re.compile(r"(?i)(password|passwd|secret|api[_-]?key|service[_-]?role)\s*[:=]\s*['\"]?[^\s'\"<>]{8,}"),
]


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def print(self) -> int:
        for msg in self.errors:
            print(f"FAIL  {msg}")
        for msg in self.warnings:
            print(f"WARN  {msg}")
        if not self.errors and not self.warnings:
            print("PASS  shared context is complete and current")
        elif not self.errors:
            print(f"PASS  with {len(self.warnings)} warning(s)")
        return 1 if self.errors else 0


# ---------- Markdown helpers ----------

def tables(text: str) -> list[list[list[str]]]:
    """Return every Markdown table as a list of rows (header first, separator dropped)."""
    found, current = [], []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
                continue
            current.append(cells)
        elif current:
            found.append(current)
            current = []
    if current:
        found.append(current)
    return found


def find_table(text: str, first_header: str) -> list[list[str]] | None:
    for table in tables(text):
        if table and table[0] and table[0][0].lower() == first_header.lower():
            return table
    return None


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S | re.I)
    return match.group(1) if match else ""


def paths_in(cell: str) -> list[str]:
    """Paths in a 'Read' cell: comma separated, optional backticks, optional #section."""
    out = []
    for part in cell.split(","):
        part = part.strip().strip("`").strip()
        if not part or part in ("-", "—"):
            continue
        out.append(part.split("#", 1)[0].strip().strip("`"))
    return out


def parse_date(value: str) -> dt.date | None:
    match = re.search(r"\d{4}-\d{2}-\d{2}", value)
    if not match:
        return None
    try:
        return dt.date.fromisoformat(match.group(0))
    except ValueError:
        return None


def git(root: pathlib.Path, *args: str) -> str | None:
    try:
        result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


# ---------- Index parsing ----------

def read_index(root: pathlib.Path, report: Report) -> dict | None:
    path = root / INDEX
    if not path.exists():
        report.error(f"{INDEX} is missing (copy the handoff skill's templates/CONTEXT_INDEX.md)")
        return None
    text = path.read_text(encoding="utf-8")
    fields: dict[str, str] = {}
    table = find_table(text, "Field")
    if table:
        for row in table[1:]:
            if len(row) >= 2:
                fields[row[0]] = row[1]
    reads: list[tuple[str, list[str]]] = []
    read_table = find_table(text, "Task type")
    if read_table:
        for row in read_table[1:]:
            if len(row) >= 2 and row[0]:
                reads.append((row[0], paths_in(row[1])))
    tiers: dict[str, str] = {}
    tier_table = find_table(text, "Path")
    if tier_table:
        for row in tier_table[1:]:
            if len(row) >= 2 and row[0]:
                for p in paths_in(row[0]):
                    tiers[p] = row[1].lower()
    return {"fields": fields, "reads": reads, "tiers": tiers, "text": text}


def tier_of(path: str, tiers: dict[str, str]) -> str:
    """Most specific matching entry wins; folders end with '/'. Default tier is 'project'."""
    best, best_len = "project", -1
    for key, tier in tiers.items():
        if (path == key or (key.endswith("/") and path.startswith(key))) and len(key) > best_len:
            best, best_len = tier, len(key)
    return best


# ---------- check ----------

def check_index(root: pathlib.Path, index: dict, report: Report, today: dt.date) -> None:
    fields = index["fields"]
    for name in REQUIRED_FIELDS:
        value = fields.get(name, "")
        if not value or value.startswith("<"):
            report.error(f"{INDEX}: field '{name}' is empty")
    updated = parse_date(fields.get("Updated", ""))
    if fields.get("Updated") and not updated:
        report.error(f"{INDEX}: 'Updated' must be a YYYY-MM-DD date")
    elif updated and (today - updated).days > 30:
        report.warn(f"{INDEX}: last updated {updated} ({(today - updated).days} days ago); refresh it at the next handoff")
    if not index["reads"]:
        report.error(f"{INDEX}: the 'Read by task' table is missing or empty")
    elif not any(name.lower().startswith("any") for name, _ in index["reads"]):
        report.warn(f"{INDEX}: add an 'Any session start' row so every tool loads the same minimum")
    for name, paths in index["reads"]:
        if not paths:
            report.error(f"{INDEX}: task '{name}' lists no files")
        for p in paths:
            if any(ch in p for ch in "*?"):
                continue
            if not (root / p).exists():
                report.error(f"{INDEX}: task '{name}' points to missing file {p}")
    for p, tier in index["tiers"].items():
        if tier not in TIERS:
            report.error(f"{INDEX}: privacy tier for {p} must be one of {', '.join(TIERS)} (got '{tier}')")


def check_commit(root: pathlib.Path, index: dict, report: Report) -> None:
    commit = index["fields"].get("Verified commit", "").strip("` ")
    if not commit or commit.startswith("<"):
        return
    head = git(root, "rev-parse", "HEAD")
    if head is None:
        report.warn("not a git repository; can't compare 'Verified commit' with the files")
        return
    full = git(root, "rev-parse", "--verify", "--quiet", f"{commit}^{{commit}}")
    if not full:
        report.error(f"{INDEX}: verified commit {commit} isn't in this repository (wrong branch or not fetched)")
        return
    if full == head:
        return
    if git(root, "merge-base", "--is-ancestor", full, head) is None:
        report.error(f"{INDEX}: verified commit {commit} isn't an ancestor of HEAD; the context came from another branch")
        return
    changed = git(root, "diff", "--name-only", full, head, "--", "docs/product", "AGENTS.md") or ""
    changed_files = [c for c in changed.splitlines() if c and c != str(INDEX)]
    if changed_files:
        shown = ", ".join(changed_files[:5]) + (" …" if len(changed_files) > 5 else "")
        report.warn(f"context files changed after the verified commit {commit}: {shown}. Re-read them, then update the index")


def check_limits(root: pathlib.Path, report: Report) -> None:
    for rel, limit in LIMITS.items():
        path = root / rel
        if not path.exists():
            report.error(f"{rel} is missing")
            continue
        lines = len(path.read_text(encoding="utf-8").splitlines())
        if lines > limit:
            report.warn(f"{rel} has {lines} lines (limit {limit}); every tool reads it at start, so keep it short")
    if not (root / "AGENTS.md").exists():
        report.error("AGENTS.md is missing; every tool reads the project rules from it")


def check_decisions(root: pathlib.Path, report: Report) -> set[str]:
    path = root / DECISIONS
    ids: set[str] = set()
    if not path.exists():
        report.error(f"{DECISIONS} is missing")
        return ids
    table = find_table(path.read_text(encoding="utf-8"), "ID")
    if table is None:
        report.warn(f"{DECISIONS}: add an ID column (D-01, D-02 …) so tools can cite decisions")
        return ids
    for row in table[1:]:
        if not any(row):
            continue
        did = row[0]
        if not re.fullmatch(r"D-\d{2,}", did):
            report.error(f"{DECISIONS}: decision ID '{did}' should look like D-01")
        elif did in ids:
            report.error(f"{DECISIONS}: decision ID {did} is used twice; IDs never change or repeat")
        ids.add(did)
    return ids


def check_assumptions(root: pathlib.Path, report: Report, today: dt.date) -> None:
    path = root / ASSUMPTIONS
    if not path.exists():
        report.error(f"{ASSUMPTIONS} is missing (copy the handoff skill's templates/ASSUMPTIONS.md)")
        return
    table = find_table(path.read_text(encoding="utf-8"), "ID")
    if table is None or len(table) < 2:
        report.error(f"{ASSUMPTIONS}: the register table is empty")
        return
    header = [h.lower() for h in table[0]]
    col = {name: header.index(name) for name in header}
    seen: set[str] = set()
    for row in table[1:]:
        if not any(row):
            continue
        aid = row[0]
        if not re.fullmatch(r"[AR]-\d{2,}", aid):
            report.error(f"{ASSUMPTIONS}: ID '{aid}' should look like A-01 (assumption) or R-01 (risk)")
        if aid in seen:
            report.error(f"{ASSUMPTIONS}: ID {aid} is used twice")
        seen.add(aid)
        get = lambda name: row[col[name]] if name in col and col[name] < len(row) else ""  # noqa: E731
        if get("confidence") and get("confidence").lower() not in CONFIDENCE:
            report.error(f"{ASSUMPTIONS}: {aid} confidence must be low, medium or high")
        if not get("owner"):
            report.error(f"{ASSUMPTIONS}: {aid} has no owner")
        review = parse_date(get("review by"))
        if review is None:
            report.error(f"{ASSUMPTIONS}: {aid} needs a 'Review by' date (YYYY-MM-DD)")
        elif review < today:
            report.warn(f"{ASSUMPTIONS}: {aid} evidence expired on {review}; re-test it before relying on it")


def check_handoff(root: pathlib.Path, index: dict, report: Report) -> None:
    path = root / HANDOFF
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    first = text.splitlines()[0] if text else ""
    handoff_date = parse_date(first)
    index_date = parse_date(index["fields"].get("Updated", ""))
    if handoff_date and index_date and handoff_date > index_date:
        report.warn(f"{HANDOFF} ({handoff_date}) is newer than {INDEX} ({index_date}); update the index at each handoff")
    if not re.search(r"^##\s*Next", text, re.M | re.I):
        report.warn(f"{HANDOFF}: no 'Next steps' section; the next tool won't know where to start")


def cmd_check(args: argparse.Namespace) -> int:
    root = pathlib.Path(args.root).resolve()
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    report = Report()
    index = read_index(root, report)
    check_limits(root, report)
    check_decisions(root, report)
    check_assumptions(root, report, today)
    if index:
        check_index(root, index, report, today)
        check_commit(root, index, report)
        check_handoff(root, index, report)
    return report.print()


# ---------- pack ----------

def summarise_review(path: pathlib.Path) -> str:
    """REVIEW.json is long; a receiving tool needs the answer, options and next actions."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return path.read_text(encoding="utf-8")
    lines = [
        f"- Product: {data.get('product')} · stage {data.get('stage')} · depth {data.get('depth')} · updated {data.get('updated')}",
        f"- Decision: {data.get('decision')} (confidence: {data.get('confidence')})",
        f"- Why: {data.get('decision_reason')}",
        "- Options:",
    ]
    for opt in data.get("options", []):
        lines.append(f"  - {opt.get('name')} ({opt.get('type')}): value {opt.get('value_range')}; effort {opt.get('effort_range')}; test: {opt.get('test')}")
    lines.append("- Unknowns:")
    for unk in data.get("unknowns", []):
        lines.append(f"  - {unk.get('question')} (blocks: {unk.get('blocks')})")
    lines.append("- Next actions:")
    for act in data.get("next_actions", []):
        lines.append(f"  - {act.get('action')} — {act.get('owner')}, {act.get('when')}; success: {act.get('success_measure')}")
    return "\n".join(lines)


def cmd_pack(args: argparse.Namespace) -> int:
    root = pathlib.Path(args.root).resolve()
    report = Report()
    index = read_index(root, report)
    if not index:
        return report.print()
    rows = dict(index["reads"])
    start = next((paths for name, paths in index["reads"] if name.lower().startswith("any")), [])
    task = next((name for name in rows if name.lower() == args.task.lower()), None)
    if task is None:
        print(f"FAIL  no task '{args.task}' in {INDEX}. Choose one of: {', '.join(rows)}")
        return 1
    wanted: list[str] = []
    for p in start + rows[task]:
        if p not in wanted:
            wanted.append(p)
    included, skipped = [], []
    for p in wanted:
        tier = tier_of(p, index["tiers"])
        if tier == "private" or (args.public_only and tier != "public"):
            skipped.append(f"{p} ({tier})")
            continue
        file = root / p
        if not file.is_file():
            skipped.append(f"{p} (missing)")
            continue
        body = summarise_review(file) if file.name == "REVIEW.json" else file.read_text(encoding="utf-8")
        body_lines = body.splitlines()
        if len(body_lines) > args.max_lines:
            body = "\n".join(body_lines[: args.max_lines]) + f"\n… (cut at {args.max_lines} lines; ask for the rest)"
        for pattern in SECRET_PATTERNS:
            if pattern.search(body):
                print(f"FAIL  {p} contains something that looks like a secret ({pattern.pattern[:24]}…). Remove it or mark the file private.")
                return 1
        included.append((p, body))
    commit = git(root, "rev-parse", "--short", "HEAD") or "not a git repository"
    created = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    fields = index["fields"]
    out = [
        f"# Context pack — {fields.get('Product', root.name)} — {task}",
        "",
        f"Created {created} for **{args.tool}** from commit `{commit}`. Generated by `context_check.py pack`; "
        "don't edit it by hand, regenerate it.",
        "",
        "## Instructions for the receiving AI tool",
        "",
        "- This pack is the only project context you have. Don't assume anything that isn't in it; say \"not in the pack\" instead.",
        "- Cite decisions and evidence by their IDs (D-01, A-01, S1 …). Label anything new as an estimate or a proposal.",
        "- You can't change the project files. End your answer with a **Handoff back** section: what you concluded, "
        "new decisions or evidence to record (with proposed IDs), and the exact next action. The owner pastes it back "
        "and a local tool records it.",
        "",
        "## Current state",
        "",
        "| Field | Value |",
        "|---|---|",
    ]
    out += [f"| {name} | {fields.get(name, '')} |" for name in REQUIRED_FIELDS]
    for p, body in included:
        fence = "````" if "```" in body else "```"
        out += ["", f"## {p}", "", fence + ("json" if p.endswith(".json") else "markdown"), body.rstrip(), fence]
    out += ["", "## Not included", ""]
    out += [f"- {s}" for s in skipped] or ["- Nothing was left out."]
    target = root / (args.out or PACK)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    words = sum(len(b.split()) for _, b in included)
    print(f"PASS  wrote {target.relative_to(root)}: {len(included)} file(s), ~{words} words, {len(skipped)} left out")
    return 0


# ---------- score ----------

def cmd_score(args: argparse.Namespace) -> int:
    key = json.loads(pathlib.Path(args.key).read_text(encoding="utf-8"))
    answers_text = pathlib.Path(args.answers).read_text(encoding="utf-8")
    answers = {m.group(1).upper(): m.group(2) for m in re.finditer(r"^##\s*(C\d{2})\b.*?$(.*?)(?=^##\s*C\d{2}\b|\Z)", answers_text, re.M | re.S | re.I)}
    total, passed, rows = 0, 0, []
    for case in key["cases"]:
        total += 1
        answer = answers.get(case["id"].upper(), "")
        low = answer.lower()
        missing = []
        for item in case["must_include"]:
            options = item if isinstance(item, list) else [item]
            if not any(opt.lower() in low for opt in options):
                missing.append(" / ".join(options))
        wrong = [w for w in case.get("must_not_include", []) if w.lower() in low]
        ok = bool(answer.strip()) and not missing and not wrong
        passed += ok
        note = "no answer" if not answer.strip() else "; ".join(
            ([f"missing: {', '.join(missing)}"] if missing else []) + ([f"wrong: {', '.join(wrong)}"] if wrong else [])
        )
        rows.append(f"| {case['id']} | {case['scenario']} | {'pass' if ok else 'fail'} | {note} |")
    print(f"Context recovery: {passed}/{total} passed ({round(100 * passed / total) if total else 0}%)\n")
    print("| Case | Scenario | Result | Notes |\n|---|---|---|---|")
    print("\n".join(rows))
    return 0 if passed == total else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check", help="health check of the shared context files")
    p.add_argument("root", nargs="?", default=".")
    p.add_argument("--today", help=argparse.SUPPRESS)
    p.set_defaults(func=cmd_check)
    p = sub.add_parser("pack", help="write docs/CONTEXT_PACK.md for a tool that can't read the folder")
    p.add_argument("root", nargs="?", default=".")
    p.add_argument("--task", required=True, help="a 'Task type' row from CONTEXT_INDEX.md")
    p.add_argument("--tool", required=True, help="who receives it, e.g. ChatGPT")
    p.add_argument("--out", help="output path relative to the project (default docs/CONTEXT_PACK.md)")
    p.add_argument("--public-only", action="store_true", help="include only files marked public")
    p.add_argument("--max-lines", type=int, default=300)
    p.add_argument("--today", help=argparse.SUPPRESS)
    p.set_defaults(func=cmd_pack)
    p = sub.add_parser("score", help="score a context-recovery answer sheet against its key")
    p.add_argument("answers")
    p.add_argument("key")
    p.set_defaults(func=cmd_score)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
