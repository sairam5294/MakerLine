# Connectors

## How tool references work

Skill files use `~~category` as a placeholder for whatever tool you connect in that category. Every Idea Pack skill works **standalone** — your words and the web are enough. Connectors are optional; connecting is your choice, per tool, under the plugin's **Connectors** tab. `.mcp.json` pre-configures the three below; any MCP server in the same category works.

## Connectors the Idea Pack can use

| Category | Placeholder | Included server | Used by | The kit reads | The kit may write (only when you ask) | Never |
|---|---|---|---|---|---|---|
| Knowledge base | `~~knowledge base` | Notion | new-idea, evaluate-idea | pages you share with the integration (prior research, notes) | a page you ask for (e.g. the one-pager) | edit or delete existing pages |
| Design | `~~design` | Figma | design-direction | frames and screenshots you point to | a new wireframe file you name | change or delete your existing frames |
| Source control | `~~source control` | GitHub | evaluate-idea (existing product) | the README and STATUS of a repo you name | — | push, open PRs, change settings |

Placeholders other skills mention (hosting, database, project tracker, chat, analytics) belong to the full Product Kit's build phases; the Idea Pack never uses them.

## What the Idea Pack runs and sends

- **Files:** reads and writes only `docs/product/` and `design/` in the folder you connect.
- **Web:** search queries about your idea's market and competitors go to the search tool built into Claude.
- **Shell:** one local script, `check_idea_pack.py`, which checks the documents it wrote. No network access.
- **No servers of its own, no telemetry, no accounts.** Connectors run under your own account, with the limits above.

## Rules

- Secrets, keys and anyone's personal data never go into prompts or documents.
- If a connector isn't available, the skill says so once and continues standalone — it never asks you to connect one.
