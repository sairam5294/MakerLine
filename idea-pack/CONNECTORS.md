# Connectors

## How tool references work

Skill files use `~~category` as a placeholder for whatever tool you connect in that category — `~~source control` means GitHub, GitLab or any other repository host with an MCP server. Every skill works **standalone** without connectors; connectors add live data and let the kit act in your tools.

`.mcp.json` pre-configures the servers below; any MCP server in the same category works. Connecting is your choice, per tool, under the plugin's **Connectors** tab.

## Connectors for this plugin

| Category | Placeholder | Included server | Other options | Used by |
|---|---|---|---|---|
| Source control | `~~source control` | GitHub | GitLab, Bitbucket | build-feature, quality-review, project-setup, ship-checklist, portfolio |
| Design | `~~design` | Figma | Penpot | design-direction, design-system, design-qa, name-product (brand) |
| Hosting | `~~hosting` | Vercel | Netlify, Cloudflare | ship-checklist, post-launch, project-setup (previews, env) |
| Database | `~~database` | Supabase | Neon, Firebase | engineering-docs, build-feature, ship-checklist (RLS, backups) |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Google Drive | evaluate-idea, new-idea, engineering-docs |
| Project tracker | `~~project tracker` | Linear | Jira, Asana, GitHub Issues | plan-build, build-feature, post-launch |
| Chat | `~~chat` | — | Slack, Microsoft Teams | handoff, post-launch, ship-checklist |
| Product analytics | `~~product analytics` | — | PostHog, Amplitude, Mixpanel | evaluate-idea (existing products), post-launch |
| Monitoring | `~~monitoring` | — | Sentry, Datadog | post-launch, ship-checklist |

## Rules

- Secrets, keys and users' personal data never go into prompts or documents, whatever is connected.
- A connector reads first; writes (creating tickets, pushing, deploying) happen only when you ask in chat.
- If a connector isn't available, the skill says so once and continues standalone — it never asks you to connect one.
