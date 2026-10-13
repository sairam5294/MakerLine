# Must catch (1 point each) — severity in brackets
1. [MUST/Critical] Service-role key in an EXPO_PUBLIC_ variable → shipped in the app bundle; full DB bypass (src/lib/admin.ts)
2. [MUST/Critical] `lessons` table has no RLS enabled / no policies; owner_id nullable
3. [MUST/High] Delete has no ownership check (relies on missing RLS) — any user can delete any lesson
4. [MUST/High] User input interpolated into PostgREST `.or()` filter → filter injection; should escape or use separate .ilike
5. [MUST] Icon-only delete button: no accessibilityRole/label, 24×24 target (< 44/48), no confirmation/undo for destructive action
6. [MUST] Raw hex colour `#999999` (token rule) and low contrast (~2.8:1 on white)
7. [MUST] Search TextInput has only a placeholder, no label
8. [MUST] No loading / empty / error / offline states; fetch errors ignored; `supabase!` non-null assertion crashes when env missing
9. [MUST] Test weakened with `it.skip` (never weaken tests)
10. [SHOULD] console.log of user email (personal data in logs)
11. [SHOULD] `timestamp` instead of `timestamptz`; `select('*')` over-fetching; no tests for the new screen; search not debounced
Pass bar: ≥ 9/11 with no invented findings.
