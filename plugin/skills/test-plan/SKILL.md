---
name: test-plan
description: Plan and write the tests for a feature. Maps acceptance criteria to tests, with edge cases, a11y checks, device matrix, write the missing tests, a manual assistive-tech script, and report against exit criteria → TEST_PLAN.md. Trigger with "test plan", "write tests", "QA this", or after quality-review and before ship-checklist.
argument-hint: "<feature, task id or release to test; nothing = the current milestone>"
---

# /test-plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Map every acceptance criterion to a test, fill the gaps, run everything and tell the owner whether it ships or needs fixes first.

**Why:** untested unhappy paths and authorization holes are what break a small product in week one.

## Usage

```
/test-plan                           # current milestone
/test-plan T-07
/test-plan release 1.0 QA this
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                        TEST PLAN                             │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Risks · AC→test map · edge cases · a11y · device matrix   │
│  ✓ Gap hunt: untested ACs, unhappy paths, authz tests        │
│  ✓ Writes the missing tests, runs them, fixes or reports     │
│  ✓ ≤ 30-min manual script for screen readers / real devices  │
│  ✓ Report: pass/fail per exit criterion, bugs P0–P3          │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Source control: CI results as evidence, tests on the PR   │
│  + Project tracker: bugs P0–P3 filed with repro steps        │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- The stories (PRD.md) and the task's acceptance criteria (PLAN.md).
- `TECH_STACK.md` test tools; `docs/TESTING.md` (project test mix and commands).
- `../product-standards/references/testing.md` (standard and TEST_PLAN template).
- Ask the owner which real devices and screen readers they can test on.

## Workflow

1. **Read** the stories, TECH_STACK test tools, `docs/TESTING.md` (project test mix and commands), `../product-standards/references/testing.md`.
2. **Write/update `docs/product/TEST_PLAN.md`** (template in testing.md): risks · AC→test map · edge cases · a11y checks · device matrix · data · exit criteria.
   - Edge cases: empty, long/Indic text, offline, slow network, double submit, back mid-flow, session expiry, permission denied.
3. **Find gaps** (untested ACs, unhappy paths, authz tests); write missing tests; run; fix or report.
4. **Manual script:** give a ≤ 30-min manual script for screen readers / real devices.
   - Before launch (and on the prototype), plan a round with real assistive-tech users: `references/accessibility-user-testing.md`.
5. **Report:** pass/fail per exit criterion, bugs P0–P3, ship / fix-first.

## Output

| File | What |
|---|---|
| `docs/product/TEST_PLAN.md` | risks, AC→test map, edge cases, a11y checks, device matrix, data, exit criteria |
| test files in the project | the missing tests, written and run |
| `docs/product/reviews/<date>-a11y-users.md` | findings from the assistive-tech user round (format in the reference) |

Present to the owner (≤ 10 lines):

```
Exit criteria: n pass / n fail
Bugs: P0 n · P1 n · P2 n · P3 n
Verdict: ship / fix-first — and what to fix first
Manual script: <link or inline, ≤ 30 min>
```

## If connectors available

If **~~source control** is connected:
- Use the CI run on the branch / PR as evidence for the pass/fail report; push new tests only when the owner asks in chat.

If **~~project tracker** is connected:
- File P0–P3 bugs with repro steps and the failing test, on request.

## Rules

- Every acceptance criterion has a test; bug fixes start with a failing test; never weaken tests.
- Unhappy paths and authorization tests are part of the plan, not extras.
- Automated tools catch only a minority of accessibility problems — the manual script and the assistive-tech user round are required before launch.
- Report honestly against the exit criteria; a "fix-first" verdict is a normal outcome.

## Tips

1. Run `/test-plan` per milestone, not only before release — gaps are cheaper to close early.
2. Test with long and Indic text early; layouts that survive it survive most locales.
3. Book the assistive-tech user round as soon as the prototype is clickable (see the reference for recruiting and pay).

## Related

- Before: `build-feature`, `quality-review` · After: `ship-checklist`
- Reads: `references/accessibility-user-testing.md`; `../product-standards/references/testing.md`; `docs/TESTING.md`, `TECH_STACK.md`
