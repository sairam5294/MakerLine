# UX Standard

Grounded in Nielsen's 10 heuristics, Apple Human Interface Guidelines, Material Design 3, and inclusive design. Designing for the user's real context beats designing for the happy path.

## 1. Before designing a screen — MUST answer

- Who is using it, where, on what device, with what connectivity? (e.g. a parent on a budget Android phone, 4G, one hand, while cooking)
- What is the ONE job of this screen? What is the primary action? There is exactly one visually primary button per screen.
- How does the user get here and where do they go next?

## 2. Every screen MUST design these states

The kit's one list: **loading, empty, error, offline, success, permission denied, partial** (same in AGENTS.md, `build-feature` and the components rule).

| State | Requirement |
|---|---|
| Loading | Skeletons for content > 300 ms; never a blank screen; spinners only for short actions |
| Empty | Explain what goes here and give the action to fill it (first-run empty ≠ no-results empty) |
| Error | Plain language, what happened, what to do next, a retry; keep user input |
| Offline | Show cached data with a "last updated" note; queue writes where possible; say what will sync later |
| Success | Confirm the result; show what changed; offer the next step |
| Permission denied | OS permission refused or the user's role can't see this: explain why it helps / who to ask, and how to enable it later |
| Partial | Some data loaded and some failed (one widget down, a few rows missing): show what you have, mark what's missing, retry just that part |

## 3. Heuristics checklist (review every flow)

1. **Visibility of status** — feedback within 100 ms of any tap; progress for anything > 1 s.
2. **Match the real world** — user's words, not system words ("Couldn't save" not "Error 500").
3. **Control & freedom** — undo over confirm dialogs; clear back/cancel; no dead ends.
4. **Consistency** — same component = same behaviour; follow platform conventions (iOS back swipe, Android system back). Repeated navigation keeps the same order on every screen, and help (contact, FAQ, chat) sits in the same place (WCAG 3.2.3, 3.2.6).
5. **Error prevention** — constrain inputs (pickers, masks), inline validation after blur, confirm only destructive irreversible actions.
6. **Recognition over recall** — show options, recent items, defaults.
7. **Flexibility** — shortcuts for frequent users without hurting new ones.
8. **Minimalist design** — every element earns its place; progressive disclosure for advanced options.
9. **Recover from errors** — specific messages with a fix.
10. **Help** — contextual help at the point of confusion, not a manual.

## 4. Platform conventions

| Platform | Conventions |
|---|---|
| **iOS (HIG)** | tab bar for top-level sections (2–5), large titles, SF Symbols, sheets for focused tasks, swipe-back must work, respect safe areas and Dynamic Island |
| **Android (Material 3)** | navigation bar (3–5) or rail on tablets, top app bar, FAB only for the single primary action, predictive back, Material You dynamic colour optional |
| **Web** | responsive breakpoints (≈ 360 / 768 / 1024 / 1440), URLs for every meaningful state (shareable, back button works), hover is an enhancement never a requirement |
| **Cross-platform apps** | share brand and layout, but respect each platform's navigation and controls |

## 5. Forms

- Single column; label above field; group related fields.
- Mark required fields in text, e.g. "Email (required)" — not colour or a lone asterisk. When most fields are required, also label the optional ones "(optional)". (Same rule in `accessibility.md` §3 and the forms-validation rule.)
- Use correct keyboard types (`email`, `tel`, `numeric`), `autocomplete`, and OTP autofill.
- Validate inline after the user leaves the field; never clear the form on error.
- On submit with errors: show an error summary at the top listing each problem as a link to its field, and move focus to the summary (or the first error field) so keyboard and screen-reader users land on it.
- Ask only what is needed now; defer the rest (progressive profiling).

## 5b. Feedback messages and time limits

- **Toasts / snackbars:** visible at least 5 s (longer for long text), pause on hover or focus, announced via a polite live region, never the only place an error or action appears. Errors and anything with an action (Undo, Retry) stay until dismissed — put errors inline, not only in a toast.
- **Session timeout:** warn before it ends (e.g. 2 minutes before) in an accessible dialog that takes focus, with one action to extend; keep the user's input if it does expire (WCAG 2.2.1).

## 6. Onboarding & first run

- Time-to-value under 60 seconds: let users try before sign-up when possible.
- Ask for permissions in context, just before the feature needs them, with a pre-prompt explaining the benefit.
- No more than 3 intro slides; make them skippable.

## 7. Content & microcopy

- Sentence case; verbs on buttons ("Save changes", not "OK"); consistent terms.
- Write for a reading age of ~12; avoid jargon; localise dates, numbers and currency (₹, lakh/crore if Indian audience).
- Plan for text expansion in translation (+30–40%) and for Indic scripts' taller line heights.

## 8. Motion

- Motion explains change (where something came from/went); 150–300 ms for UI transitions; respect reduced-motion.

## 9. Measuring UX

- Define one task-success metric per core flow (e.g. "% of new users who complete first lesson in session 1").
- Run a 5-user usability test on the prototype before building, and again before launch.
