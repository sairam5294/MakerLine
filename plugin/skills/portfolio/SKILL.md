---
name: portfolio
description: Show all my projects and what to do next. Covers phase, approval gate, next step, blockers, staleness — plus idea outcomes → portfolio/PORTFOLIO.md + index.html. Trigger with "my projects", "portfolio", "what am I working on", "which project next?", or when choosing what to work on.
argument-hint: "<folders to scan, or nothing for ~/Projects and ~/Documents>"
---

# /portfolio

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Give the owner one table of every project and one recommendation for what to do next.

## Usage

```
/portfolio                       # scans ~/Projects and ~/Documents
/portfolio ~/Code ~/Side         # scan these folders
/portfolio which project next?
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                         PORTFOLIO                            │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ scripts/portfolio.py → index.html + PORTFOLIO.md          │
│  ✓ No shell: build the table from each STATUS.md             │
│  ✓ Active · blocked · stale (> 14 days) · awaiting approval  │
│  ✓ One recommendation, using OUTCOMES.md                     │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Source control: last commit dates for staleness           │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- Kit folder from `docs/product/OWNER.md`; optional folders to scan (default ~/Projects and ~/Documents).
- Each project's `docs/product/STATUS.md`.
- `portfolio/OUTCOMES.md` for parked/launched ideas.

## Workflow

1. **Run the script** if a shell is available: `python3 <kit>/scripts/portfolio.py [folders]` (kit folder from `docs/product/OWNER.md`; default scans ~/Projects and ~/Documents).
   - It writes `portfolio/index.html` (open in a browser) and `portfolio/PORTFOLIO.md`.
2. **No shell:** read each project's `docs/product/STATUS.md` you can reach and build the same table.
3. **Summarise** in ≤ 8 lines: what's active, what's blocked, what's stale (> 14 days), which projects wait on the owner's approval, and one recommendation (e.g. "park X, it missed its kill criteria").
   - Use `portfolio/OUTCOMES.md` for parked/launched ideas.

## Output

| File | What |
|---|---|
| `portfolio/index.html` | the portfolio table, open in a browser |
| `portfolio/PORTFOLIO.md` | the same table in Markdown |

Present to the owner (≤ 8 lines):

```
Active: <projects and current phase>
Blocked: <project — blocker>
Stale (> 14 days): <projects>
Awaiting your approval: <projects>
Recommendation: <one line, e.g. "park X, it missed its kill criteria">
```

## If connectors available

If **~~source control** is connected:
- Use last-commit dates to confirm staleness when STATUS.md is out of date.

## Rules

- Staleness is > 14 days without a STATUS.md update.
- Only the owner approves; the portfolio reports the gate, never changes it.
- One recommendation, with the reason (kill criteria, outcome data, blocker).

## Tips

1. Run it on Monday to pick the week's project.
2. A stale project is a candidate to park, not a failure — record it in OUTCOMES.md.

## Related

- Anytime: `handoff`, `post-launch` (writes `portfolio/OUTCOMES.md`)
- Reads: `scripts/portfolio.py`, each project's `docs/product/STATUS.md`, `portfolio/OUTCOMES.md`
