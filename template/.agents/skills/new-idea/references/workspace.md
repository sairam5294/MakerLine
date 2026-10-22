# Product workspace — the folder around the repo

One standard folder per product, so every project looks the same to you and to every AI tool (Claude, ChatGPT, Cursor, Codex). The repo inside it stays the single home of everything a tool reads; the workspace holds what doesn't belong in git.

## 1. The tree

```
<Product>/                  e.g. ~/Desktop/Code_Projects/Lekka
├── README.md               what it is, where everything lives, links (Figma, hosting, database, stores)
├── AGENTS.md               ≤ 15 lines for every AI tool → points into the repo
├── CLAUDE.md               one line: @AGENTS.md
├── STATUS.md               pointer to the repo's docs/product/STATUS.md (never a second status)
├── 00_inbox/               unfiled AI outputs from any tool — emptied at each handoff
├── 01_research/            interviews, surveys, competitor screenshots, raw evidence (private)
├── 02_brand/               source files and explorations (splash/, drafts) — final logo SVGs the app uses: repo design/brand/
├── 03_design/              mockups/, assets/, exports/ + LINKS.md for Figma
├── 04_repos/<repo-name>/   git clones — docs/product/, design/tokens.json, tests live HERE
├── 05_qa/                  device and screen-reader recordings, bug screenshots, tester reports
├── 06_releases/<version>/  store screenshots, release notes, signed builds (not in git)
├── 07_launch/              landing copy, store listing, social posts
├── 08_ops/                 ACCOUNTS.md (service names only), costs exports, legal (privacy, terms, licences)
├── 90_reference/           outside material you read but didn't make
├── 98_bin/                 things to delete — only the owner deletes
└── 99_archive/             YYYY-MM-DD-<what>/ copies made before deleting or replacing anything
```

## 2. Rules

| Rule | Why |
|---|---|
| **The repo is the only home** of product docs (`docs/product/`), engineering docs (`docs/`), design tokens (`design/`) and tests. No `product_docs/` or `design_system/` copy outside it. | Two copies drift; tools read the wrong one |
| **One status.** `STATUS.md` lives in the repo; the workspace file only points to it. No dated status files (`STATUS-22-Oct.md`). | Dated copies multiply and cost tokens |
| **Create a folder when it's first needed.** The names and numbers are fixed; empty folders are not required. Always present: the four root files, `00_inbox/`, `04_repos/`, `98_bin/`, `99_archive/`. | An idea doesn't need 15 empty folders |
| **Idea stage:** create `04_repos/<slug>/` at once as a private, docs-only repo. MakerLine writes `docs/product/` there from the first run. | Docs start in their final place; nothing moves at approval |
| **Several repos** (app + admin, product + docs): one folder each under `04_repos/`; the workspace README lists them; each repo's `CONTEXT_INDEX.md` names the others. | One map for multi-repo products |
| **Never secrets.** `08_ops/ACCOUNTS.md` lists services, plans and which email owns them — never passwords, keys or tokens. Keys live in a password manager and the hosting dashboards; `.env` only inside a repo, git-ignored. | Workspace folders often sync to iCloud or Drive |
| **Archive before delete.** Copy to `99_archive/YYYY-MM-DD-<what>/`, move the original to `98_bin/`; the owner empties the bin. | Nothing is lost by an AI tool |

## 3. Naming

- Folders: `NN_lowercase_snake` (`01_research`), inside them `lowercase-kebab` (`splash-v2/`). No spaces, no tool names (`Claude outputs` → `00_inbox`).
- Dated files: `YYYY-MM-DD-what.md` — it sorts. Branches keep `<type>/<Mon>-<DD>-<summary>`.
- Canonical docs in CAPS (`README.md`, `STATUS.md`); everything else lowercase.
- Number gaps are fine; never renumber an existing folder.

## 4. Several AI tools, one memory

No extra "tool" or "memory" file. The repo already has one rulebook and four memory layers:

