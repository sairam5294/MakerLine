---
name: standards-refresh
description: Checks whether the kit's standards are outdated (WCAG, OWASP, MASVS, DPDP/GDPR/COPPA, App Store/Play rules, framework versions) and proposes edits. Use quarterly or for "update standards", "are our rules current?".
---

# Standards Refresh

1. Read `../product-standards/VERSIONS.md` (what each standard is pinned to and when checked).
2. Web-search official sources for each: W3C WAI (WCAG), OWASP (Top 10, ASVS, MASVS, LLM Top 10), MeitY (DPDP Rules phases), EU/UK GDPR guidance, FTC COPPA, Apple App Review Guidelines, Google Play policy updates, Expo SDK / React Native / Next.js / Supabase release notes; **accessibility law** (`references/accessibility-law.md` "watch" list: DOJ Title II dates, EAA enforcement and EN 301 549 OJEU citation, AODA reports, India DEPwD/MeitY and RBI notifications, Apple label requirement); **AI advancements** (`references/ai.md` and `context-budget.md` model routing): current model families and prices, context windows and caching, agent/tool features of Claude Code, Cursor and Codex, MCP changes, new eval or safety guidance — so the kit recommends what exists now, never a remembered model name.
2b. For each project that has `docs/RULES.md` and `docs/SECURITY.md`, list the rule lines that the changes affect; apply with the owner's approval.
3. Report table: standard · pinned · latest · what changed · impact on kit (file + proposed edit) · urgency.
4. With approval, apply edits, update VERSIONS.md dates, bump kit version + CHANGELOG.

Cite a source URL for every change; don't edit on rumours or drafts (note drafts separately).
