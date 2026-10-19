---
name: tool-plan
description: Product Kit AI-tool plan — asks which AI subscriptions and free tiers the owner has (Claude, ChatGPT, Cursor, Codex, Gemini, Copilot, GitHub/Vercel/Supabase…) and splits the project's jobs across them so each tool does what it's best at and limits aren't hit → TOOL_PLAN.md. Use at kickoff, after approval, or for "which tool should I use for…", "I have ChatGPT and Claude, how do I split the work?", "I keep hitting limits".
---

# Tool plan

Why: most solo builders pay for two or three AI tools and use them interchangeably, so they hit limits, lose context between tools and pay twice for the same work. A written split — who does what, and how context moves between them — fixes both.

## Steps
1. **Ask once** (skip what `docs/product/OWNER.md` already says), as one multiple-choice round:
   - AI subscriptions and plan level: Claude (free / Pro / Max / Team) · ChatGPT (free / Plus / Pro / Team) · Cursor (free / Pro) · Codex · GitHub Copilot · Gemini · local models (Ollama) · other.
   - Build and hosting accounts and their tier: GitHub · Vercel · Supabase · Figma · Expo/EAS · Apple / Google developer accounts.
   - Where they work: Claude app/desktop · Claude Code (terminal) · Cursor · VS Code · browser only.
   - Which limits they hit today, and roughly when (e.g. "Claude by mid-afternoon").
   Save the answers to OWNER.md ("Accounts & tools").
2. **Check current plans and limits** in the vendors' official pages before recommending (they change often; never quote a limit from memory). Note anything you couldn't verify.
3. **Split the jobs** with `references/tool-routing.md`: map every phase and recurring task of this project to a primary tool and a fallback, based on what the owner actually has. Keep the core rule: one tool owns a document at a time; the repo (`AGENTS.md`, `docs/`) is the shared memory every tool reads.
4. **Handoffs:** for each tool that can't read the repo (e.g. ChatGPT in the browser), define the context it gets — `docs/CONTEXT_PACK.md` (made by project-setup) or the one-pager — and how its output comes back (paste into a named file, then the owning tool reviews it).
5. **Limits and cost:** daily rhythm (heavy reasoning early in the window, mechanical edits on the cheaper tool), what to do when a limit hits (switch to the fallback for that job, never to a tool without the context), and the monthly cost of the stack in COSTS.md.
6. Write `docs/product/TOOL_PLAN.md` from `references/tool-plan-template.md`; present the split as one table; log the choice in DECISIONS.md.

Rules: recommend from what the owner has — never push a new subscription unless a job truly can't be done otherwise, and then say what it costs and the free alternative. Secrets and users' personal data never go into any AI tool. Re-run when the owner's subscriptions change; `standards-refresh` re-checks the routing quarterly.
