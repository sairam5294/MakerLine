---
name: tech-stack
description: Recommend a tech stack with costs. Compares 2–3 stacks (frontend web/iOS/Android, backend, DB, auth, hosting, payments, analytics, AI, testing, CI) with plain-language trade-offs and costs, then record the owner's choice as an ADR → TECH_STACK.md. Trigger with "which tech/framework/stack?", "what should I build this with?", or after approval and name-product.
argument-hint: "<constraints (e.g. 'web only', 'must be free'), or nothing to use the brief and OWNER.md>"
---

# /tech-stack

Help the owner choose a stack they can actually run — explained in plain words, costed, and written down as a decision.

## Usage

```
/tech-stack                       # candidates from the brief, OWNER.md and evaluation
/tech-stack web only              # constrain the candidates
/tech-stack which framework?
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                     TECH STACK                               │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ 2–3 candidates from references/stack-options.md           │
│  ✓ Per candidate: components, fit, trade-offs, learning      │
│    curve, cost at 100/1k/10k users, lock-in, AI-friendliness │
│  ✓ Versions verified in official docs / registry, not memory │
│  ✓ TECH_STACK.md as an ADR · kit starters skip setup         │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- Gate: STATUS `Evaluation: APPROVED`.
- The brief (platforms, features, scale, budget, builder), `docs/product/OWNER.md` (accounts, tools, budget) + the evaluation's feasibility section.
- Ask ≤ 5 missing questions.
- `references/stack-options.md` — the catalogue of defaults, simpler, native and cross-platform options, decision factors and tools beyond code.

## Workflow

1. **Gate and read.** Confirm STATUS `Evaluation: APPROVED`; read the brief, `OWNER.md` and the evaluation's feasibility. Ask ≤ 5 missing questions.
2. **Build 2–3 candidates** from `references/stack-options.md`:
   - recommended default
   - simpler/cheaper
   - native/powerful (only if justified)
3. **Describe each candidate:** components table · fit · trade-offs in plain words · owner learning curve · monthly cost at 100/1k/10k users · lock-in · AI-tool friendliness.
4. **Verify versions.** Check current stable versions and breaking changes in official docs or the package registry (`npm view <pkg> version` — doesn't count as a page read) — never from memory. Check each host's terms for commercial use on its free tier.
   - If the newest major is under ~3 months old or breaks the starter (e.g. a compiler rewrite), recommend the major the kit starter pins and note when to revisit.
5. **Owner decides** → write `docs/product/TECH_STACK.md` as an ADR (context, decision, versions, rejected options, consequences, commands).
6. **Scaffold with a kit starter** so setup is skipped: `scripts/new-project.sh <path> --starter` (Expo + Supabase: iOS/Android/app-like web) or `<path> --web` (Next.js: SEO/marketing/landing pages, Lighthouse ≥ 0.9). Products needing both usually use both (site + app).
7. **Record.** Fill AGENTS.md "Commands"; update DECISIONS + STATUS.

## Output

| File | What | Size |
|---|---|---|
| `docs/product/TECH_STACK.md` | ADR: context, decision, versions, rejected options, consequences, commands | one page |
| `AGENTS.md` "Commands" | the real setup/run/test commands for the chosen stack | — |
| `docs/product/DECISIONS.md`, `STATUS.md` | the decision logged; phase updated | — |

Present ≤ 10 lines: the candidates side by side (fit, cost at 100/1k/10k users, learning curve, lock-in), the recommendation and why, what to verify before launch.

## Rules

- Managed services over self-hosting.
- One language (TypeScript) where possible.
- Mature over trendy.
- Flag native code, paid tiers and store-review impacts.
- Versions come from official docs or the registry, never from memory.

## Tips

1. Say which accounts and tools you already have (or keep `OWNER.md` current) — the cost column depends on it.
2. Pick the simpler candidate unless a feature in the brief truly needs the powerful one.
3. Re-check free-tier commercial terms before launch; they change.

## Related

- Before: approval, `name-product` · After: `design-system`, `write-prd` (full), `engineering-docs`, `project-setup`
- Reads: `references/stack-options.md`; `docs/product/OWNER.md`; `scripts/new-project.sh`
