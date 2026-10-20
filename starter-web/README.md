# MakerLine Web Starter — Next.js (SEO-fast landing page + waitlist)

Use for: **validate-idea landing pages**, marketing sites, SEO-critical public pages, simple web apps.
(Use the Expo starter for app-like products on iOS/Android/web.)

Measured (Lighthouse, mobile, Sept 2026, with strict nonce CSP): Performance 1.0 · Accessibility 1.0 · SEO 1.0 · LCP 1.6 s.

## Security & AI
- Strict CSP with a per-request nonce (`src/proxy.ts`, `src/lib/csp.ts`), HSTS, nosniff, no framing. An e2e test fails on any CSP violation.
- Waitlist: server-side validation, honeypot, 5 attempts per IP per 10 min (`src/lib/rateLimit.ts`), optional Cloudflare Turnstile (`src/lib/turnstile.ts`, set both keys).
- AI: `src/ai/provider.ts` (server-only, timeout, retry, schema-validated output) + example `src/ai/features/summariseFeedback.ts`. Live evals: `ANTHROPIC_API_KEY=… AI_MODEL=… npm run ai:eval` (cases in `evals/ai/`).

## First run
```bash
npm install
cp .env.example .env.local        # Supabase URL + service key (server-only; optional for local preview)
npm run dev                       # http://localhost:3000
npx lefthook install
```
Waitlist storage: run `supabase/migrations/…_waitlist.sql` in your Supabase project (RLS on, no public access; only the server adds rows).
Deploy: push to GitHub → import in Vercel → add the two server-only env vars.

## Quality commands
| Command | What it does |
|---|---|
| `npm run check` | typecheck + lint (incl. jsx-a11y) + unit tests |
| `npm run contrast` | WCAG AA check of all token colour pairs (light + dark) |
| `npm run build && npm run test:e2e` | axe accessibility on every route, skip link, form errors |
| `npx @lhci/cli autorun` | performance ≥ 0.9, accessibility ≥ 0.95, SEO ≥ 0.9 (fails CI below) |

## Built in
Design tokens → CSS variables → Tailwind classes (one source, lint blocks raw colours) · skip link · visible focus ·
reduced motion · no zoom blocking · accessible form (label, `aria-invalid`, announced errors, keeps input, works without JS) ·
honeypot spam trap · server-side validation · no public database access · security headers (CSP, HSTS…) · privacy page.

Next.js specifics for AI agents: `docs/kit/nextjs-rules.md` (read the bundled docs in `node_modules/next/dist/docs/`).
