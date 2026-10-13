# Connected tools (MCP)

Same servers are configured for all three tools: Claude Code `.mcp.json`, Cursor `.cursor/mcp.json`, Codex `.codex/config.toml`. (JSON files can't hold comments, so they're explained here.) In Claude Cowork/desktop, connect the same services from Settings → Connectors instead.

| Server | Why | Setup |
|---|---|---|
| context7 | Current library docs → fewer made-up APIs | none |
| playwright | Real browser: screenshots, accessibility tree, design-qa | none (downloads a browser on first use) |
| figma | Read frames, variables, components; sync design tokens | sign in to Figma when prompted |
| supabase (optional) | Inspect schema, run read-only SQL, check RLS | add manually — see below |
| github (optional) | Issues, PRs, CI status | Claude/Cursor: add `https://api.githubcopilot.com/mcp/` with OAuth; or use the `gh` CLI |
| vercel (optional) | Deployments, logs | `https://mcp.vercel.com` with OAuth |

## Supabase — add read-only, one project only
```json
"supabase": {
  "command": "npx",
  "args": ["-y", "@supabase/mcp-server-supabase@latest", "--read-only", "--project-ref=YOUR_PROJECT_REF"],
  "env": { "SUPABASE_ACCESS_TOKEN": "${SUPABASE_ACCESS_TOKEN}" }
}
```
Keep `--read-only` and point it at a **development** project, never production. Put the token in your shell profile, never in a committed file.

## Token tip
Every connected server adds its tool list to the AI's context. Keep only what the current phase needs (e.g. Figma during design, Supabase during backend work) and disable the rest.
