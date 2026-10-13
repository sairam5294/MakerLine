# Stack Options Catalogue

Starting points — always verify current versions and pricing before recommending.

## Recommended default for a solo, AI-assisted builder (web + iOS + Android)

| Layer | Choice | Why |
|---|---|---|
| App (iOS/Android/web) | **Expo (React Native) + Expo Router**, TypeScript | One codebase for 3 platforms; file-based routing; EAS build/submit/updates; AI tools know it well |
| Marketing site / web app with SEO | **Next.js** (App Router) on **Vercel** | SEO, fast pages; share TS types and logic with the app |
| UI | NativeWind (Tailwind for RN) or Tamagui; shadcn/ui on web | Token-based styling that maps to a design system |
| Backend / DB / auth / storage | **Supabase** (Postgres, Auth, Storage, Edge Functions, RLS) | Managed, SQL, row-level security, generous free tier |
| Alternative BaaS | Firebase | Strong mobile SDKs, offline sync; NoSQL modelling is harder to keep consistent |
| Payments | Razorpay (India web), Stripe (global web), RevenueCat for App Store / Play subscriptions | Store rules require in-app purchase for digital goods in apps |
| Analytics | PostHog (product analytics, flags, session replay with masking) | Privacy controls, free tier |
| Errors | Sentry | Web + RN + server |
| Email | Resend / Postmark | Deliverability |
| AI | Provider SDK via server functions only (Anthropic / OpenAI / Google) | Keep keys server-side; cap usage |
| Media | Supabase Storage / Cloudflare R2 + CDN; Mux or Cloudflare Stream for video | Streaming, cost |
| Testing | Vitest + Testing Library, Playwright (web e2e), Maestro (mobile e2e), axe-core | See testing standard |
| CI/CD | GitHub Actions + Vercel previews + EAS Build | Automated checks on every PR |

## Simpler options

- **Web only, content-first**: Next.js (or Astro) + Supabase + Vercel. Add a PWA for "installable" feel before committing to stores.
- **No-code/low-code prototype for validation**: Figma prototype, Framer site, or a Softr/Glide app on top of Airtable/Google Sheets — to test demand before coding.

## Native options (when justified)

- **iOS**: Swift + SwiftUI, SwiftData/Core Data, StoreKit 2.
- **Android**: Kotlin + Jetpack Compose, Room, Play Billing.
- Choose native when: heavy real-time audio/video processing, AR, widgets/watch-first experiences, platform-specific integrations, or a performance bar Expo can't meet. Cost: two codebases.

## Other cross-platform

- **Flutter** (Dart): excellent performance and consistent UI; smaller web SEO story; different language from web stack.

## Decision factors to show the owner

| Factor | Question |
|---|---|
| Platforms | Which platforms at launch? Is SEO important? |
| Team | Solo + AI? Will you hire? What do local freelancers know? |
| Features | Offline, media, real-time, background audio, AI, payments? |
| Cost | Free tier limits; cost at 10k users; store fees |
| Lock-in | How hard to move off this provider later? |
| AI-friendliness | Is it popular, well-documented, stable? |
