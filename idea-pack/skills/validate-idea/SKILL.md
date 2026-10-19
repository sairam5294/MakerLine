---
name: validate-idea
description: Test demand before building anything. Covers kill criteria set up front, then the cheapest tests that fit (user interviews, landing page + waitlist, prototype usability test, concierge MVP, pre-sale) — and record results → VALIDATION.md. Trigger with "validate demand", "test before building", "interview users", or after evaluation.
argument-hint: "<assumption to test, or nothing to pick from EVALUATION.md>"
---

# /validate-idea

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Get evidence that real people want this, for the least time and money.

**Why:** a kill criterion written before the test is the only thing that stops a hopeful owner from reading any result as a win.

## Usage

```
/validate-idea                              # picks the 1–3 riskiest assumptions from EVALUATION.md
/validate-idea interview users
/validate-idea landing page for the waitlist
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                      VALIDATE IDEA                           │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ 1–3 riskiest assumptions, each with a kill criterion      │
│  ✓ Cheapest test first: interviews · landing page · prototype│
│    test · concierge MVP · pre-sale                           │
│  ✓ Raw results vs kill criteria → validated / invalidated /  │
│    unclear + what changes                                    │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Hosting: deploy the landing page                          │
│  + Product analytics: visits → signups without a spreadsheet │
│  + Design: run the prototype test from a Figma prototype     │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `docs/product/EVALUATION.md` — the riskiest assumptions and the validation tests it proposed.
- `design/wireframes/index.html` (design-direction) or a Figma prototype, for the prototype test.
- `references/validation-template.md`, `references/interview-guide.md`.
- No gate: validation happens before approval and only produces docs, static files or a separate landing project.

## Workflow

1. **Pick the assumptions.** From EVALUATION.md pick the 1–3 riskiest assumptions. For each, set a **kill criterion** before testing (e.g. "< 40 waitlist signups from 1,000 visitors in 14 days → rethink"). Record them in `docs/product/VALIDATION.md` (template: `references/validation-template.md`).
2. **Choose tests** (cheapest first):
   - **Interviews** (5–10): use `references/interview-guide.md`. Ask about past behaviour, never "would you use…?".
   - **Landing page + waitlist**: one-page promise, 3 benefits, one CTA, privacy note; track visits → signups. Build it as a **separate project** (`new-project.sh ~/Projects/<name>-landing --web`; owner approves it with `scripts/approve.sh "validation landing page"`), or as static files in this project's `validation/` folder — both pass the approval gate. Deploy on Vercel.
   - **Prototype test** (5 users): the design-direction wireframes in Prototype mode (`design/wireframes/index.html`) or a Figma prototype, 3 tasks, measure task success + time + confusion points. Include 1–2 assistive-tech users if your audience needs it (`../idea-pack/references/accessibility-user-testing.md`).
   - **Concierge/manual MVP**: deliver the value by hand (WhatsApp, Google Sheet) to 5–10 users for 2 weeks.
   - **Pre-sale / deposit** when money is part of the model.
3. **Run and record.** Record raw results, compare with kill criteria, and summarise: validated / invalidated / unclear + what changes.
4. **Feed results back.** Into evaluate-idea (re-score with new evidence) before the approval gate.

## Output

| File | What | Size |
|---|---|---|
| `docs/product/VALIDATION.md` | assumptions, tests, kill criteria, results, verdicts, decision | per `validation-template.md` |
| `validation/` or `~/Projects/<name>-landing` | the landing page (static files, or a separate project) | — |

Presentation to the owner (≤ 8 lines):

```
Assumption A1 · test · kill criterion · result · verdict
…
What changes in the brief / scope / positioning
Next: re-score in evaluate-idea
```

## If connectors available

If **~~hosting** is connected:
- Deploy the landing page and read the deployment URL back into VALIDATION.md.

If **~~product analytics** is connected:
- Pull visits, signups and conversion for the landing page instead of counting by hand.

If **~~design** is connected:
- Use the Figma prototype for the 5-user test and link the file in VALIDATION.md.

## Rules

- Kill criteria are set **before** the test, never after — and recorded in VALIDATION.md.
- Interviews ask about the past, never "would you use…?".
- Cheapest test first; a concierge MVP beats code.
- The landing page passes the approval gate only as a separate project (approved with `scripts/approve.sh "validation landing page"`) or as static files in `validation/` — never as app code in this repo.
- Results change scores only through evaluate-idea; never edit EVALUATION.md scores here.

## Tips

1. Five honest interviews beat fifty "nice idea" replies — recruit where your users already spend time (brief §B).
2. Write the kill criterion as a number and a date; "enough interest" isn't one.
3. If the prototype test confuses users on the core action, fix the direction before the PRD.

## Related

- Before: `evaluate-idea`, `design-direction` · After: `evaluate-idea` (re-score), approval
- Reads: `references/validation-template.md`, `interview-guide.md`; `../idea-pack/references/accessibility-user-testing.md`
