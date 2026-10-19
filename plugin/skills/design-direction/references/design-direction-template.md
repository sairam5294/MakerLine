<!-- Size: Standard ≤ 1,500 words incl. tables; flows as Mermaid, not prose. -->
# Design Direction — {{working name}}

_Draft v{{n}} · {{date}} · Based on PROJECT_BRIEF v{{n}}, EVALUATION v{{n}} · Wireframes: `design/wireframes/index.html`{{ · Figma: link}}_

## 1. Summary
{{3–4 sentences: who it's for, the feeling, the recommended visual direction, and how fast a new user reaches the core action (vs the leaders).}}

## 2. Experience principles
| Principle | This means… | This doesn't mean… |
|---|---|---|
| | | |

## 3. Competitor UX teardown
| Leader | Steps to core action | Borrow | Avoid (from review complaints) | Source |
|---|---|---|---|---|

## 4. Information architecture
- Navigation model: {{tabs / sidebar / single flow}} — because {{reason}}
```mermaid
flowchart TD
  Home --> A[Screen]
```

## 5. Core flows
### 5.1 First run → first value
```mermaid
flowchart LR
  Start --> Step1 --> Aha
```
Steps to the core action: {{n}} (leaders: {{n}})
### 5.2 The core action
### 5.3 Recovery path ({{error / offline / permission denied}})

## 6. Screen inventory
| # | Screen | Purpose | Primary action | Key content | States | MVP? |
|---|---|---|---|---|---|---|
| S-01 | | | | | empty · loading · error · offline · success | MVP |

## 7. Content and voice
- Tone: {{3 words}} — do: … · don't: …
- Terminology: {{concept}} → "{{word}}" (never "{{alternative}}")
| Moment | Copy |
|---|---|
| Onboarding promise | |
| Main empty state | |
| Main error | |
| Success moment | |

## 8. Visual directions
### Option A — {{name}} (recommended)
- Mood: {{3 words}}
- Palette:

  | Role | Colour | On | Contrast |
  |---|---|---|---|

  (one hex per Colour and On cell, ratio as n:1, nothing else in the row — the checker recomputes it)

- Type: {{display}} / {{text}}; base size {{n}}
- Shape and spacing: {{radius, density}}
- Imagery and icons:
- Motion:
- Reference product (for feel, not to copy):
### Option B — {{name}}
### Option C — {{name}} (optional)
**Recommendation and why:**
Platform conventions to follow: {{HIG / Material 3 / web}}

## 9. Accessibility and inclusion plan
- Conformance target: {{WCAG 2.2 AA (kit floor) + what launch markets require, from EVALUATION §11}}
| Need (persona · permanent / temporary / situational) | Design response | Where (S-xx) |
|---|---|---|
- Cognitive: plain language (reading age {{n}}), one task per screen, no time pressure, forgiving inputs
- Languages and scripts: {{launch / later}}
- Locked in now (expensive to retrofit): {{no drag-only, no CAPTCHA, captions, text not in images, status never colour-only}}
Floor: WCAG 2.2 AA — contrast, 44 pt / 48 dp targets, text to 200 %, screen-reader names, focus order, reduced motion.

## 10. Wireframes
- File: `design/wireframes/index.html` — open in a browser; "Prototype" mode clicks through the core flow.
- Screens covered: {{list}} · states shown: {{empty, error…}}
- What a 5-person prototype test should check (→ validate-idea):

## 11. Design decisions for the owner
| Decision | Options | Recommendation |
|---|---|---|

## 12. Open questions (also in CLARITY.md)
-
