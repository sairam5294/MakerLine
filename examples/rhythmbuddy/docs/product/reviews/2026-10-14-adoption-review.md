# Quality review — RhythmBuddy v1.0 at adoption · 2026-10-14

**Scope.** Boot-path modules listed in `STATUS.md` (no diff: the project was adopted whole), `ui/`, `tests/`, `check_accessibility.py`, `ACCESSIBILITY.md`, `backup_manager.py`, `update_checker.py`, `export_stats.py`, entitlements, build and release scripts, GitHub workflows. Reviewers: accessibility-auditor, security-reviewer, code-reviewer + qa-engineer (Product Kit v0.5). Every finding was checked against the source line before it went in this table; speculative ones were dropped.

**Verdict: Ready after fixes.** The app is shipped and stable, but four accessibility AA failures, two tests that write to the developer's real data and hit the network, and unpinned dependencies and actions must be fixed before the next release. Nothing here blocks daily use.

## Findings

| # | Severity | Area | File:line | Problem | Fix |
|---|---|---|---|---|---|
| 1 | MUST | a11y | `rhythm_buddy.py:2000` | Section captions use `secondaryLabelColor` at 11 pt: measured 3.9:1 on the Preferences card, below WCAG 1.4.3's 4.5:1 | Use `labelColor` or a darker grey; add the pair to `check_accessibility.py` |
| 2 | MUST | a11y | `rhythm_buddy.py:2373-2388` | ✎ and ✕ buttons are glyph-only with a tooltip and no accessibility label; `ACCESSIBILITY.md` claims every Preferences control is labelled | `setAccessibilityLabel_(f"Edit {name}")` / `f"Delete {name}"` |
| 3 | MUST | a11y | `rhythm_buddy.py:940` | Decorative mascot is exposed to VoiceOver as "RhythmBuddy character" | `setAccessibilityElement_(False)` (already done for the emoji at :972) |
| 4 | MUST | a11y | `rhythm_buddy.py:1119-1131` | Custom-drawn Done/Snooze/Skip buttons have no visible focus indicator (2.4.7, AA); `ACCESSIBILITY.md` calls this "minor" | Draw a focus ring when the button is first responder |
| 5 | MUST | test | `tests/test_backup.py:210-229` | `import_all_data()` runs with default paths, so the test overwrites the developer's real `~/Library/Application Support/RhythmBuddy/settings.json` and `stats.json`; the test `return`s instead of asserting, so it cannot fail | Monkeypatch `SETTINGS_PATH`, `STATS_PATH`, `BACKUP_DIR` to `tmp_path`; replace `return True/False` with `assert` |
| 6 | MUST | test | `tests/test_update_checker.py:134` | `test_live_update_check` calls api.github.com and wraps everything in `except Exception: return True`; never fails, breaks the no-real-network rule | Mock `urllib.request.urlopen`; assert on the parsed result |
| 7 | MUST | security | `requirements.txt`, `requirements-dev.txt`, `Start RhythmBuddy.command:15` | Dependencies unpinned, no lockfile, auto-installed with `--break-system-packages` on first launch | `pip-compile --generate-hashes`; install from the lock; add Dependabot for pip |
| 8 | MUST | security | `.github/workflows/ci.yml`, `release.yml` | Actions pinned to mutable tags (`@v4`, `action-gh-release@v1`); `ci.yml` has no `permissions:` block | Pin to commit SHAs; `permissions: contents: read` |
| 9 | SHOULD | code | `stats_store.py:57-59` | `record_completed` saves before `_record_timestamps` mutates memory; the last timestamps are lost on quit | `save()` after `_record_timestamps` |
| 10 | SHOULD | code | `stats_store.py:316` | `int(completed/due)` truncates to 0 unless 100%, so `best_weekday` is almost always `None`; the test at `test_phase3_enhancements.py:82` never asserts it | Drop `int()`; write the failing test first |
| 11 | SHOULD | code | `rhythm_buddy.py:3811-3815` | Scheduler uses naive datetimes feeding a real-time `NSTimer`; a timer spanning a DST switch fires an hour off; no DST test | Compare aware local datetimes (`astimezone()`); add a `zoneinfo` test |
| 12 | SHOULD | code | `rhythm_buddy.py:3650-3652` | Snoozes live only in memory; a snoozed reminder reverts to its natural schedule after a restart | Persist snoozes with expiry in settings or stats JSON |
| 13 | SHOULD | code | `rhythm_buddy.py:3680` → `update_checker.py:173` | Synchronous `urlopen(timeout=10)` in controller init on the main thread; menu bar can hang up to 10 s offline | Background thread or `NSOperationQueue`, marshal the result to the main thread |
| 14 | SHOULD | security | `backup_manager.py:133-186`, `rhythm_buddy.py:4513` | Import checks key presence only; values flow unchecked into `Settings.from_dict` and `stats.json`; `config_validator.py` exists but is never called | Run `config_validator` on import; type-check stats counts; wrap `_merge_stats` errors in `ValidationError` |
| 15 | SHOULD | privacy | `RhythmBuddy.entitlements:14-27` | Requests `healthkit.access: health-records` (clinical records) and CloudDocuments; code only writes DietaryWater/MindfulSession and uses the KV store | Remove both; entitlements match actual use |
| 16 | SHOULD | security | `release.yml:81-116`, `build_app.py:253` | Release zip is unsigned with no checksums | Publish SHA-256 sums; sign and notarize per `docs/CODE_SIGNING.md` |
| 17 | SHOULD | a11y | `rhythm_buddy.py:328-333, 40-41` | Font sizes are fixed; the "enlarged system text grows the popup" claim (1.4.4) is false | `preferredFontForTextStyle` or drop the claim |
| 18 | SHOULD | a11y | `check_accessibility.py:92-141` | Wallpaper contrast is tested only against pure black and white; mid-grey wallpaper fails 3:1 for the urgent popup and Done button; target size and animation length are constant checks, not rendered behaviour | Sweep wallpaper luminance; test the real layout; soften the "any wallpaper" claim |
| 19 | SHOULD | a11y | `rhythm_buddy.py:1941-1969` | Preferences window is ~1158 pt tall, non-resizable, no scroll view; Save can fall off-screen on laptops | Scroll view or resizable window |
| 20 | SHOULD | a11y | `ACCESSIBILITY.md:1-5`, `rhythm_buddy.py:920` | Targets WCAG 2.1 not 2.2; popup at window level 25 on all Spaces can cover the focused control in another app (2.4.11) | Map 2.2 criteria; keyboard-reachable dismiss or reposition |
| 21 | SHOULD | code | `rhythm_buddy.py` (4910 lines, 7 classes); `APP_VERSION` in 4 files; duplicate `log()` in `ui/login_item.py:22` | God object and duplicated constants; `STATUS.md` already lists the extraction | Continue the `ui/` extraction; single `version.VERSION` and logging helper |
| 22 | SHOULD | test | `tests/` | No tests for `themes`, `sounds`, `version`, or the controller's fire/snooze/done logic; ~25 tests assert nothing (`config_validator` valid cases, `healthkit:24/:52`, `auto_theme:54`); `test_ml_insights.py` skips 16 with a reason (fine) | Extract a headless controller engine; add asserts |
| 23 | SHOULD | security | `.pre-commit-config.yaml`, `ci.yml` | No secret scan or dependency audit | Add gitleaks and `pip-audit` |
| 24 | Suggestion | code | `stats_store.py:37-38, 74-75`; `rhythm_buddy.py:3920` | Silent `pass` on corrupt stats; a `show_reminder` exception after `record_due` makes the group vanish | Log with context; record missed on failure |
| 25 | Suggestion | code | `rhythm_buddy.py:3899-3906` | Focus-mode suppression counts as *missed* and breaks streaks for reminders never shown | Re-snooze instead of `record_missed` |
| 26 | Suggestion | security | `rhythm_buddy.py:4796` | `webbrowser.open(result.release_url)` trusts the API's `html_url` | Require the `https://github.com/sairam5294/rhythm_buddy/` prefix |
| 27 | Suggestion | privacy | `rhythm_buddy.py:526` | User-defined reminder titles are logged to `~/Library/Logs`; LaunchAgent captures stdout | Log the reminder id, not the title |
| 28 | Suggestion | security | `custom_sounds.py:170-176` | `name` used in a filename unsanitised (`../` escapes `sounds_dir`); module not yet wired | `Path(name).name` before use |
| 29 | Suggestion | hygiene | git-tracked `.coverage`; `ui/palette.py:35-36` comment; stale Preferences screenshot in docs | Binary with local paths committed; comment says 15.1:1 / 9.4:1, real values 14.55:1 / 9.08:1; screenshot shows 5 sections, code builds 7 | `.gitignore` + remove; fix comment; retake screenshot |

## What is good

- `scheduler.py` and `models.py` are Cocoa-free and well tested (37 scheduler tests covering snooze, floor and skip-date).
- The text-contrast table in `ACCESSIBILITY.md` matches recomputed ratios exactly; Reduce Motion skips the walk-in; the 5 s animation cap, 44 pt button floor, Increase Contrast borders, VoiceOver announcements and menu-bar twins for Done/Snooze/Skip are all present as documented.
- Atomic write-and-rename in settings, stats and backups; every `subprocess` call uses argument lists with no shell; the only network call is a TLS-verified GET to a fixed GitHub URL with a 10 s timeout, parsed as JSON and shown as text — exactly what `docs/PRIVACY.md` says.
- CI runs lint, mypy, the accessibility checker and pytest on four Python versions.

## Next

MUSTs 1–8 are each under an hour; fix them in one branch (`fix/adoption-review-musts`) with a failing test first for 5, 6, 9 and 10. SHOULDs become tasks in `docs/product/PLAN.md`.
