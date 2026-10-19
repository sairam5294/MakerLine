<!-- PR-body template for build-feature: the evidence a reviewer (and the owner) needs to trust a UI task without running it. Paste into the PR description; fill every section or say why it's missing. -->
# PR evidence template

Use this for every task that changes UI. Non-UI tasks keep only **What changed**, **Tests** and **Acceptance criteria → tests**.

## How to capture (starters already have the tools)

Both starters (`starter-web` Next.js, `starter` Expo) ship `@playwright/test` and `@axe-core/playwright` as dev dependencies, with `e2e/a11y.spec.ts` running axe on every route listed there. No new dependency is needed.

| Evidence | Web (`starter-web`) | Expo (`starter`) |
|---|---|---|
| Checks | `npm run check` | `npm run check` |
| E2E + axe | `npm run build` then `npm run test:e2e` | `npm run build:web` then `npm run test:e2e` (runs against the web export) |
| New route in axe | add it to the route list in `e2e/a11y.spec.ts` | add it to `routes` in `e2e/a11y.spec.ts` |
| Screenshot | `await page.screenshot({ path, scale: 'css' })` in a spec, or `npx playwright screenshot --viewport-size=390,844 <url> <file>.png` | iOS simulator: `xcrun simctl io booted screenshot <file>.png` · Android emulator: `adb exec-out screencap -p > <file>.png` · or the web export via Playwright |

- Save to `docs/product/evidence/<task-id>/` as `before-<screen>.png` / `after-<screen>.png`.
- Keep each PNG ≤ 300 KB: viewport (not full page) and `scale: 'css'` — a 3× phone screenshot is several MB and bloats git history forever.
- Use seed or test data only. **Never commit a screenshot that shows real user data** (names, emails, messages, locations).
- *Before* = the screen on the main branch (or "new screen — no before").

## Template

```markdown
## What changed (T-xx, US-xx)
- <1–3 bullets, plain English>
- How to see it: <command or route / screen>

## Screenshots
| Screen | Before | After |
|---|---|---|
| S-xx <name> | ![](docs/product/evidence/T-xx/before-<screen>.png) | ![](docs/product/evidence/T-xx/after-<screen>.png) |
States shown: loading · empty · error · offline · success  <!-- tick the ones captured -->

## Accessibility (axe-core, WCAG 2.2 AA tags)
| Impact | Violations |
|---|---|
| critical | 0 |
| serious | 0 |
| moderate | <n> — <rule ids, or "none"> |
| minor | <n> — <rule ids, or "none"> |
Routes scanned: <list> · Required: zero critical and zero serious.

## Keyboard path
<Tab order through the changed screen, e.g. "Skip link → Email → Join → error alert announced; focus returns to Email"; any trap or missing focus ring>

## Tests
`npm run check`: <pass/fail, n tests> · `npm run test:e2e`: <pass/fail, n tests, projects run>

## Acceptance criteria → tests
| AC (from PLAN / PRD) | Test file › test name |
|---|---|
| US-xx AC1 | `tests/….test.ts › …` |

## Not captured
<anything missing and why, e.g. "no simulator in this session — iOS screenshot not taken"; or "nothing">
```

## Rules

| Rule | Why |
|---|---|
| Zero critical / serious axe violations before the PR is opened | these block real users (no label, no contrast, keyboard trap) |
| Every AC maps to at least one named test | proves "done" without the owner reading code |
| Missing evidence is listed, never silently skipped | an empty section looks the same as "checked, fine" |
| Screenshots ≤ 300 KB, seed data only | repo size and privacy |
