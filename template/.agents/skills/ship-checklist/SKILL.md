---
name: ship-checklist
description: Run the launch checklist before shipping. Covers quality, security and privacy, expert review, operations, stores, launch, rollout and rollback — with evidence per item → RELEASE.md. Trigger with "ship", "launch", "release", "submit to app store", "ready to launch?", or after test-plan.
argument-hint: "<version or release name, e.g. 1.0; nothing = the release in STATUS.md>"
---

# /ship-checklist

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Walk every launch gate with evidence, write `docs/product/RELEASE.md`, and stop the release if a MUST is red.

**Why:** a release is the one irreversible step; the checklist makes the owner's go/no-go a decision with evidence, not a feeling.

## Usage

```
/ship-checklist                      # release in STATUS.md
/ship-checklist 1.0
/ship-checklist ready to launch?
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                      SHIP CHECKLIST                          │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Blocks: Quality · Security & privacy · Expert review ·    │
│    Operations · Stores · Launch                              │
│  ✓ Each item ✅/❌/N/A with evidence; runs what it can verify │
│  ✓ RELEASE.md: version, date, results, known issues,         │
│    rollout, rollback                                         │
│  ✓ A ❌ in a MUST block stops release unless owner accepts   │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Hosting: release build, headers, env, preview → prod      │
│  + Database: RLS, backups and restore evidence               │
│  + Monitoring: error tracking, uptime, alerts verified       │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `STATUS.md`, the latest review in `docs/product/reviews/`, `TEST_PLAN.md` results, `TECH_STACK.md`.
- `references/expert-review.md` (brief for a professional) and `../test-plan/references/accessibility-user-testing.md`.
- `../product-standards/references/accessibility-law.md` for launch-market obligations.
- Ask the owner: launch markets, whether payments / children's data / health or finance data / > 10k users apply, and who owns week-1 monitoring.

## Workflow

1. **Read** STATUS, latest review, TEST_PLAN results, TECH_STACK.
2. **Mark each item** ✅/❌/N/A with evidence; run what can be verified (tests, build, `npm audit`, gitleaks, header check).
3. **Write `docs/product/RELEASE.md`** (version, date, results, known issues, rollout, rollback).
   - Any ❌ in a MUST block stops release unless the owner accepts the risk in DECISIONS.md.

### The checklist

**Quality (MUST)**
- tests green on release build · no P0/P1 · no open MUST review findings
- axe clean + manual screen-reader pass + a usability round with 3–5 assistive-tech users (`../test-plan/references/accessibility-user-testing.md`)
- performance budgets met on low-end Android
- accessibility statement published with a working feedback route; ACR (VPAT) ready if selling to businesses or government
- launch-market obligations met (`../product-standards/references/accessibility-law.md`, e.g. AODA compliance report, EAA service information)

**Security & privacy (MUST)**
- audit + secrets scan clean, exposed keys rotated
- authz/RLS tests green, admin MFA
- headers (web) / obfuscation, debug off (mobile)
- privacy policy, terms, data inventory, store privacy labels accurate
- account deletion + export work · children's rules met if relevant

**Expert review (MUST if payments, children's data, health/finance data, or > 10k users)**
- send a professional the brief from `references/expert-review.md`; record outcome

**Operations (MUST)**
- error tracking with source maps · uptime monitor · billing alerts
- backups + tested restore · rollback tested
- success-metric events verified in prod

**Stores**
- icons, screenshots, copy, support + privacy URLs
- age rating / Kids & Families rules
- TestFlight/internal test with 5+ real users · staged rollout · minimum-version check

**Launch**
- landing/store page live · waitlist notified · in-app feedback
- week-1 monitoring owner · post-launch reviews at week 1 and 4 (post-launch skill)

## Output

| File | What |
|---|---|
| `docs/product/RELEASE.md` | version, date, checklist results with evidence, known issues, rollout, rollback |
| `docs/product/DECISIONS.md` | any accepted risk for a ❌ in a MUST block; expert-review outcome |

Present to the owner (≤ 10 lines):

```
Release <version>: GO / NO-GO
MUST blocks: Quality ✅ · Security & privacy ❌ (n) · Expert review N/A · Operations ✅
Open ❌ items and what closes each
Rollout plan · rollback tested? · week-1 owner
```

## If connectors available

If **~~hosting** is connected:
- Verify the release build, security headers, env variables and the preview → production promotion; deploy only when the owner asks in chat.

If **~~database** is connected:
- Confirm RLS policies are enabled on every user-data table, backups are on and a restore was tested; attach the evidence.

If **~~monitoring** is connected:
- Confirm error tracking (with source maps), uptime checks and alerts are live and fire on a test event.

## Rules

- Any ❌ in a MUST block stops release unless the owner accepts the risk in DECISIONS.md — the owner, not the skill, accepts risk.
- Evidence per item: a command output, a link or a screenshot; "should be fine" is a ❌.
- Expert review is MUST when payments, children's data, health/finance data, or > 10k users are involved.
- Ask before anything irreversible: production settings, store submission, paid services.

## Tips

1. Run a dry `/ship-checklist` a week before launch so the ❌ items have time to close.
2. Rehearse the rollback once on staging — it is the cheapest insurance on the list.
3. Line up the expert reviewer early; professionals book out weeks ahead.

## Related

- Before: `quality-review`, `test-plan` · After: `post-launch`
- Reads: `references/expert-review.md`; `../test-plan/references/accessibility-user-testing.md`; `../product-standards/references/accessibility-law.md`, `security.md`, `privacy.md`
