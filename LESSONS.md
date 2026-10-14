# Kit lessons log

After each project (post-launch retro), add what the kit got wrong or missed. Turn each into an edit, bump the version, note it in CHANGELOG.md.

| Date | Project | What went wrong / was missing | Kit change (file) | Version |
|---|---|---|---|---|
| 2026-09-27 | kit build | Dark-mode pressed colour failed contrast (3.1:1) — caught by the new contrast test | starter `src/theme/tokens.ts` | 0.2.0 |
| 2026-09-27 | kit build | Stack header + page heading produced two `<h1>`s and pages had no `<title>` — caught by axe | starter screens use one heading + `<Head>` | 0.2.0 |
| 2026-09-27 | kit build | Accessibility ESLint plugin forces ESLint 8 (end-of-life) — dropped; a11y enforced by typed components, RNTL role queries, axe | starter | 0.2.0 |
| 2026-09-28 | kit build | RN `accessibilityState.checked` doesn't emit `aria-checked` on web → axe failure on the language radio group | starter: use `aria-checked` prop | 0.3.0 |
| 2026-09-28 | kit build | Next.js adds a hidden route-announcer `role=alert`; tests must scope alerts to the form | starter-web e2e | 0.3.0 |
| 2026-09-28 | kit build | GitHub Free can't protect branches on private repos | setup-github.sh fallback + pre-push hook | 0.3.0 |
| 2026-09-28 | evals | quality-review under-rated injection/missing states; new-idea used leading "recommended" answers on factual questions | quality-review, new-idea skills | 0.3.0 |
| 2026-09-28 | kit build | Expo and Next.js now ship their own AGENTS.md; kept as docs/kit/expo-rules.md + nextjs-rules.md so ours stays the single rules file | template/docs/kit | 0.3.0 |
| 2026-09-28 | kit build | Colours duplicated in two starters could drift | design/tokens.json + generator + kit CI cmp | 0.4.0 |
| 2026-09-28 | kit build | Similar skills in other installed plugins could be picked instead of the kit's (WCAG 2.1 vs 2.2) | "Product Kit" descriptions + precedence rule | 0.4.0 |
| 2026-09-28 | kit build | Nonce CSP forces per-request rendering — measured no Lighthouse loss (1.0) on the landing page | starter-web | 0.5.0 |
| 2026-09-28 | kit build | Code Connect needs a Figma Organization/Enterprise plan; templates added but inactive on Pro | starter/figma | 0.5.0 |
| 2026-09-28 | kit build | Lazy SDK imports + async routes cut Expo web first load ~14%; RN web still ~0.75 Lighthouse — keep public pages on Next.js | starter | 0.5.0 |
| 2026-10-13 | kit CI | Web starter e2e failed on mobile-safari only: WebKit applies CSP `upgrade-insecure-requests` to localhost (open WebKit bug 250776), so the server-action fetch was upgraded to https and failed silently | starter-web `csp.ts` emits the directive only on HTTPS requests; CI prints Playwright error context + uploads traces on failure | 0.5.1 |
| 2026-10-14 | quick-start audit | GETTING-STARTED assumed the kit was already on the Mac and pointed at a git-ignored `.plugin` file; a stranger cloning from GitHub had no install path. Both starters, the gate and the marketplace install all passed on a fresh clone | GETTING-STARTED Part 1 rewritten (clone step, marketplace install, `scripts/build-plugin.sh`); README setup block | 0.6.0 |
