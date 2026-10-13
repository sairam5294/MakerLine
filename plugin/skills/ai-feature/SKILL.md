---
name: ai-feature
description: Designs an AI feature end-to-end — is AI right, model choice, prompt versioning, structured output, AI UX (streaming, labels, control, errors), eval set, safety, privacy, content rights, cost per user → AI_FEATURE_<name>.md. Use for "add AI", "chatbot", "AI generate", "use an LLM".
---

# AI Feature

Standard: `../product-standards/references/ai.md` (read it first).

1. **Justify**: user problem, non-AI alternative, cost of a wrong answer, fallback when AI is down. If a non-AI option is as good → recommend it and stop.
2. **Design the UX** (owner leads; offer patterns): entry point, example prompts, waiting (stream/progress/cancel), output with "AI" label + sources, edit/regenerate/undo/turn off, feedback + report, errors with a non-AI path, quotas. Include accessible behaviour (polite live region, alt text).
3. **Spec the engine** — start from the web starter's harness (`src/ai/provider.ts`: server-only, timeout, retry, Zod-validated output, typed failures; example `src/ai/features/summariseFeedback.ts` with redaction + per-user quota). Expo apps call it through a server/Edge Function, never from the device. Then: server-side call, model (cheapest that passes evals; verify current models/prices in official docs), prompt file `src/ai/prompts/<feature>.v1.md`, JSON output schema + Zod validation, timeouts/retries/fallback, rate limits and per-user token caps, moderation.
4. **Eval set**: write 20–50 cases in `evals/ai/<feature>.cases.json` (format + runner: `tests/ai-eval.live.test.ts`, run `npm run ai:eval`) (typical, edge, other languages, abusive, prompt-injection) with pass criteria. No launch until pass rate meets the bar the owner sets.
5. **Privacy & rights**: data sent to the provider, consent, redaction, no-training settings, children rules; content ownership/licence per generator; synthetic-media labels (India IT Rules 2026) and store policies (Play AI-content: in-app reporting).
6. **Cost**: tokens × price × uses per active user per month; cache/pre-generate options; add to unit economics.
7. Write `docs/product/AI_FEATURE_<name>.md` (all of the above), add stories to PRD (`US-xx`) and tasks to PLAN; log model choice in DECISIONS.md.
