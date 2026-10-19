---
name: write-prd
description: Write a PRD for my product. Covers a draft PRD at the idea stage (problem, goals and metrics, personas, positioning, scope, journeys, user stories, design links, risks, release plan) and the full PRD after approval (adds data and permissions, analytics, stack, non-functional detail) → PRD.md. Trigger with "PRD", "spec", "requirements", "user stories", or after design-direction / design-system.
argument-hint: "<'draft' or 'full', or nothing to pick the mode from STATUS.md>"
---

# /write-prd

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Turn the brief, evaluation and design direction into one PRD that is concrete enough to test, estimate and approve — then promote it after approval.

**Why:** the draft makes the idea concrete before any code; the full version adds what engineering needs without starting over.

## Usage

```
/write-prd                 # draft (v0.x) before approval, full (v1.x) after — read from STATUS.md
/write-prd draft
/write-prd full
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                        WRITE PRD                             │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Draft v0.x (idea stage) or Full v1.x (after approval)     │
│  ✓ User stories US-01… with Given/When/Then incl. error,     │
│    empty, offline and permission-denied cases                │
│  ✓ Differentiator made visible in first-session stories      │
│  ✓ ~8-week scope check → cuts or a Release 0 (≤ 4 weeks)     │
│  ✓ Links personas, flows, screens, competitors by ID         │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Design: link stories to the Figma flows and screens       │
│  + Knowledge base: reuse prior specs and decisions           │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `docs/product/CLARITY.md` — read first; move answered questions down with the source.
- **Draft:** PROJECT_BRIEF, EVALUATION (personas, positioning, MVP cut, risks), COMPETITORS, DESIGN_DIRECTION (flows, screens, wireframes), VALIDATION if done.
- **Full:** the draft plus NAMING, TECH_STACK, DESIGN_SYSTEM; `docs/product/OWNER.md` hours for the scope check.
- Template: `references/prd-template.md`. Non-functional MUSTs: `../product-standards/`.
- Gate: Draft needs no approval (docs only, so the gate allows it). Full needs `Evaluation: APPROVED` in STATUS.md.

## Modes

| Mode | When | What |
|---|---|---|
| **Draft (v0.x)** | before approval | Fill every section except those marked **(full)** — write "after approval" under those headings. The draft makes the idea concrete enough to test, estimate and approve. |
| **Full (v1.x)** | after `Evaluation: APPROVED` | Adds NAMING, TECH_STACK, DESIGN_SYSTEM: data and permissions (→ RLS), analytics events, technology, non-functional detail. Promote the draft; don't start over. |
| **Pivot** | EVALUATION's verdict is Pivot | Spec the recommended pivot (see evaluate-idea) and label it at the top. |

## Workflow

1. **Write `docs/product/PRD.md`** from the template, in the mode above. Read CLARITY.md first.
2. **User stories** `US-01…` by epic: As a / I want / so that · MoSCoW · Given/When/Then including error, empty, offline and permission-denied cases · the screen (S-xx) it lives on · personal data used and why.
3. **Make the differentiator visible.** Name the stories and screens where a user will notice it in the first session. If none, flag it — the MVP isn't testing the idea.
4. **Scope check.** If Musts exceed ~8 weeks for this owner (OWNER.md hours), propose cuts that keep the core action and the differentiator.
   - If even the smallest wedge is longer, define a **Release 0**: a standalone slice of ≤ 4 weeks that tests the riskiest assumption with real users (a free tool, a single flow, a concierge version), then the MVP as Release 1.
   - Multi-release scope (platform approved, wedge first): full stories for Release 0 and Release 1; Release 2+ as epics with goals, the metric that triggers starting them and the stories' titles only — detail them when the previous release ships. The ~8-week check applies to each release.
   - AI features before approval: describe them in PRD §12 (what the AI does, human approval, failure path, cost cap) and mark `ai-feature: after approval`; run ai-feature and link `AI_FEATURE_*.md` only once it exists.
5. **Testable and measurable.** Every acceptance criterion must be automatable; every metric needs an event that measures it.
6. **Present** in ≤ 12 lines: the MVP in one sentence, number of Must stories, estimated build time, top 3 risks, open questions that block approval.
7. **Iterate.** Owner reviews (draft) or approves (full) → STATUS: PRD draft `Done` after review.

## Output

| File | What | Size |
|---|---|---|
| `docs/product/PRD.md` | Draft v0.x or Full v1.x, per `references/prd-template.md` | per the template's size note |
| `docs/product/CLARITY.md` | answered questions moved down with their source | — |
| `docs/product/STATUS.md` | PRD draft `Done` after review; full after approval | — |

Presentation (≤ 12 lines):

```
MVP: <one sentence>
Must stories: <n> · Estimated build: <weeks> for this owner
Top 3 risks: …
Blocks approval: <open questions>
```

## If connectors available

If **~~design** is connected:
- Link each story's screen (S-xx) to its Figma frame instead of describing it.

If **~~knowledge base** is connected:
- Search prior specs and decisions on the topic before writing new sections.

## Rules

- **Link, don't copy:** refer to personas, flows, screens and competitors by their IDs in EVALUATION / DESIGN_DIRECTION / COMPETITORS.
- Non-functional MUSTs come from `../product-standards/`; AI features → run ai-feature and link its document.
- Full mode promotes the draft; never start over.
- Every acceptance criterion automatable; every metric has an event.
- A Pivot verdict is specced as the pivot, labelled at the top.

## Tips

1. If no story makes the differentiator visible in the first session, the MVP isn't testing the idea — cut until it does.
2. Prefer a Release 0 you can ship in 4 weeks over a perfect MVP you can't.
3. Keep Should/Could stories to one line each; detail belongs to Musts.

## Related

- Before: `evaluate-idea`, `design-direction` (draft); `name-product`, `tech-stack`, `design-system` (full) · After: `validate-idea` (draft), `engineering-docs` → `plan-build` (full)
- Reads: `references/prd-template.md`; `../product-standards/` (non-functional MUSTs); `ai-feature` for AI features
