---
name: standards-refresh
description: Check whether the kit's standards are outdated (WCAG, OWASP, MASVS, DPDP/GDPR/COPPA, App Store/Play rules, framework versions, accessibility law, AI models and prices) and propose edits → report table, then VERSIONS.md + CHANGELOG with approval. Trigger with "update standards", "are our rules current?", or quarterly.
argument-hint: "<area to check (e.g. accessibility law, AI models), or nothing for all>"
---

# /standards-refresh

Keep the kit's rulebook pinned to what exists now, with a source for every change.

**Why:** the kit recommends standards, laws and models by name; a stale name is worse than none.

## Usage

```
/standards-refresh                   # all standards
/standards-refresh accessibility law
/standards-refresh AI models
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                    STANDARDS REFRESH                         │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Reads VERSIONS.md: what is pinned, when checked           │
│  ✓ Web-searches official sources per standard                │
│  ✓ Report: pinned · latest · changed · impact · urgency      │
│  ✓ With approval: edits, VERSIONS.md dates, version bump     │
├──────────────────────────────────────────────────────────────┤
│  No connectors used — official web sources only.             │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `../product-standards/VERSIONS.md` (what each standard is pinned to and when checked).
- `../product-standards/references/accessibility-law.md` "watch" list, `ai.md`, `context-budget.md` model routing.
- `../tool-plan/references/tool-routing.md`; each project's `docs/GITHUB.md`, `docs/RULES.md`, `docs/SECURITY.md`.
- Ask the owner: approval before any edit is applied.

## Workflow

1. **Read `../product-standards/VERSIONS.md`** — what each standard is pinned to and when checked.
2. **Web-search official sources** for each:
   - W3C WAI (WCAG), OWASP (Top 10, ASVS, MASVS, LLM Top 10), MeitY (DPDP Rules phases), EU/UK GDPR guidance, FTC COPPA, Apple App Review Guidelines, Google Play policy updates, Expo SDK / React Native / Next.js / Supabase release notes.
   - **Accessibility law** (`references/accessibility-law.md` "watch" list): DOJ Title II dates, EAA enforcement and EN 301 549 OJEU citation, AODA reports, India DEPwD/MeitY and RBI notifications, Apple label requirement.
   - **AI advancements** (`references/ai.md` and `context-budget.md` model routing): current model families and prices, context windows and caching, agent/tool features of Claude Code, Cursor and Codex, MCP changes, new eval or safety guidance — so the kit recommends what exists now, never a remembered model name.
3. **Re-check tool routing and limits.** `../tool-plan/references/tool-routing.md` (what each AI tool is good at now) and project `docs/GITHUB.md` free-tier limits.
4. **Map to project rules.** For each project that has `docs/RULES.md` and `docs/SECURITY.md`, list the rule lines that the changes affect; apply with the owner's approval.
5. **Report table:** standard · pinned · latest · what changed · impact on kit (file + proposed edit) · urgency.
6. **Apply with approval:** edit the files, update VERSIONS.md dates, bump kit version + CHANGELOG.

## Output

| File | What |
|---|---|
| Report (in chat) | table: standard · pinned · latest · what changed · impact on kit (file + proposed edit) · urgency |
| `../product-standards/VERSIONS.md` | updated pins and check dates (after approval) |
| `../product-standards/references/*.md` | the approved edits |
| `CHANGELOG.md` + kit version | bumped (after approval) |
| project `docs/RULES.md`, `docs/SECURITY.md` | affected rule lines (after approval) |

## Rules

- Cite a source URL for every change.
- Don't edit on rumours or drafts (note drafts separately).
- Nothing is applied without the owner's approval; the report comes first.
- Never a remembered model name — verify in official docs.

## Tips

1. Run it quarterly, or before `ship-checklist` on a store launch.
2. Say an area name to keep the run small: *"accessibility law"*, *"AI models"*.
3. Mark anything you couldn't confirm against an official source as **unverified**.

## Related

- Anytime: `product-standards` (the rulebook), `tool-plan` (tool routing)
- Reads: `../product-standards/VERSIONS.md`, `references/accessibility-law.md`, `references/ai.md`, `references/context-budget.md`, `../tool-plan/references/tool-routing.md`
