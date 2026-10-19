# Database — {{product}}

_Updated {{date}} · Engine: {{Postgres via Supabase / …}} · Migrations: `{{supabase/migrations/}}` · Source of truth for data and permissions (PRD §10)._

## 1. Entity model
```mermaid
erDiagram
  PROFILE ||--o{ {{ENTITY}} : owns
  {{ENTITY}} ||--o{ {{CHILD}} : has
  PROFILE {
    uuid id PK
    text display_name
    timestamptz created_at
  }
```

## 2. Tables
One block per table. "Owner column" is what row-level security checks.

### `{{table}}`
- Purpose: {{one line}}
- Owner column: `{{user_id}}` → `auth.users.id` · Tenant/group column: {{if any}}
- RLS: select {{owner / members of group / public}} · insert {{…}} · update {{…}} · delete {{…}} — policy names: `{{table}}_select_own` …
- Personal data: {{none / which columns and why}} · Retention: {{n}} · Export/delete covered by: {{function}}
- Indexes: `({{user_id}}, created_at desc)` {{…}}
- Invariants: {{e.g. status ∈ enum; end_at > start_at — enforced by CHECK / trigger}}

## 3. Access matrix
| Table | Anonymous | Signed-in user | Group member / staff | Admin | Service role (server only) |
|---|---|---|---|---|---|

## 4. Migrations and seeds
- One migration per change, forward-only, named `YYYYMMDDHHMM_<what>.sql`; every table gets RLS enabled in the same migration that creates it.
- Seed data for local and tests: `{{path}}`; never real personal data.
- Test for every policy: user A cannot read or write user B's rows (`tests/rls/`).

## 5. Backups and recovery
- Provider backups: {{daily, n-day retention}} · Point-in-time: {{yes/no}} · Restore tested on {{date}} (ship-checklist).

## 6. Analytics and derived data
- Events table / provider: {{…}} (no personal data in properties); materialised views or aggregates: {{…}}.

## 7. Open questions
- {{→ CLARITY.md ids}}
