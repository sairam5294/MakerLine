#!/usr/bin/env python3
"""Build the standalone Idea Pack plugin from the kit's single source (plugin/).

    plugin/skills/{new-idea,evaluate-idea,...}  -> idea-pack/skills/...
    plugin/agents/{market-researcher,...}.md    -> idea-pack/agents/...
    standalone/idea-pack/SKILL.md               -> idea-pack/skills/idea-pack/SKILL.md (orchestrator)
    product-kickoff templates + checker script  -> idea-pack/skills/idea-pack/{templates,scripts}

Why generated: the Idea Pack skills must stay identical to the full kit's, so
there is one source to edit (plugin/) and this script copies and re-points paths.

Usage:
    python3 scripts/build-idea-pack.py           rebuild idea-pack/
    python3 scripts/build-idea-pack.py --check   fail if idea-pack/ is out of date (CI)
    python3 scripts/build-idea-pack.py --zip DIR also write DIR/idea-pack.plugin
"""
import filecmp
import json
import pathlib
import re
import shutil
import sys
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "plugin"
STANDALONE = ROOT / "standalone" / "idea-pack"
OUT = ROOT / "idea-pack"

SKILLS = ["new-idea", "evaluate-idea", "design-direction", "write-prd", "validate-idea", "tool-plan", "product-standards"]
AGENTS = ["market-researcher", "devils-advocate", "idea-champion", "accessibility-strategist"]

# Path rewrites: the orchestrator replaces product-kickoff, and the one test-plan
# reference the pack needs is copied into the orchestrator's folder.
REWRITES = [
    ("../product-kickoff/templates/", "../idea-pack/templates/"),
    ("(product-kickoff/scripts)", "(idea-pack/scripts)"),
    ("product-kickoff/scripts", "idea-pack/scripts"),
    ("../test-plan/references/accessibility-user-testing.md", "../idea-pack/references/accessibility-user-testing.md"),
    ("test-plan/references/accessibility-user-testing.md", "idea-pack/references/accessibility-user-testing.md"),
]


def build(out: pathlib.Path) -> None:
    if out.exists():
        shutil.rmtree(out)
    (out / "skills").mkdir(parents=True)
    (out / "agents").mkdir()
    for s in SKILLS:
        shutil.copytree(SRC / "skills" / s, out / "skills" / s, ignore=shutil.ignore_patterns(".DS_Store"))
    for a in AGENTS:
        shutil.copy2(SRC / "agents" / f"{a}.md", out / "agents" / f"{a}.md")

    orch = out / "skills" / "idea-pack"
    (orch / "templates").mkdir(parents=True)
    (orch / "scripts").mkdir()
    (orch / "references").mkdir()
    shutil.copy2(STANDALONE / "SKILL.md", orch / "SKILL.md")
    (out / "skills" / "start").mkdir()
    shutil.copy2(STANDALONE / "start" / "SKILL.md", out / "skills" / "start" / "SKILL.md")
    tpl = SRC / "skills" / "product-kickoff" / "templates"
    for name in ["ONE_PAGER.md", "IDEA_PACK_README.md", "DECISIONS.md", "COSTS.md"]:
        shutil.copy2(tpl / name, orch / "templates" / name)
    shutil.copy2(STANDALONE / "STATUS.md", orch / "templates" / "STATUS.md")
    shutil.copy2(SRC / "skills" / "product-kickoff" / "scripts" / "check_idea_pack.py", orch / "scripts" / "check_idea_pack.py")
    shutil.copy2(SRC / "skills" / "test-plan" / "references" / "accessibility-user-testing.md",
                 orch / "references" / "accessibility-user-testing.md")
    shutil.copy2(STANDALONE / "README.md", out / "README.md")
    shutil.copy2(SRC / "CONNECTORS.md", out / "CONNECTORS.md")
    shutil.copy2(SRC / ".mcp.json", out / ".mcp.json")

    for f in out.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        new = text
        for a, b in REWRITES:
            new = new.replace(a, b)
        if new != text:
            f.write_text(new, encoding="utf-8")

    kit = json.loads((SRC / ".claude-plugin" / "plugin.json").read_text())
    (out / ".claude-plugin").mkdir()
    (out / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": "idea-pack",
        "version": kit["version"],
        "description": "Turn a product idea into an Idea Pack before any code: discovery, honest constructive evaluation with competitors, differentiator test and path to Go, accessibility and compliance lens, design direction with clickable wireframes, draft PRD and one-pager.",
        "author": kit.get("author", {"name": "Sai"}),
        "keywords": ["idea", "discovery", "evaluation", "competitors", "prd", "wireframes", "accessibility"],
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Every ../<skill>/ reference must resolve inside the pack.
    missing = set()
    for f in out.rglob("*.md"):
        if "templates" in f.parts:
            continue  # templates are project documents; their ../ links point into the project
        for ref in re.findall(r"(?<!\.\./)\.\./([a-z-]+)/", f.read_text(encoding="utf-8")):
            if not (out / "skills" / ref).is_dir():
                missing.add(f"{f.relative_to(out)} → ../{ref}/")
    if missing:
        sys.exit("Idea Pack references skills it doesn't include:\n  " + "\n  ".join(sorted(missing)))


def same_tree(a: pathlib.Path, b: pathlib.Path) -> bool:
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.funny_files:
        return False
    _, mismatch, errors = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    if mismatch or errors:
        return False
    return all(same_tree(a / d, b / d) for d in cmp.common_dirs)


def main() -> None:
    args = sys.argv[1:]
    if "--check" in args:
        with tempfile.TemporaryDirectory() as tmp:
            fresh = pathlib.Path(tmp) / "idea-pack"
            build(fresh)
            if not OUT.exists() or not same_tree(fresh, OUT):
                sys.exit("idea-pack/ is out of date — run: python3 scripts/build-idea-pack.py")
        print("idea-pack/ is up to date")
        return
    build(OUT)
    n_skills = len(list((OUT / "skills").iterdir()))
    print(f"Built idea-pack/ ({n_skills} skills, {len(AGENTS)} agents)")
    if "--zip" in args:
        dest = pathlib.Path(args[args.index("--zip") + 1]).expanduser().resolve() / "idea-pack.plugin"
        dest.unlink(missing_ok=True)
        with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(OUT.rglob("*")):
                if f.is_file() and f.name != ".DS_Store":
                    z.write(f, f.relative_to(OUT))
        print(f"✅ Built {dest}")


if __name__ == "__main__":
    main()
