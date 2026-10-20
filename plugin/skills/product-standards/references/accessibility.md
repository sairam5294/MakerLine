# Accessibility Standard

Target: **WCAG 2.2 Level AA** on web, plus platform guidance for iOS (VoiceOver, Dynamic Type) and Android (TalkBack, font scaling). Accessibility is a MUST, not a later phase. New to a term (APG, live region, WCAG-EM)? See `glossary.md`.

WCAG 2.2 is the latest W3C Recommendation and, since Oct 2025, also the ISO standard **ISO/IEC 40500:2025** (it replaced ISO/IEC 40500:2012, which was WCAG 2.0). WCAG 3.0 is still a W3C Working Draft (10 Sep 2026) — don't target or claim it; watch only. *(Last verified 2026-10-20: w3.org/WAI/news/2025-10-21/wcag22-iso.)*

## 1. Perceivable

**MUST**
- Text contrast ≥ 4.5:1; large text (≥ 18.66px bold / 24px regular) ≥ 3:1.
- Non-text contrast (input borders, icons that convey meaning, focus indicators, chart lines) ≥ 3:1 against adjacent colours, in light and dark themes (1.4.11).
- Never use colour alone to convey meaning (errors need an icon or text; charts need labels or patterns).
- Instructions don't rely on shape, size, position or sound alone — not "tap the round button on the right" (1.3.3 Sensory Characteristics).
- All meaningful images have alt text; decorative images are hidden from assistive tech (`alt=""`, `accessibilityElementsHidden`, `importantForAccessibility="no"`).
- Pre-recorded video has captions; audio-only content has a transcript.
- **Live** video with speech (webinars, streams) has live captions (1.2.4). Pre-recorded video has audio description when the visuals carry information the soundtrack doesn't (1.2.5) — or a narration that already describes it.
- Media players: every control (play, pause, volume, captions on/off, audio description on/off, full screen) is keyboard and screen-reader operable, and caption / audio-description controls sit at the same level as play and volume (EN 301 549 §7.1–7.3). Captions stay in sync and are kept when the video is converted or streamed.
- Content reflows at 320 CSS px width (= 1280 px at 400% zoom) without horizontal scrolling (except maps, tables, diagrams) (1.4.10).
- Text can scale to 200% (web) and to the largest Dynamic Type / font scale on mobile without clipping or overlap.
- Text spacing: nothing is cut off or overlaps when users set line height 1.5×, paragraph spacing 2×, letter spacing 0.12× and word spacing 0.16× the font size (1.4.12) — use `min-height`, not fixed heights, on text containers.
- Content on hover or focus (tooltips, popovers): can be dismissed with Esc without moving the pointer, the pointer can move onto it without it vanishing, and it stays until the user moves away or dismisses it (1.4.13).
- Don't lock orientation unless essential.
- No content flashes more than 3 times per second (2.3.1, Level A) — it can trigger seizures.

**SHOULD**
- Support dark mode with contrast re-checked in both themes.
- Respect `prefers-reduced-motion` / Reduce Motion / Remove animations.

## 2. Operable

**MUST**
- Everything works with keyboard alone (web) and with switch / screen-reader gestures (mobile). No keyboard traps.
- Single-character keyboard shortcuts (e.g. "s" to send) can be turned off or remapped, or only work when that control has focus (2.1.4) — speech-input users trigger them by accident.
- Visible focus indicator on every focusable element; focus is never hidden behind sticky headers, cookie banners or chat bubbles (2.4.11 Focus Not Obscured).
- Logical focus order that matches the visual order; after opening a modal, focus moves into it and returns to the trigger on close.
- Target size ≥ 24×24 CSS px (2.5.8); product standard is 44×44 pt iOS / 48×48 dp Android / 44px web.
- Multi-finger or path gestures (pinch, two-finger swipe, drawing a shape) have a single-pointer alternative such as + / − buttons (2.5.1 Pointer Gestures).
- Actions fire on pointer **up**, not down, so a slip can be cancelled by moving away (2.5.2 Pointer Cancellation).
- Any drag action has a single-pointer alternative (2.5.7), e.g. reorder via up/down buttons.
- Shake, tilt or other motion triggers have an on-screen alternative and can be turned off (2.5.4 Motion Actuation).
- Anything that moves, blinks, scrolls or auto-updates for more than 5 seconds (carousels, tickers, animated banners) can be paused, stopped or hidden (2.2.2).
- Any time limit can be turned off, adjusted or extended — warn before a session expires and let the user extend it with one action (2.2.1).
- Provide a "skip to main content" link on web pages with repeated navigation.

