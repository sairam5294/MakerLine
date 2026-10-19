# UX Standard

Grounded in Nielsen's 10 heuristics, Apple Human Interface Guidelines, Material Design 3, and inclusive design. Designing for the user's real context beats designing for the happy path.

## 1. Before designing a screen — MUST answer

- Who is using it, where, on what device, with what connectivity? (e.g. a parent on a budget Android phone, 4G, one hand, while cooking)
- What is the ONE job of this screen? What is the primary action? There is exactly one visually primary button per screen.
- How does the user get here and where do they go next?

## 2. Every screen MUST design these states

| State | Requirement |
|---|---|
| Loading | Skeletons for content > 300 ms; never a blank screen; spinners only for short actions |
| Empty | Explain what goes here and give the action to fill it (first-run empty ≠ no-results empty) |
| Error | Plain language, what happened, what to do next, a retry; keep user input |
| Partial / offline | Show cached data with a "last updated" note; queue writes where possible |
| Success | Confirm the result; show what changed; offer the next step |
| Permission denied | Explain why the permission helps and how to enable it later |

## 3. Heuristics checklist (review every flow)

1. **Visibility of status** — feedback within 100 ms of any tap; progress for anything > 1 s.
2. **Match the real world** — user's words, not system words ("Couldn't save" not "Error 500").
3. **Control & freedom** — undo over confirm dialogs; clear back/cancel; no dead ends.
4. **Consistency** — same component = same behaviour; follow platform conventions (iOS back swipe, Android system back).
5. **Error prevention** — constrain inputs (pickers, masks), inline validation after blur, confirm only destructive irreversible actions.
6. **Recognition over recall** — show options, recent items, defaults.
7. **Flexibility** — shortcuts for frequent users without hurting new ones.
8. **Minimalist design** — every element earns its place; progressive disclosure for advanced options.
9. **Recover from errors** — specific messages with a fix.
10. **Help** — contextual help at the point of confusion, not a manual.

## 4. Platform conventions

- **iOS (HIG)**: tab bar for top-level sections (2–5), large titles, SF Symbols, sheets for focused tasks, swipe-back must work, respect safe areas and Dynamic Island.
- **Android (Material 3)**: navigation bar (3–5) or rail on tablets, top app bar, FAB only for the single primary action, predictive back, Material You dynamic colour optional.
- **Web**: responsive breakpoints (≈ 360 / 768 / 1024 / 1440), URLs for every meaningful state (shareable, back button works), hover is an enhancement never a requirement.
- Cross-platform apps: share brand and layout, but respect each platform's navigation and controls.

## 5. Forms

- Single column; label above field; group related fields; mark optional fields rather than required when most are required.
- Use correct keyboard types (`email`, `tel`, `numeric`), `autocomplete`, and OTP autofill.
- Validate inline after the user leaves the field; never clear the form on error.
- Ask only what is needed now; defer the rest (progressive profiling).

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
