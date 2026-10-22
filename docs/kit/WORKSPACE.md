# Product workspace

One standard folder per product: the repo(s) in `04_repos/`, plus what doesn't belong in git — research, brand, design files, QA recordings, release files, launch copy, an inbox for AI outputs, an archive and a bin.

- **The standard** (tree, rules, naming, several AI tools, reading order): [`plugin/skills/new-idea/references/workspace.md`](../../plugin/skills/new-idea/references/workspace.md) — one source, shipped with both plugins.
- **Create one:** `./scripts/new-workspace.sh ~/Projects/MyApp [--name "My App"] [--full]`
- **Move an existing repo in:** `./scripts/new-workspace.sh ~/Projects/MyApp --adopt ~/Code/my-app` (preview), then add `--apply`.
- **Skills that use it:** new-idea (where the first docs go), handoff (empties `00_inbox/`, clears `Writing:`), project-setup (STRUCTURE's Workspace section), ship-checklist and post-launch (release and launch files), tool-plan (ChatGPT's context pack and inbox), portfolio (finds repos under `04_repos/`).
