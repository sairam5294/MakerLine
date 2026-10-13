---
name: tech-stack
description: Product Kit tech stack: recommends 2–3 stacks (frontend web/iOS/Android, backend, DB, auth, hosting, payments, analytics, AI, testing, CI) with plain-language trade-offs and costs; records TECH_STACK.md. Use for "which tech/framework/stack?".
---

# Tech Stack

1. Gate: STATUS `Evaluation: APPROVED`.
2. Read brief (platforms, features, scale, budget, builder), `docs/product/OWNER.md` (accounts, tools, budget) + evaluation feasibility. Ask ≤ 5 missing questions.
3. Build 2–3 candidates from `references/stack-options.md`: recommended default, simpler/cheaper, native/powerful (only if justified).
4. Per candidate: components table · fit · trade-offs in plain words · owner learning curve · monthly cost at 100/1k/10k users · lock-in · AI-tool friendliness.
5. Verify current stable versions and breaking changes in official docs (or via the docs MCP) — never from memory.
6. Owner decides → write `docs/product/TECH_STACK.md` as an ADR (context, decision, versions, rejected options, consequences, commands).
7. Kit starters skip setup: `new-project.sh --starter` (Expo + Supabase: iOS/Android/app-like web) or `--web` (Next.js: SEO/marketing/landing pages, Lighthouse ≥ 0.9). Products needing both usually use both (site + app). Fill AGENTS.md "Commands"; update DECISIONS + STATUS.

Rules: managed services over self-hosting; one language (TypeScript) where possible; mature over trendy; flag native code, paid tiers, store-review impacts.
