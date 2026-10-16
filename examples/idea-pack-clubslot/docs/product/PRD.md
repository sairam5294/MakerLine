# PRD — ClubSlot

_Draft v0.1 (idea stage) · 2026-10-16 · Owner: ClubSlot owner (senior UX designer) · Status: Draft_
_Inputs: PROJECT_BRIEF v1 · EVALUATION v1 · COMPETITORS v1 · DESIGN_DIRECTION v0.1 · CLARITY (2026-10-16)_

Sections marked **(full)** are filled after approval; in a draft write "after approval" under the heading.

> Scope follows the **pivot** recommended in EVALUATION (fair booking for contested amenities, web-first, no payments in v1). These are defaults taken while the owner was unavailable — see CLARITY Q-03, Q-04, Q-07, Q-10. If the owner keeps the original all-in-one brief, this PRD must be re-scoped.

## 1. Summary
ClubSlot is a web app, opened from a WhatsApp link, that lets residents of large gated communities book shared amenities — courts, pool lanes, party hall — and gives every flat a fair shot at peak slots. Today bookings run on WhatsApp "first message wins" and a paper register at the security desk, causing double bookings and weekly disputes (owner's 900-flat community). All-in-one society apps (MyGate, NoBrokerHood, ADDA) include booking modules, but bundle it with gates, ads and accounting. ClubSlot wins on one job: **fair booking** — a weekly ballot for committee-marked peak slots, automatic release of no-shows, and a public rules log — with no ads and no phone numbers shown. Version 1 is a resident booking app plus a committee rules screen, piloted in the owner's own community.

## 2. Problem
- Problem statement: residents of large gated communities struggle to get fair access to contested amenities because bookings run on WhatsApp messages and a paper register, which leads to double bookings, the same few people getting peak slots, no-shows blocking others, and committee volunteers refereeing disputes.
- Evidence (sourced, from EVALUATION / VALIDATION): owner observes weekly disputes in a 900-flat community (brief; n=1). Incumbents built per-flat caps, prime slots, cancellation windows and no-show blacklists (EVALUATION §4, [C2][C11]) — signal that contention is common. No interviews or VALIDATION yet (T1–T5 pending).
- Current alternatives and why they fall short (from COMPETITORS): WhatsApp + register (no record, first-message-wins favours the always-online); MyGate (booking rules exist but app is ad-heavy — "3-4 HOAX / distracting notifications … ADS" [C3]); NoBrokerHood (simple FCFS booking, reschedule = cancel + rebook [C7]); ADDA (prime-slot rules in a paid package [C11]). None offers a ballot for peak slots (as far as public material shows — verify in F-03).

## 3. Goals, non-goals and success metrics
| Goal | Primary metric | Target (6 months) | Input metrics | How measured |
|---|---|---|---|---|
| Residents book fairly without WhatsApp | % of court/hall bookings in pilot community made in ClubSlot | ≥ 80 % by week 8 of pilot | Weekly active bookers; bookings/week | `booking_confirmed` events vs committee's register count |
| Peak slots feel fair | Ballot participation among regular court users | ≥ 40 % | Ballot entries/week; distinct winning flats/month | `ballot_entered`, `ballot_drawn` |
| No-shows stop blocking others | Released slots re-used by waitlist | ≥ 50 % of released slots | No-show rate | `slot_released`, `waitlist_booked` |
| Committee stops refereeing | Disputes reported by committee | −75 % vs T1 baseline | — | Monthly committee check-in (manual) |
| Business signal | Paying communities | 1 own pilot + 2 paying pilots (reset from brief's 20, Q-05) | LOIs | CRM sheet |
- Non-goals (explicitly not doing in v1): gate/visitor passes, notices, complaints/helpdesk, maintenance billing, in-app payments, native iOS/Android apps, multi-language UI (Telugu in v1.1), classes/coach scheduling.
- Guardrail metrics (must not get worse): booking error rate (double bookings = 0), page load on 4G (LCP < 2.5 s), accessibility (axe: 0 serious violations), support messages to the owner per week.

## 4. Users
### Personas
| Persona | Context | Goal | Frustration today | Accessibility needs |
|---|---|---|---|---|
| Lakshmi, 34, resident, IT professional | iPhone, plays badminton twice a week | Get the Saturday 7 pm court sometimes | The same early-messaging group always wins | One-handed use, quick |
| Mr. Rao, 67, retired resident | Budget Android, WhatsApp-only user | Book the party hall for family events | Has to go to the security desk and ask; unsure it's really his | Large text (200 %), plain language, no install; Telugu later |
| Ravi, 41, sports secretary (committee volunteer) | Laptop + Android | Stop refereeing; rules enforce themselves | Friday-night WhatsApp arguments | — |
### Jobs to be done
- When I want to play this week, I want to see what's free and book it in seconds, so I can plan my evening.
- When a slot is popular, I want a fair chance at it, so I don't lose to whoever messages fastest.
- When someone doesn't show up, I want the slot to go to the next person, so the court isn't wasted.
- When residents argue about a booking, I (committee) want a clear record and rules everyone can see, so I don't have to arbitrate.

## 5. Positioning and differentiation
- Positioning statement: For clubhouse committees in large gated communities who are tired of WhatsApp booking fights, ClubSlot is a fair-booking tool that gives every flat a fair shot at peak slots. Unlike the booking module in all-in-one society apps, it is built only for contested amenities — ballots, no-show release and a public rules log — with no ads.
- Differentiators this release must make visible (and where in the product): **peak-slot ballot** (S-04 "Peak · ballot" chip, S-06, S-07 — US-06, US-07); **no-show release** (S-05 check-in rule, S-07 released variant — US-08); **public rules log** (S-09 — US-10); **no ads, no numbers shown** (every screen; S-02 privacy line — US-02). A first-session user sees the ballot chip and the check-in rule on their first booking.
- What we deliberately don't compete on: gate security, accounting, payments, notices, breadth of modules.

## 6. Scope
| Capability | MoSCoW | Release | Why |
|---|---|---|---|
| Join via invite link + phone OTP + roster match | Must | v1 | Entry from WhatsApp, verified flat |
| Amenity list with "what's free today" | Must | v1 | Core action |
| Book / cancel a free slot with rules (length, hours, advance window, weekly cap, closed dates) | Must | v1 | Core action; no double booking |
| Peak-slot ballot with fair-share weighting | Must | v1 | Differentiator |
| Check-in + no-show auto-release to waitlist | Must | v1 | Differentiator |
| Committee: amenity rules editor | Must | v1 | Committee control |
| Committee: roster import + approve join requests | Must | v1 | Trust; abuse prevention |
| Public rules log | Should | v1 | Transparency differentiator |
| My bookings (upcoming/past) | Should | v1 | Basic expectation |
| Reminders (SMS/WhatsApp) before slot and ballot draw | Could | v1.1 | Retention; message cost |
| Booking fee shown (billed with maintenance) | Could | v1 | Party hall fees without payments |
| Telugu UI | Could | v1.1 | Older residents |
| UPI payments via Razorpay (Route to RWA account) | Won't (v1) | Later | Aggregator, refunds, GST unknowns |
| Notices, visitor passes, helpdesk | Won't | — | Incumbents' core; not the differentiator |
- MVP definition: the smallest product that tests **A-02/A-05 — that residents will use a fair ballot for contested slots instead of WhatsApp** and delivers **conflict-free booking of 2–3 contested amenities**.
- Later releases (themes only): payments; reminders; coach/class recurring slots; multi-community committee dashboard; integration with existing society apps.

**Scope check (write-prd step 4):** Musts estimated at ~70–90 h with AI tools (EVALUATION §10) ≈ 7–9 weeks at 10 h/week — at the top of the 6–8-week guide. If the plan exceeds it, cut in this order: rules log → Should; roster CSV import → manual add; fair-share weighting → plain random ballot. Keep booking, ballot and no-show release.

## 7. User journeys
Flows: DESIGN_DIRECTION §5.1 (first run → first value), §5.2 (peak-slot ballot), §5.3 (recovery).
- **Book a free slot** — happy: link → amenity → slot → confirm → booked (4 taps returning). Edge: slot taken meanwhile → error with 2 nearest free slots; weekly cap reached → error with reset time; offline → cached view, booking disabled with message; slow network → button shows progress, no double submit.
- **Enter ballot** — happy: slot → enter ballot → result notification/next visit → check in. Edge: ballot closed → show result or next ballot; not drawn → waitlist offer; did not check in → release + no-show count.
- **Join** — happy: link → OTP → roster match → home. Edge: wrong OTP; number not on roster → join request; link expired → ask committee for a new link; permission denied (location for check-in, if used) → QR or manual check-in fallback.
- **Committee edits rules** — happy: edit → validate → publish → rules log entry. Edge: invalid combination (peak > 50 % of slots) → inline error; conflicting existing bookings when closing dates → list affected bookings and notify flats.

## 8. Requirements and user stories
### Epic E1 — Join and sign in
**US-01** · As a resident, I want to open the community link and sign in with my phone number so that I can book without installing an app · Must
- Given a valid invite link, when I open it on a phone browser, then I see the community name and "Continue with phone number" (S-01).
- Given my number is on the committee roster, when I enter the correct OTP, then I land on Book with my flat shown (S-02 → S-03b).
- Given I enter a wrong OTP, when I submit, then I see "That code didn't match…" and can resend after 30 s; my number stays filled in.
- Given an expired or invalid link, when I open it, then I see "This invite link has expired. Ask your committee for a new one." and no sign-in form.
- Given I'm offline, when I tap Send code, then I see "You're offline. Connect and try again." and nothing is sent.
- Design: S-01, S-02 · Personal data used: phone number (sign-in, roster match), flat number (eligibility, caps).

**US-02** · As a resident, I want my phone number never shown to other residents so that joining doesn't expose me · Must
- Given any resident-facing screen, when bookings by others are shown, then only "Booked" appears — no name, flat or phone.
- Given a committee member, when they view a booking, then they see flat number only (no phone) unless they open the roster.
- Design: S-04, S-09 · Personal data used: none shown.

**US-03** · As a resident not on the roster, I want to request to join so that the committee can approve me · Must
- Given my number isn't on the roster, when OTP succeeds, then a join request with my flat is created and I see "Request sent to the committee — we'll SMS you when approved."
- Given the committee rejects it, when I open the link, then I see "Your request wasn't approved. Contact the clubhouse committee." 
- Design: S-02 note, S-11 · Personal data used: phone, claimed flat number.

### Epic E2 — Book a slot
**US-04** · As a resident, I want to see what's free today across amenities so that I can choose quickly · Must
- Given amenities exist, when I open Book, then I see each amenity with free-slot count and closed/peak notes (S-03).
- Given no amenities are set up, when I open Book, then I see "Your committee hasn't added amenities yet." (empty).
- Given I'm offline with cached data, when I open Book, then I see cached slots with "Showing slots from 9:32 am. Booking needs a connection."
- Given the server errors, when loading, then I see "Couldn't load slots. Try again." with a retry button.
- Design: S-03, S-03b · Personal data used: flat (to show my next booking).

**US-05** · As a resident, I want to book a free slot within the rules so that it's mine without asking anyone · Must
- Given a free, non-peak slot within my cap and the advance window, when I tap Book, then the slot is booked and S-05 shows time, check-in rule and free-cancellation deadline.
- Given two residents tap Book on the same slot at the same moment, when both requests reach the server, then exactly one booking succeeds and the other sees the S-04b "just taken" error with 2 alternative slots.
- Given I've used my weekly cap, when I tap Book, then I see "You've used 3 of 3 court slots this week. Your limit resets Monday at 6 am."
- Given the slot is beyond the advance window or on a closed date, then it isn't bookable and shows why.
- Given I'm offline, when I tap Book, then nothing is booked and I see the offline message; nothing shows as booked until the server confirms.
- Design: S-04, S-04b, S-05 · Personal data used: flat.

**US-09** · As a resident, I want to see and cancel my bookings so that others can use slots I don't need · Should
- Given upcoming bookings, when I open My bookings, then I see them with status (Booked, In ballot, Won, Released).
- Given I cancel before the free-cancellation deadline, then the slot frees immediately, the first waitlisted flat is offered it, and I see "Cancelled. Undo" for 5 s.
- Given I cancel after the deadline, then I'm told it counts as a no-show before confirming.
- Given no bookings, then I see "Nothing booked. Your past bookings will show here too."
- Design: S-08 · Personal data used: flat.

### Epic E3 — Fair access (differentiator)
**US-06** · As a resident, I want to enter a ballot for a peak slot so that I have a fair chance instead of racing on WhatsApp · Must
- Given a slot the committee marked peak, when I open it before the ballot closes, then I see close time, entrants count and my fair-share count, and can enter in one tap (S-06).
- Given I've already entered, then the button reads "Leave ballot".
- Given the ballot has closed, then I see the result or "Ballot closed — result at 9:05 pm".
- Given I've reached my monthly peak-slot cap, then I can't enter and see why.
- Design: S-04, S-06 · Personal data used: flat.

**US-07** · As a committee, I want ballots drawn automatically and fairly so that results can't be disputed · Must
- Given a ballot closes, when the draw runs, then winners are chosen at random with one extra entry for flats with 0 peak slots in the last 4 weeks, and a draw record (time, entrant count, seed hash) is written to the rules log.
- Given zero entrants, then the slot becomes a normal free slot.
- Given the draw job fails, then it retries and the committee is alerted; residents see "Result delayed" rather than a wrong result.
- Design: S-07, S-09 · Personal data used: flat (in draw; not published).

**US-08** · As a resident on the waitlist, I want no-show slots released to me so that the amenity isn't wasted · Must
- Given a booked or won slot, when no check-in happens by start + 15 min (committee-set), then the slot is released, the first waitlisted flat is notified in-app, and the no-show is counted.
- Given I check in within the window (QR at the court or in-app tap), then the booking shows "Checked in".
- Given location permission is denied (if location check-in is used), then QR/manual check-in is offered.
- Design: S-05, S-07 · Personal data used: flat; check-in time.

**US-10** · As a resident, I want to see the rules and recent draws/releases so that I can trust the system · Should
- Given rules exist, when I open Rules, then I see current rules, last change date and recent draws/releases with no names or flat numbers.
- Given no activity yet, then I see the rules and "No draws yet."
- Design: S-09 · Personal data used: none shown.

### Epic E4 — Committee tools
**US-11** · As a committee member, I want to set rules per amenity so that the app enforces what we agreed · Must
- Given I'm a committee member, when I edit slot length, hours, advance window, weekly cap, peak slots, check-in window and closed dates and save, then the rules apply to new bookings and a rules-log entry is created.
- Given peak slots exceed 50 % of open slots, then I see an inline error and can't publish.
- Given closing dates conflict with existing bookings, then I see affected bookings and can notify those flats before saving.
- Given I'm not a committee member, when I open the committee URL, then I see "Only committee members can change rules." (permission denied).
- Design: S-10 · Personal data used: none.

**US-12** · As a committee member, I want to import the flat roster and approve join requests so that only residents can book · Must
- Given a CSV of flat + phone, when I import, then valid rows are added and invalid rows are listed with the reason.
- Given a pending request, when I approve or reject, then the resident is informed.
- Design: S-11 (not wireframed yet) · Personal data used: flat, phone (roster) — stored only for sign-in matching; deletable by committee and on resident request.

Acceptance-criteria → test mapping: each Given/When/Then above becomes at least one automated test (unit for rules/ballot logic, integration with a test database for booking concurrency and permissions, Playwright E2E for US-01, US-05, US-06/07, US-08). Concurrency (US-05 #2) needs a database-level uniqueness constraint test.

## 9. Experience and design
- Experience principles (from DESIGN_DIRECTION): fair and visible · one job, done fast · no app, no ads · committee in control · everyone can use it.
- Screen inventory with states: DESIGN_DIRECTION §6 and `design/wireframes/index.html` (S-01–S-10; S-11 to be wireframed).
- Visual direction chosen: **pending owner (Q-09)** — recommended A, Courtside calm.
- Content and voice: calm, fair, plain. Key terms: amenity, slot, ballot, flat, committee, no-show. Microcopy in DESIGN_DIRECTION §7.
- Accessibility requirements: WCAG 2.2 AA; 48 px targets; text to 200 %; slot status as text not colour; screen-reader labels for each slot ("6 pm to 7 pm, free"); reduced motion.
- Localisation: English at launch with externalised strings; Telugu in v1.1 (Q-06); ₹ and Indian date formats.

## 10. Data and permissions **(full)**
After approval. (Draft note: entities will include community, flat, resident, amenity, rule set, slot, booking, ballot, ballot entry, check-in, rules-log entry; per-community row-level security; personal data limited to phone + flat.)

## 11. Analytics **(full in detail; draft lists the funnel)**
| Event | When | Properties (no personal data) | Funnel step |
|---|---|---|---|
| `invite_opened` | S-01 loads | community_id | 1 |
| `signin_completed` | OTP verified | roster_match: bool | 2 |
| `amenity_opened` | S-04 loads | amenity_type | 3 |
| `booking_confirmed` | Server confirms | amenity_type, is_peak: false, lead_time_h | 4 |
| `booking_conflict` | Slot taken / cap error | reason | 4 (error) |
| `ballot_entered` | Entry saved | amenity_type | 4 (peak) |
| `ballot_drawn` | Draw completes | entrants, winners | — |
| `checked_in` / `slot_released` / `waitlist_booked` | As named | amenity_type | 5 |

## 12. Non-functional requirements
- Performance: LCP < 2.5 s on mid-range Android over 4G; booking confirmation < 1 s p95.
- Reliability: zero double bookings (database constraint); ballot draw idempotent with retries.
- Security (OWASP): server-side authorization on every request; per-community RLS; schema-validated input; rate-limited OTP; no secrets in client.
- Privacy (DPDP Act 2023 + Rules 2025): plain-language notice at sign-in; phone + flat only; residents can delete their account; committee can delete roster rows; no under-18 accounts; no third-party ads or ad trackers.
- Accessibility: WCAG 2.2 AA (see §9).
- Offline behaviour: cached read-only "what's free" with "last updated"; no offline writes.
- Supported devices: last 2 versions of Chrome (Android), Safari (iOS 16+), desktop Chrome/Edge/Safari for committee; 360 px minimum width.
- AI features: none.

## 13. Technology **(full)**
After approval. Provisional (EVALUATION §10): responsive web app (Next.js PWA) + Supabase + Indian SMS OTP provider; payments later via Razorpay Route.

## 14. Dependencies and risks
| Risk / dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| Owner's community already uses a society app's booking module (F-01) | High | High | T1 audit before build | Owner |
| Committees won't pay a single-job tool (A-03) | High | High | T5 LOI; per-community pricing | Owner |
| Residents keep using WhatsApp | High | Medium | Committee declares ClubSlot the only valid record; T3 concierge ballot | Owner + committee |
| Ballot perceived as unfair or rigged | Medium | Medium | Public draw record, simple rules, committee-owned | Owner |
| Booking concurrency bugs (double booking) | High | Low | DB constraint + tests | Builder |
| SMS OTP deliverability/cost (DLT registration in India) | Medium | Medium | Verify provider + DLT template before build | Owner |
| Incumbent copies ballot | Medium | Medium | Local trust, speed, integration rather than replacement | Owner |

## 15. Release plan
| Milestone | Scope | Exit criteria | Target date |
|---|---|---|---|
| Validation (T1–T5) | Audit, interviews, concierge ballot, LOI | T1 shows the need; ≥ 40 % ballot participation; ≥ 1 LOI | ~5 weeks (Nov 2026) |
| Prototype test | wireframes | ≥ 4/5 complete the core task | Week 2 of validation |
| Private beta | MVP Musts in owner's community, 2 amenities | 4 weeks, zero double bookings, ≥ 80 % of bookings in-app | ~9 weeks after approval |
| Public launch | 2 more communities | ≥ 1 paying community | ~4 months after approval |
- Launch channels for the first 100 users (from EVALUATION §5): owner's community WhatsApp groups via the sports secretary; 3 committee contacts; committee-to-committee referrals.
- Kill or pivot criteria after launch: < 30 % of court bookings in-app after 6 weeks of pilot; no paying community after 3 pilots → stop, or switch to Pivot B (setup service for existing apps).

## 16. Open questions and decisions
- Open (blocking): F-01, Q-05, A-03 (approval); Q-03, Q-04, Q-07 (scope defaults taken); Q-10 ballot rules; Q-11 flat verification — see CLARITY.md.
| Date | Decision | Options considered | Why |
|---|---|---|---|
| 2026-10-16 | Draft scoped to the pivot (fair booking, web-first, no payments) — default, owner to confirm | Brief's all-in-one scope · pivot | Evaluation: brief scope 4–6× owner capacity and fully served by incumbents |

## Appendix
- Glossary: **amenity** — a bookable shared space · **slot** — a bookable time block · **peak slot** — committee-marked high-demand slot allocated by ballot · **ballot** — random draw among entrants with fair-share weighting · **no-show** — booked but not checked in within the window · **committee** — the RWA's clubhouse/sports committee.
- Research links: COMPETITORS.md, research/competitors.md.

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-16 | First draft from EVALUATION v1 + DESIGN_DIRECTION v0.1 (owner unavailable; defaults per CLARITY) |
