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
- Apple: in-app account deletion; Sign in with Apple if you offer other third-party social sign-ins; in-app purchase for digital goods (check current regional rules).
- Google: target the latest required API level; Families Policy if children are an audience.
- Keep a "force update" mechanism (minimum supported version check) for breaking API changes.

## 4. Media-heavy apps (audio/video)

- Background audio configured properly (iOS audio session, Android foreground service/media session) with lock-screen controls.
- Download for offline with storage management UI.
- Stream with adaptive bitrate (HLS) for video; compressed AAC/Opus for audio.
