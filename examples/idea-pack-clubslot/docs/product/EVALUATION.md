# Idea Evaluation Report — ClubSlot

_Version 1 · 2026-10-16 · Based on PROJECT_BRIEF v1 · Competitors: COMPETITORS.md · Open questions: CLARITY.md · Research cache: research/competitors.md_

> Run without the owner present ("give me everything"). Defaults taken are listed in CLARITY.md. Three perspectives were run in sequence (market-researcher → devils-advocate → idea-champion) and merged; disagreements are called out in §2 and §3.

## 1. Verdict
**Pivot** — confidence **Medium** that the idea *as briefed* won't work; **Low** for the pivot until tests T1–T3 run.
The problem is real (the owner sees booking fights weekly in a 900-flat community), but the product as briefed — an all-in-one society app with booking, UPI payments, notices, visitor passes and helpdesk on Android + iOS + web — already exists from three established players, and is 4–6× bigger than this owner can build in 10 weeks at 10 h/week. The version worth testing is narrow: **fair booking for contested amenities** in large communities, web-first, sold to clubhouse committees, piloted in the owner's own community first.

**In one minute**
- What's genuinely promising: a lived, frequent problem; the owner's insider access to 3 committees; a specific, under-served job (peak-slot fairness, no-shows, disputes) where incumbents offer only caps and blacklists; an ad-free, privacy-respecting angle incumbents can't easily copy because ads are 65–70% of MyGate's revenue.
- The biggest reality check: "There are no competitors doing this" is false. MyGate, NoBrokerHood and ADDA all ship amenity booking with rules and payments; NoBrokerHood is "free with add-ons".
- The one change that most improves the odds: cut to one job (fair booking for 2–3 contested amenities), one form (responsive web app, no native apps in v1) and one community (the owner's own) before selling to anyone.
- Next step (cheapest test that could change this verdict): T1 — a one-week audit of the owner's own community: which society app is installed, whether its booking module is switched on, and how many booking disputes happened in the last 8 weeks of WhatsApp history. If the community already uses MyGate/NBH booking without fights, drop the idea or move to a different community type.

### Scorecard
| Dimension | Score | Why (evidence) | Raise it by… (→ target) |
|---|---|---|---|
| Problem severity & frequency | 5 | Owner observes weekly disputes (brief; Evidence, n=1 community). But incumbents already solve the mechanics (slots, caps, blacklists) [C2][C11] — the remaining pain may be adoption, not software | Count disputes in owner's WhatsApp history; 10 resident interviews (T1, T2) → 6–7 |
| Audience clarity & reach | 6 | Clear payer (committee) and user (resident); owner has 3 committee contacts (brief). B2B committee decisions are slow and political (Opinion) | Narrow to clubhouse/sports sub-committees of 600+ flat communities; pilot in own community → 7 |
| Market size & growth | 4 | Hyderabad sold ~44,885 homes in 2025, −23% YoY [C14]; the category is crowded and consolidated around 3 national players [C1] | Size the 600+ flat segment from Telangana RERA (CLARITY F-02) → stays 4–5 (niche) |
| Differentiation | 2 | As briefed, parity at best with free/cheap incumbents; differentiator test fails (COMPETITORS) | Reframe to fair-booking (ballots, no-show release, rules log) + ad-free; passes 4 of 5 questions, copyable → 5 |
| Feasibility for owner | 2 | Brief scope: 2 native apps + web admin + UPI + visitor passes ≈ 400–600 h (Estimate) vs ~100 h available (10 h × 10 weeks) | Web-only, booking-only, no in-app payments in v1 ≈ 70–90 h → 7 |
| Monetization | 4 | Brief: ₹15/flat/month. Incumbents: NBH free, ADDA Lite $0/unit, MyGate reported ₹20–50 (unverified) [C1][C12] | Price per community for the clubhouse budget (e.g. ₹2,500/month); get 1 paid LOI (T5) → 5–6 |
| Distribution & retention | 4 | Booking is weekly-ish for active residents, never for others; no gate-style daily hook; committee-by-committee sales | Committee-to-committee referrals across Hyderabad; WhatsApp-shareable booking links → 5 |
| Risk | 5 | Payments (aggregator rules, refunds, GST on fees unknown), DPDP for resident data, store review for payments | Defer payments; collect flat number + phone only; DPDP notice → 7 |
| **Weighted total** | **3.95/10** | 5×.20 + 6×.15 + 4×.10 + 2×.15 + 2×.15 + 4×.10 + 4×.10 + 5×.05 = 1.00+0.90+0.40+0.30+0.30+0.40+0.40+0.25 | **target after changes: 5.80/10** (6,7,4,5,7,5,5,7) |

Calibration: OWNER.md gives no OUTCOMES path and there's no `OUTCOMES-snapshot.md` in the project. The kit's `portfolio/OUTCOMES.md` was found but has no rows or calibration notes yet, so no score changed.

Verdict rule note: 3.95 is below the 5.5 Drop line, but the problem and audience are real and a credible fix exists, which is the definition of Pivot. As a **learning project** (UX designer learning to build with AI) the pivot MVP is a clear **Go**.

## 2. The strongest version of this idea
*(idea-champion, checked against the evidence)* ClubSlot is not a society app. It is **the fair way to book contested amenities** in large gated communities — the Saturday-evening badminton court, the party hall in Diwali week, summer pool lanes. A resident opens a link from the community WhatsApp group (no install), sees what's free in one screen, and books in under 30 seconds. For peak slots, booking isn't first-come-first-served — residents enter a weekly **ballot** that gives every flat a fair chance, with a cap per flat. If nobody checks in within 15 minutes, the slot is **released** to the waitlist. Every rule and every decision is visible in a **public rules log**, so the committee stops refereeing on WhatsApp. No ads, no phone numbers shown to neighbours.

It wins first in the owner's own 900-flat community, run hands-on by the owner (unfair advantage: insider, designer, trusted resident), then spreads committee-to-committee across Hyderabad. It sits *beside* MyGate/NBH (which keep the gate), not against them. Ceiling (honest): a niche tool for a few hundred large communities — a solid side income or a portfolio piece, not a venture-scale business, unless it becomes the amenity layer other platforms integrate.

Where the perspectives disagreed: the devil's advocate argues committees will simply switch on MyGate's booking caps instead; the champion argues caps don't solve peak-slot contention or no-shows. Evidence can't settle it yet → test T1/T2 (does the owner's community already have the module, and why isn't it used?).

## 3. Reality check
### Fatal flaws (must fix before building)
- **Scope vs capacity**: the briefed MVP (Android + iOS + web admin, UPI, notices, visitor passes, helpdesk) in 10 weeks at 10 h/week is not buildable by one light-coding owner, even with AI tools. → **fix:** one job, web-only, no payments in v1 (see §8 MVP cut).
- **"No competitors"**: the brief's positioning rests on a false premise; a committee will ask "why not MyGate?" in the first meeting. → **fix:** reposition on fair booking + ad-free, beside (not instead of) the gate app; prepare a one-slide answer.

### Serious risks
| Risk | Likelihood | Impact | Mitigation or test |
|---|---|---|---|
| Owner's community already has MyGate/NBH with booking — problem is configuration, not software | High | High | T1 audit; if so, offer to configure it (service) or pick a community without it |
| Committees won't pay for a single-job tool when all-in-one apps are free/cheap | High | High | T5 pricing LOI; price per community from clubhouse budget, not per flat |
| Residents won't adopt a second app/link next to the gate app | Medium | High | No-install web link; T3 concierge ballot measures participation |
| Payments: holding RWA money needs a payment-aggregator path; refunds/disputes; GST on amenity fees unknown | Medium | Medium | Defer payments; later use Razorpay Route to settle directly to RWA account [C15]; ask a CA (CLARITY F-05) |
| Incumbent copies ballots/no-show release in a quarter | Medium | Medium | Win on local trust and onboarding speed; consider integration partnership |
| Committee politics: a booking tool changes who gets the court; losers complain | Medium | Medium | Committee owns the rules; public rules log; pilot with committee vote |

### Weak assumptions in the brief
| Assumption (quoted) | Why it's shaky | How to verify | CLARITY id |
|---|---|---|---|
| "There are no competitors doing this." | MyGate, NBH, ADDA all ship it [C1][C2][C7][C11] | Done — false | A-01 (contradicted) |
| "20 communities signed, ₹1.5 lakh MRR" in 6 months | Needs ~10,000 flats at ₹15 (avg 500 flats × 20); 3 warm contacts today | T2 + T5; reset target to 3 pilots in 6 months | A-04 |
| "RWA pays ₹15/flat/month" | Competing with free (NBH) and bundled; no committee asked yet | T5 LOI | A-03 |
| Scope: "Android + iOS + web admin … UPI, notices, visitor passes, complaints" | 4–6× owner capacity; visitor passes = incumbents' core | Decision: cut (Q-03, Q-04) | Q-03 |
| "Launch in 10 weeks" | Only with the cut MVP | PLAN after approval | Q-08 |

## 4. Problem validation
- Evidence the problem is real: the owner's first-hand observation in a 900-flat community, weekly (brief). Incumbents built caps, prime slots, cancellation windows and blacklists [C2][C11] — they would not have built them without disputes and no-shows (Opinion, reasonable inference).
- Evidence against / unknowns: whether the owner's community already has a booking module unused (F-01); how many communities still book on WhatsApp (Unknown); whether disputes cluster on 2–3 amenities (Assumption A-02).
- Current workarounds and why people tolerate them: WhatsApp "first message wins" + security-desk register — free, everyone already uses WhatsApp, and the committee member who arbitrates is a volunteer whose pain is invisible to residents.

## 5. Users and market
### Segments
| Segment | Size estimate | Pain level | Willingness to pay | Reachability | Priority |
|---|---|---|---|---|---|
| Clubhouse/sports committees, 600+ flat communities, Hyderabad | Unknown (F-02) | High (contested amenities) | Unknown; clubhouse budgets exist (maintenance ₹3,000–6,000 per 2BHK/month [C13]) | Owner: 3 contacts + referrals | **1 (wedge)** |
| Active amenity users (players, party hosts) | Within the above | High at peak times | Low (residents expect free) | Via committee WhatsApp groups | 1 (users) |
| Small communities (< 200 flats) | Unknown | Low (few clashes) | Low | Hard | 3 |
| Facility management companies | Unknown | Medium | Medium | No access yet | 2 (later) |

### Personas
**Ravi, 41, sports secretary of the owner's community (volunteer)** — runs the badminton/tennis WhatsApp group; spends Friday nights settling "who booked first"; Android, good 4G; goal: stop being the referee; switch trigger: a tool the committee trusts that makes rules enforce themselves. Accessibility: none specific; time-poor.

**Lakshmi, 34, resident, IT professional, Tower B** — wants the Saturday 7 pm court twice a month; loses to the same early-messaging group; iPhone; goal: a fair chance; switch trigger: "I actually got a slot". Needs: quick one-handed booking, Telugu/English UI optional.

**Mr. Rao, 67, retired resident** — books the party hall for family events twice a year; uses WhatsApp but not many apps; goal: know the hall is his without asking the security desk; needs larger text (200 %), simple language, no app install, possibly Telugu.

### Market size
| Level | Definition | Estimate | Math & sources |
|---|---|---|---|
| TAM | Flats in Hyderabad gated communities | Unknown; ≥ ~225,000 flats sold since 2021 alone (Estimate) | ~45,000–58,000 sales/year [C14] × 5 years; older stock adds more. Verify via Telangana RERA (F-02) |
| SAM | Flats in 600+ flat communities with contested amenities and no working booking | Unknown — likely a minority given incumbents' reach (Opinion) | Needs F-01/F-02 |
| SOM (yr 1–2) | Communities the owner can sign | 3–8 communities ≈ 2,700–6,000 flats (Estimate) | 3 warm contacts + ~1 referral each; at ₹2,500/community/month = ₹7,500–20,000 MRR |

### Reaching the first 100 → 1,000 users
| Channel | Why this audience is there | Cost | Owner's access | First experiment |
|---|---|---|---|---|
| Owner's own community WhatsApp groups | All residents already there | ₹0 | Direct | T3 concierge ballot for Saturday courts |
| 3 committee contacts | Payers | ₹0 | Warm | T2 interviews + T5 LOI |
| Committee-to-committee referrals (Hyderabad RWA federations, Gachibowli/Kondapur clusters) | Committees talk to each other | Time | Indirect | Ask each pilot committee for 2 introductions |
| Sports coaches who run classes in clubhouses | They need reliable slots | ₹0 | Unknown | 2 coach interviews |

### Retention
Trigger: weekly ballot opens (WhatsApp share) → action: enter ballot / book in < 30 s → reward: "You got Saturday 7 pm" → investment: booking history, fair-share counter. Weekly for active players; the loop breaks if residents can still win by WhatsApp-ing the guard, so the committee must make ClubSlot the only valid record.

## 6. Competitive landscape (summary — evidence in COMPETITORS.md)
| Leader | What they do well | Where users complain | Where this idea would win |
|---|---|---|---|
| MyGate | Gate + deep booking rules + payments; 27,000+ communities | Ad notifications, UI, support, data privacy [C3][C6] | Ad-free, focused, fair peak-slot ballots |
| NoBrokerHood | Free, simple booking flow | Number exposure; reschedule = cancel + rebook [C7][C9] | Fairness rules, privacy |
| ADDA | Prime slots, caps, accounting | Advanced clubhouse rules in a paid package [C11] | Simpler resident UX, ballot |
- Positioning map: single-job × committee-paid/no-ads is the open quadrant — possibly empty because committees want one app (hypothesis).
- Why hasn't anyone done this?: they have, as a module; the gate is the hook that gets installs. A booking-only product must win on fairness and trust, not features.

## 7. Differentiation and positioning
| Differentiator | Passes the 5-question test? | Defensibility | Keep / reframe / drop |
|---|---|---|---|
| All-in-one society app | No (parity; owner can't deliver) | None | Drop |
| Fair peak-slot ballot + no-show release + public rules log | 4/5 (fails "hard to copy") | Low alone; local trust + onboarding make it stick | Keep (lead) |
| Ad-free, private | 4/5; hard for MyGate given ad revenue [C5] | Medium | Keep (support) |
- **Positioning statement:** For clubhouse committees in large gated communities who are tired of WhatsApp booking fights, ClubSlot is a fair-booking tool that gives every flat a fair shot at peak slots. Unlike the booking module in all-in-one society apps, it is built only for contested amenities — ballots, no-show release and a public rules log — with no ads.
- **Wedge:** sports/clubhouse committees of 600+ flat Hyderabad communities × the 2–3 most contested amenities.
- **Owner's unfair advantages:** lives in a 900-flat community (pilot site and lived insight); 3 committee contacts; senior UX designer (can make a booking flow residents of every age can use — a real gap given complaints about incumbents' UI).

## 8. Strengthening plan
### Path to Go
Move from Pivot to Go when: (1) T1 shows the owner's community has no working booking module and ≥ 4 disputes/month; (2) T3 concierge ballot gets ≥ 40 % of regular court users participating for 4 weeks and the committee asks to continue; (3) at least one committee signs an LOI at a stated price (T5). With those, Problem → 7, Audience → 7, Monetization → 6, giving ≈ 6.2 (Go with changes) and a basis for Go after the pilot.

| Weak dimension (score) | Change | Evidence that would confirm it | Effort | Expected score after |
|---|---|---|---|---|
| Feasibility (2) | Web-only, booking-only MVP; no payments v1 | Plan fits ≤ 90 h | Low | 7 |
| Differentiation (2) | Reframe to fair booking + ad-free | 5 prototype users say "fairer than WhatsApp"; committee prefers it over enabling MyGate caps | Low | 5 |
| Problem (5) | Quantify disputes | WhatsApp history count; 10 interviews | Low | 6–7 |
| Monetization (4) | Per-community pricing | 1 LOI | Low | 5–6 |
| Distribution (4) | Referral asks per committee | 2 intros per pilot | Low | 5 |
| Market (4) | Accept niche; size segment | RERA count | Medium | 4–5 |

### Improvements ranked by impact ÷ effort
| # | Suggestion | Why it helps | Effort | Impact |
|---|---|---|---|---|
| 1 | Audit own community (T1) | Could invalidate or confirm everything in a week | XS | High |
| 2 | Concierge ballot with Google Forms (T3) before code | Tests the differentiator at ₹0 | S | High |
| 3 | Cut scope to web booking-only | Makes 10 weeks real | S | High |
| 4 | Price per community, from clubhouse budget | Avoids per-flat comparison with free apps | XS | Medium |
| 5 | Position beside MyGate, not against | Removes the committee's switching cost | XS | Medium |

### Recommended MVP cut
- Keep: amenity list + slot calendar with rules (duration, advance window, per-flat caps); booking + cancel; **peak-slot ballot**; **check-in + no-show auto-release** to waitlist; public rules log; committee admin (amenities, rules, blackout dates, residents by flat); phone OTP sign-in with flat verification by committee.
- Cut or defer: native iOS/Android apps (web link works from WhatsApp); UPI payments (fees noted on the booking, collected via existing maintenance bill); notices; visitor passes (incumbents' core — don't compete); complaints/helpdesk.

### Pivots worth considering
| Pivot | What changes | Why it might be stronger | What it gives up |
|---|---|---|---|
| A. Fair booking for contested amenities (recommended) | Single job, committee buyer, web | Real gap, buildable, testable in own community | All-in-one ambition |
| B. Setup service for existing apps | Owner configures MyGate/ADDA booking rules for committees for a fee | Zero build; uses UX skill; tests demand fast | No product; low ceiling |
| C. Clubhouse class & coach scheduling | Coaches book recurring slots, residents enrol | Coaches have revenue → may pay | Different user; more payments complexity |

## 9. Business model
- Pricing benchmarks (sourced): NBH "free with add-ons"; ADDA Lite $0/unit, packages by quote; MyGate reported ₹20–50/flat/month (unverified, second-hand); SocietynMore ₹5–15/flat; Codingclave ₹2,999/society/month [C1][C12].
- Unit economics sketch: price ₹2,500/community/month (Assumption; 900 flats ≈ ₹2.8/flat). Costs per community ≈ ₹150–300/month (hosting share + OTP SMS; Estimate). No store fees (web). Payments later: gateway fee + Route 0.1–0.25 % per transfer [C15].
- Path to the 6-month success metric: ₹1.5 L MRR at ₹2,500 needs 60 communities — not realistic. At ₹15/flat it needs ~10,000 flats (20 × 500). **Recommend resetting the 6-month goal** to: 1 live pilot in own community + 2 paying pilots + ≥ 40 % ballot participation (Q-05).

## 10. Feasibility, tools and cost for this owner
- Build complexity: **Medium** for the cut MVP (rules engine + ballot + auth + admin); **High** for the brief.
- Estimated MVP time at 10 h/week with AI tools: cut MVP ≈ 70–90 h → 8–9 weeks (Estimate); brief ≈ 400–600 h (Estimate).
### Provisional tools & technology (final choice in tech-stack)
| Need | Suggested tool | Why | Cost now → at 1,000 users |
|---|---|---|---|
| Design & prototyping | Figma + the HTML wireframes in `design/wireframes/` | Owner's home tool | ₹0 (existing) |
| App / site | Next.js responsive web app (PWA), one codebase for residents and admin | Opens from a WhatsApp link, no store review | ₹0 → Vercel Pro ~$20/month (Hobby plan is non-commercial) |
| Backend, auth, data | Supabase (Postgres + RLS + auth) | RLS fits per-community data isolation | ₹0 → ~$25/month Pro |
| Auth | Phone OTP via an Indian SMS provider (MSG91 or similar) through Supabase | Residents expect OTP | ~₹0.2–0.3/OTP (Estimate — verify) |
| AI (if any) | None in v1 | Not needed | ₹0 |
| Analytics & feedback | PostHog (IP anonymised) | Funnel for ballot participation | Free tier |
| Payments (if any) | Deferred; later Razorpay with Route to RWA account | Don't hold RWA money | Gateway fee + 0.1–0.25 % [C15] |
| Building with AI | Claude Code · Cursor · Codex (+ the kit) | Owner's tools | Existing subscriptions |
- Monthly running cost at 100 / 1,000 / 10,000 users (rough): ~₹0–500 / ~₹4,500–5,500 / ~₹10,000–15,000 (Estimate). Fits the ₹8,000/month budget up to ~1,000–3,000 users.
- Skills gaps & how to cover them: booking concurrency (no double booking under load) and ballot logic → use database constraints + well-tested server functions; ask a developer friend for a 1-hour review of the data model.

## 11. Legal, platform & ethical considerations
- DPDP Act 2023 + Rules 2025: resident phone + flat number are personal data → notice, purpose limitation, deletion; do not show phone numbers to other residents (a known incumbent complaint [C9]). Children: no under-18 accounts; parents book on their behalf.
- Payments: don't collect money on behalf of RWAs without a payment aggregator; GST treatment of amenity fees collected by RWAs is Unknown (F-05 — ask a CA).
- Fairness: ballot rules must be transparent and auditable; committee decides rules, product enforces them.
- Accessibility: older residents → WCAG 2.2 AA, 200 % text, simple language, Telugu later.

## 12. Cheapest validation tests (before building)
| Test | Assumption it tests (CLARITY id) | Success threshold | Kill criterion | Cost/time |
|---|---|---|---|---|
| T1 Own-community audit (app installed? module on? dispute count in 8 weeks of WhatsApp) | F-01, A-02 | No working booking module and ≥ 4 disputes/month | Booking module in use without disputes | ₹0 · 1 week |
| T2 3 committee + 10 resident interviews | A-02, A-03 | ≥ 2/3 committees want a pilot; ≥ 6/10 residents report losing a peak slot unfairly | 0/3 committees interested | ₹0 · 2 weeks |
| T3 Concierge ballot (Google Form + sheet) for Saturday courts, 4 weeks | A-05 | ≥ 40 % of regular court users enter; committee asks to continue | < 15 % participation | ₹0 · 4 weeks |
| T4 Prototype test with wireframes, 5 residents incl. 1 aged 60+ | Usability | ≥ 4/5 book a slot in < 60 s unaided | ≤ 2/5 | ₹0 · 1 week |
| T5 Pricing LOI at ₹2,500/community/month after free pilot | A-03 | ≥ 1 signed LOI | 0 of 3 | ₹0 · 2 weeks |

## 13. Clarity — questions to answer next
| Question | Blocks | How to find out |
|---|---|---|
| F-01 Does the owner's community already use MyGate/NBH/ADDA, with booking switched on? | Approval | Owner checks (T1) |
| Q-05 Is the goal business or learning-with-upside? (target reset) | Approval | Ask owner |
| A-03 Will a committee pay, and from which budget? | Approval | T2 + T5 |
| Q-03 Web-first PWA instead of native apps? (default: yes) | Design, PRD | Owner decision |
| Q-04 Payments out of v1? (default: yes) | PRD | Owner decision |
| F-02 How many 600+ flat communities in Hyderabad? | Market sizing | Telangana RERA project registry |

## 14. Sources
Competitor sources C1–C12 are listed in COMPETITORS.md (same numbering). Additional:
- C13 NoBrokerHood, "Apartment maintenance charges in Hyderabad" (2026-07-28) — https://www.nobrokerhood.com/blog/apartment-maintenance-charges-in-hyderabad/ — checked 2026-10-16
- C14 The Hans India, "Hyderabad housing sales nosedive 23% during 2025" (ANAROCK data; 2025-12-27) — https://www.thehansindia.com/business/hyderabad-housing-sales-nosedive-23-during-2025-1034112 — checked 2026-10-16
- C15 Razorpay Route — https://razorpay.com/route/ — checked 2026-10-16
- C5 Inc42 MyGate FY25 (2026-02-25) — https://inc42.com/buzz/mygate-trims-fy25-loss-by-61-to-₹15-4-cr/
- Not retrieved: Google Play listings (tool permission blocked) — see CLARITY F-03.

## Revision log
| Version | Date | What changed | Score changes & why |
|---|---|---|---|
| 1 | 2026-10-16 | First evaluation (owner unavailable; defaults in CLARITY) | — |
