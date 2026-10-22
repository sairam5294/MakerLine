# Install and use MakerLine in AI tools

_Checked against official product documentation on 2026-10-22. Installation surfaces change; use the linked vendor guide if a menu has moved._

MakerLine has two kinds of files: **skills** (`SKILL.md`, loaded when relevant) and **project rules** (`AGENTS.md` and thin tool adapters, loaded with a project). The full Claude plugin also has agents and hooks. A tool that reads a skill does not automatically gain the repo, browser, Figma or analytics access needed to complete every step. The HTML report generator needs a local Python 3.9+ environment; a chat without local file execution can still follow the review and produce the JSON for a local tool to render.

The invocation spelling differs by host: Claude uses `/makerline:product-opportunity-review`; ChatGPT uses `@` to select the skill; Codex uses `$product-opportunity-review` or `/skills`; Cursor uses `/product-opportunity-review`; Copilot can be asked to use `/product-opportunity-review`. The plain-language prompts in the HTML report avoid host-specific syntax.

## Claude Code and Claude desktop

From Claude Code, add the GitHub marketplace once, then install the full plugin:

```text
claude plugin marketplace add sairam5294/makerline
claude plugin install makerline@makerline
```

Start a new session and type `/makerline:start` for a fresh idea or `/makerline:product-opportunity-review` for an existing product. In the Claude desktop app, use **Customize → Plugins → Add marketplace**, enter `sairam5294/makerline`, then install **makerline**. MakerLine's existing `makerline-idea` package is only for the idea stage; use the full package for the new review. A single local skill can also live at `.claude/skills/<name>/SKILL.md` in a project or `~/.claude/skills/<name>/SKILL.md` for Claude Code. Claude Cowork/cloud sessions may need the skill enabled in the Claude account rather than only in a local folder. See [Claude skills](https://code.claude.com/docs/en/skills) and [Claude plugins](https://code.claude.com/docs/en/plugins).

## ChatGPT and Codex

MakerLine's full `plugin/` folder now has a portable `plugin.json`; the repo also has `.agents/plugins/marketplace.json` pointing to it. In the **ChatGPT desktop app**, open this trusted repository as a project, restart the app after adding or updating the marketplace, then open **Plugins**, choose **MakerLine local**, and install **makerline**. Start a new chat and type `@` to select the plugin or a skill, or describe the task directly. This is a local marketplace; it is not a public directory listing. A workspace administrator can publish a tested plugin to selected workspace roles later. See [OpenAI's local marketplace instructions](https://developers.openai.com/plugins/build/plugins) and [using plugins](https://learn.chatgpt.com/docs/plugins).

In Codex CLI or desktop, the same local marketplace can provide the plugin. For a **repo-scoped standalone skill** without the whole plugin, copy a skill folder into `<project>/.agents/skills/`; for a personal skill, use `~/.agents/skills/` or `~/.codex/skills/`. Start a new session; invoke it with `$product-opportunity-review` or choose it from `/skills`. The existing `template/.agents/skills/` files are what a MakerLine-created project receives. See [OpenAI's skill locations and invocation](https://learn.chatgpt.com/docs/build-skills).

ChatGPT in a browser can use an installed plugin when available to that account or workspace, but it may not have access to local project files or the Python renderer. Give it the approved context pack and review record, then let a local tool render the HTML. Do not paste secrets or identifiable customer research.

## Cursor

For a project skill, put the folder in `<project>/.agents/skills/` or `<project>/.cursor/skills/`; for a personal local skill use `~/.cursor/skills/`. Cursor also discovers compatible skills in `.claude/skills/` and `.codex/skills/`. Start Agent in the project, type `/product-opportunity-review` or attach it with `@`. MakerLine's `AGENTS.md` and `.cursor/rules/` continue to provide project-wide rules. See [Cursor skills](https://cursor.com/help/customization/skills).

## GitHub Copilot and other tools

GitHub Copilot supports project skills in `.github/skills/`, `.claude/skills/` or `.agents/skills/`, and personal skills in `~/.copilot/skills/` or `~/.agents/skills/`. Put the entire skill folder there, start a supported Copilot agent session, and ask it to use `/product-opportunity-review`. See [GitHub's skill instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).

For another AI tool, first check whether it supports the [Agent Skills format](https://agentskills.io). If it does, place the full skill directory in its documented skills location. If it only accepts persistent rules, point its rule file at the relevant MakerLine workflow document and `AGENTS.md`; do not paste all 26 skills into an always-on prompt. The existing [agent adapter guide](../template/docs/kit/AGENT-ADAPTERS.md) covers how MakerLine project rules reach other coding tools. Test the first run: can the tool see the skill, read the project files, execute the renderer, and resume from `HANDOFF.md`?

## Verify an installation

1. Start a **new** chat/session after installation.
2. Ask: “Which MakerLine skills are available?” and check for `product-opportunity-review`.
3. Open a project folder and run a no-code prompt: “Review this half-built product; create the stage-aware progress report.”
4. Check for `docs/product/opportunity/REVIEW.json` and `index.html`. Open the HTML in a browser.

Installing a skill does not automatically authorize deployment, publishing, sending messages or giving an AI tool private client data.
