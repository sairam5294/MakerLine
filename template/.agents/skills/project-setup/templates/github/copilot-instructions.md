# Copilot instructions — {{Name}}

Follow `AGENTS.md` (the shared rulebook for every AI tool), `docs/RULES.md` and the scoped rules in `.cursor/rules/` for the folder you're editing. Key points:
- Tokens only for colours/spacing/type; strings from `i18n/`; config from `{{lib/config.ts}}`.
- Every screen: loading, empty, error, offline, success; WCAG 2.2 AA.
- Server-side authorization and RLS; validate input with the shared schema; no secrets in client code.
- Tests for every acceptance criterion; `{{npm run check}}` must pass.
- Branch names `<type>/<Mon>-<DD>-<summary>`.
