# Privacy and data handling

This page covers the **makerline** and **makerline-idea** Claude plugins and this website. Short version: the plugins are instructions and checklists that run inside your own Claude session. They have no server, collect nothing and send nothing to the author.

## What the plugins touch

| What | When | Where it goes |
|---|---|---|
| Files in the folder you connect | Every run: the skills read and write Markdown and HTML documents there (for example `docs/product/ONE_PAGER.md`) | Stays in your folder. The kit never asks for files outside it |
| Your idea and your answers | When you type them | Your Claude conversation, under your Claude account's terms |
| Web search queries | During evaluation and competitor research | The web search and fetch tools in your Claude session. Queries describe the market and competitors, not you |
| A local check script | The Idea Pack runs `check_idea_pack.py` to check the documents before you see them | Runs on your machine or Claude's sandbox; reads only the pack's files; makes no network requests |
| Connectors (GitHub, Figma, Vercel, Supabase, Notion, Linear) | Only if you choose to connect them in Claude | Those services, under their own terms. Every skill works without them. They are listed in each plugin's `CONNECTORS.md` |

## What the plugins never do

- No analytics, telemetry or tracking
- No server run by the author; nothing is sent to the author
- The skills keep project memory in your folder (`docs/`), not in Claude's memory or chat history, and never ask Claude to search past chats
- No secrets: the rules forbid putting keys, passwords or users' personal data in prompts or documents
- Connectors read first; they only write (create a ticket, push, deploy) when you ask in the chat

## The full MakerLine, when you build

Projects created with the full kit include safety settings that block reading `.env` secret files and destructive commands in Claude Code. The apps you build are yours: the kit's standards ask for the minimum personal data, and for verifiable parental consent before any children's data.

## This website

Static pages on GitHub Pages. No cookies, no scripts, no analytics, no external fonts. GitHub, as the host, may keep standard server logs under [GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Contact

Questions or concerns: [open an issue on GitHub](https://github.com/sairam5294/makerline/issues/new/choose). To report a security problem privately, follow [SECURITY.md](../../SECURITY.md).