| File (in the repo) | Answers | Rule |
|---|---|---|
| `AGENTS.md` (+ `CLAUDE.md`, `.cursor/rules/`) | How do we work here? | One rulebook; tool files only point to it |
| `docs/product/STATUS.md` | Where are we, and who is writing? | One live file; `Writing:` line names the tool and branch |
| `docs/product/HANDOFF.md` | What did the last session do; what's next? | Overwritten at every handoff, ≤ 40 lines |
| `docs/MEMORY.md` | What must every session know that lives nowhere else? | ≤ 60 lines, condensed, never appended forever |
| `docs/product/DECISIONS.md` | Why did we choose X? | Append-only, `D-xx` IDs; read only when needed |
| `docs/product/CONTEXT_INDEX.md` | Which files does this task need? | Updated by `handoff` |
| `docs/CONTEXT_PACK.md` | Everything a tool that can't open the folder needs | Regenerated at handoff, never edited |

- **Claude Code and Cursor** open the repo (or the workspace) and follow AGENTS.md.
- **ChatGPT** gets `CONTEXT_PACK.md` as a file in a ChatGPT Project, refreshed at each handoff. Its answers are saved to `00_inbox/`; the next Claude or Cursor session files them and records decisions.
- **One writer per branch.** Before writing, a tool checks `Writing:` in STATUS; it sets it when it starts and clears it at handoff.
- **Built-in tool memory** (Claude memory, ChatGPT memory, Cursor memories) doesn't sync between tools — use it for personal preferences only, never for project state.

## 5. Reading order (keeps tokens low)

1. `HANDOFF.md` → `STATUS.md` → `docs/MEMORY.md`.
2. `CONTEXT_INDEX.md` → only the files listed for this task type.
3. Never scan `02_brand/`, `03_design/`, `05_qa/`, `06_releases/`, `90_reference/`, `98_bin/`, `99_archive/` unless the task names a file there. Claude Code also loads `CLAUDE.md` from parent folders, so the workspace AGENTS.md stays ≤ 15 lines.

## 6. Moving an existing product in

Opt-in, owner-approved, never automatic: `scripts/new-workspace.sh <folder> [--name <Name>] --adopt <existing-repo-path>` prints the move it would make; nothing moves without `--apply`. It never overwrites: if `04_repos/<repo>` exists, or the workspace would sit inside the repo, it stops and changes nothing. Then move loose docs that duplicate repo files to `98_bin/` (after archiving).

## 7. Root file skeletons

`scripts/new-workspace.sh` writes these blocks; with no shell, create them by hand from here.

<!-- file: README.md -->
```
# {{Name}} — workspace

_One line: what it is and who it's for (fill in)._

| What | Where |
|---|---|
| Repos | `04_repos/{{slug}}/` |
| Status | `04_repos/{{slug}}/docs/product/STATUS.md` |
| Design (Figma) | `03_design/LINKS.md` |
| Hosting, database, stores | `08_ops/ACCOUNTS.md` (names only, no secrets) |

Standard: MakerLine product workspace (new-idea `references/workspace.md`). Created {{date}}.
```
<!-- end -->

<!-- file: AGENTS.md -->
```
# AGENTS.md — {{Name}} workspace

This folder holds one product. Code and every doc a tool needs are in the repo(s) under `04_repos/`.
1. Work inside `04_repos/{{slug}}/` and follow its AGENTS.md.
2. Start with its `docs/product/HANDOFF.md`, `STATUS.md` (check `Writing:`), `docs/MEMORY.md`, then only what `CONTEXT_INDEX.md` lists for the task.
3. Don't read `02_brand/`, `03_design/`, `05_qa/`, `06_releases/`, `90_reference/`, `98_bin/`, `99_archive/` unless the task names a file there.
4. Save outputs that have no home yet to `00_inbox/YYYY-MM-DD-<tool>-<topic>.md`.
5. Never delete: copy to `99_archive/YYYY-MM-DD-<what>/`, move the original to `98_bin/`.
6. Never write secrets anywhere in this folder.
```
<!-- end -->

<!-- file: CLAUDE.md -->
```
@AGENTS.md
```
<!-- end -->

<!-- file: STATUS.md -->
```
# Status — {{Name}}

The live status is `04_repos/{{slug}}/docs/product/STATUS.md`. Don't keep a second one here.
```
<!-- end -->
