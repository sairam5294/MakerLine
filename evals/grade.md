# Grading checklist (1 point each)

Universal (every case):
1. Verdict + confidence at the top; verdict within the case's expected range
2. Critique section comes before strengths; ≥ 3 serious risks with mitigation/test
3. Every score has a one-line reason; weighted total shows the calculation
4. TAM → SAM → SOM with math and sources (or explicit assumptions)
5. Named, real competitors/substitutes incl. a free/"do nothing" alternative, with sources
6. Personas (2–3) that match the brief's audience
7. Cheapest validation test with a numeric kill criterion
8. Concrete improvement suggestions (incl. what to cut from the MVP)
9. Sources section with working URLs; evidence vs estimate vs opinion labelled
10. Tone: candid, no hype, no invented precision

Case-specific: each item in `cases/<case>/expected.md` = 1 point.

Score = points / total. Note any hallucinated facts (−2 each).

## Idea Pack checklist (v0.7+, 1 point each) — when the full pack is run

Evaluation and competitors
11. "Strongest version of this idea" section comes before the reality check and is specific (audience, wedge, form)
12. Every score ≤ 6 has a "Raise it by…" change with evidence to look for, and a target weighted score is shown
13. Strengthening plan has a "Path to Go" table; tone is constructive — no fatal flaw or risk without a fix or test
14. COMPETITORS.md covers all four rings (direct, indirect, substitute, doing nothing) with real, linked names and dated prices/ratings
15. Leader profiles quote real review complaints with sources
16. Job matrix and positioning map with stated axes; the idea does not win every row
17. Differentiator test applied (5 questions) with keep / reframe / drop per differentiator; positioning statement and wedge stated
18. Provisional tools & technology table with monthly cost at 1,000 users
19. CLARITY.md exists: open questions typed (decision / fact / assumption), each naming the phase it blocks; no defaults invented for facts

Design direction
20. 3–5 experience principles with "means / doesn't mean"
21. Competitor UX teardown with steps-to-core-action compared
22. IA + 2–4 Mermaid flows incl. one recovery path
23. Screen inventory with states (empty, loading, error, offline, success)
24. 2–3 visual directions with contrast ratios ≥ 4.5:1 for text pairs, and a recommendation
25. `design/wireframes/index.html` renders, uses real content (no lorem / no leftover {{placeholders}}), shows ≥ 1 empty and ≥ 1 error state, and the core flow clicks through in Prototype mode

PRD (draft) and one-pager
26. PRD draft: metrics table, personas, MoSCoW scope, ≥ 6 user stories with Given/When/Then incl. error/empty, screens referenced (S-xx), "(full)" sections deferred
27. Differentiator visible in named stories/screens; scope fits the owner's hours or cuts are proposed
28. ONE_PAGER.md fits one page and matches the evaluation; README index links every document

Pass bar for the Idea Pack: ≥ 80% of items 11–28, plus the universal 1–10 and the case's expected list.

## Accessibility, inclusion and compliance (v0.8+, 1 point each)
29. EVALUATION §11 names who could be excluded (permanent / temporary / situational) with a source or labelled estimate
30. Obligations-by-launch-market table uses `accessibility-law.md`, says *why* each law applies or not, flags uncertain + high-stakes items for a lawyer and CLARITY; includes the privacy row
31. COMPETITORS records leaders' accessibility signals (statement, ACR/VPAT, store label, review mentions)
32. DESIGN_DIRECTION §9 states the conformance target, cognitive and language needs, and locked-in "cheap now" choices; wireframes carry accessibility notes
33. PRD includes accessibility statement + feedback route, alternate formats when required, ACR when selling to organisations, assistive-tech users in tests
34. `check_idea_pack.py --mode <mode>` passes with 0 FAIL
35. Global baseline applied whatever the launch market (inclusion.md): no forced gender/name splits, languages and low-end devices considered, no decision based on protected characteristics

## Token efficiency (record every blind run)
| Date | Case | Mode | Tokens | Tool calls | Minutes | Score | Notes |
|---|---|---|---|---|---|---|---|
| 2026-10-16 | community-amenities | Standard (v0.7.0) | ~224k | 72 | 18 | 6/6 must-catch | baseline before budgets |
| 2026-10-16 | new-idea-pitch | discovery (v0.7.0) | ~115k | 14 | 3 | ≈ 10/11 | |
