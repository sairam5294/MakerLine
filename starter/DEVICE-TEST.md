# Device test (about 15 minutes)

Run this on a real iPhone and a real Android phone after any Expo SDK upgrade, before merging. Simulators miss gestures, TalkBack and VoiceOver behaviour, and real performance. Record the result in the pull request.

## Set up (once)

1. On your Mac, in this folder: `npm ci`, then `npx expo start`.
2. On each phone, install **Expo Go** from the App Store or Play Store, and make sure it supports the SDK in `package.json` (`expo` ~58). If Expo Go is behind, use a development build instead: `npx expo run:ios` or `npx expo run:android` with the phone plugged in.
3. Scan the QR code from the terminal: Camera app on iPhone, Expo Go on Android.

## Checks

Do each check on both phones. Write ✓ or what went wrong.

| # | Check | iPhone | Android |
|---|---|---|---|
| 1 | App opens with no red error screen, and the first screen appears in under 3 seconds | | |
| 2 | The home and sign-in screens open; going back works (swipe on iPhone, back button on Android) | | |
| 3 | Sign-in form: wrong email shows the error message under the field; the screen reader reads it | | |
| 4 | **VoiceOver / TalkBack** on: swipe through the first screen; every button says what it does, and nothing is silent or "button" only | | |
| 5 | **Largest text size** (iPhone: Settings → Accessibility → Display & Text Size → Larger Text; Android: Font size to max): nothing is cut off or overlaps | | |
| 6 | **Dark mode** on: text is readable everywhere; switching back works without restarting | | |
| 7 | **Reduce Motion** (iPhone) / **Remove animations** (Android): no sliding or bouncing animations | | |
| 8 | Language: switch the phone to Hindi or Telugu; the app's text changes; switch back to English | | |
| 9 | Airplane mode: the app doesn't crash, and once your screens use `ScreenState`, its offline state shows | | |
| 10 | Rotate the phone (if supported) and lock and unlock it: the app keeps its place | | |

## If something fails

Open an issue with the phone model, OS version, the check number and what happened (a screenshot helps). Don't merge the SDK upgrade until it's fixed or you've decided it can wait.
