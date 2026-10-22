# Device test (about 15 minutes)

Run this on a real iPhone and a real Android phone after any Expo SDK upgrade, before merging. Simulators miss gestures, TalkBack and VoiceOver behaviour, and real performance. Record the result in the pull request.

## Set up (once)

1. On your Mac, in this folder: `npm ci`, then `npx expo start`.
2. On each phone, install **Expo Go** from the App Store or Play Store. It must support the SDK in `package.json` (`expo` ~58). If it says **"Project is incompatible with this version of Expo Go"**, the store hasn't got the new Expo Go yet (it arrives a few weeks after an SDK release, even when the app says it's up to date). Then use a **development build** instead, which installs this app itself on the phone:
   - **iPhone** (needs Xcode from the Mac App Store, and a free Apple ID): plug the phone in with a cable, unlock it, tap **Trust**, turn on **Developer Mode** (Settings → Privacy & Security → Developer Mode, restart), then run `npx expo run:ios --device` and pick your iPhone. The first build takes 10–15 minutes. If iOS says "Untrusted Developer", go to Settings → General → VPN & Device Management → your Apple ID → **Trust**.
   - **Android** (needs Android Studio): on the phone, Settings → About phone → tap **Build number** 7 times, then Settings → Developer options → turn on **USB debugging**. Plug it in, allow the prompt, then run `npx expo run:android --device`.
3. With Expo Go: scan the QR code from the terminal (Camera app on iPhone, Expo Go on Android). With a development build: the app opens on the phone by itself.

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

## No phone ready? Simulator route

The iOS Simulator (press `i` in `npx expo start`) installs the right Expo Go for you and covers most checks. The "Setup needed" box on the home screen is expected without Supabase keys.

| # | In the Simulator |
|---|---|
| 1–3 | As on a phone (click instead of tap) |
| 4 | VoiceOver isn't in the Simulator. Use Xcode → Open Developer Tool → **Accessibility Inspector**, pick the Simulator, click the crosshair and hover each control: it must show a Label and the Button role. Then press `w` for the web version and test it in Safari with Mac **VoiceOver** (Cmd+F5) |
| 5 | Simulator **Settings** app → Accessibility → Display & Text Size → Larger Text → largest |
| 6 | Shift+Cmd+A switches dark and light |
| 7 | Settings app → Accessibility → Motion → Reduce Motion |
| 8 | The app's own Language buttons, then Settings app → General → Language & Region |
| 9 | Turn off your Mac's Wi-Fi for a moment |
| 10 | Cmd+→ rotates, Cmd+L locks |

Android: Android Studio's emulator (press `a`) works the same way, and TalkBack can be turned on inside it. Note in the pull request that the run was on a simulator; a real-phone pass is still worth doing once the store Expo Go supports the SDK.

## If something fails

Open an issue with the phone model, OS version, the check number and what happened (a screenshot helps). Don't merge the SDK upgrade until it's fixed or you've decided it can wait.
