# PRD — {{working name}}

_{{Draft v0.x (idea stage) · Full v1.x (after approval)}} · {{date}} · Owner: {{name}} · Status: Draft / In review / Approved_
_Inputs: PROJECT_BRIEF v{{n}} · EVALUATION v{{n}} · COMPETITORS · DESIGN_DIRECTION v{{n}} · CLARITY · (full only) TECH_STACK · DESIGN_SYSTEM_

Sections marked **(full)** are filled after approval; in a draft write "after approval" under the heading.

## 1. Summary
{{4–6 sentences: what it is, for whom, the problem, why now, how it wins (the differentiator that passed the test), what version 1 is.}}

## 2. Problem
- Problem statement: {{audience}} struggle to {{job}} because {{cause}}, which leads to {{consequence}}.
- Evidence (sourced, from EVALUATION / VALIDATION):
- Current alternatives and why they fall short (from COMPETITORS):

## 3. Goals, non-goals and success metrics
| Goal | Primary metric | Target (6 months) | Input metrics | How measured |
|---|---|---|---|---|
- Non-goals (explicitly not doing in v1):
- Guardrail metrics (must not get worse): {{e.g. crash-free sessions, support tickets, accessibility score}}

## 4. Users
### Personas
| Persona | Context | Goal | Frustration today | Accessibility needs |
|---|---|---|---|---|
### Jobs to be done
- When {{situation}}, I want to {{motivation}}, so I can {{outcome}}.

## 5. Positioning and differentiation
- Positioning statement:
- Differentiators this release must make visible (and where in the product):
- What we deliberately don't compete on:

## 6. Scope
| Capability | MoSCoW | Release | Why |
|---|---|---|---|
- MVP definition: the smallest product that tests {{riskiest assumption}} and delivers {{core value}}.
- Later releases (themes only):

## 7. User journeys
Link the flows in DESIGN_DIRECTION §5. For each core journey: happy path, then edge paths (error, empty, offline, permission denied, slow network).

## 8. Requirements and user stories
### Epic E1 — {{name}}
**US-01** · As a {{persona}}, I want {{action}} so that {{outcome}} · {{Must}}
- Given {{context}}, when {{action}}, then {{result}}
- Given {{error/empty/offline/permission-denied}}, when …, then …
- Design: {{screen S-xx in DESIGN_DIRECTION / wireframes}}
- Personal data used: {{what and why, or "none"}}

## 9. Experience and design
- Experience principles (from DESIGN_DIRECTION):
- Screen inventory with states: link DESIGN_DIRECTION §6 and `design/wireframes/index.html`
- Visual direction chosen:
- Content and voice: key microcopy, terminology
- Accessibility requirements: WCAG 2.2 AA + the persona-specific needs + what the launch markets require (EVALUATION §11)
  - Accessibility statement (conformance level, known gaps, how to report a barrier) and a feedback route answered within {{n}} days
  - Alternate formats / communication support on request (required by e.g. AODA)
  - Accessibility Conformance Report (VPAT) if businesses, schools or government will buy — by {{milestone}}
  - Assistive-tech users in the prototype test and the beta
  - Example criterion: Given a screen-reader user, when they book a slot, then every control is announced with name, role and state and the confirmation is announced
- Localisation: languages and scripts at launch / later

## 10. Data and permissions **(full)**
| Entity | Key fields | Who can read | Who can write | Retention |
|---|---|---|---|---|
- Row-level security rules, personal data inventory, deletion and export

## 11. Analytics **(full in detail; draft lists the funnel)**
| Event | When | Properties (no personal data) | Funnel step |
|---|---|---|---|

## 12. Non-functional requirements
- Performance budgets · Reliability · Security (OWASP) · Privacy (DPDP / GDPR as relevant) · Accessibility · Offline behaviour · Supported devices and OS versions
- AI features (if any): run ai-feature; link AI_FEATURE_*.md (evals, cost caps, labelling, user control)

## 13. Technology **(full)**
- Stack (from TECH_STACK.md ADR), key services, third-party dependencies and their risks

## 14. Dependencies and risks
| Risk / dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
Carry the top risks from EVALUATION; add delivery risks (store review, payment approval, content rights).

## 15. Release plan
| Milestone | Scope | Exit criteria | Target date |
|---|---|---|---|
| Prototype test | wireframes | ≥ 4/5 complete the core task | |
| Private beta | MVP Musts | | |
| Public launch | | | |
- Launch channels for the first 100 users (from EVALUATION §5):
- Kill or pivot criteria after launch:

## 16. Open questions and decisions
- Open (blocking): link CLARITY.md ids
| Date | Decision | Options considered | Why |
|---|---|---|---|

## Appendix
- Glossary · Research links · Competitor screenshots or notes · Change log

| Version | Date | Change |
|---|---|---|
