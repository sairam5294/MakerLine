# Skill style guide

Every `SKILL.md` in `plugin/skills/` follows the same shape, so a reader (human or model) always knows where to look. Modelled on Anthropic's knowledge-work plugins.

## Frontmatter
```yaml
---
name: evaluate-idea                      # folder name
description: <what it does> — <outputs>. Trigger with "...", "...", or when <situation>.   # ≤ 400 chars, starts with a verb phrase
argument-hint: "<what to pass after the command>"   # omit only for skills with no input
---
```

## Body, in this order
1. `# /name` — the slash command as the title.
2. Connector note (one line, only for skills that use connectors): `> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).`
3. One-sentence purpose, then **Why** in ≤ 2 sentences when the reason isn't obvious.
4. `## Usage` — a code block with the command and 1–3 example invocations.
5. `## How it works` — the standalone / supercharged box (ASCII box, ≤ 12 lines).
6. `## Inputs` — a short list: files read, the gate, what to ask the owner.
7. `## Workflow` — numbered steps with **bold step names**; each step ≤ 4 lines; sub-bullets for options; rules that apply to a step live in that step.
8. `## Output` — files written (path · what · size cap), then the ≤ n-line presentation to the owner, as a code block when the shape matters.
9. `## If connectors available` — `If **~~category** is connected:` + bullets (skip if none).
10. `## Rules` — the standing rules, as bullets (never prose paragraphs).
11. `## Tips` — 2–4 numbered tips for the owner.
12. `## Related` — previous / next skills and the references this skill reads.

## Writing rules
- Headings, bullets, tables and code blocks; no paragraph longer than 3 sentences.
- Paths in backticks; owner-facing phrases in *italics* or quotes.
- Keep every rule that existed before a reformat; move it, don't drop it. Say "MUST" only for hard rules.
- Reference files (`references/*.md`) and templates keep their own structure, but get: a one-line purpose at the top, `##` sections, and tables for anything compared.
- Length: a SKILL.md stays under ~1,200 words; detail moves to `references/`.
