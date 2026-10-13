# Performance Standard

Design for a mid/low-end Android phone on a patchy 4G connection — if it's fast there, it's fast everywhere.

## Web — MUST budgets (75th percentile, mobile)

- Core Web Vitals: **LCP ≤ 2.5 s**, **INP ≤ 200 ms**, **CLS ≤ 0.1**.
- Initial JS ≤ ~170 KB compressed for the first route; code-split everything else.
- Lighthouse Performance ≥ 90 and Accessibility ≥ 95 in CI on key pages.
- Exception: Expo (React Native) web builds of app screens behind sign-in — performance is a warning at ≥ 0.8 because the RN web bundle is large. Public, SEO or marketing pages MUST use the web starter (Next.js) and meet ≥ 90.

Practices: server/static rendering for public pages; `next/image` or responsive `srcset` with AVIF/WebP; lazy-load below the fold; preload the LCP image and critical fonts; `font-display: swap` and subset fonts (Indic fonts are large — subset them); avoid layout shift by reserving media dimensions; cache via CDN.

## Mobile — MUST budgets

- Cold start to interactive ≤ 2 s on a mid-range Android device; ≤ 1 s warm.
- 60 fps scrolling; no JS-thread blocking > 50 ms during interactions.
- App download size: keep under ~50 MB; ship media on demand, not in the bundle.

Practices: virtualised lists (FlashList / LazyColumn / List); memoise expensive rows; image caching (`expo-image`); Hermes engine; avoid unnecessary re-renders; move heavy work off the UI thread; measure with React Native DevTools / Xcode Instruments / Android Studio profiler.

## Network & data

- Every screen works on slow 3G throttling (loading states, no timeouts under 15 s for normal calls).
- Offline-first for core content where it matters (downloaded audio/video, cached lists).
- Compress API responses; paginate; request only needed fields.

## Monitoring

- Real-user monitoring: Vercel Speed Insights / web-vitals for web, Firebase Performance or Sentry for mobile.
- Track p75 and p95; alert on regressions per release.
