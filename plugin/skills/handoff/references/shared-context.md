# Shared context for every AI tool

One project, several AI tools (for example Claude, ChatGPT and Cursor). This contract keeps them working from the same facts without re-reading the whole project or re-doing research. It adds two small files to what MakerLine already writes and one script that checks them. No database, no service: files, IDs and checks.

## 1. The files

| File | Role | Who updates it, and when |
|---|---|---|
| `AGENTS.md` | Project rules every tool follows | Owner; rarely |
| `docs/product/STATUS.md` | Phase, task, approval (≤ 60 lines) | At each task change |
| `docs/product/HANDOFF.md` | Last session: done, next, gotchas (≤ 40 lines) | Overwritten at every handoff |
| `docs/product/CONTEXT_INDEX.md` **new** | The state in ten fields, and which files to read for each kind of task | At every handoff |
| `docs/product/DECISIONS.md` | Decisions with stable IDs (`D-01`) and evidence IDs | Append only; a reversed decision gets a new row that names the old ID |
| `docs/product/ASSUMPTIONS.md` **new** | What must be true (`A-01`), what could go wrong (`R-01`), evidence, review-by date; decision rules | When evidence or a decision changes |
| `docs/product/opportunity/REVIEW.json` | The current strategic review, sources `S1…` | `product-opportunity-review` |
| `docs/CONTEXT_PACK.md` | Generated export for a tool that can't open the folder | Regenerated, never edited |

Templates: `templates/CONTEXT_INDEX.md` and `templates/ASSUMPTIONS.md` beside the handoff skill. Copy them; don't move existing content into them.

## 2. Stable IDs

| Prefix | Meaning | Lives in |
|---|---|---|
| `D-01` | Decision | DECISIONS.md |
| `A-01` / `R-01` | Assumption / risk | ASSUMPTIONS.md |
| `S1` | Source (dated, opened) | REVIEW.json `sources`, or `docs/product/research/` as `R1` in Idea Packs |
| `T-01` | Build task | PLAN.md |

IDs never change or repeat. Cite them instead of copying the fact: "per D-04" costs a few tokens; re-explaining D-04 costs hundreds and drifts.

## 3. Privacy tiers

| Tier | Who may see it | In a context pack? |
|---|---|---|
| public | Anyone | Yes |
| project (default) | Repo collaborators and the AI tools that open the folder | Yes, for the owner's own tools |
| private | Only this machine | Never |

Mark tiers in the index's "Privacy tiers" table. Secrets, personal data, named research participants and real customer records are always private and never belong in `docs/product/` at all. `pack` refuses a file that looks like it holds a secret.

## 4. Start and end of every session

**Start:** confirm the project folder and branch → read `AGENTS.md`, then `CONTEXT_INDEX.md` → run `context_check.py check .` → read only the "Any session start" row plus your task's row → open other files only when a question needs them.

**End (the handoff skill):** write `HANDOFF.md` → append new decisions and assumptions with IDs → update the index's ten fields, including `Verified commit` (after committing) and `Next tool` → run `check` again.

**Tools that can't open the folder** (ChatGPT in the browser, a phone chat): run `context_check.py pack . --task "<task type>" --tool ChatGPT`, attach `docs/CONTEXT_PACK.md`, and paste the tool's "Handoff back" section into the project with a local tool, which records it and re-runs `check`.

**One writer at a time.** One tool owns a file or task at a time. Parallel code work uses `scripts/worktree.sh`; parallel research writes separate files that one tool then links.

## 5. What `check` catches

Missing or empty index fields · index paths that don't exist · a `Verified commit` that isn't on this branch, or context files that changed after it · HANDOFF over 40 lines, STATUS over 60 · duplicate or malformed decision and assumption IDs · assumptions without an owner or a review-by date, and expired evidence · a HANDOFF newer than the index.

## 6. Context recovery test

The direct test of the contract: a tool that has **only** the official context answers ten questions. Score with `context_check.py score answers.md key.json`. Each project keeps its answer key outside the project folder, so the tool being tested can't read it (format: `evals/context-recovery/README.md` in the kit). Run it at least once per tool, and after changing the contract.

| Case | Lost-context situation | The receiving tool must answer |
|---|---|---|
| C01 | New tool, first session | What is the product, and what stage is it in? |
| C02 | Switched tools mid-task | What is the active task, and who owns it? |
| C03 | Two weeks away | What is the current strategic decision, and how confident is it? |
| C04 | Owner asks "why?" | Which evidence or source IDs support that decision? |
| C05 | Before spending more | Which assumptions or risks matter most, and when do they expire? |
| C06 | About to write code | Is the idea approved, and what needs the owner's approval? |
| C07 | Picking up a half-done session | What was done last session, and what is half-done? |
| C08 | "What now?" | What is the exact next action, and which tool does it? |
| C09 | Tempted to revisit an old idea | What was rejected or tried already, and why? |
| C10 | Writing a pull request | Which project rules constrain the work (branches, accessibility, secrets)? |

Record each run in the kit's `evals/results.md` (context-recovery table): tool, path (folder or pack), score, wrong claims, tokens, time.
