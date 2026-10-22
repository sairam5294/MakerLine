# Scale test: small project vs larger product

Does the same MakerLine workflow (opportunity review + shared context + context recovery) hold up on a product much bigger than a one-person app? Tested 2026-10-22. Raw rows: `results.md` Run 4; costs: `TOKEN-METRICS.md`.

## The two cases

| | Small: RhythmBuddy | Larger: Tindi 1.0 |
|---|---|---|
| Shape | One macOS app, one repo | 3 apps (customer, partner, admin) + Supabase, a monorepo **and** a separate product-docs repo |
| Docs | ~290 lines of project docs | ~68,000 words across 22 product documents (110 rules, 355 + 155 screens) |
| Plan | 15 small tasks | 5 releases, role-tagged work ([You], [Eng], [Adviser]), ~23 weeks to pilot with an engineering lead |
| Built | Shipped v1.0 | R0 scaffold only |

## Results

| Measure | RhythmBuddy | Tindi | Read |
|---|---|---|---|
| Opportunity review: total tokens / MakerLine's share | 137k / ~59k | 175k / ~97k | Long docs cost more, but the agent read 10 files in full of 25+ by following README → PRD → TASKS → MEMORY |
| Tool calls · searches · page reads | 36 · 8 · 12 | 43 · 7 · 13 | Similar research load |
| Review check | clean | clean, no warnings | Same workflow, no special handling |
| Context pack for one task (words) | 3,183 (Strategy) | 1,355 (Payments) · 2,763 (Strategy) · 4,679 (Customer app) | Section anchors keep each task's pack to **2–7% of the docs** |
| Context recovery (10 questions) | 10/10, 0 wrong claims, ~100k | **9/10 by hand** (C04 partial: listed the evidence IDs but not the reasons), 0 wrong claims, ~114k | The keyword scorer said 8/10: it counted a quoted "not in the files: no Evaluation: APPROVED line" as a wrong claim. README now warns about `must_not_include` |
| Files a fresh tool opened to recover | 7 | 8 (6 full, 2 partial), across both repos | The index's per-app rows and section anchors did the routing |

## What had to change for the larger product (all fixed on 2026-10-22)

| Found | Fix |
|---|---|
| Evidence lives in another repo; the review had no way to say which commit | Sources may use `repo@commit:path`; the index has a **Related repos** table that `check` verifies |
| Progress differs per app; only free text could say so | Review `areas` table: "Where each part stands" |
| Long documents: a whole-file pack would be ~68k words | Section anchors (`RULES.md#orders`, numbered headings match too); `check` fails on a missing section |
| Project rules live in the docs repo, not the code repo | `check` accepts a sibling repo's `AGENTS.md` listed in the "Any session start" row |
| Different owners per area ([Eng] vs owner) | Optional Owner column in "Read by task" |
| Markets below country level (US confirmed, state open) | Listed as their own entry, the open choice as an unknown |

## What this does **not** prove yet (enterprise)

Tindi is a larger product with a team-shaped plan, but it's still one maker's repos. Not yet tested:

- Many teams writing at once: CODEOWNERS-based ownership, review rules, and more than two repositories.
- Enforced permissions: privacy tiers are advisory (they keep files out of packs); they don't stop a tool with folder access from reading.
- Company data rules: data classification, retention, SSO-only AI tools, audit trails of who changed which decision.
- Monorepos with dozens of packages, and indexes that must stay small as the product grows.

**Next step:** one real multi-team repository, run read-only with the owner's permission, plus a ChatGPT and a Cursor recovery run on RhythmBuddy (`context-recovery/README.md`).
