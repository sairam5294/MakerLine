# Quality review — T-05 Lessons list screen (2026-09-28)

**Scope:** `evals/cases/review-planted-bugs/changes.patch` on top of `starter/` — `src/app/lessons.tsx` (new), `src/lib/admin.ts` (new), `supabase/migrations/20260201000000_lessons.sql` (new), `src/components/__tests__/Button.test.tsx` (modified).
**Reviewers run (in sequence):** accessibility-auditor (accessibility.md) · ux-reviewer (ux.md) · security-reviewer (security.md, privacy.md, backend.md) · code-reviewer (development.md, performance.md, mobile.md) · qa-engineer (testing.md). None skipped. No `docs/product/DESIGN_SYSTEM.md` / `TECH_STACK.md` exist in the starter; `src/theme/tokens.ts` and existing components were used as the design-system reference.

## Verdict: **Not ready**

Two data-exposure holes (no RLS on `lessons`, service-role key in a client-bundled env var) let any app user read or delete every lesson, and a regression test was skipped instead of fixed.

## Findings

| # | Severity | Area | Location | Problem | Fix |
|---|---|---|---|---|---|
| 1 | MUST | Security (A01) | `supabase/migrations/20260201000000_lessons.sql:1-7` | `lessons` is created without `enable row level security` or policies. With the public anon key anyone can `select`/`delete` every row, and the screen's `deleteLesson` relies on nothing else for authorization. | Copy the `profiles` pattern: `alter table public.lessons enable row level security;` plus select/insert/update/delete policies `using ((select auth.uid()) = owner_id)`; add `supabase/tests/lessons_rls.test.sql`. |
| 2 | MUST | Security (A02 / secrets) | `src/lib/admin.ts:4-7` | Service-role key read from `EXPO_PUBLIC_SUPABASE_SERVICE_ROLE_KEY`. `EXPO_PUBLIC_*` values are inlined into the app bundle (see `.env.example`, `env.ts`), so the key that bypasses all RLS would ship to every device as soon as this file is imported. Currently unused (dead code). | Delete `admin.ts`. Do teacher/admin actions in a Supabase Edge Function holding the key server-side, or with role-based RLS policies. Rotate the key if it was ever put in `.env.local`. |
| 3 | MUST | Test integrity | `src/components/__tests__/Button.test.tsx:13` | The double-submit/busy test was changed to `it.skip`, silently disabling a regression guard (development.md: never disable tests to make them pass). | Revert to `it(...)`; if it fails, fix `Button` or explain why the test is wrong. |
| 4 | MUST | A11y (WCAG 1.4.3) / design tokens | `src/app/lessons.tsx:30` | Title colour hard-coded `#999999`: 2.85:1 on light `background` (#FFFFFF), below 4.5:1; also bypasses tokens (no dark-mode handling). | `style={[type.body, { color: colors.textPrimary }]}`. |
| 5 | MUST | A11y (WCAG 4.1.2, 2.5.8) | `src/app/lessons.tsx:31-33` | Icon-only delete `Pressable` has no `accessibilityRole` or `accessibilityLabel` (screen readers announce nothing useful) and is 24×24, below the product minimum `minTouchTarget` (48). | `accessibilityRole="button" accessibilityLabel={`Delete ${item.title}`}`, `minWidth/minHeight: minTouchTarget` (or `hitSlop`). |
| 6 | MUST | A11y (WCAG 3.3.2) / DS | `src/app/lessons.tsx:24` | Search is a raw `TextInput` with placeholder only — no visible label or accessible name; unstyled (no token colours/border). | Use `<TextField label="Search lessons" value={q} onChangeText={setQ} />`. |
| 7 | MUST | Correctness / UX | `src/app/lessons.tsx:31, 41-45` | Delete fires on a single tap with no confirmation/undo, ignores the returned `error`, and never updates `lessons` state — the row stays on screen after a successful delete, and failures are silent. | Confirm (or undo toast), check `{ error }`, remove the item from state (or refetch) on success, show a message on failure. |
| 8 | MUST | Privacy / A09 | `src/app/lessons.tsx:42-43` | `console.log` writes the user's email to logs on every delete (personal data in logs; debug leftover). The `getUser()` call exists only for this. | Remove both lines. |
| 9 | MUST | Correctness | `src/app/lessons.tsx:15, 42, 44` | `supabase!` non-null assertion. `supabase` is intentionally `null` when `.env.local` is missing (`lib/supabase.ts`), so this screen crashes with a TypeError instead of showing setup help. | Guard: `if (!supabase) return <ScreenState kind="error" … />`. |
| 10 | SHOULD | Security (A05) | `src/app/lessons.tsx:18` | Raw user input interpolated into a PostgREST `.or()` filter string; characters like `,` `(` `)` `.` let a user alter the filter (add conditions on other columns). | Escape/strip reserved characters (or validate `q` with a schema), or use an RPC / full-text search with a parameter. |
| 11 | SHOULD | UX states | `src/app/lessons.tsx:14-20, 25-36` | No loading, empty ("no lessons" vs "no results for …"), or error state; query `error` is discarded, so failures look like an empty list. | Track `isLoading`/`error`; render `ScreenState` for loading, empty and error with retry. |
| 12 | SHOULD | Correctness / performance | `src/app/lessons.tsx:14-20` | A request per keystroke with no debounce or cancellation; responses can resolve out of order and show results for an older query. `select('*')` unpaginated fetches `description`/`owner_id` the UI never uses. | Debounce ~300 ms, ignore stale responses (flag in effect cleanup) or use TanStack Query keyed on `q`; `select('id,title')` with `.range()`/limit. |
| 13 | SHOULD | Data model (backend.md) | `supabase/migrations/20260201000000_lessons.sql:3-6` | `owner_id` nullable with no `on delete cascade`; `title` nullable with no length check; `created_at` is `timestamp` not `timestamptz`; no index on `owner_id`. | `owner_id uuid not null references auth.users(id) on delete cascade`, `title text not null check (char_length(title) <= 120)`, `created_at timestamptz not null default now()`, `create index on public.lessons(owner_id)`. |
| 14 | SHOULD | Tests (testing.md) | `src/app/lessons.tsx` (no tests) | No component tests for search/delete/empty/error, and no authorization test that user A cannot read/delete user B's lessons. | Add RNTL tests querying by role/label with a mocked client, and a pgTAP RLS test like `profiles_rls.test.sql`. |
| 15 | Suggestion | Structure | `src/app/lessons.tsx:14-20, 41-45` | Data access lives in the route component, against the feature-folder convention. | Move to `src/features/lessons/api` + a `useLessons(q)` hook so it can be unit-tested. |

## Manual checks (a11y)
VoiceOver/TalkBack: focus the search field (should announce "Search lessons, text field"), swipe to a row's delete button (should announce "Delete <title>, button"). Largest font size: titles don't clip beside the icon. Dark mode: title and input text readable.

## What's good
- Uses `FlatList` with a stable `keyExtractor` (virtualised list).
- Delete icon uses the `colors.danger` token and padding uses `space.md` from `useTheme`.
- Schema is versioned as a migration with a UUID primary key and an owner column, ready for RLS.

## Next step
Fix MUSTs 1–9 now (all small, localized edits); SHOULDs 10–14 become PLAN tasks.
