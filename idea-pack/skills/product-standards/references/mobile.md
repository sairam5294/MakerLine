# Mobile Platform Standard (iOS & Android)

What a mobile app must do to feel native, survive the platform's lifecycle and pass store review.

## 1. Cross-platform defaults

- One codebase with Expo (React Native) unless the brief needs deep native features (AR, heavy real-time audio/video processing, widgets-first apps, watch apps) — then native Swift/SwiftUI and Kotlin/Jetpack Compose.
- Support: iOS current and previous major version; Android API 26+ (check your audience's device data — Indian audiences skew to older Android versions).
- Test on at least: one small iPhone, one large iPhone, one low-end Android (2–3 GB RAM), one tablet if tablets are in scope.

## 2. Platform behaviour (MUST)

- Respect safe areas, notches, Dynamic Island, gesture navigation bars.
- iOS: swipe-back works; sheets and haptics follow HIG. Android: system/predictive back works on every screen; edge-to-edge display.
- Handle app lifecycle: backgrounding mid-flow, process death on Android (restore state), interrupted audio (calls, other apps), network changes.
- Deep links / universal links validated and routed safely.
- Permissions: request just-in-time with rationale; app must still work (degraded) if denied.
- Localisation-ready from day one (i18n library, no hard-coded strings); Indic fonts tested for clipping.

## 3. Release & stores

- Use EAS Build/Submit (Expo) or Fastlane; automated versioning; separate dev/preview/prod builds and bundle IDs.
- Over-the-air updates (EAS Update) only for JS/asset fixes; native changes go through store review.
- Staged rollout: 1% → 10% → 50% → 100% on Play; phased release on App Store; watch crash-free rate before each step.
- Store listing: screenshots for required device sizes, privacy labels / Data safety form accurate, age rating correct, support URL and privacy policy URL live.
- Apple: in-app account deletion; Sign in with Apple if you offer other third-party social sign-ins (accept relay emails from both `privaterelay.appleid.com` and `private.icloud.com`); in-app purchase for digital goods (check current regional rules). Build with the iOS 26 SDK / Xcode 26 (required since 28 Apr 2026; iOS 27 SDK from April 2027). Answer the age-rating questionnaire incl. the social-media questions (required since Sep 2026); use the Declared Age Range API where age laws apply (e.g. Brazil, Australia, Singapore, Utah, Louisiana). Apps with user-generated content must filter objectionable content, offer reporting and blocking (Guideline 1.2, updated 16 Oct 2026).
- Google: new apps and updates target Android 16 / API 36 (required since 31 Aug 2026; extension to 1 Nov 2026 on request); register every app in Play Console for Android developer verification; use the Play Age Signals API where age laws apply; Families Policy if children are an audience.
- Store rules last verified 2026-10-20.
- Keep a "force update" mechanism (minimum supported version check) for breaking API changes.

## 4. Media-heavy apps (audio/video)

- Background audio configured properly (iOS audio session, Android foreground service/media session) with lock-screen controls.
- Download for offline with storage management UI.
- Stream with adaptive bitrate (HLS) for video; compressed AAC/Opus for audio.
