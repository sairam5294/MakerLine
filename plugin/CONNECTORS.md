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

## What the kit reads and writes — know before you connect

The kit has no servers of its own and sends no telemetry. A connector runs under **your** account and permissions; the kit only asks it to do the things below. Reads happen when a skill needs them; every write waits for you to ask in chat.

| Connector | The kit reads | The kit may write (only when you ask) | Never |
|---|---|---|---|
| GitHub | repo files, branches, PR diffs and comments, CI status, issues | branches, commits, PRs, PR review comments, issues | merge to `main`, change repo settings or branch protection, delete branches, read secrets |
| Figma | frames, components, variables, screenshots of nodes you point to | new files and frames (wireframes, logo, tokens) in a file you name | delete or overwrite your existing frames, change sharing |
| Vercel | projects, deployments, build and runtime logs, env var **names** | a preview deployment, an env var you dictate | promote to production, read env var **values**, change domains or billing |
| Supabase | schema, RLS policies, migrations list, advisors | a migration on a **development** branch/project you confirm | run SQL on production, read user rows, change auth or billing settings |
| Notion | pages and databases you share with the integration | a page you ask for (e.g. the one-pager) | edit or delete existing pages |
| Linear | issues, projects, cycles | issues from PLAN.md tasks or review SHOULDs | close, delete or reassign others' issues |
| Chat (Slack, Teams) | — | a message you've approved, word for word | read DMs or channels you didn't name |
| Analytics, monitoring | aggregate metrics and error summaries | — | export or store individual users' events or personal data |

Data that leaves your machine goes only to the service you connected, under its own terms. Revoke a connector anytime in the plugin's **Connectors** tab or the service's settings.

## Rules

- Secrets, keys and users' personal data never go into prompts or documents, whatever is connected.
- A connector reads first; writes (creating tickets, pushing, deploying) happen only when you ask in chat.
- If a connector isn't available, the skill says so once and continues standalone — it never asks you to connect one.
