---
name: product-standards
description: Apply the Product Kit quality rulebook — accessibility (WCAG 2.2 AA, iOS/Android), accessibility law, inclusion, UX, development, testing, backend, security (OWASP 2025, MASVS), privacy, performance, mobile, AI features, context budget. Trigger with "standards", "definition of done", "which rules apply?", or when designing, building, reviewing or testing anything.
argument-hint: "<area, e.g. accessibility, security, or nothing for the index>"
---

# /product-standards

The definition of done: an index of reference files, loaded one at a time as the task needs them.

**Why:** the rules are long; loading all of them wastes tokens and attention. Load **only** the reference files the task touches.

## Usage

```
/product-standards                 # the index and the always-on rules
/product-standards security        # load references/security.md
/product-standards accessibility law India
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                     PRODUCT STANDARDS                        │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Always-on rules (no file needed)                          │
│  ✓ 13 reference files, loaded per task area                  │
│  ✓ MUST / SHOULD vocabulary and the findings format          │
│  ✓ Versions pinned in VERSIONS.md (standards-refresh)        │
├──────────────────────────────────────────────────────────────┤
│  No connectors used — the rulebook is read by other skills.  │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- The task at hand (design, build, review, test) → pick the area(s) from the table below.
- `VERSIONS.md` for what each standard is pinned to.

## Reference files

Load **only** the reference files the task touches:

| Area | File |
|---|---|
| Accessibility | references/accessibility.md |
| Accessibility law by market (AODA, ADA, 508, EAA, UK, India…) | references/accessibility-law.md |
| Inclusion, non-discrimination, global accessibility baseline | references/inclusion.md |
| UX, states, copy | references/ux.md |
| Code, git, deps | references/development.md |
| Tests | references/testing.md |
| API, DB, ops | references/backend.md |
| Security | references/security.md |
| Privacy, children, payments | references/privacy.md |
| Speed budgets | references/performance.md |
| iOS/Android, stores | references/mobile.md |
| AI features, AI content | references/ai.md |
| Context/token budget, local models | references/context-budget.md |

## Workflow

1. **Pick the area(s)** the task touches from the table; load those files only (1–2 per task).
2. **Apply the vocabulary.** MUST = always. SHOULD = default; skipping needs a reason in DECISIONS.md.
3. **Report findings** as MUST-violation / SHOULD-gap / Suggestion with location + fix.

## Always (no file needed)

- No secrets in code/logs/client.
- Every control has an accessible name and works with keyboard/screen reader.
- Contrast ≥ 4.5:1 (3:1 large text, UI boundaries).
- Targets ≥ 44pt/48dp.
- Loading/empty/error/offline/success states.
- Server-side authorization + schema validation + parameterized queries.
- Tests for every acceptance criterion.
- Minimum personal data.

## Output

| What | Shape |
|---|---|
| Findings (in a review) | MUST-violation / SHOULD-gap / Suggestion, each with location + fix |
| Skipped SHOULD | a reason in `docs/product/DECISIONS.md` |

## Rules

- MUST = always; SHOULD = default, skipping needs a reason in DECISIONS.md.
- Load only the files the task touches; never the whole rulebook.
- Versions tracked in VERSIONS.md; `standards-refresh` updates them.

## Tips

1. A review gets the diff + one standard file, not the repo (`references/context-budget.md`).
2. Accessibility law tells you what to *prove*; `inclusion.md` tells you what to *build*.

## Related

- Used by: `design-direction`, `design-system`, `build-feature`, `quality-review`, `test-plan`, `ship-checklist`, `ai-feature`
- Maintained by: `standards-refresh` · Pins: `VERSIONS.md`
