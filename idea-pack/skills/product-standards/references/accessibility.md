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

## 5b. Custom widgets, ARIA and single-page apps (IAAP WAS Body of Knowledge, Domain 1)

**MUST**
- Native first; a custom widget follows the matching ARIA Authoring Practices Guide (APG) pattern: role, accessible name, states, and the documented keyboard model. Composite widgets (tabs, menus, grids, listboxes) use one tab stop plus arrow keys (roving `tabindex` or `aria-activedescendant`).
- Never override a native role with ARIA (`<button role="link">`); document every custom component's keyboard and screen-reader behaviour next to the component.
- Accessible name contains the visible label text (WCAG 2.5.3 Label in Name) so speech-input users can say what they see.
- Single-page apps: on route change update `document.title`, move focus to the new view's heading (or main), and announce async results (loading → loaded, errors) with a polite live region.
- Device-independent events: anything on hover or pointer-down also works on focus and keyboard; no action on focus alone.
- If users create content (posts, notices, listings, pages), the editor itself is accessible and helps authors make accessible content — prompts for alt text, real headings, link text (ATAG 2.0).

**User strategies to design and test for:** screen reader (desktop and mobile gestures), screen magnifier and 200–400% zoom, speech input, keyboard / switch, captions and transcripts, reading support for low literacy and cognitive disabilities.

**Accessibility support:** test the combinations your audience uses, at minimum NVDA + Chrome or Firefox and JAWS + Chrome (Windows web), VoiceOver + Safari (macOS, iOS), TalkBack + Chrome (Android). A feature that works in one combination only is not done; when support is missing, use a well-supported pattern rather than a hack.

## 6. Testing checklist (every feature)

1. Automated: axe-core (web: `@axe-core/playwright` or `jest-axe`), eslint-plugin-jsx-a11y, Accessibility Inspector (iOS), Accessibility Scanner (Android). Automation catches roughly a third of issues — manual checks are required.
2. Keyboard-only pass through the full flow.
3. Screen-reader pass: VoiceOver (macOS/iOS) and TalkBack (Android) through the primary task.
4. 200% zoom / largest font size pass.
5. Contrast check of all new colours in light and dark themes.
6. Reduced-motion pass.

**Evaluating a whole product (audits, ship-checklist):** follow WCAG-EM — define scope and conformance target, explore, pick a representative sample (every template, key flows, every state), audit, report. Use tools that implement W3C ACT Rules (axe-core does) and record which success criteria were tested manually.

**Prioritising fixes (WAS Domain 3):** severity = impact on the user (blocker · serious · moderate · minor) × how often the screen or flow is used. A WCAG failure is a MUST; a best practice that isn't a failure is a SHOULD — label which is which. When the same widget fails many criteria, recommend redesigning it with a native or APG pattern instead of patching each failure.

## 7. Law, buyers and public statements

- Which laws apply depends on where you launch and who pays: see `accessibility-law.md` (AODA, ADA, Section 508, European Accessibility Act, UK, India RPwD/GIGW, and others). WCAG 2.2 AA meets or exceeds the WCAG 2.0/2.1 AA levels most laws cite, but some laws ask for more (feedback routes, alternate formats, statements, reports).
- MUST: an accessibility statement (conformance level, known gaps, contact) and a way to report barriers, from the first public release.
- Selling to businesses, schools or government: expect to provide an Accessibility Conformance Report (VPAT template).

## 8. Content for children or low-literacy users (when relevant)

- Pair text with icons and audio; keep sentences short; large targets (≥ 56dp for young children); no reliance on reading to complete core tasks.