## 3. Understandable

**MUST**
- Set page language (`<html lang>`), and mark language changes inside content (important for Telugu/Hindi/English mixes).
- Every form field has a visible label (placeholder is not a label) and input purpose (`autocomplete`) where applicable.
- **Required fields are marked in text**, e.g. "Email (required)" — not by a colour or a lone asterisk. When most fields are required, also label the few optional ones "(optional)". (Same rule in `ux.md` §5 and the forms-validation rule.)
- Errors identify the field, describe the problem in text and suggest a fix; errors are announced to screen readers. On submit, show an error summary at the top and move focus to it or the first error.
- Changing a field or choice never causes a surprise change of context (submitting, opening a new page, moving focus) unless the user was told first (3.2.2 On Input).
- Legal, financial or data-changing submissions (payments, contracts, deleting data, test answers) can be reversed, are checked for errors, or have a review-and-confirm step (3.3.4 Error Prevention).
- Don't ask users to re-enter information already provided in the same flow (3.3.7 Redundant Entry).
- Login must not rely on a cognitive test (memorising, puzzles) without an alternative — allow paste into password fields, password managers, passkeys, magic links (3.3.8 Accessible Authentication).
- Navigation repeated across screens stays in the same order (3.2.3); help mechanisms (contact, FAQ, chat) appear in the same place across screens (3.2.6 Consistent Help).

## 4. Robust

**MUST**
- Use native / semantic elements first (`<button>`, `<a>`, `<nav>`, `<main>`, headings in order; `Button`, `Toggle` on mobile). ARIA only when no native element exists — "no ARIA is better than bad ARIA".
- Every custom control exposes name, role, state and value (e.g. `aria-expanded`, `accessibilityState={{ selected }}`).
- Status messages (toasts, "saved", cart counts) use live regions / `accessibilityLiveRegion` / `AccessibilityInfo.announceForAccessibility`.

## 5. Platform specifics

| Platform | Requirements |
|---|---|
| **iOS** | every tappable view has `accessibilityLabel` and appropriate traits; use Dynamic Type text styles; group related elements; test with VoiceOver rotor, Voice Control and Full Keyboard Access (`mobile.md` §5) |
| **Android** | `contentDescription` on icons; `minTouchTargetSize`; test with TalkBack, Voice Access and at 200% font scale; use `semantics { heading() }` in Compose |
| **React Native / Expo** | `accessible`, `accessibilityRole`, `accessibilityLabel`, `accessibilityHint`, `accessibilityState`; don't disable `allowFontScaling` |

## 5b. Custom widgets, ARIA and single-page apps (IAAP WAS Body of Knowledge, Domain 1)

**MUST**
- Native first; a custom widget follows the matching ARIA Authoring Practices Guide (APG) pattern: role, accessible name, states, and the documented keyboard model. Composite widgets (tabs, menus, grids, listboxes) use one tab stop plus arrow keys (roving `tabindex` or `aria-activedescendant`).
- Never override a native role with ARIA (`<button role="link">`); document every custom component's keyboard and screen-reader behaviour next to the component.
- Accessible name contains the visible label text (2.5.3 Label in Name) so speech-input users can say what they see.
- Single-page apps: on route change update `document.title`, move focus to the new view's heading (or main), and announce async results (loading → loaded, errors) with a polite live region.
- Device-independent events: anything on hover or pointer-down also works on focus and keyboard; no action on focus alone.
- If users create content (posts, notices, listings, pages), the editor itself is accessible and helps authors make accessible content — prompts for alt text, real headings, link text (ATAG 2.0).

**User strategies to design and test for:** screen reader (desktop and mobile gestures), screen magnifier and 200–400% zoom, speech input, keyboard / switch, captions and transcripts, reading support for low literacy and cognitive disabilities.

**Screen-reader matrix (the one list the kit uses):** VoiceOver + Safari (macOS and iOS), TalkBack + Chrome (Android), NVDA + Chrome or Firefox (Windows web) — plus JAWS + Chrome when buyers (government, enterprise, education) require it. Test the combinations your audience uses. A feature that works in one combination only is not done; when support is missing, use a well-supported pattern rather than a hack.

