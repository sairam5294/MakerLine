# Clarity Log — ClubSlot

_Updated 2026-10-19 · Created by evaluate-idea from PROJECT_BRIEF v1 (no discovery interview; owner unavailable)_
**Readiness:** Evaluation can start (provisional) · 6 questions block approval · 0 of 6 blocking answered

A question is **blocking** if a phase can't sensibly proceed without it and it has no default (facts, assumptions), or the owner must confirm its default before approval (decisions).

Every open question about the idea lives here until it is answered. Each one names the decision it blocks, so the owner can see at a glance what stands between the idea and the next step. Skills read and update this file; nothing is deleted, answered rows move to the bottom.

## Readiness by phase

| Phase | Ready? | Blocked by |
|---|---|---|
| Evaluation (evaluate-idea) | provisional (done with defaults) | Q-05, Q-08 would sharpen scores |
| Design direction (design-direction) | yes (done with defaults) | Q-01, Q-02 confirm the pivot and platform |
| PRD draft (write-prd) | yes (done with defaults) | Q-01, Q-03 |
| Validation test (validate-idea) | yes | Q-04 (who to recruit) |
| Approval | no | Q-01, Q-02, Q-03, Q-08, A-01, A-02 |
| Naming (name-product) | no | Approval |
| Tech stack (tech-stack) | no | Approval, Q-02 |
| PRD full (write-prd) | no | Approval |

## Open questions

| ID | Question | Why it matters | Blocks | Type | How to find out | Owner | Default if unanswered |
|---|---|---|---|---|---|---|---|
| Q-01 | Accept the pivot: amenity booking only (no visitor passes, complaints, notices) for v1? | The brief's scope is not buildable in 10 weeks at 10 h/week; incumbents already bundle everything (R2, R3) | Approval / Design direction / PRD draft | Decision | Ask owner | Owner | **[Default] Yes — booking-only wedge** (EVALUATION §8) |
| Q-02 | Platform for v1: installable web app (PWA) with WhatsApp links, or native Android + iOS + web admin? | Native on two platforms plus admin triples the build and adds store review; residents already open WhatsApp links (R13) | Design direction / Tech stack | Decision | Ask owner | Owner | **[Default] PWA + WhatsApp share links; native later** |
| Q-03 | Pricing: ₹15/flat/month (brief) vs market band ₹3–15 (R8) vs flat ₹1,500–2,500/community/month? | Free-with-ads incumbents (R3, R17) set the anchor; committees compare per-flat | Approval / PRD draft | Decision | 3 committee conversations (owner's contacts) | Owner | **[Default] ₹8/flat/month, min ₹1,500/community, first 3 communities free for 3 months** |
| Q-04 | Which of the owner's 3 contact communities is the pilot, and who is the committee sponsor? | Pilot community decides the first rule set and test users | Validation test | Decision | Ask owner | Owner | [Default] owner's own 900-flat community (brief) |
| Q-05 | How many gated communities / registered RWAs exist in Hyderabad, and how many still book amenities on WhatsApp or paper? | Sizes SAM/SOM; brief's "20 communities" target depends on it | Approval | Fact | Desk research: Telangana Registrar of Societies, GHMC, MyGate/NoBrokerHood city pages; ask 3 facility managers | Claude | none — must be found out |
| Q-06 | What do residents and committees complain about in NoBrokerHood and ADDA (independent reviews)? | Only MyGate complaints are sourced (R9); differentiator test needs the others | Approval | Fact | Read Play / App Store (India) reviews, G2, Reddit r/hyderabad | Claude | none — must be found out |
| Q-07 | India store ratings and counts for MyGate, NoBrokerHood, ADDA | Scale signal for the leader profiles | — | Fact | Open apps.apple.com/in and Play listings (fetch failed, R16) | Claude | none — must be found out |
| Q-08 | Will committees pay for booking alone, and how much? | Monetization score rests on it | Approval | Fact | 5 committee interviews with a price card (₹5 / ₹8 / ₹15 per flat) | Owner | none — must be found out |
| Q-09 | Which communities' bylaws require registered-owner-only booking, deposits or refundable damage fees? | Drives the rules engine scope and the payment flow | PRD full | Fact | Ask the 3 contact committees for their amenity bylaws | Owner | none — must be found out |
| Q-10 | Does the pilot community already use MyGate / NoBrokerHood for the gate? | If yes, ClubSlot must coexist, not replace | Design direction / Validation test | Fact | Ask owner | Owner | none — must be found out |
| Q-11 | Languages for v1: English only, or English + Telugu (+ Hindi)? | Older residents and security staff; inclusion baseline | Design direction / PRD draft | Decision | Ask owner; check pilot community's notices | Owner | **[Default] English + Telugu UI strings in v1; Hindi later** |

**Type.** *Decision* — the owner chooses (goal, platform, scope, price). *Fact* — knowable about users or the market; never assume, find out. *Assumption* — a belief the idea depends on; it becomes a validation test.

**Default if unanswered.** For a Decision, the recommended option and why. For a Fact or Assumption, write "none — must be found out", never a guess.

## Assumptions the idea depends on (ranked by risk)

| ID | We believe… | If wrong, then… | Evidence so far | Test | Status |
|---|---|---|---|---|---|
| A-01 | Committees will pay for a booking-only tool even when a free gate app offers booking | No revenue; must bundle or go free | Incumbents bundle booking free (R2, R3); vendor claims 71% still on WhatsApp (R13, weak) | Price-card interviews with 5 committees (Q-08) | Untested |
| A-02 | Double bookings and disputes are frequent enough that residents switch from WhatsApp | Low adoption; committee cancels | Owner's weekly observation (brief); vendor figure 18% double-bookings (R13, weak) | Count disputes in 2 WhatsApp groups over 4 weeks; prototype test | Untested |
| A-03 | Facility managers will enforce app bookings at the clubhouse desk | Paper register continues in parallel; app loses | None | Pilot: desk shows app screen; count paper entries | Untested |
| A-04 | "There are no competitors" (brief) | Positioning is wrong; incumbents can copy any feature | **Contradicted** — 10+ products bundle amenity booking (R2–R7) | Done | Contradicted |
| A-05 | Owner can build a PWA + Supabase backend in ~10 weeks at 10 h/week with AI tools | Launch slips; budget overrun | Owner is a designer with light coding (brief) | Build the booking calendar spike in week 1–2 | Untested |

## Answered

| ID | Answer | Source (owner, research link, test) | Date | Changed |
|---|---|---|---|---|
| — | | | | |
