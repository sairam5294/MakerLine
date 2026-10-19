# PRD — ClubSlot

_Draft v0.1 (idea stage) · 2026-10-19 · Owner: (see OWNER.md — blank; brief's owner section used) · Status: Draft_
_Inputs: PROJECT_BRIEF v1 · EVALUATION v1 · COMPETITORS v1 · DESIGN_DIRECTION v1 · CLARITY · Research `research/market.md`_

**Pivot: booking-only wedge** (EVALUATION §8, pivot A). This draft specs the pivot. If the owner keeps the brief as written, add epics for visitor passes, complaints, notices and maintenance dues; the Must count roughly triples and the build estimate exceeds 20 weeks at 10 h/week.

Sections marked **(full)** are filled after approval; in a draft write "after approval" under the heading. Decisions marked **[Default]** were taken because the owner was unavailable.

## 1. Summary
ClubSlot is a shared-amenity booking service for gated communities in Hyderabad: residents book courts, pool slots, the lounge and the party hall from a link in their community WhatsApp group; the committee's rules (turns per flat, advance windows, fees, deposits) are applied automatically and explained in plain words; the desk verifies any booking in five seconds. The problem is weekly: bookings today happen in WhatsApp threads and a paper register, so double bookings and disputes land on volunteer committee members. Now is the moment because the incumbents have bundled booking into ad-funded super-apps that residents complain about (R9) while most mid-size communities still run on WhatsApp (R13, weak). ClubSlot wins by doing one job with visible fairness, no install and no ads. Version 1 is a PWA for residents and the desk plus a desktop console for the committee, piloted in one community.

## 2. Problem
- Problem statement: residents and committees of gated communities struggle to share amenities fairly because bookings live in chat threads and paper registers with no confirmation or rules, which leads to double bookings, hoarding and weekly disputes that volunteers must settle.
- Evidence (sourced, from EVALUATION / VALIDATION): owner's first-hand weekly observation (brief); vendor cohort figures of 18% double bookings and 71% of societies on WhatsApp (R13, weak); all incumbents ship a booking module (R2–R7). Validation pending (T1–T4 in EVALUATION §12).
- Current alternatives and why they fall short (from COMPETITORS): WhatsApp + register (reach, but no confirmation or fairness); MyGate / NoBrokerHood / ADDA (booking exists but requires a platform migration, an install and tolerating ads and notification noise, R9; rules support unknown, Q-06).

## 3. Goals, non-goals and success metrics
| Goal | Primary metric | Target (6 months) | Input metrics | How measured |
|---|---|---|---|---|
| Stop booking disputes in pilot communities | Disputes escalated to the committee per month | ≤ 1 (from ≥ 2/week baseline, T3) | Share of bookings via ClubSlot ≥ 80%; paper register retired | Committee monthly check-in form; `booking_created` events |
| Residents book without help | Link → confirmed booking conversion | ≥ 30% of link opens convert in the first month | OTP completion ≥ 80%; median time to confirm < 90 s | Events `link_opened`, `otp_verified`, `booking_confirmed` |
| Paying communities **[Default target, reset from brief]** | Communities paying | 5–8 paying, ₹10k–16k MRR | 3 pilots → 2 referrals each | Billing records |
| Fairness is understood | Residents who can state the rule after first booking | ≥ 4 of 5 in prototype test; ≥ 70% in in-app one-question survey | — | T2; `survey_rule_understood` |
- Non-goals (explicitly not doing in v1): visitor passes, complaints/helpdesk, notices feed, maintenance dues and accounting, native app-store apps, multi-city, AI features, ads.
- Guardrail metrics (must not get worse): booking-related messages sent per resident per week ≤ 3; accessibility audit score (axe + manual) with 0 critical issues; support requests per community per month ≤ 5; no personal data beyond name, phone, flat.

## 4. Users
### Personas
| Persona | Context | Goal | Frustration today | Accessibility needs |
|---|---|---|---|---|
| P-01 Srinivas, committee amenities secretary (EVALUATION §5) | Volunteer, mid-range Android | Fewer arguments, an AGM record | WhatsApp fights, no-shows | Large text, Telugu for notices |
| P-02 Priyanka, resident | iPhone, books courts twice a week | See what's free, book in seconds | Scrolling threads, slot already gone | Situational one-handed use |
| P-03 Ramesh, facility manager / desk | Low-end Android, basement office | Settle disputes fast, no blame | "I messaged the group" | Telugu, large text, slow data |
### Jobs to be done
- When I want the court tonight, I want to see what's free and book it in a tap, so I can stop scrolling the group.
- When two families claim the hall, I want a record everyone trusts, so I'm not the referee.
- When a resident arrives at the desk, I want to confirm their slot in seconds, so there's no argument at the counter.
- When heavy users hoard slots, I want rules applied automatically, so the committee doesn't have to police them.

## 5. Positioning and differentiation
- Positioning statement: For committees of gated communities in Hyderabad who are tired of amenity-booking disputes, ClubSlot is a shared-amenity booking service that gives every flat a fair, confirmed slot from a WhatsApp link. Unlike MyGate or NoBrokerHood, it does one job, with no ads and no app to install.
- Differentiators this release must make visible (and where in the product): fair rules shown before and at booking — US-03, US-05 on S-01, S-03, S-04; book from a link without install — US-01, US-02 on S-01, S-02; quiet — US-09 (only booking messages); desk-proof — US-08 on S-08.
- What we deliberately don't compete on: gate security, dues, accounting, community feed, breadth of modules.

## 6. Scope
| Capability | MoSCoW | Release | Why |
|---|---|---|---|
| Community set-up: amenities, hours, rules, fees (console) | Must | Pilot | Without it nothing works |
| Week view per amenity from a public link | Must | Pilot | The first-session value |
| Phone OTP + flat sign-in | Must | Pilot | Fairness needs the flat |
| Book / cancel with rule enforcement and plain-language reasons | Must | Pilot | The core action + differentiator |
| Waitlist with auto-promotion | Must | Pilot | Stops "first message wins" fights |
| Confirmation with desk code; booking-only messages (SMS/WhatsApp link) | Must | Pilot | Desk-proof; quiet |
| Desk view (today, search, mark arrived, book on behalf) | Must | Pilot | Retires the paper register (A-03) |
| English + Telugu UI **[Default]** | Must | Pilot | Inclusion baseline; staff |
| Accessibility statement + barrier feedback route; DPDP consent and deletion | Must | Pilot | Law and kit floor |
| Fees and deposits via Razorpay payment links | Should | Beta | Party hall needs it; courts don't |
| Committee reports (utilisation, no-shows) | Should | Beta | Renewal reason |
| Home-screen install prompt | Could | Beta | Convenience |
| Hindi / Kannada | Could | Later | Bengaluru |
| Native apps, visitor passes, complaints, notices, dues | Won't (v1) | — | Pivot scope |
- MVP definition: the smallest product that tests *committees will pay for fair, confirmed booking alone* (A-01) and delivers *a confirmed slot in a tap with rules everyone can see*.
- Later releases (themes only): payments depth, reports, multi-community for facility-management firms, Bengaluru.

## 7. User journeys
Flows are in DESIGN_DIRECTION §5 (first run → first value; core action; recovery). For each core journey:
- **Book from link** — happy: link → week view → OTP + flat → slot → confirm → confirmed (S-01 → S-02 → S-04 → S-05). Edge: wrong OTP (S-02 error); unknown flat (S-02 error, committee approval queue); slot taken while confirming (S-04 error, next options); quota reached (S-04 rule copy, waitlist); offline (cached bookings, banner, retry); slow network (skeletons, no timeouts under 30 s); permission denied (resident not approved for this community → "Ask the committee to approve your flat" with a one-tap request).
- **Cancel / undo** — happy: My bookings → Cancel → 10-minute undo bar. Edge: cancel after the free window → counts as a used turn, stated before confirming; offline → queued with a notice.
- **Desk verification** — happy: search flat or code → booking shown → mark arrived. Edge: no booking found → "No booking for B-1204 today — book on their behalf?"; offline → last synced list with timestamp.
- **Committee set-up** — happy: create community → add amenity → set hours, turns, advance window, fee → preview rule in plain words → share link. Edge: conflicting rules (validation message); empty community (no amenities yet → guided first amenity).

## 8. Requirements and user stories
### Epic E1 — See and book a slot
**US-01** · As a resident (P-02), I want to open the amenity's week view from the WhatsApp link without installing anything so that I can see what's free in seconds · **Must**
- Given a valid community link, when I open it on a phone browser, then I see the amenity, the current week, each slot's state (free / booked / waitlist) and the rule in one line within 2 s on a 3G connection.
- Given the community has no amenities set up yet, when I open the link, then I see "Nothing to book yet — the committee is setting up" and a way to notify the committee.
- Given I am offline, when I open the link, then I see an offline banner and any cached bookings instead of a blank page.
- Design: S-01 · Personal data used: none until sign-in.

**US-02** · As a resident, I want to sign in with my phone number and flat so that the community's rules apply to my flat · **Must**
- Given I enter my number, when I request a code, then an SMS arrives within 30 s and the code field is focused and labelled.
- Given a wrong or expired code, when I submit, then the field is marked invalid with a message that says how to get a new code, and no booking proceeds.
- Given a flat number not in the community, when I continue, then I see "We don't have B-1240 in Lakeview Heights…" with a one-tap request to the committee, and I cannot book until approved (permission denied).
- Given a flat already linked to another phone, when I sign in, then I am added as a second member of that flat and the first member is notified (no silent takeover).
- Design: S-02 · Personal data used: phone (identity, OTP, booking messages), flat (rules); both shown in the consent notice.

**US-03** · As a resident, I want to book a free slot and see how it counts against my flat's turns so that I know the booking is fair · **Must**
- Given a free slot within my flat's turns, when I confirm, then the booking is created atomically (no two flats can hold the same slot), and I see the confirmation with a desk code.
- Given the slot was taken between viewing and confirming, when I confirm, then I see an error naming the next two free slots and a waitlist option, and nothing is booked.
- Given my flat has used its turns, when I tap a slot, then I see the rule, when my next turn opens, and the waitlist option; the confirm button is not shown.
- Given a screen-reader user, when they book a slot, then every slot button announces time and state, and the confirmation is announced via a live region.
- Design: S-01, S-04, S-05 · Personal data used: flat and phone (booking record).

**US-04** · As a resident, I want to join a waitlist and be promoted automatically so that "first message wins" fights end · **Must**
- Given a booked slot, when I join its waitlist, then I see my position (count only, no names).
- Given the slot is cancelled, when I am first in line and still within my turns, then the slot is booked for me and I am messaged within 1 minute; otherwise the next eligible flat is promoted.
- Given I leave the waitlist, when I confirm, then positions behind me move up.
- Design: S-01, S-06 · Personal data used: flat.

### Epic E2 — Manage my bookings
**US-05** · As a resident, I want to see and cancel my bookings with an undo so that mistakes aren't costly · **Must**
- Given upcoming bookings, when I open My bookings, then I see each with its desk code, cancellation terms and my remaining turns.
- Given I cancel, when the undo bar is visible (10 min), then tapping Undo restores the booking if the slot is still free, else explains it was taken.
- Given no bookings, when I open the tab, then I see the empty state with a concrete free slot to book.
- Given I am offline, when I cancel, then the cancellation is queued, labelled "pending", and sent when back online.
- Design: S-06, S-07 · Personal data used: flat.

### Epic E3 — Desk
**US-08** · As desk staff (P-03), I want today's bookings in large text in Telugu and to find a flat in one search so that I can settle a dispute in 5 seconds · **Must**
- Given the desk view, when I type a flat or code, then matching bookings for today appear as I type, at ≥ 19 px text, in the selected language.
- Given no booking matches, when I search, then I see "No booking for B-1204 today" and a button to book on their behalf, which logs my name and a reason.
- Given the desk device is offline, when I open the view, then I see the last synced list with its time.
- Given a desk login, when I try to open the committee console, then I am told I don't have access (permission denied) and nothing is shown.
- Design: S-08 · Personal data used: flat, resident name (shown to staff only).

### Epic E4 — Committee console
**US-06** · As a committee member (P-01), I want to set up amenities and rules in one evening and see the rule in plain words so that residents understand it the same way I do · **Must**
- Given a new community, when I add an amenity with hours, turns per flat per week, advance window and fee, then a plain-language preview appears ("2 court hours per flat per week, book up to 7 days ahead, no fee") and is what residents see.
- Given conflicting settings (e.g. slot length longer than opening hours), when I save, then I see which field conflicts and nothing is saved.
- Given a resident requests approval of an unknown flat, when I open Members, then I can approve or reject with one tap and the resident is messaged.
- Given the console on a phone, when I open it, then all actions remain usable (responsive), though desktop is recommended.
- Design: S-09 (described in DESIGN_DIRECTION §6; not wireframed) · Personal data used: member names, phones, flats (committee role only).

**US-07** · As a committee member, I want a monthly summary of bookings, no-shows and disputes so that I can justify the fee at the AGM · **Should**
- Given a month of data, when I open Reports, then I see utilisation per amenity and no-show counts with export to CSV.
- Design: S-11 (later) · Personal data used: aggregated only.

### Epic E5 — Trust, privacy and accessibility
**US-09** · As a resident, I want to receive only messages about my own bookings so that the app stays quiet · **Must**
- Given a booking, when it is confirmed, promoted, cancelled by the desk, or 1 hour away, then I receive one message each; no other messages are sent.
- Given I turn off reminders, when a booking approaches, then no reminder is sent but confirmations still are.
- Design: S-10 settings · Personal data used: phone.

**US-10** · As any user, I want a consent notice, data deletion and an accessibility statement with a way to report a barrier so that I can trust the service · **Must**
- Given first sign-in, when the consent notice is shown, then it lists each data item and purpose in plain English or Telugu, and I can withdraw later from Community › Privacy (DPDP Rules, R12).
- Given I request deletion, when 48 hours pass without me cancelling the request, then my personal data is erased and bookings are anonymised to the flat.
- Given the Community tab, when I open Accessibility, then I see the conformance level (WCAG 2.2 AA target), known gaps, and a form plus WhatsApp number to report a barrier, answered within 5 working days.
- Given a data breach, when it is confirmed, then affected users are notified without delay and the Board report is filed within 72 h (operational runbook, full PRD).
- Design: S-10 · Personal data used: as inventoried in §10 (full).

Must stories: 9 (US-01–06, 08–10) · Should: 1 · Build estimate: ~8 weeks of Musts at 10 h/week with AI tools (EVALUATION §10), confirmed by the week-2 spike (A-05).

## 9. Experience and design
- Experience principles (from DESIGN_DIRECTION §2): fair and seen to be fair · one tap from WhatsApp · quiet · desk-proof · calm under conflict.
- Screen inventory with states: DESIGN_DIRECTION §6 and `../../design/wireframes/index.html` (S-01 to S-08).
- Visual direction chosen: A "Notice board" **[Default]**, pending owner choice.
- Content and voice: DESIGN_DIRECTION §7 — "amenity", "slot", "rules", "desk", "your turns this week".
- Accessibility requirements: WCAG 2.2 AA + persona needs (large text, Telugu, screen-reader slot names, one-handed, low-end phone, offline) + India RPwD/GIGW alignment and DPDP (EVALUATION §11)
  - Accessibility statement (conformance level, known gaps, how to report a barrier) and a feedback route answered within 5 working days — US-10
  - Alternate formats / communication support on request: rules and confirmations available as plain text by SMS or from the desk
  - Accessibility Conformance Report (VPAT): keep test evidence from the pilot so an ACR can be produced if an RWA federation or facility-management firm asks — by public launch
  - Assistive-tech users in the prototype test (1 large-text or screen-reader user of 5) and the beta
  - Example criterion: Given a screen-reader user, when they book a slot, then every control is announced with name, role and state and the confirmation is announced
- Localisation: English + Telugu at launch **[Default]** (Q-11); Hindi, Kannada later; dates and times in IST with 12-hour clock.

## 10. Data and permissions **(full)**
after approval — draft note: entities will be Community, Amenity, Rule, Member (phone, name, flat, role), Booking, WaitlistEntry, DeskLog, Consent; RLS by community and role; personal data limited to name, phone, flat.

## 11. Analytics **(full in detail; draft lists the funnel)**
| Event | When | Properties (no personal data) | Funnel step |
|---|---|---|---|
| link_opened | S-01 loads | community_id, amenity_id, referrer=whatsapp/other | 1 |
| otp_requested / otp_verified | S-02 | community_id | 2 |
| slot_viewed | slot list rendered | amenity_id, free_count | 3 |
| booking_attempted | confirm tapped | amenity_id, rule_state | 4 |
| booking_confirmed / booking_failed | result | amenity_id, reason (taken / quota / network) | 5 |
| waitlist_joined / waitlist_promoted | — | amenity_id, position | — |
| booking_cancelled / undo_used | — | hours_before | — |
| desk_search / desk_mark_arrived / desk_booked_on_behalf | S-08 | community_id | — |
| survey_rule_understood | after first booking | yes/no | goal 4 |
| a11y_barrier_reported | S-10 | category | guardrail |

## 12. Non-functional requirements
- Performance budgets: first load < 200 KB, S-01 interactive < 2 s on 3G, slot list render < 500 ms; works on Android 9+ / iOS 15+ Safari **[Default]**.
- Reliability: bookings are atomic (unique constraint on amenity + slot); 99.5% monthly availability target for pilot.
- Security (OWASP): OTP rate-limited; server-side authorization for every community/role; parameterized queries; no secrets in client; hosted checkout for payments.
- Privacy (DPDP): minimum data, consent notice, 48-h erasure notice, breach process, logs retained ≥ 1 year (R12); no children's data collected.
- Accessibility: WCAG 2.2 AA; axe clean + manual screen-reader pass on the core flow before pilot.
- Offline behaviour: cached My bookings and desk list; queued cancellations; clear banners.
- AI features: none in v1.

## 13. Technology **(full)**
after approval — provisional: PWA (Next.js or SvelteKit) on Vercel, Supabase (Postgres + RLS + phone OTP), Razorpay payment links, PostHog, SMS via MSG91 (EVALUATION §10).

## 14. Dependencies and risks
| Risk / dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| Committees won't pay for booking alone (A-01) | Fatal to business | High | T1 price-card interviews before building | Owner |
| Paper register survives (A-03) | Adoption collapse | High | Desk view first; pilot rule "app bookings only" | Owner + committee |
| Incumbent copies fair rules | Differentiator erodes | Medium | Focus, speed, trust; rule-set stickiness | Owner |
| SMS OTP delivery cost and DLT registration in India | Sign-in friction, cost | Medium | Register sender ID early; WhatsApp link fallback | Owner |
| Razorpay onboarding / KYC for a new entity | Fees blocked | Medium | Start KYC in week 1; courts need no fees | Owner |
| DPDP obligations during year 1 (R12) | Compliance effort | Medium | Design in consent, erasure, logs now | Owner |
| Owner capacity (10 h/week) | Slip past 10 weeks | Medium | One pilot; Musts only; AI tools for mechanical work | Owner |

## 15. Release plan
| Milestone | Scope | Exit criteria | Target date |
|---|---|---|---|
| Price-card interviews (T1) + prototype test (T2) | wireframes | ≥ 3/5 committees would pilot; ≥ 4/5 residents complete the core task | Week 2 |
| Build spike (T5) | calendar + one rule | Working end to end in ≤ 20 h | Week 2 |
| Pilot (private beta) | MVP Musts, one amenity, one community | ≥ 80% of bookings via ClubSlot in 4 weeks; paper register retired; 0 critical a11y issues | Week 10 |
| Paid pilots | + payments, 3 communities | 2 of 3 convert to paid after free period | Month 4 |
| Public launch (Hyderabad) | + reports | 5–8 paying communities | Month 6 |
- Launch channels for the first 100 users (from EVALUATION §5): owner's community, 3 committee contacts, WhatsApp share link, RWA federation case study.
- Kill or pivot criteria after launch: < 2 paying communities by month 4 → pivot B (free residents, paid reports) or park; pilot conversion < 30% after fixes → re-examine the link-first assumption.

## 16. Open questions and decisions
- Open (blocking): Q-01 pivot acceptance, Q-02 platform, Q-03 price, Q-08 willingness to pay, Q-09 pilot bylaws, Q-10 existing super-app at the pilot (CLARITY.md).
| Date | Decision | Options considered | Why |
|---|---|---|---|
| 2026-10-19 | Spec the booking-only pivot **[Default, unconfirmed]** | As briefed; pivot A; pivot B; pivot C | Feasibility and differentiation (EVALUATION §1, §8) |
| 2026-10-19 | PWA + WhatsApp links for v1 **[Default]** | Native Android + iOS; PWA | One codebase, no store review, matches the link habit |
| 2026-10-19 | English + Telugu **[Default]** | English only | Staff and older residents; inclusion baseline |

## Appendix
- Glossary: amenity, slot, rules, turns, desk code, waitlist, console.
- Research links: `research/market.md`.
- Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-19 | First draft from the Standard Idea Pack; owner unavailable, defaults marked |
