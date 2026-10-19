---
name: {{project}}-{{job}}
description: {{Name}} — how to {{job, e.g. add a screen}} in this repo, using its real folders, commands and rules. Use for "{{trigger phrases}}".
---

# {{Job}} in {{Name}}

1. Branch: `scripts/branch.sh feat "{{summary}}"`.
2. {{Create `app/(main)/<feature>/page.tsx` …}} — see `docs/STRUCTURE.md` "Where does it go?".
3. {{Strings in `i18n/en.json` (+ te, hi); tokens only; five states.}}
4. {{Data via `hooks/<resource>.ts`; new table → migration + RLS + `tests/rls/` test + DATABASE.md.}}
5. Tests for each acceptance criterion; `{{npm run check}}` green.
6. Update STRUCTURE / `.env.example` / DATABASE if you added a folder, variable or table. Commit `feat(scope): … (T-xx)`; PR with the template.
