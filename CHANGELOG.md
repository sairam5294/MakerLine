# Changelog

Versions follow MAJOR.MINOR.PATCH. Each project records the kit version it started from in `docs/product/STATUS.md`.


## 0.14.0 — 2026-10-21
Quick Idea Pack runs are cheaper and more honest (measured 120k → 106k tokens, 19 → 12 tool calls; the verdict follows the owner's stated goal, and the business case when none is stated). Docs site rebuilt: theme switch, diagrams, demo, comparison, showcase, Hindi and Spanish home pages, email route for accessibility barriers. Details:
Site, part 2: a replayable demo of a Quick run (and `docs/kit/brand/makerline-demo.gif` for READMEs, plays once), "Why not just ask Claude?" comparison, link to the sample one-pager, the home page in Hindi and Spanish (AI-translated, marked as such, with language links and `hreflang`), case studies become a showcase with an "add your project" form, "What a run costs" in the 5-minute guide, and a no-GitHub email route for accessibility barriers. Kit docs: `LAUNCH.md` (LinkedIn, article outline, Product Hunt, communities) and `VOICEOVER-TEST.md` (screen reader script).
Docs site: fixed the broken logo on the overview page (brand images now served by the site, with a dark-theme version) and the site address (GitHub Pages uses the lowercase `…/makerline/`). New home page with a numbers band, a "pick your path" router, the six stops drawn as one line, a "many sources in, one verdict out" diagram, a measured token chart and a maker credit. Light/dark switch, mobile menu, copy buttons, "On this page" contents for long pages, reading time, reading-progress line, page-to-page fades, a page-not-found page and a fuller footer. All motion is off under reduced motion; 0 axe issues on 23 pages in both themes; no sideways scroll at 320 px; works without JavaScript. The 5-minute guide's token figure now matches the measured run (about 120k, not 50–70k).
Quick run trimmed toward 70–100k tokens: research capped at 4 batched searches and 1 page read (was 8 and 4), ≤ 12 tool calls (was 25) with all documents written in one shell call that ends with the checker, Quick brief/CLARITY/one-pager/README skeletons inline in quick-run.md (no template reads; STATUS updated by one command), only the launch market's rows of the accessibility-law summary, tighter Quick caps (EVALUATION 1,400, CLARITY 600, COMPETITORS 450, one-pager 450) enforced by the checker; Quick reading 4,526 → ~2,550 words. Verdict honesty: the verdict follows the goal the owner stated; with no stated goal the business lens decides and the assumed goal goes to CLARITY (Quick guide, rubric, evaluate-idea). Quick fetches default to 0 (≤ 1 for a must-have fact), title-only search results cited as such, DECISIONS/COSTS row formats in the guide, read budget counts all 3 reads, template-read command exits 0 without OWNER.md.

## 0.13.0 — 2026-10-20
Renamed to MakerLine (plugins makerline and makerline-idea; commands /makerline:… and /makerline-idea:…). New logo, marks, favicon set, social previews and brand guide. Accessibility statement on the site. Independent accessibility audit: WCAG 2.2 gaps closed in the rules (flashing, text spacing, hover/focus content, live captions, audio description, pointer and keyboard criteria), AODA customer-service duties in full, beyond-WCAG list (508, EN 301 549), ACR/VPAT how-to, one severity mapping, one list of seven UI states, glossary. Wireframe template and local cockpit fixes; cockpit save form works in Chrome

## 0.12.1 — 2026-10-20
Quick run in one guide (157k → 120k tokens, 30 → 19 calls); project-setup trimmed; kit-ui accessibility check in CI (0 axe violations) and verified on Python 3.9; directory submission screenshots and checklist progress

## 0.12.0 — 2026-10-20
Roadmap release: Try-it-ready skill descriptions and author credit; token trim round 2 (Quick 157k → 146k, 30 → 24 calls; Quick-only templates, accessibility-law summary, context-budget split, Idea card, model routing per step); validation results loop; Figma wireframes when connected; PR evidence (screenshots, axe, tests); 'what changed' on re-runs; connector privacy table; standards refresh (MASVS 2.1, DPDP Rules dates, COPPA, EU AI Act Art. 50, store policies, model names); docs site landing + walkthrough + case studies; directory submission pack; issue forms + monthly kit retro; rules for 12 more AI coding tools from one AGENTS.md; local web cockpit (kit-ui); branch cleanup script

## 0.11.0 — 2026-10-20
Skills restructured to a consistent, scannable shape (style guide in docs/kit/SKILL-STYLE.md); plugin README with Try-it prompts, command tables and example workflows; CONNECTORS.md and .mcp.json (GitHub, Figma, Vercel, Supabase, Notion, Linear) for both plugins; standalone Idea Pack README

## 0.10.0 — 2026-10-20
One command runs the whole kit: /product-kit:start and /idea-pack:start; 'give me everything' (full Idea Pack), 'set it all up' after approval (tool plan, names + brand, stack, design system, full PRD, engineering docs, project setup in one go), 'build it' (one task per session); token rules from measured runs (few large tool calls, document size caps with checker warnings, exact Quick reading list); portfolio/learning and personal-tool verdicts; tested on Trust Kit and the task tracker

## 0.9.0 — 2026-10-20
After approval, the full project set: brand kit in name-product (logo concept + easy path + guidelines, colours, fonts, icons, rules); tool-plan skill (split jobs across Claude, ChatGPT, Cursor, Codex by what the owner has); engineering docs gain LIFECYCLE; new project-setup skill (README, SETUP from clone/ZIP to deploy, STRUCTURE, fully commented .env.example, GITHUB rules for PRs/merge/branches/previews/retention/storage, CONTEXT_PACK, scoped .cursor rules, .claude project skills, .github copilot/CODEOWNERS/repo-health); exp/ branches; build-before-push; per-phase research budgets; plugin install steps; fixes from two more runs

## 0.8.0 — 2026-10-19
Accessibility, inclusion and compliance lens (accessibility-strategist agent, accessibility-law reference for AODA/ADA/508/EAA/UK/India/AU/JP, global inclusion baseline, IAAP WAS alignment); Quick/Standard/Deep depth modes with token rules and check_idea_pack.py; engineering-docs skill (ARCHITECTURE, DATABASE, SECURITY, CODE_STYLE, TESTING, RULES, MEMORY); branch convention `<type>/<Mon>-<DD>-<summary>` enforced by hook + CI; standalone idea-pack plugin; GitHub Pages docs site; Ontario eval case; fixes from three blind runs

## 0.7.0 — 2026-10-16
Idea Pack: clarity log, honest-coach evaluation with strongest version and path to Go, COMPETITORS with differentiator test, idea-champion agent, design direction + clickable wireframes, draft PRD, one-pager; owner-unavailable mode; tested blind on two eval cases

## 0.6.1 — 2026-10-14
Figma library published to Community (https://www.figma.com/community/file/1692097443572763844/product-kit-design-system); kit docs link to it; publish guide updated with the real thumbnail, category and author steps

## 0.6.0 — 2026-10-14
Open-source baseline (MIT, governance, public repo, CI green), quick start for strangers (clone + marketplace install + build-plugin), adopt mode in upgrade-project for existing projects of any stack with tests, projects git-ignore OWNER.md, stack-aware pre-push check, actions pinned to current majors, examples/ with the RhythmBuddy case study and review, quality-review scope rule for adopted projects, Lighthouse median-of-3, WebKit CSP fix in the web starter

## 0.5.0 — 2026-09-28
**Figma library** — "Product Kit — Design System": Primitives + Semantic (Light/Dark modes) + Dimensions variables from tokens.json, 5 type styles, Button / TextField / ScreenState component sets bound to variables. Code Connect templates (`starter/figma/*.figma.ts`, parse-validated) switch on with a Figma Organization/Enterprise plan.
**Expo web** — Sentry/PostHog load lazily (dynamic import) + async routes on web: first load 509 KB → ~440 KB gzipped; SDKs only download when keys are set.
**Web starter security** — strict nonce-based CSP via `src/proxy.ts` (no unsafe-inline scripts; e2e test fails on any CSP violation) — Lighthouse still Performance 1.0 / Accessibility 1.0 / SEO 1.0. Waitlist: per-IP rate limit + optional Cloudflare Turnstile (fails closed).
**AI harness** (`starter-web/src/ai/`) — server-only provider wrapper (timeout, retry, Zod-validated output, typed failures), versioned prompt, example feature with PII redaction + per-user quota, 8 mocked tests, live eval runner `npm run ai:eval` with 5 cases (incl. prompt injection, personal data, Telugu).
**Plugin marketplace** — `.claude-plugin/marketplace.json`: install/update with `claude plugin marketplace add <you>/product-kit` → `claude plugin install product-kit@product-kit-marketplace` (tested).
**Costs** — `docs/product/COSTS.md` per project; handoff/post-launch log spend; portfolio shows cost to date; outcomes include total cost.
**Assistive-tech user testing** — guide for recruiting, paying and running sessions with screen-reader and other disabled users; wired into validate-idea, test-plan, ship-checklist.

## 0.4.0 — 2026-09-28
**Plugin overlap** — kit skills labelled "Product Kit" + precedence rule in CLAUDE.md/kickoff; `docs/kit/PLUGIN-OVERLAP.md` maps which of your design/engineering/product-management skills the kit replaces vs complements.
**Upgrades** — `scripts/upgrade-project.sh` (preview → `--apply`): replaces kit-owned files with backups, never touches yours, shows diffs for AGENTS.md/settings; projects record `.product-kit-version`.
**One token source** — `design/tokens.json` (W3C Design Tokens) → `npm run tokens` → `src/theme/tokens.generated.ts` in both starters; `npm run check` fails if stale; Figma ↔ tokens.json sync guide (Figma connector or Tokens Studio).
**Portfolio** — `scripts/portfolio.py` + `portfolio` skill: accessible light/dark dashboard (`portfolio/index.html`) of all projects' phase, gate, next step, staleness and idea outcomes.
**Owner profile** — `owner/OWNER.md` copied into each project; new-idea/evaluate-idea/tech-stack read it instead of re-asking.
**Cross-project learning** — `portfolio/OUTCOMES.md`: post-launch logs what happened vs the evaluation; evaluate-idea applies its calibration notes.
**AI review on PRs** — `.github/workflows/ai-review.yml` (claude-code-action v1; OAuth token or API key; skips without a secret; sonnet + 30-turn cap).
**Monthly evals** — scheduled task on your Mac (3rd of each month) + `evals/RUNBOOK.md`; quarterly adds a full evaluation case.
**AI features** — `ai.md` standard + `ai-feature` skill: when to use AI, server-side calls, prompt versioning, structured output, AI UX patterns, eval sets, safety, privacy, cost per user.
**AI content rules** — rights to AI outputs, no imitation of real artists/people, India IT Amendment Rules 2026 labelling, Google Play AI-content policy.
**Deep-scan fixes (independent audit, 25 findings)**
- Hooks now parse Claude's JSON with python3/node. The old regex let `git push origin main`, `printenv` and `env` through, and wrongly blocked `.env.example`. There are now 30 hook tests using real hook JSON, and they run in kit CI.
- AI tools can no longer approve their own evaluation. Only the owner approves, with `scripts/approve.sh`.
- lefthook: a secret found by gitleaks now actually blocks the commit; pre-push no longer breaks before the app exists; lint and format run in sequence.
- CI: removed job-level `hashFiles` (GitHub rejects it, which silently disabled all CI); actions pinned to SHAs; WebKit e2e added; new RLS database test job; actionlint runs in kit CI.
- Web starter: security headers (CSP, HSTS, nosniff…); waitlist inserts only via the server's service key (no public DB access). Lighthouse reports are kept private.
- Branch protection applies to admins too. Worktrees live next to the project. `.env.example` is readable. Validation landing pages pass the gate (`validation/` or a separate project).
**Local models** — Ollama guidance in context-budget + `scripts/local-ai.sh` (summarise interviews, draft translations, ask) — free and private.

## 0.3.0 — 2026-09-28
**GitHub** — `scripts/setup-github.sh`: private repo + push + branch protection (needs gh CLI; falls back gracefully on GitHub Free) + Dependabot alerts. Local `no-push-to-main` pre-push hook as the free safeguard. Kit repo gets its own CI (`.github/workflows/kit-ci.yml`: sync check + both starters).
**CI dry-run** — fresh `--starter` and `--web` projects: npm ci, check, audit (no high/critical), web build, Playwright + axe, gitleaks — all green.
**Web starter** (`starter-web/`, `new-project.sh --web`) — Next.js 16 + Tailwind 4 landing page with accessible waitlist (server action, honeypot, insert-only RLS), tokens → CSS variables, skip link, privacy page. Lighthouse: Performance 0.98 · Accessibility 1.0 · SEO 1.0 · LCP 1.6 s (Expo web: 0.79 / 3.7 s).
**Expo starter** — English/Telugu/Hindi (i18next; key + placeholder parity test; taller line height for Indic scripts; accessible language switcher), Sentry (off without DSN, PII scrubbed), PostHog (off without key, opt-in per user, sanitised props). 47 unit + 8 e2e tests.
**Evals** — quality-review (planted-bug branch: 11/11 found) and new-idea (10/11) added and run; fixes: severity rule in quality-review, no "recommended" answers on factual questions, shorter first reply.
**Cost** — per-agent model routing (sonnet/medium for checklist agents), research cache (`docs/product/research/`), measured cost table in context-budget.

## 0.2.0 — 2026-09-27
**Enforcement**
- CI (GitHub Actions): approval gate, secret scan, typecheck/lint/tests, dependency audit, web build + axe + Lighthouse.
- Git hooks (lefthook): approval gate, gitleaks, lint, format on commit; full check on push.
- Claude Code: permission rules + hooks (approval gate, dangerous-command guard, auto-format). Codex: sandbox + approval config. Cursor: permissions.json, .cursorignore.
**Starter** — tested Expo SDK 57 + Supabase app: tokens with automatic contrast tests, accessible Button/TextField/ScreenState, passwordless sign-in, chunked secure session storage, RLS migration + pgTAP test, Jest, Playwright + axe, Lighthouse, Maestro.
**New skills** — validate-idea, handoff, design-qa, post-launch, standards-refresh. Expert-review brief in ship-checklist.
**MCP** — context7, Playwright, Figma for all three tools; Supabase/GitHub/Vercel documented.
**Parallel work** — `scripts/worktree.sh`.
**Token optimisation** — ~45% smaller always-loaded text (skill + agent descriptions, AGENTS.md); leaner skill bodies; context-budget standard; subagents return ≤ 300-word summaries.
**Fixes** — agents no longer duplicated in Claude (Cursor agents moved to `.cursor/agents`); relative standards paths; approval gate skips the scaffold commit; new-project never overwrites files.
**Tested** — evaluate-idea run on 3 sample ideas with planted flaws (see `evals/`).

## 0.1.0 — 2026-09-27
First version: 13 skills, 12 agents, standards, AGENTS.md, Cursor rules, sync + new-project scripts.
