#!/usr/bin/env python3
"""Copy MakerLine from its single source (plugin/) into the project template.

    plugin/skills/*     -> template/.agents/skills/*      Cursor + Codex read skills here
    plugin/agents/*.md  -> template/.cursor/agents/*.md   Cursor subagents (Claude gets agents
                                                          from the plugin, so no duplicates)
    plugin/agents/*.md  -> template/.codex/agents/*.toml  Codex custom agents (converted)

Rule: edit files in plugin/ only, then run:  python3 scripts/sync.py
"""
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC_SKILLS = ROOT / "plugin" / "skills"
SRC_AGENTS = ROOT / "plugin" / "agents"
TEMPLATE = ROOT / "template"


def parse_agent(text: str):
    """Split an agent .md file into (name, description, readonly, prompt body)."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        raise ValueError("agent file is missing its --- frontmatter --- block")
    frontmatter, body = match.group(1), match.group(2).strip()
    field = lambda key: re.search(rf"^{key}:\s*(.+)$", frontmatter, re.M)  # noqa: E731
    name = field("name").group(1).strip()
    description = field("description").group(1).strip()
    readonly = bool(re.search(r"^readonly:\s*true", frontmatter, re.M))
    return name, description, readonly, body


def toml_string(value: str) -> str:
    """Quote a one-line string for TOML."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def fresh_dir(path: pathlib.Path) -> pathlib.Path:
    """Delete and recreate a generated folder so removed skills/agents don't linger."""
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
    return path


def main() -> None:
    # 1. Skills: copied as-is (same SKILL.md format works in Claude, Cursor and Codex).
    skills_dst = TEMPLATE / ".agents" / "skills"
    if skills_dst.exists():
        shutil.rmtree(skills_dst)
    shutil.copytree(SRC_SKILLS, skills_dst)

    # 2. Agents: Markdown for Cursor, TOML for Codex.
    cursor_dst = fresh_dir(TEMPLATE / ".cursor" / "agents")
    codex_dst = fresh_dir(TEMPLATE / ".codex" / "agents")

    for agent_file in sorted(SRC_AGENTS.glob("*.md")):
        text = agent_file.read_text()
        # Cursor uses its own model names, so Cursor copies always inherit the chat's model.
        (cursor_dst / agent_file.name).write_text(re.sub(r"^model: .*$", "model: inherit", text, flags=re.M))
        name, description, readonly, body = parse_agent(text)
        # Codex: map Claude's cheaper "sonnet" routing to lower reasoning effort (fewer tokens).
        light = bool(re.search(r"^model: sonnet", text, re.M))
        body = body.replace("'''", "' ' '")  # ''' would end the TOML multi-line string early
        toml = (
            f"name = {toml_string(name)}\n"
            f"description = {toml_string(description)}\n"
            # Reviewers/researchers only read; Codex enforces that with a read-only sandbox.
            + ('sandbox_mode = "read-only"\n' if readonly else "")
            + f'model_reasoning_effort = "{"medium" if light else "high"}"\n'
            + "developer_instructions = '''\n"
            + body
            + "\n\nFollow AGENTS.md and .agents/skills/product-standards/. "
            + "Return a concise summary (max ~300 words) to the parent agent.\n'''\n"
        )
        (codex_dst / f"{name}.toml").write_text(toml)

    # 3. Design tokens source + generator (same files the starters use).
    design_dst = TEMPLATE / "design"
    design_dst.mkdir(exist_ok=True)
    for name in ("tokens.json", "build-tokens.mjs"):
        shutil.copy(ROOT / "design" / name, design_dst / name)

    n_skills = len(list(skills_dst.iterdir()))
    n_agents = len(list(cursor_dst.iterdir()))
    print(f"Synced {n_skills} skills and {n_agents} agents into template/")


if __name__ == "__main__":
    main()