## 5c. Beyond WCAG (procurement standards)

WCAG covers web content. Buyers using Section 508 or EN 301 549 also check:

| Standard · clause | What it adds | When it matters |
|---|---|---|
| Section 508 Ch. 5 (Software) | Desktop/mobile apps work with platform assistive tech and **honour user settings** (contrast, font size, cursor) (502–503); authoring tools produce accessible output (504) | Selling software to US federal agencies |
| Section 508 Ch. 6 (Support docs and services) | Help docs are accessible and describe accessibility features; help desks and training support people with disabilities | Same |
| EN 301 549 §5.3 Biometrics | Biometric login (face, fingerprint) is never the only way in | Any biometric or liveness check |
| EN 301 549 §6 Two-way voice | Voice/video calls support real-time text (RTT, §6.2) and good audio; video calls carry sign-language-quality video | Calling, telehealth, support lines |
| EN 301 549 §11.7 User preferences | Software follows platform settings for colour, contrast, font size and focus cursor | EU public sector, EAA products |
| EN 301 549 §12 Documentation and support | Product docs in accessible formats; support services can communicate with users' assistive needs | Same |

*(Sources: section508.gov; 36 CFR 1194 Appendix C; ETSI EN 301 549 V3.2.1.)*

## 6. Testing checklist (every feature)

1. Automated: axe-core (web: `@axe-core/playwright` or `jest-axe`), eslint-plugin-jsx-a11y, Accessibility Inspector (iOS), Accessibility Scanner (Android). Automation catches roughly a third of issues — manual checks are required.
2. Keyboard-only pass through the full flow.
3. Screen-reader pass through the primary task with the §5b matrix: VoiceOver (macOS/iOS), TalkBack (Android), NVDA (Windows web), + JAWS where buyers require.
4. Zoom and text: 200% zoom / largest font size; reflow at 320 CSS px (400% zoom) with no horizontal scroll; text-spacing bookmarklet (1.4.12) shows nothing clipped.
5. Speech input: Voice Control (iOS/macOS) or Voice Access (Android) — say each visible label and check the control activates (label in name).
6. Forced colours: Windows High Contrast / `forced-colors: active` — borders, focus rings and icons stay visible.
7. Contrast check of all new colours (text 4.5:1, non-text 3:1) in light and dark themes.
8. Reduced-motion pass.

**Evaluating a whole product (audits, ship-checklist):** follow WCAG-EM — define scope and conformance target, explore, pick a representative sample (every template, key flows, every state), audit, report. Use tools that implement W3C ACT Rules (axe-core does) and record which success criteria were tested manually.

**Prioritising fixes (WAS Domain 3):** severity = impact on the user × how often the screen or flow is used. A WCAG failure is a MUST; a best practice that isn't a failure is a SHOULD — label which is which. When the same widget fails many criteria, recommend redesigning it with a native or APG pattern instead of patching each failure.

### Severity mapping (one table for every reviewer)

Agents and skills rate in their own words; this is how they line up (same mapping as `quality-review` step 3).

| Kit verdict | Accessibility impact | Bug priority (`testing.md` §4) | Security / generic | Means |
|---|---|---|---|---|
| **MUST** | blocker · serious | P0 · P1 | Critical · High | Fix before merge/release |
| **SHOULD** | moderate | P2 | Medium | Plan it; fix soon |
| **Suggestion** | minor | P3 | Low | Backlog |

Any WCAG 2.2 AA failure is at least **MUST**, whatever its impact label. A blocker (someone cannot finish the task at all) is P0.

## 7. Law, buyers and public statements

- Which laws apply depends on where you launch and who pays: see `accessibility-law.md` (AODA, ADA, Section 508, European Accessibility Act, UK, India RPwD/GIGW, and others). WCAG 2.2 AA meets or exceeds the WCAG 2.0/2.1 AA levels most laws cite, but some laws ask for more (feedback routes, alternate formats, statements, reports, staff training).
- MUST: an accessibility statement (conformance level, known gaps, contact) and a way to report barriers, from the first public release.
- Selling to businesses, schools or government: expect to provide an Accessibility Conformance Report (VPAT template) — how-to in `../../ship-checklist/references/acr-vpat.md`.

## 8. Content for children or low-literacy users (when relevant)

- Pair text with icons and audio; keep sentences short; large targets (≥ 56dp for young children); no reliance on reading to complete core tasks.
