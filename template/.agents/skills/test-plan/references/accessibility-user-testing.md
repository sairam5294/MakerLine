# Usability testing with disabled users (screen readers & more)

Automated tools (axe, Lighthouse) catch only a minority of accessibility problems. Real users of assistive technology find the rest: confusing announcements, focus traps, tiring flows. Budget for it like any usability study.

## When
- Once on the clickable prototype (validate-idea / design-system), once before launch (ship-checklist), then after major UI changes.

## Who (3–5 people per round is enough to find most blockers)
- **Screen-reader users**: in India most use Android + TalkBack; also include one iPhone + VoiceOver user and, for web, NVDA on Windows.
- Low vision (zoom / large text / high contrast), motor (switch access, keyboard only), cognitive / low literacy, older adults — pick those relevant to your audience (e.g. parents, grandparents).
- Prefer people who use the assistive tech every day, not simulations by sighted testers.

## Where to recruit
- Disability-led and accessibility organisations that run testing panels with visually impaired testers, e.g. Vision-Aid (digital accessibility testing) and Enabled.in (screen-reader testing) — check their current services and rates.
- Local blind / disability associations, university disability cells, accessibility communities on LinkedIn/WhatsApp. Ask for referrals from your first participants.

## Pay & respect
- Pay at least your normal usability-participant rate (more for expert testers); pay promptly.
- Don't ask for diagnoses — ask what tech they use and how.
- Make everything accessible: invitation, consent form (plain text/email, not a scanned PDF), meeting link.

## Running the session (remote works well)
1. Video call where they share screen **and system audio** (so you hear the screen reader).
2. They use **their own device and settings** — never ask them to change speech rate or to install anything unusual.
3. 3–4 real tasks from the PRD (e.g. "sign up and join the waitlist", "play a song offline"). Think aloud; don't help unless they're stuck > 2 minutes.
4. Note: where they got lost, what was announced wrongly/not at all, extra swipes, time on task, their own words.
5. End with: "What was the most frustrating part?" and "Would you use this?"

## Reporting
Add findings to `docs/product/reviews/<date>-a11y-users.md` in the quality-review format (MUST = blocked a task). Fix blockers before launch; re-test with at least one participant.

Sources: [Vision-Aid digital accessibility testing](https://visionaid.org/educate/digital-accessibility-testing/) · [Enabled.in screen-reader testing](https://enabled.in/screen-reader-testing/)
