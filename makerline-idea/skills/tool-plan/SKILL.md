---
name: tool-plan
description: Split the work across my AI subscriptions. Assigns each job to the AI subscriptions and free tiers the owner has (Claude, ChatGPT, Cursor, Codex, Gemini, Copilot, GitHub/Vercel/Supabase…) so each tool does what it's best at and limits aren't hit → TOOL_PLAN.md. Trigger with "which tool should I use for…", "I have ChatGPT and Claude, how do I split the work?", "I keep hitting limits", at kickoff, or after approval.
argument-hint: "<your tools and plans, or nothing to be asked once>"
---

# /tool-plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Write the split: which AI tool does which job on this project, and how context moves between them.

**Why:** most solo builders pay for two or three AI tools and use them interchangeably, so they hit limits, lose context between tools and pay twice for the same work. A written split — who does what, and how context moves between them — fixes both.

## Usage

```
/tool-plan                                        # asks once what you have, then writes the split
/tool-plan I have Claude Pro, ChatGPT Plus and Cursor free
/tool-plan I keep hitting limits by mid-afternoon
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                        TOOL PLAN                             │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ One round of questions: subscriptions, accounts, where    │
│    you work, which limits you hit                            │
│  ✓ Plans and limits checked on vendors' official pages       │
│  ✓ Every phase and recurring job → primary + fallback tool   │
│  ✓ Handoffs for tools that can't read the repo               │
│  ✓ Daily rhythm, limit playbook, monthly cost → COSTS.md     │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Source control: confirm which tools already have repo     │
│    access and which need CONTEXT_PACK.md                     │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `docs/product/OWNER.md` ("Accounts & tools") — skip whatever it already answers.
- `references/tool-routing.md` (default job split) and `references/tool-plan-template.md`.
- `docs/product/COSTS.md` for the monthly cost of the stack.
- No gate: runs anytime — at kickoff, after approval, or whenever subscriptions change.

## Workflow

1. **Ask once** (skip what `docs/product/OWNER.md` already says), as one multiple-choice round:
   - AI subscriptions and plan level: Claude (free / Pro / Max / Team) · ChatGPT (free / Plus / Pro / Team) · Cursor (free / Pro) · Codex · GitHub Copilot · Gemini · local models (Ollama) · other.
   - Build and hosting accounts and their tier: GitHub · Vercel · Supabase · Figma · Expo/EAS · Apple / Google developer accounts.
   - Where they work: Claude app/desktop · Claude Code (terminal) · Cursor · VS Code · browser only.
   - Which limits they hit today, and roughly when (e.g. "Claude by mid-afternoon").
   - Save the answers to OWNER.md ("Accounts & tools"). Owner unavailable: assume the free tier of any tool whose plan isn't known, mark it `[Default]`, and add a CLARITY question — the split is provisional until confirmed.
2. **Check current plans and limits** in the vendors' official pages before recommending (they change often; never quote a limit from memory). Note anything you couldn't verify.
3. **Split the jobs** with `references/tool-routing.md`: map every phase and recurring task of this project to a primary tool and a fallback, based on what the owner actually has. Keep the core rule: one tool owns a document at a time; the repo (`AGENTS.md`, `docs/`) is the shared memory every tool reads.
4. **Handoffs.** For each tool that can't read the repo (e.g. ChatGPT in the browser), define the context it gets — `docs/CONTEXT_PACK.md` (made by project-setup) or the one-pager — and how its output comes back (paste into a named file, then the owning tool reviews it).
5. **Limits and cost.** Daily rhythm (heavy reasoning early in the window, mechanical edits on the cheaper tool), what to do when a limit hits (switch to the fallback for that job, never to a tool without the context), and the monthly cost of the stack in COSTS.md.
6. **Write and present.** `docs/product/TOOL_PLAN.md` from `references/tool-plan-template.md`; present the split as one table; log the choice in DECISIONS.md.

## Output

| File | What | Size |
|---|---|---|
| `docs/product/TOOL_PLAN.md` | what you have, the job split (primary + fallback), handoffs, daily rhythm, limit playbook | per `tool-plan-template.md` |
| `docs/product/OWNER.md` | "Accounts & tools" updated | — |
| `docs/product/COSTS.md` | monthly cost of the tool stack | — |
| `docs/product/DECISIONS.md` | the split logged | one row |

Presentation to the owner: the split as one table (job · primary · fallback · why), then one line on what to do when a limit hits.

## If connectors available

If **~~source control** is connected:
- Note which tools can read the repo directly and which need `docs/CONTEXT_PACK.md`; put that in the handoffs section.

## Rules

- Recommend from what the owner has — never push a new subscription unless a job truly can't be done otherwise, and then say what it costs and the free alternative.
- Never quote a plan limit from memory; check the vendor's page and note what you couldn't verify.
- Secrets and users' personal data never go into any AI tool.
- One tool owns a document at a time; the repo is the shared memory every tool reads.
- Re-run when the owner's subscriptions change; `standards-refresh` re-checks the routing quarterly.

## Tips

1. Answer the "which limits, and when" question honestly — it decides the daily rhythm.
2. Do heavy reasoning (evaluation, specs, reviews) early in your usage window; save mechanical edits for the cheaper tool.
3. When a limit hits, switch to the fallback for that job and start from HANDOFF.md — never redo work that's already in the repo.

## Related

- Offered at: `product-kickoff` (kickoff, and first in "set it all up") · Feeds: `project-setup` (CONTEXT_PACK.md), `handoff`, `standards-refresh`
- Reads: `references/tool-routing.md`, `tool-plan-template.md`; `docs/product/OWNER.md`, `COSTS.md`
