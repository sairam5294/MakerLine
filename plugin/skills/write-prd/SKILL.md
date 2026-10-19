---
name: write-prd
description: Product Kit PRD — a draft PRD at the idea stage (problem, goals and metrics, personas, positioning, scope, journeys, user stories, design links, risks, release plan) and the full PRD after approval (adds data and permissions, analytics, stack, non-functional detail) → PRD.md. Use for "PRD", "spec", "requirements", "user stories".
---

# Write PRD

Template: `references/prd-template.md`. Read CLARITY.md first; move answered questions down with the source.

**Two modes**
- If EVALUATION's verdict is Pivot, spec the recommended pivot (see evaluate-idea) and label it at the top.
- **Draft (v0.x) — before approval.** Docs only, so the gate allows it. Inputs: PROJECT_BRIEF, EVALUATION (personas, positioning, MVP cut, risks), COMPETITORS, DESIGN_DIRECTION (flows, screens, wireframes), VALIDATION if done. Fill every section except those marked **(full)** — write "after approval" under those headings. The draft makes the idea concrete enough to test, estimate and approve.
- **Full (v1.x) — after `Evaluation: APPROVED`.** Adds NAMING, TECH_STACK, DESIGN_SYSTEM: data and permissions (→ RLS), analytics events, technology, non-functional detail. Promote the draft; don't start over.

Steps
1. Write `docs/product/PRD.md` from the template.
2. User stories `US-01…` by epic: As a / I want / so that · MoSCoW · Given/When/Then including error, empty, offline and permission-denied cases · the screen (S-xx) it lives on · personal data used and why.
3. Make the differentiator visible: name the stories and screens where a user will notice it in the first session. If none, flag it — the MVP isn't testing the idea.
4. Scope check: if Musts exceed ~8 weeks for this owner (OWNER.md hours), propose cuts that keep the core action and the differentiator. If even the smallest wedge is longer, define a **Release 0**: a standalone slice of ≤ 4 weeks that tests the riskiest assumption with real users (a free tool, a single flow, a concierge version), then the MVP as Release 1.
   Multi-release scope (platform approved, wedge first): full stories for Release 0 and Release 1; Release 2+ as epics with goals, the metric that triggers starting them and the stories' titles only — detail them when the previous release ships. The ~8-week check applies to each release.
   AI features before approval: describe them in PRD §12 (what the AI does, human approval, failure path, cost cap) and mark `ai-feature: after approval`; run ai-feature and link `AI_FEATURE_*.md` only once it exists.
5. Every acceptance criterion must be automatable; every metric needs an event that measures it.
6. Present in ≤ 12 lines: the MVP in one sentence, number of Must stories, estimated build time, top 3 risks, open questions that block approval. Iterate → owner reviews (draft) or approves (full) → STATUS: PRD draft `Done` after review.

Link, don't copy: refer to personas, flows, screens and competitors by their IDs in EVALUATION / DESIGN_DIRECTION / COMPETITORS.

Non-functional MUSTs come from `../product-standards/`; AI features → run ai-feature and link its document.
