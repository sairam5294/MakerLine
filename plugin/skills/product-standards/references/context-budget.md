# Context & Token Budget

Tokens = cost + quality. Most tokens are not the documents — they are the conversation re-read on every tool call. A 50-call run re-reads its history 50 times.

## 1. MUST (every phase)
- Read only what the task needs: AGENTS.md → HANDOFF/STATUS → the one task or story → the 1–2 standards it touches. Resume from STATUS.md + HANDOFF.md only; never scan `docs/product/` to work out where you are.
- Search before reading (`rg`, file ranges). Never read `node_modules`, lockfiles, build output, generated native folders or media.
- Subagents return ≤ 300-word summaries; reviewers get the diff + their standard files only.
- Living docs stay short: HANDOFF ≤ 40 lines, STATUS ≤ 60, AGENTS.md ≤ ~120.
- One task per session. Long or off-topic session → `handoff`, then start fresh.
- More than one AI tool: start from `docs/product/CONTEXT_INDEX.md` and read only your task's row (the `handoff` skill's shared-context guide, full kit).
- Show the changed part, not whole files. Prefer tables over prose in docs the AI rereads.

## 2. Idea Pack depth (pick before starting; default Standard)
| Mode | Use when | Produces | Research budget | Target |
|---|---|---|---|---|
| **Quick** — one guide: `../../evaluate-idea/references/quick-run.md` | "Worth a weekend?" | brief, CLARITY, short EVALUATION (500–1,000 prose words), COMPETITORS Lite (`../../evaluate-idea/references/competitors-lite.md`), ONE_PAGER | ≤ 4 searches, ≤ 1 page read (batched; no snippet trade) | ≤ 12 tool calls · ~70–100k target (measured 120k at 0.12.1 with 7 searches, 4 reads, 19 calls) |
| **Standard** | Deciding whether to build | + DESIGN_DIRECTION, wireframes (≤ 8 screens), PRD draft | ≤ 15 searches, ≤ 8 page reads | ≤ 45 tool calls · ~120–150k |
| **Deep** | Before spending money or pitching | + all four competitor rings, 12+ screens, Figma, payer research | ≤ 30 searches | ~250k+ |

Searches that return bare links (no snippets), Standard and Deep: two unused searches buy one extra page read, so search in two batches. Quick has no such trade. A redirect that lands on the page you wanted counts as one read.

## 3. Size caps (words, tables included; WARNs in `check_idea_pack.py`)
| Document | Quick | Standard | Deep |
|---|---|---|---|
| EVALUATION.md | 1,400 | 3,000 | 4,500 |
| COMPETITORS.md | 450 | 1,200 | 2,000 |
| DESIGN_DIRECTION.md | — | 1,500 | 2,500 |
| PRD.md (draft) | — | 2,000 (full stories for Musts, one line per Should/Could) | 3,000 |
| CLARITY.md | 600 | 1,000 | 1,500 |
| ONE_PAGER.md | 450 | 550 | 550 |

## 4. Token rules for the Idea Pack (MUST)
1. **Research once, cite everywhere.** Facts go to `docs/product/research/<topic>.md` with IDs (R1, R2…); other docs cite the ID. Facts from the kit's own references cite the file (e.g. `accessibility-law-summary.md`) instead of a URL.
2. **One home per fact.** Competitor detail lives in COMPETITORS (EVALUATION §6 ≤ 150 prose words). The PRD links personas, flows and screens by ID.
3. **Snippets first.** A snippet with figure and date is enough to cite. Open a page only for a number or quote you need; prefer round-up pages. Stop a ring when two sources agree. Out of budget → CLARITY question, not a guess.
4. **Copy templates, don't read them.** `cp` the template, read its HOW TO FILL comment (top of file) and one example, then write the filled document. Short templates (brief, CLARITY, STATUS, DECISIONS, COSTS, one-pager, README index) and the wireframe template have no HOW TO FILL comment — read each once in full, never twice.
5. **Write once, check with a script.** Write each document in one call from your notes (draft the section lengths against the cap first); don't re-read your output — run `check_idea_pack.py` (with `--only` for the files this phase wrote) and fix only what it flags.
6. **Small subagent briefs.** Each perspective agent gets the brief's **Idea card** (§0, ≤ 120 words) + its one reference + the research file, not the whole brief. Their searches count inside the budget. No subagents → play them inline: ≤ 5 lines each (Quick), ≤ 10 (Standard).
7. **Few, large tool calls.** One call per document — or several small documents (STATUS, DECISIONS, COSTS, README index) in one shell call; all searches for a ring in one turn; every check in one shell call.
8. **Raw research stays out of the conversation.** Write findings to the research file; carry forward only R-ids and one-line facts.
9. **Accessibility law:** read `accessibility-law-summary.md` at the idea stage; open the full `accessibility-law.md` only for Deep or `ship-checklist`, and then grep the launch market's rows.

## 5. Model routing per step (when the tool lets you choose)
| Step | Model |
|---|---|
| Interview questions, filling templates, tables, one-pager, index, formatting, renames, small UI/copy edits | **fast** (Claude Sonnet/Haiku, GPT-6 Luna, Gemini Flash, Cursor auto — names change; `standards-refresh` re-checks them) |
| Market research, checklist reviews (`market-researcher`, `qa-engineer`, `accessibility-auditor`, `ux-reviewer`) | **fast** |
| Evaluation verdict and scorecard, devil's advocate, architecture, security review, build tasks touching auth, data, payments or AI | **strongest** |

Agents declare `model:` in their frontmatter. Inline, switch the model in chat if the tool allows; otherwise keep the fast steps short.

## More
After approval — which doc to load per task, research budget per phase, measured costs, local models: `context-budget-more.md`.
