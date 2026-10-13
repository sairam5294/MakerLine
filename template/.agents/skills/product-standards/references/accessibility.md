# Accessibility Standard

Target: **WCAG 2.2 Level AA** on web, plus platform guidance for iOS (VoiceOver, Dynamic Type) and Android (TalkBack, font scaling). Accessibility is a MUST, not a later phase.

## 1. Perceivable

**MUST**
- Text contrast ≥ 4.5:1; large text (≥ 18.66px bold / 24px regular) ≥ 3:1.
- Non-text contrast (input borders, icons that convey meaning, focus indicators, chart lines) ≥ 3:1 against adjacent colours.
- Never use colour alone to convey meaning (errors need an icon or text; charts need labels or patterns).
- All meaningful images have alt text; decorative images are hidden from assistive tech (`alt=""`, `accessibilityElementsHidden`, `importantForAccessibility="no"`).
- Video has captions; audio-only content has a transcript.
- Content reflows at 320 CSS px width without horizontal scrolling (except maps, tables, diagrams).
- Text can scale to 200% (web) and to the largest Dynamic Type / font scale on mobile without clipping or overlap.
- Don't lock orientation unless essential.

**SHOULD**
- Support dark mode with contrast re-checked in both themes.
- Respect `prefers-reduced-motion` / Reduce Motion / Remove animations; no flashing more than 3 times per second.

## 2. Operable

**MUST**
- Everything works with keyboard alone (web) and with switch / screen-reader gestures (mobile). No keyboard traps.
- Visible focus indicator on every focusable element; focus is never hidden behind sticky headers, cookie banners or chat bubbles (WCAG 2.4.11 Focus Not Obscured).
- Logical focus order that matches the visual order; after opening a modal, focus moves into it and returns to the trigger on close.
- Target size ≥ 24×24 CSS px (WCAG 2.5.8); product standard is 44×44 pt iOS / 48×48 dp Android / 44px web.
- Any drag action has a single-pointer alternative (WCAG 2.5.7), e.g. reorder via up/down buttons.
- Any time limit can be turned off, adjusted or extended.
- Provide a "skip to main content" link on web pages with repeated navigation.

## 3. Understandable

**MUST**
- Set page language (`<html lang>`), and mark language changes inside content (important for Telugu/Hindi/English mixes).
- Every form field has a visible label (placeholder is not a label), clear required markers, and input purpose (`autocomplete`) where applicable.
- Errors identify the field, describe the problem in text and suggest a fix; errors are announced to screen readers.
- Don't ask users to re-enter information already provided in the same flow (WCAG 3.3.7 Redundant Entry).
- Login must not rely on a cognitive test (memorising, puzzles) without an alternative — allow paste into password fields, password managers, passkeys, magic links (WCAG 3.3.8 Accessible Authentication).
- Help mechanisms (contact, FAQ) appear in the same place across screens (WCAG 3.2.6 Consistent Help).

## 4. Robust

**MUST**
- Use native / semantic elements first (`<button>`, `<a>`, `<nav>`, `<main>`, headings in order; `Button`, `Toggle` on mobile). ARIA only when no native element exists — "no ARIA is better than bad ARIA".
- Every custom control exposes name, role, state and value (e.g. `aria-expanded`, `accessibilityState={{ selected }}`).
- Status messages (toasts, "saved", cart counts) use live regions / `accessibilityLiveRegion` / `AccessibilityInfo.announceForAccessibility`.

## 5. Platform specifics

**iOS**: every tappable view has `accessibilityLabel` and appropriate traits; use Dynamic Type text styles; group related elements; test with VoiceOver rotor.
**Android**: `contentDescription` on icons; `minTouchTargetSize`; test with TalkBack and at 200% font scale; use `semantics { heading() }` in Compose.
**React Native / Expo**: `accessible`, `accessibilityRole`, `accessibilityLabel`, `accessibilityHint`, `accessibilityState`; don't disable `allowFontScaling`.

## 6. Testing checklist (every feature)

1. Automated: axe-core (web: `@axe-core/playwright` or `jest-axe`), eslint-plugin-jsx-a11y, Accessibility Inspector (iOS), Accessibility Scanner (Android). Automation catches roughly a third of issues — manual checks are required.
2. Keyboard-only pass through the full flow.
3. Screen-reader pass: VoiceOver (macOS/iOS) and TalkBack (Android) through the primary task.
4. 200% zoom / largest font size pass.
5. Contrast check of all new colours in light and dark themes.
6. Reduced-motion pass.

## 7. Content for children or low-literacy users (when relevant)

- Pair text with icons and audio; keep sentences short; large targets (≥ 56dp for young children); no reliance on reading to complete core tasks.
