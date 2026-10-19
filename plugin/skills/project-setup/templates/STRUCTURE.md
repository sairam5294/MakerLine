# Structure — {{Name}}

_Updated {{date}} · Scoped AI rules for each folder: `.cursor/rules/` (index in `project.mdc`)._

## Tree
```
{{repo}}/
├── {{app/}}                 # routes and screens, one folder per feature route
│   ├── (auth)/              # sign-in, sign-up — public
│   ├── (main)/              # signed-in app
│   └── api/                 # server routes (only when the BaaS can't do it)
├── {{components/}}
│   ├── ui/                  # design-system components only (tokens, no business logic)
│   └── {{feature}}/         # components used by one feature
├── {{lib/}}                 # framework-free logic: api clients, formatters, validation schemas
├── {{hooks/}}               # data hooks (queries, mutations) and UI hooks
├── {{stores/}}              # global client state (auth session, settings) — keep small
├── {{types/}}               # shared TypeScript types and interfaces
├── {{constants/}}           # routes, limits, feature flags, config read from env
├── {{i18n/}}                # strings per language — no user-facing text in components
├── {{supabase/}}            # migrations/, seed.sql, policies, edge functions
├── {{tests/}}               # e2e/, fixtures/, rls/
├── design/                  # tokens.json, brand/, wireframes/
├── docs/                    # engineering docs + product/ docs
├── scripts/                 # branch.sh, check-gate.sh, approve.sh …
└── .claude/ .cursor/ .github/   # AI-tool rules and CI (all point to AGENTS.md)
```

## Where does it go?
| You're adding… | Put it in | Name it | Also update |
|---|---|---|---|
| A screen / route | `{{app/(main)/<feature>/page.tsx}}` | kebab-case folder | STRUCTURE if a new feature |
| A reusable UI component | `components/ui/` | `PascalCase.tsx` | DESIGN_SYSTEM.md |
| A feature-only component | `components/<feature>/` | `PascalCase.tsx` | — |
| An API call | `lib/api/<resource>.ts` | `get…`, `create…` | — |
| A data hook | `hooks/<resource>.ts` | `use…` | — |
| Global state | `stores/` | `use…Store` | ask first — prefer server state |
| A type shared by 2+ files | `types/` | `I…` / `T…` | — |
| A constant / route / limit | `constants/` | `SCREAMING_SNAKE` | — |
| User-facing text | `i18n/<lang>.json` | `feature.key` | every launch language |
| A table / column | `supabase/migrations/` | `YYYYMMDDHHMM_what.sql` | DATABASE.md, RLS test |
| An env variable | `.env.example` (+ dashboards) | `SERVICE_NAME` | SETUP.md |
| A test | next to the code (`*.test.ts`) or `tests/e2e/` | `<thing>.test.ts` | — |
| An image / icon / logo | `public/` or `design/brand/` | kebab-case | alt text |

## Rules
- One home per thing: no second `utils/` or `helpers/`; search before creating.
- Files stay small: aim ≤ 300 lines; split by responsibility, not by line count alone.
- Imports via aliases (`{{@/}}`), never deep `../../../`.
- Feature code may import from `ui/`, `lib/`, `hooks/`, `types/`, `constants/`; `ui/` imports nothing feature-specific.
- No user-facing strings, colours, routes or env reads inline — use `i18n/`, tokens, `constants/`, config.
- Generated files (`{{tokens.generated.ts}}`, lockfiles, build output) are never edited by hand.
