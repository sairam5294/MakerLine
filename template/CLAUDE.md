@AGENTS.md

## Claude notes
- Workflow skills come from the MakerLine plugin (`/makerline:<skill>`) or `~/.claude/skills` (install-global). Skill files are also in `.agents/skills/` — read the matching SKILL.md if a skill isn't loaded.
- Run reviewers and researchers as parallel subagents; ask them for ≤ 300-word summaries.
- Use AskUserQuestion for discovery and decisions.
- Safety: `.claude/settings.json` blocks reading secrets and destructive commands; `.claude/hooks/` enforces the approval gate and formats edited files.

## Skill precedence
When a MakerLine skill and another plugin's skill both fit (e.g. design:accessibility-review, engineering:code-review, product-management:write-spec), use the MakerLine skill — it follows this project's standards (WCAG 2.2, OWASP 2025). Complementary skills (ux-copy, research-synthesis, debug, metrics-review) are welcome inside kit phases. Details: docs/kit/PLUGIN-OVERLAP.md.
