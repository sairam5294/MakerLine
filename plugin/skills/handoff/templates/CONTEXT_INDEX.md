# Context index — <product>

<!-- HOW TO FILL: a thin map, not a story. Every AI tool reads AGENTS.md, then this file, then only the
files listed for its task. Update the "Field" table at every handoff (the handoff skill does this) and
run `context_check.py check .`. Paths are relative to the project root; add #section to point at part of a file. -->

| Field | Value |
|---|---|
| Product | <name> |
| Stage | <idea / partial / prelaunch / delayed / live> |
| Objective | <the one outcome the project is working toward now> |
| Active task | <T-xx and a few words, or "none"> |
| Current decision | <D-xx: the decision now in force> |
| Next action | <the exact next step, one line> |
| Next tool | <Claude / ChatGPT / Cursor / owner> |
| Owner | <who approves and merges> |
| Verified commit | <short commit hash the fields above were checked against> |
| Updated | <YYYY-MM-DD> |

## Read by task

| Task type | Read (in order) | Notes |
|---|---|---|
| Any session start | AGENTS.md, docs/product/STATUS.md, docs/product/HANDOFF.md | Always, and nothing more |
| Strategy | docs/product/DECISIONS.md, docs/product/ASSUMPTIONS.md, docs/product/opportunity/REVIEW.json | Opportunity review, investment decisions |
| Build a task | docs/product/PLAN.md | Then the task's own files and standards |
| Review | docs/product/DECISIONS.md | Then the diff and one standard file per reviewer |

## Privacy tiers

Default is **project** (repo collaborators and the AI tools that open this folder). **public** may go in a
context pack for any tool. **private** never leaves this machine and never goes in a pack.

| Path | Tier |
|---|---|
| docs/product/STATUS.md | public |
| docs/product/research/ | project |
| .env | private |
