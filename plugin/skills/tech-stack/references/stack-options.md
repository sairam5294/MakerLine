# Stack Options Catalogue

Starting points for the 2–3 candidates in `tech-stack` — always verify current versions and pricing before recommending.

## Recommended default for a solo, AI-assisted builder (web + iOS + Android)

| Layer | Choice | Why |
|---|---|---|
| App (iOS/Android/web) | **Expo (React Native) + Expo Router**, TypeScript | One codebase for 3 platforms; file-based routing; EAS build/submit/updates; AI tools know it well |
| Marketing site / web app with SEO | **Next.js** (App Router) on **Vercel** | SEO, fast pages; share TS types and logic with the app. Vercel's free Hobby plan is for personal, non-commercial use — a product that charges (or a business site) needs Pro or another host; check current terms and price before launch |
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

| Option | Stack | Notes |
|---|---|---|
| Web only, content-first | Next.js (or Astro) + Supabase + Vercel | Add a PWA for "installable" feel before committing to stores |
| No-code/low-code prototype for validation | Figma prototype, Framer site, or a Softr/Glide app on top of Airtable/Google Sheets | To test demand before coding |

## Native options (when justified)

| Platform | Stack |
|---|---|
| iOS | Swift + SwiftUI, SwiftData/Core Data, StoreKit 2 |
| Android | Kotlin + Jetpack Compose, Room, Play Billing |

Choose native when: heavy real-time audio/video processing, AR, widgets/watch-first experiences, platform-specific integrations, or a performance bar Expo can't meet. Cost: two codebases.

## Other cross-platform

| Option | Strengths | Trade-offs |
|---|---|---|
| **Flutter** (Dart) | Excellent performance and consistent UI | Smaller web SEO story; different language from web stack |

## Decision factors to show the owner

| Factor | Question |
|---|---|
| Platforms | Which platforms at launch? Is SEO important? |
| Team | Solo + AI? Will you hire? What do local freelancers know? |
| Features | Offline, media, real-time, background audio, AI, payments? |
| Cost | Free tier limits; cost at 10k users; store fees |
| Lock-in | How hard to move off this provider later? |
| AI-friendliness | Is it popular, well-documented, stable? |

## Tools beyond code (for the evaluation's provisional tools table)

Verify current pricing before recommending; prefer tools the owner already has (OWNER.md).

| Need | Default | Alternatives | Notes |
|---|---|---|---|
| Design & prototyping | Figma (+ the kit's Community design system) | Penpot (open source) | Wireframes start as the kit's HTML template; push to Figma when the owner wants to iterate visually |
| Landing page / waitlist | Kit `--web` starter on Vercel | Framer, Carrd | Validation before building |
| Forms & surveys | Tally, Google Forms | Typeform | Interview screeners, waitlist questions |
| User interviews | Google Meet / Zoom + Calendly | Cal.com | Record with consent; summarise with `scripts/local-ai.sh` |
| Prototype testing | Wireframe prototype mode, Figma prototype | Maze, Lyssna | 5 users, 3 tasks |
| Product analytics | PostHog | Plausible (web-only, simple) | No personal data in events |
| Feedback & support | GitHub issues (dev tools), Tally form, WhatsApp Business (India consumer) | Canny, Crisp | One channel to start |
| Project tracking | `docs/product/PLAN.md` + GitHub issues | Linear, Notion | Keep the plan in the repo so every AI tool reads it |
| Building with AI | Claude Code + MakerLine | Cursor, Codex | Same AGENTS.md and skills in all three |
| Payments (India) | Razorpay / UPI | Cashfree, PhonePe PG | App-store rules for digital goods |
| Email | Resend | Postmark | |
