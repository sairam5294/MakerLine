# Product Kit Starter — Expo (iOS · Android · Web) + Supabase

Tested base for new products: accessible components, design tokens with automatic contrast checks,
passwordless sign-in, secure session storage, RLS-protected database, unit + e2e + accessibility tests.

## First run (10 minutes)
```bash
npm install
cp .env.example .env.local        # add your Supabase URL + anon key (Supabase dashboard → Project settings → API)
npx expo start                    # press i (iOS simulator), a (Android), w (web) — or scan the QR code with Expo Go
npx lefthook install              # git hooks: approval gate, secret scan, lint, format
```

## Database
```bash
npx supabase init                 # once: creates supabase/config.toml (keeps the migrations folder)
npx supabase start                # local Postgres + auth in Docker
npx supabase db reset             # applies supabase/migrations locally
npx supabase test db              # runs supabase/tests (RLS/authorization tests)
```

## Quality commands
| Command | What it does |
|---|---|
| `npm run check` | typecheck + lint + unit tests (run before every commit/PR) |
| `npm run contrast` | fails if any token colour pair breaks WCAG AA (light + dark) |
| `npm run build:web && npm run test:e2e` | web build + Playwright flows + axe accessibility scan |
| `maestro test .maestro/` | mobile smoke test on a simulator/emulator |

## Languages, errors, analytics
- **Languages** (`src/i18n/`): English, Telugu, Hindi. Telugu and Hindi are machine-drafted, so get a native speaker to review them. Add a language with a new `xx.ts`; a test fails if any key or `{{placeholder}}` is missing. Telugu/Hindi get 20% taller line height automatically (no clipped matras).
- **Error tracking** (Sentry): off until `EXPO_PUBLIC_SENTRY_DSN` is set. No user identity is sent, and emails/phones are scrubbed. For readable stack traces in store builds, add `SENTRY_AUTH_TOKEN` as an EAS secret.
- **Analytics** (PostHog): off until `EXPO_PUBLIC_POSTHOG_KEY` is set, and **opt-in per user** (`setAnalyticsConsent(true)`). Properties are sanitised. Keep it off entirely for children's apps.

## Where things live
```
src/app/            screens (Expo Router: every file = a route)
src/components/     shared accessible components (Button, TextField, ScreenState)
src/features/<x>/   feature logic + tests (keep business logic out of screens)
src/lib/            env validation, Supabase client, secure session storage, privacy, monitoring, analytics
src/i18n/           translations (en, te, hi) + language detection
src/theme/          design tokens — the only place raw colours are allowed (lint enforces this)
supabase/           migrations (with RLS) and database tests
e2e/  .maestro/     end-to-end tests (web / mobile)
```

## Rename before you build
`app.json`: name, slug, scheme, `ios.bundleIdentifier`, `android.package` · `package.json`: name · `.maestro/smoke.yaml`: appId.

## Known trade-off
Expo web bundles are large (~2 MB). Fine for app-like web; for SEO-critical marketing pages, add a Next.js site
(see tech-stack options). Lighthouse performance is a warning, accessibility is a hard gate.

Expo specifics for AI agents: `docs/kit/expo-rules.md` (always use `npx expo install`, check versioned docs).
