---
name: write-prd
description: Product Kit PRD: writes PRD.md for the MVP — goals, personas, journeys, numbered user stories with Given/When/Then criteria, screens with states, data + access rules, analytics, non-functional requirements. Use for "PRD", "spec", "requirements", "user stories".
---

# Write PRD

1. Gate check. Read brief, evaluation (MVP cut), validation, naming, stack, design system.
2. Write `docs/product/PRD.md`:
   1. Summary, goals (→ success metric), non-goals
   2. Personas + top 3 jobs-to-be-done
   3. Journeys: happy + key edge paths per core flow
   4. Stories `US-01…` by epic: As a / I want / so that · MoSCoW · Given/When/Then incl. error, empty, offline, permission-denied
   5. Screens: purpose · primary action · states · components
   6. Data: entities, fields, relations, who can read/write (→ RLS)
   7. Analytics events (no personal data) + funnel for the success metric
   8. Non-functional: relevant MUSTs from `../product-standards/` (AI features → run the ai-feature skill and link its doc)
   9. Copy, notifications · 10. Release criteria, open questions
3. If must-haves exceed ~6–8 weeks for the owner, propose cuts.
4. Iterate → Approved → STATUS.

Every criterion must be automatable; every personal-data story states what and why.
