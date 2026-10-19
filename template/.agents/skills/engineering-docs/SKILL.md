---
name: engineering-docs
description: Product Kit engineering doc set, written once the idea is approved and the stack, design system and full PRD exist — docs/ARCHITECTURE.md, DATABASE.md, SECURITY.md, CODE_STYLE.md, TESTING.md, RULES.md, MEMORY.md and a docs/README.md index that also points at PRD, DESIGN_SYSTEM, PLAN (tasks) and AGENTS.md. Use for "engineering docs", "architecture doc", "database schema doc", "project rules", "set up the docs folder", or after write-prd (full) and before plan-build.
---

# Engineering Docs

Gate: STATUS `Evaluation: APPROVED`, and TECH_STACK.md, DESIGN_SYSTEM.md and PRD.md (full) exist. Run **once** here (phase 7a); later skills keep the files current.

Why: AI coding tools work from what they can read. One short doc per concern (how the system fits together, the data model, the security model, how code is written, how it's tested, the rules, what to remember) stops every session re-deriving — or re-inventing — those decisions. Short beats complete: each file ≤ ~80 lines; detail links out.

## Steps
1. **Read** TECH_STACK.md (ADR), PRD.md (stories, data & permissions, analytics, non-functional), DESIGN_SYSTEM.md, EVALUATION §11 (accessibility and compliance), DECISIONS.md, OWNER.md. Load the standards the project touches: `../product-standards/references/` `backend.md`, `security.md`, `development.md`, `testing.md`, `context-budget.md`, `ai.md` if any AI feature, `mobile.md` if native apps. Ask ≤ 3 questions only if something blocks (e.g. multi-tenant or not).
2. **Write** each file from its template in `templates/` into `docs/`, in this order (each builds on the last):
   - `ARCHITECTURE.md` — system context and container diagrams (Mermaid), the request path for the core action, boundaries and folder layout, cross-cutting rules (auth, errors, logging, config), the decisions table linking TECH_STACK and DECISIONS.
   - `DATABASE.md` — entity model (Mermaid `erDiagram`), one table per entity with purpose, owner column and RLS policy, personal-data flag and retention, indexes, migrations and seed rules, backups.
   - `SECURITY.md` — threat model (assets, actors, entry points), the OWASP 2025 controls this project implements and where, secrets, auth and session rules, data protection (DPDP / GDPR as applicable), AI-specific risks if any, incident basics.
   - `CODE_STYLE.md` — language and framework versions, folder and naming conventions, component and state patterns, error handling, accessibility-in-code rules, comments ("why", in plain English), lint/format commands, review checklist.
   - `TESTING.md` — test mix and tools, what every story needs, how to run each layer, accessibility and performance checks, test data, CI expectations, definition of done.
   - `RULES.md` — the project's standing rules an agent must obey every session: token budget, security MUSTs, AI-feature MUSTs, accessibility baseline, branch naming, "never do" list. Pull from AGENTS.md and the standards; make each rule concrete for this stack (names of real tables, commands, services).
   - `MEMORY.md` — long-lived project memory: facts every session needs that live nowhere else (environment quirks, things that broke before, do-not-touch areas, naming decisions, external accounts in use). Starts short; `handoff` appends.
   - `docs/README.md` — the index from `templates/docs-README.md`: every doc above plus the kit's product docs under their familiar names (PRD → `product/PRD.md`, DESIGN → `product/DESIGN_SYSTEM.md`, TASKS → `product/PLAN.md`, AGENTS → `../AGENTS.md`).
3. **No duplication:** each fact lives in one file; others link to it. PRD, design system and plan are not copied here.
4. **Check:** every Mermaid block renders (paste into the browser preview if available); every table in DATABASE.md has an RLS policy or an explicit "no user data"; SECURITY.md covers every OWASP row with a control or "not applicable because…"; no secrets or personal data in any file.
5. Present in ≤ 10 lines: what was written, the 3 decisions that most constrain the build, open questions → CLARITY.md. Owner confirms → STATUS `7a Engineering docs: Done`; offer plan-build.

## Keeping them current
- build-feature: reads ARCHITECTURE, DATABASE, CODE_STYLE for its task; updates DATABASE.md with every migration.
- quality-review: reviews against SECURITY.md and CODE_STYLE.md; findings that change a rule update the doc.
- handoff: appends to MEMORY.md (gotchas, decisions) and keeps it ≤ 60 lines by condensing.
- standards-refresh: re-checks RULES.md and SECURITY.md against the updated standards.

Adopted projects (phases marked "Done (before kit)"): write the set from the code that exists — read the project's README, schema, config and tests; mark anything inferred rather than decided as "observed", and list gaps as tasks for PLAN.md.
