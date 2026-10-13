---
name: portfolio
description: Shows all Product Kit projects at a glance — phase, approval gate, next step, blockers, staleness — plus idea outcomes. Use for "my projects", "portfolio", "what am I working on", "which project next?".
---

# Portfolio

1. If a shell is available: run `python3 <kit>/scripts/portfolio.py [folders]` (kit folder from `docs/product/OWNER.md`; default scans ~/Projects and ~/Documents). It writes `portfolio/index.html` (open in a browser) and `portfolio/PORTFOLIO.md`.
2. Otherwise read each project's `docs/product/STATUS.md` you can reach and build the same table.
3. Summarise in ≤ 8 lines: what's active, what's blocked, what's stale (> 14 days), which projects wait on the owner's approval, and one recommendation (e.g. "park X, it missed its kill criteria"). Use `portfolio/OUTCOMES.md` for parked/launched ideas.
