---
name: ai-feature
description: Design an AI feature end-to-end — is AI right, model choice, prompt versioning, structured output, AI UX (streaming, labels, control, errors), eval set, safety, privacy, content rights, cost per user → AI_FEATURE_<name>.md. Trigger with "add AI", "chatbot", "AI generate", "use an LLM", or when a PRD story needs a model.
argument-hint: "<feature name or what the AI should do>"
---

# /ai-feature

Spec one AI feature so it is justified, safe, evaluated and priced before anyone writes code.

**Why:** AI features fail on wrong answers, cost and trust, not on model choice. The standard is `../product-standards/references/ai.md` — read it first.

## Usage

```
/ai-feature summarise feedback
/ai-feature chatbot for lesson questions
/ai-feature                          # asks which PRD story needs AI
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                        AI FEATURE                            │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Justify: non-AI alternative, cost of a wrong answer       │
│  ✓ UX patterns: streaming, "AI" label, edit/undo, errors     │
│  ✓ Engine spec from the web starter's src/ai/ harness        │
│  ✓ Eval set (20–50 cases) · privacy & rights · cost per user │
│  ✓ AI_FEATURE_<name>.md + PRD stories + PLAN tasks           │
├──────────────────────────────────────────────────────────────┤
│  No connectors used — the work is design and specification.  │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `../product-standards/references/ai.md` (read it first).
- `docs/product/PRD.md` (the story that needs AI), `PLAN.md`, `DECISIONS.md`.
- The web starter's harness: `src/ai/provider.ts` and the example `src/ai/features/summariseFeedback.ts`.
- Ask the owner: the user problem, the acceptable error rate (eval pass bar), the monthly budget.

## Workflow

1. **Justify.** User problem, non-AI alternative, cost of a wrong answer, fallback when AI is down.
   - If a non-AI option is as good → recommend it and stop.
2. **Design the UX** (owner leads; offer patterns): entry point, example prompts, waiting (stream/progress/cancel), output with "AI" label + sources, edit/regenerate/undo/turn off, feedback + report, errors with a non-AI path, quotas.
   - Include accessible behaviour (polite live region, alt text).
3. **Spec the engine.** Start from the web starter's harness (`src/ai/provider.ts`: server-only, timeout, retry, Zod-validated output, typed failures; example `src/ai/features/summariseFeedback.ts` with redaction + per-user quota).
   - Expo apps call it through a server/Edge Function, never from the device.
   - Then: server-side call, model (cheapest that passes evals; verify current models/prices in official docs), prompt file `src/ai/prompts/<feature>.v1.md`, JSON output schema + Zod validation, timeouts/retries/fallback, rate limits and per-user token caps, moderation.
4. **Eval set.** Write 20–50 cases in `evals/ai/<feature>.cases.json` (format + runner: `tests/ai-eval.live.test.ts`, run `npm run ai:eval`): typical, edge, other languages, abusive, prompt-injection, each with pass criteria.
   - No launch until pass rate meets the bar the owner sets.
5. **Privacy & rights.** Data sent to the provider, consent, redaction, no-training settings, children rules; content ownership/licence per generator; synthetic-media labels (India IT Rules 2026) and store policies (Play AI-content: in-app reporting).
6. **Cost.** Tokens × price × uses per active user per month; cache/pre-generate options; add to unit economics.
7. **Write and link.** `docs/product/AI_FEATURE_<name>.md` (all of the above); add stories to PRD (`US-xx`) and tasks to PLAN; log model choice in DECISIONS.md.

## Output

| File | What |
|---|---|
| `docs/product/AI_FEATURE_<name>.md` | justification, UX, engine spec, eval plan, privacy & rights, cost |
| `docs/product/PRD.md` | new `US-xx` stories |
| `docs/product/PLAN.md` | build tasks for the feature |
| `docs/product/DECISIONS.md` | model choice and why |
| `evals/ai/<feature>.cases.json` | 20–50 eval cases with pass criteria |
| `src/ai/prompts/<feature>.v1.md` | versioned prompt (when building starts) |

Present to the owner (≤ 8 lines): is AI right · chosen pattern · model and why · eval bar · cost per active user · open questions.

## Rules

- Models are called only from the server; keys never reach the client.
- Model output is untrusted: validate structured output, never execute or render it raw.
- Label AI-generated content; users can edit, regenerate, undo or turn it off.
- Verify current models and prices in official docs — never a remembered model name.
- No launch without evals passing the owner's bar.

## Tips

1. Start with the cheapest model and let the evals argue for a bigger one.
2. Write the eval cases before the prompt — they define "good".
3. Pre-generating content is often cheaper and safer than live generation.

## Related

- Before: `write-prd` (the story) · After: `plan-build`, `build-feature`, `quality-review`
- Reads: `../product-standards/references/ai.md`, `security.md` §5, `privacy.md`, `inclusion.md` §6
