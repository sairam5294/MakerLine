# Idea Evaluation Report — ClubSlot

_Version 1 · 2026-10-19 · Based on PROJECT_BRIEF v1 · Competitors: COMPETITORS.md · Open questions: CLARITY.md · Research: `research/market.md` (R-ids) · Mode: Standard · Owner unavailable: every decision below marked **[Default]** is the recommended default, unconfirmed_

## 1. Verdict
**Pivot** — confidence **Medium-Low** (evidence is mostly vendor claims and one aggregator; no interviews yet)

Not like this. As briefed — Android + iOS + web admin, booking plus UPI payments plus notices plus visitor passes plus complaints, in ten weeks at ten hours a week, against "no competitors" — the idea scores 4.95/10: the scope is not buildable for this owner, and the competitive claim is wrong (ten-plus products already bundle amenity booking; the two leaders each claim 25,000+ communities, R2, R3). The problem underneath is real, frequent and visible in the owner's own 900-flat community every week. The recommended pivot — **a booking-only, fair-rules, no-install web service for mid-size Hyderabad communities still on WhatsApp and paper** — reaches a target of 6.4/10, which is "Go with changes" territory once two assumptions are tested.

**In one minute**
- What's genuinely promising: a painful, weekly, dispute-generating problem; a payer (the committee) who feels it directly; an owner with three committee contacts and senior design skills in a category whose leaders are criticised for ads and noise (R9).
- The biggest reality check: amenity booking is a free checkbox feature inside every incumbent (R2–R7). ClubSlot must win on *experience and fairness*, not on existence.
- The one change that most improves the odds: cut v1 to booking + rules + desk view, delivered as a web link shared in the WhatsApp group; drop visitor passes, complaints, notices and native apps.
- Next step (cheapest test that could change this verdict): five committee conversations with a price card (₹5 / ₹8 / ₹15 per flat) and the clickable wireframes — go if 3 of 5 would pilot and at least 2 accept ₹8/flat or ₹1,500/month.

### Scorecard
_Score = the idea as briefed · target = the strongest version (§2) after the changes._

| Dimension | Score | Why (evidence) | Raise it by… (→ target) |
|---|---|---|---|
| Problem severity & frequency (20%) | 7/10 | Weekly disputes observed by owner (brief); vendor claims 18% double-bookings and 71% of societies on WhatsApp (R13, weak) | Count disputes in 2 WhatsApp groups for 4 weeks (A-02) → 7 (confirm, not raise) |
| Audience clarity & reach (15%) | 6/10 | Clear segment (RWAs, residents) and 3 warm contacts; but residents vs committee needs blur and no channel beyond contacts | Narrow to committees of 100–500-flat communities on WhatsApp; recruit via the 3 contacts and Hyderabad RWA federations → 7 |
| Market size & growth (10%) | 5/10 | Hyderabad adds ~39k registered homes per half-year (R10) and keeps building gated stock; but a booking-only tool at ~₹1,500–4,000/community/month is a small niche | Add Bengaluru later; add utilisation reports committees pay more for → 5 (no change in yr 1) |
| Differentiation (15%) | 3/10 | Brief claims no competitors (contradicted, A-04); as scoped it is a smaller copy of the incumbents; nothing passes the 5-question test | Fair-rules booking + WhatsApp-link booking + no ads pass questions 1, 2, 4, 5 (COMPETITORS.md); stickiness via rule sets and history → 6 |
| Feasibility for owner (15%) | 3/10 | Two native apps + admin + payments + 4 more modules in 10 weeks at 10 h/week with light coding is not realistic (Opinion, from the kit's cost reference) | PWA + Supabase + Razorpay links, booking only, ~8 weeks of Musts → 7 |
| Monetization (10%) | 5/10 | ₹15/flat is at the top of the ₹3–15 band (R8) while leaders are free with ads (R3, R17); no willingness-to-pay evidence (Q-08) | ₹8/flat with ₹1,500 minimum, 3 pilots free for 3 months, price-card interviews → 6 |
| Distribution & retention (10%) | 5/10 | Committee-led sales via 3 contacts; residents return when they want a slot (weekly for courts, monthly for halls); no viral loop | WhatsApp share link = built-in distribution inside each community; committee-to-committee referral → 6 |
| Risk (5%) | 5/10 | DPDP consent/breach duties (R12); visitor data in the brief; payments handling; RPwD accessibility expectations (R19) | Drop visitor data from v1; minimum personal data (name, flat, phone); Razorpay hosted checkout → 6 |
| **Weighted total** | **4.95/10** | 7×.20 + 6×.15 + 5×.10 + 3×.15 + 3×.15 + 5×.10 + 5×.10 + 5×.05 = 1.40+0.90+0.50+0.45+0.45+0.50+0.50+0.25 | **target after changes: 6.40/10** (1.40+1.05+0.50+0.90+1.05+0.60+0.60+0.30) |

Calibration: **No calibration data yet** — `portfolio/OUTCOMES.md` not reachable from this project and no `OUTCOMES-snapshot.md` exists. Feasibility was judged from the brief's owner section because OWNER.md is the blank template (logged in DECISIONS.md).

## 2. The strongest version of this idea
*(idea-champion perspective)* If the owner makes smart choices, ClubSlot is not a society app. It is the quiet, fair booking desk for shared amenities — the thing a facility manager pins to the top of the community WhatsApp group. A resident taps the link, sees the badminton court's week at a glance, books a slot in three taps, pays the ₹100 fee by UPI if the community charges one, and gets a confirmation the guard can check at the desk. The rules the committee argued about for years — two court hours per flat per week, party hall bookable 30 days ahead with a deposit, no back-to-back hoarding — are enforced by the system, visibly and without a human having to be the bad guy. The committee pays because disputes stop landing in their inbox, and because the tool took one evening to set up rather than a platform migration.

The form is an installable web app, not two native apps: residents already open WhatsApp links (R13, weak but plausible), the owner can ship one codebase, and there is no store review in the critical path. The audience is the committees of mid-size (100–500 flat) Hyderabad communities that either never adopted a super-app or adopted one and left the booking module unused. The owner's unfair advantages are real: ten years of UX craft in a category whose leaders are criticised for ads, notification floods and paywalled features (R9); residency in a 900-flat community (a free, permanent research site); and three committee relationships, which in a committee-sold product is the whole top of the funnel.

- Honest ceiling (idea-champion): a Hyderabad-plus-Bengaluru niche business. At ₹8/flat/month and an average of 250 flats, one community is ~₹2,000/month; the brief's ₹1.5 lakh MRR needs ~75 communities, not 20. Fifty to a hundred communities over two to three years, run by one person with AI tools, is realistic if willingness to pay holds (A-01); a venture-scale outcome is not, because the leaders can copy any booking feature in a quarter. The way to lift the ceiling is a second job committees will pay more for — amenity utilisation and maintenance reports — not a return to the super-app scope.

## 3. Reality check
### Fatal flaws (must fix before building — or "none found")
- **Scope vs capacity.** The MVP as briefed (two native apps, admin, UPI, notices, visitor passes, complaints) is not buildable in 10 weeks at 10 h/week by an owner with light coding, even with AI tools. → **fix:** the pivot's cut (§8): booking + rules + desk view as a PWA; everything else deferred.
- **"There are no competitors."** The positioning and pricing in the brief rest on an absence that research contradicts (A-04). → **fix:** reposition against the incumbents' weak spots (COMPETITORS.md) and price inside the ₹3–15 band (R8).

### Serious risks (at least 3)
| Risk | Likelihood | Impact | Mitigation or test |
|---|---|---|---|
| Committees won't pay for one job when MyGate/NoBrokerHood give booking free (A-01) | High | Fatal to the business, not to a learning project | Price-card interviews with 5 committees (Q-08); if < 2 of 5 pay, pivot to free resident tool + paid committee reports |
| Parallel paper register survives; app becomes "one more place to check" (A-03) | High | Adoption collapses in month 2 | Pilot rule: desk accepts only app bookings; a desk/guard view that works on the guard's phone; count paper entries weekly |
| Incumbent copies "fair rules" once visible | Medium | Erases the feature differentiator | Accept it; compete on focus, speed, trust, design; build rule-set and history stickiness |
| DPDP obligations (consent notice, 72-h breach report, erasure) land during the first year (R12) | Medium | Compliance cost; reputational if mishandled | Minimum data (name, flat, phone); hosted checkout; plain-language consent; retention policy from day one |
| Payments: 2% + GST per transaction (R11) on ₹100 court fees looks like a tax to residents | Medium | Residents pay cash at the desk instead | Make fees optional per amenity; show the fee; consider "pay at desk, record in app" for small amounts |
| Owner burnout: 10 h/week across design, build, sales and support for 3 pilot communities | Medium | Launch slips past 10 weeks | One pilot first; support hours posted; AI tools for mechanical work |

### What would have to be true (devils-advocate)
- Committees see booking disputes as *their* problem worth ₹1,500+/month, not a resident annoyance (→ Q-08, test T1 in §12).
- Residents will use a web link instead of demanding a store app (→ T2 prototype test; A-02).
- The facility desk enforces app bookings within 4 weeks of pilot start (→ A-03, pilot metric).
- The owner can ship a working booking calendar with rules in ≤ 8 weeks of Musts (→ A-05, week-2 spike).
- At least one of the three contact communities is not locked into a super-app's booking module (→ Q-10).

### Perspectives disagree on…
- **Whether "no ads, no install" is a differentiator or a nicety.** The champion says residents' ad complaints (R9) show they care; the devil's advocate says committees, not residents, pay, and committees don't see the ads. Evidence that settles it: in the price-card interviews, ask committees what residents complain about; if ads/notifications come up unprompted in ≥ 2 of 5, keep it in the positioning.
- **Whether the pivot is too small to matter.** The market researcher notes the ₹3–15 band and free incumbents make the ceiling modest; the champion says modest is fine for a solo owner. Settled by the owner's goal (Business, ₹1.5 lakh MRR): at ₹8/flat that needs ~75 communities, so the 6-month target in the brief should be reset to 5–8 paying communities.

### Weak assumptions in the brief
| Assumption (quoted) | Why it's shaky | How to verify | CLARITY id |
|---|---|---|---|
| "There are no competitors doing this" | Ten-plus products list amenity booking (R2–R7) | Done — contradicted | A-04 |
| "RWA pays ₹15/flat/month" | Top of the ₹3–15 band (R8); leaders are free (R3, R17) | Price-card interviews | Q-03, Q-08 |
| "20 communities signed, ₹1.5 lakh MRR in 6 months" | 20 × 250 flats × ₹15 = ₹75k; needs 400-flat average or 40 communities | Re-set target after pricing test | Q-03 |
| "Android + iOS + web admin … in 10 weeks" | Three surfaces plus six modules at 10 h/week | Week-2 build spike | A-05 |
| "Bookings happen over WhatsApp groups and paper registers" | True in the owner's community; the share elsewhere is a vendor figure (R13) | Ask 5 facility managers | Q-05 |

## 4. Problem validation
- Evidence the problem is real (sourced): the owner's weekly observation in a 900-flat community (brief, first-hand); a vendor's cohort figure of 18% facility-booking double-bookings and 71% of societies running on WhatsApp (R13, vendor marketing, unlinked sources — Estimate); every incumbent ships a booking module, which signals demand (R2–R7 — Evidence of demand, not of pain).
- Evidence against / unknowns: no independent survey of booking disputes was found within budget; incumbents' booking modules may already solve it for the communities that adopted them (Q-10); NoBrokerHood and ADDA complaint data is missing (Q-06).
- Current workarounds and why people tolerate them: WhatsApp has near-universal reach and zero setup (R13); the paper register gives the guard something physical to check; disputes are intermittent, so each one feels like a one-off. People tolerate it because the alternative, a committee-wide platform migration, is a bigger fight than the booking fight.

## 5. Users and market
### Segments
| Segment | Size estimate | Pain level | Willingness to pay | Reachability | Priority |
|---|---|---|---|---|---|
| Committees / facility managers of 100–500-flat Hyderabad communities on WhatsApp/paper | Unknown (Q-05); Estimate: hundreds | High (they absorb disputes) | Unknown (Q-08) | 3 warm contacts; RWA federations | **1 — wedge** |
| Committees already on MyGate/NBH with an unused booking module | Unknown (Q-10) | Medium | Low (already paying or free) | Via same contacts | 2 |
| Residents who book courts weekly (young professionals, families with children) | Est. 20–40% of flats actively book (Opinion) | Medium–High when they lose a slot | Low (committee pays) | WhatsApp group link | Users, not payers |
| Large 900+-flat townships | Few per city | High but complex rules | Higher | Owner's own community | Pilot, then 1 |

### Personas (2–3)
**P-01 Srinivas, 52, RWA joint secretary (amenities)** — context: volunteer, runs a 320-flat community's clubhouse bookings from his phone between office hours; goals: fewer arguments, a record he can show in the AGM; frustrations: "first come first served" fights on WhatsApp, members who book the hall and don't show; devices: mid-range Android, patchy data in the basement office; moment: Sunday 9 pm, two families claim the party hall for the same Saturday; switch trigger: a tool he can set up himself in an evening and that doesn't need the whole society to migrate; accessibility: reading glasses, prefers large text, Telugu-first for formal notices.

**P-02 Priyanka, 31, resident, product manager** — context: books the badminton court twice a week; goals: see what's free and book in seconds; frustrations: scrolls 200 messages to find the booking thread, then finds the slot already taken; devices: iPhone, fast data; moment: 7:30 am booking for the evening; switch trigger: a link in the group that just works, no install; accessibility: none permanent; situational — one hand, walking.

**P-03 Ramesh, 44, facility manager / security supervisor** — context: employed by the association, keeps the paper register; goals: no blame when two families turn up; frustrations: residents say "I messaged the group"; devices: low-end Android, limited data; moment: a dispute at the desk at 6 pm; switch trigger: a screen that shows today's bookings clearly; accessibility: reads Telugu more comfortably than English; low-end phone.

### Market size
| Level | Definition | Estimate | Math & sources |
|---|---|---|---|
| TAM | Indian gated communities that could use a booking tool | Tens of thousands of communities | Leaders each claim ~25k communities (R2–R4); overlap unknown — Estimate |
| SAM | Hyderabad (then Bengaluru) communities of 100+ flats with shared amenities, reachable by a committee-sold web tool | **Unknown — Q-05** | Hyderabad registers ~39k homes per half-year (R10), most in apartment stock; a count of RWAs was not found. Placeholder for planning only: if 1,500–3,000 such communities exist (Opinion), SAM ≈ ₹3–7 crore/yr at ₹2,000/community/month |
| SOM (yr 1–2) | Communities the owner can sign through contacts and referrals | 8–25 communities | 3 contacts → 1–3 pilots → 2–3 referrals each per half-year (Estimate) = ₹16k–₹50k MRR at ₹2,000 avg; the brief's ₹1.5 lakh needs ~75 |

### Reaching the first 100 → 1,000 users
| Channel | Why this audience is there | Cost | Owner's access | First experiment |
|---|---|---|---|---|
| Owner's own community (900 flats) | Lived-in research site and pilot | ₹0 | Resident | Pilot with one amenity (courts) for 4 weeks |
| 3 committee contacts | Decision-makers | ₹0 | Warm | Price-card interviews, then 1 pilot |
| WhatsApp share link inside each community | Where residents already are (R13) | ₹0 | Via committee | Measure link → booking conversion |
| Hyderabad RWA federations / Facebook & WhatsApp RWA groups | Committees ask each other for tools | ₹0 | Unknown | Post a case study after pilot 1 |
| Facility-management companies serving multiple communities | One contract = many communities | Time | None yet | Ask the pilot's FM company for an intro |

### Retention
- Trigger: wanting a slot (weekly for courts, monthly for halls) → action: tap link, book → reward: a confirmed, fair slot and no argument → investment: the community's rule set, booking history, and the committee's AGM record live in ClubSlot. The loop breaks if the desk keeps a paper register (A-03), if the rules feel unfair to heavy users, or if the committee changes and the new one brings MyGate.

## 6. Competitive landscape (summary — evidence in COMPETITORS.md)
| Leader | What they do well | Where users complain | Where this idea would win |
|---|---|---|---|
| MyGate | Gate security at scale, dues, trust with guards (R2) | Ads, notification flood, paywalled features, support (R9) | Quiet, booking-only, no install |
| NoBrokerHood | Free entry, bundled services (R3) | Unknown (Q-06) | Focus and fairness rules |
| ADDA | Accounting, zero-fee UPI, committee tooling (R4) | Unknown (Q-06) | Resident experience, one-evening setup |
| WhatsApp + register | Reach, zero setup (R13) | Double bookings, no record | Confirmation, visibility, fairness |
- Positioning map: *super-app ↔ one job* × *free/ads ↔ committee pays*. "One job, committee pays" is empty; the test is whether it's empty because committees won't pay (A-01).
- Why hasn't anyone done this?: booking alone is too small for venture-funded gate apps; it is a checkbox inside their bundle (Opinion, COMPETITORS.md).

## 7. Differentiation and positioning
| Differentiator | Passes the 5-question test? | Defensibility | Keep / reframe / drop |
|---|---|---|---|
| Fair-rules booking (quotas, waitlist, auto-release, visible history) | Passes 1 (weak evidence), 2, 4, 5; fails 3 | Low; stickiness via rule sets + history | Keep |
| Book from a WhatsApp link, no install | Passes 1 (R13, weak), 2, 4, 5; fails 3 | Low; distribution advantage | Keep |
| No ads, booking-only notifications | Passes 1 (R9), 2, 4, 5; incumbents unlikely to copy (ads are their model) | Medium | Keep |
| Full suite as briefed | Fails 2 and 4 | None | Drop from v1 |
- **Positioning statement:** For committees of gated communities in Hyderabad who are tired of amenity-booking disputes, ClubSlot is a shared-amenity booking service that gives every flat a fair, confirmed slot from a WhatsApp link. Unlike MyGate or NoBrokerHood, it does one job, with no ads and no app to install.
- **Wedge:** committees of 100–500-flat Hyderabad communities on WhatsApp/paper × "stop the booking fights".
- **Owner's unfair advantages:** senior UX craft (make the booking flow obviously better in the first session); lives in a 900-flat community (continuous research and a pilot site); three committee contacts (the first three sales); AI tooling plus this kit (build at a designer's pace).

## 8. Strengthening plan
### Path to Go
The verdict moves from Pivot to Go with changes when (a) the scope is cut to the booking wedge, (b) two of five committees accept ₹8/flat or ₹1,500/month in a price-card conversation, and (c) a four-week pilot in one community shows the paper register retired and ≥ 60% of bookings made through the link. Those three results lift Feasibility to 7, Differentiation to 6 and Monetization to 6 — a target of 6.4.

| Weak dimension (score) | Change | Evidence that would confirm it | Effort | Expected score after |
|---|---|---|---|---|
| Differentiation (3) | Position against incumbents' ads/noise and unused booking modules; ship fair rules visibly | Committees mention disputes and ads unprompted; residents book via link in prototype test | M | 6 |
| Feasibility (3) | PWA + Supabase + Razorpay payment links; booking only; defer visitor/complaints/notices/native | Week-2 spike: calendar with one rule works end to end | M | 7 |
| Monetization (5) | ₹8/flat with ₹1,500 minimum; 3 pilots free for 3 months; annual billing option | 2 of 5 committees accept the card | S | 6 |
| Distribution & retention (5) | WhatsApp share link as the only entry; desk view for guards; monthly "fair-share" summary to residents | Link → booking conversion ≥ 30% in pilot | S | 6 |
| Audience (6) | Narrow to 100–500-flat communities; name the committee role (amenities secretary) as the buyer | 3 contacts confirm who decides | S | 7 |
| Risk (5) | Minimum data; hosted checkout; consent notice; no visitor data in v1 | Privacy checklist passes | S | 6 |

### Improvements ranked by impact ÷ effort
| # | Suggestion | Why it helps | Effort | Impact |
|---|---|---|---|---|
| 1 | Cut v1 to booking + rules + desk view | Makes it buildable and testable | S | Very high |
| 2 | Run 5 price-card interviews before any code | Tests the fatal assumption A-01 for ₹0 | S | Very high |
| 3 | Web link instead of native apps | One codebase, no store review, matches WhatsApp habit | S | High |
| 4 | Visible fairness ("your turns this month", waitlist order) | The differentiator residents see in session one | M | High |
| 5 | Desk view in Telugu with large text | Retires the paper register (A-03); inclusion baseline | S | High |
| 6 | Optional per-amenity fees; "pay at desk, record in app" for small amounts | Avoids the 2% + GST friction on tiny fees (R11) | S | Medium |
| 7 | Monthly committee summary (utilisation, no-shows) | Gives the payer a reason to renew; seeds the second paid job | M | Medium |
| 8 | Reset the 6-month target to 5–8 paying communities | Honest plan; avoids judging a good pilot as failure | — | Medium |

### Recommended MVP cut
- Keep (the core action + what makes the differentiator visible): community set-up by a committee member (amenities, hours, rules); resident sign-in by phone OTP + flat number; week view per amenity; book / cancel; quota, advance-window and waitlist rules with plain-language reasons; optional UPI fee via payment link; desk view (today's bookings, large text, Telugu); booking-only notifications via WhatsApp/SMS link.
- Cut or defer (and why): visitor passes (served by incumbents; sensitive personal data); complaints/helpdesk (different job); notices (WhatsApp does it); native iOS/Android (store review, 2× build); maintenance dues (ADDA/MyGate territory, accounting rules); multi-language beyond English + Telugu.
### Pivots worth considering (if relevant)
| Pivot | What changes | Why it might be stronger | What it gives up |
|---|---|---|---|
| **A — Booking-only wedge (recommended)** | Scope, platform, price; same audience | Buildable; tests the real differentiator; keeps the three contacts | The super-app vision; dues revenue |
| B — Free resident tool, paid committee reports | Residents free; committee pays for utilisation/no-show reports | Sidesteps A-01 if committees won't pay for booking | Slower revenue; needs data first |
| C — Plug-in for existing super-apps (API/partner) | Build the fair-rules engine; sell to Neighbium/SocietynMore-class vendors | Distribution via partners | Direct relationship; partner risk; needs B2B sales |

## 9. Business model
- Pricing benchmarks (sourced): market band ₹3–15/flat/month (R8); Neighbium premium from ₹10/flat (R6); SocietynMore ₹25/unit (R7); SocietyManagementApp ₹10/flat (R7); MyGate and NoBrokerHood unpublished / free-with-add-ons (R1, R3); ADDA Lite from ₹12/unit (R4).
- Unit economics sketch: price ₹8/flat/month, average community 250 flats → ₹2,000/month; hosting and messaging per community ≈ ₹100–300/month at this scale (Estimate: Supabase/Vercel free tiers initially, SMS/WhatsApp message costs); payment-link fees 2% + 18% GST are passed through on amenity fees (R11); no store fees for a PWA. Gross margin > 80% once past free tiers (Estimate). Sales cost = the owner's time, ~2–4 hours per community.
- Path to the 6-month success metric: as briefed (20 communities, ₹1.5 lakh MRR) is out of reach at any price in the band — 20 × 250 × ₹15 = ₹75k. Realistic 6-month target **[Default]**: 1 pilot live by week 10, 3 paying by month 4, 5–8 paying (₹10k–₹16k MRR) by month 6, with the owner's three contacts as the first three.

## 10. Feasibility, tools and cost for this owner
- Build complexity: **Medium** for the pivot (a calendar with rules is the hard part; payments via hosted links; one PWA). **High** as briefed.
- Estimated MVP time at 10 h/week with AI tools: ~8 weeks of Musts for the pivot (calendar + rules 3 weeks, auth/community set-up 1.5, desk view + notifications 1.5, payment links 1, accessibility and test 1) — Estimate; the week-2 spike (A-05) confirms it. 10 weeks includes the pilot start.
### Provisional tools & technology (final choice in tech-stack)
| Need | Suggested tool | Why | Cost now → at 1,000 users |
|---|---|---|---|
| Design & prototyping | These HTML wireframes → Figma (owner's tool) | Owner's strength; wireframes double as prototype | ₹0 → ₹0 (existing Figma seat) |
| App / site | Next.js or SvelteKit PWA on Vercel **[Default]** | One codebase, installable, no store review; AI tools know it well | ₹0 → ~₹1,700/month (Vercel Pro ~$20) |
| Backend, auth, data | Supabase (Postgres, RLS, phone OTP) **[Default]** | Row-level security per community; OTP auth; free tier | ₹0 → ~₹2,100/month (Pro ~$25) |
| AI (if any) | None in v1 | Not needed for booking; avoid ai.md obligations | ₹0 |
| Analytics & feedback | PostHog (free tier) + an in-app "report a problem" link | Funnel: link → view → book | ₹0 → ₹0 |
| Payments (if any) | Razorpay payment links / hosted checkout | UPI, no setup fee, 2% + GST (R11); keeps card data off our servers | ₹0 + 2.36% of fees |
| Messaging | SMS OTP via Supabase/MSG91; WhatsApp links (no Business API in v1) | Keeps cost and approval out of the critical path | ~₹0.2–0.3/SMS (Estimate) |
| Building with AI | Claude Code · Cursor · Codex (+ the kit) | Owner's existing tools | within the ₹8,000/month budget (Estimate: ₹2–5k) |
- Monthly running cost at 100 / 1,000 / 10,000 users (rough): ₹0–500 / ₹2,000–4,000 / ₹10,000–15,000 (Estimate; dominated by SMS and paid tiers). Fits the ₹8,000/month budget until roughly 5,000 users.
- Skills gaps & how to cover them: backend rules logic and RLS (use the kit's engineering-docs and architect agent; keep rules in one well-tested module); payments webhooks (Razorpay's hosted flow minimises this); sales conversations with committees (a one-page price card and the wireframes).

## 11. Accessibility, inclusion and compliance
_Not legal advice; sources: `accessibility-law.md` (verified 2026-10-19) and `research/market.md`. Accessibility-strategist perspective; 1 of its 4 searches used (R15)._
### Who could be excluded
| Group (permanent / temporary / situational) | Share of audience (source or estimate) | What would stop them | Design response |
|---|---|---|---|
| Older residents, low vision, reading glasses (permanent/temporary) | Estimate: a 900-flat community includes many retirees; no sourced figure | Small text, low contrast, dense calendars | Text to 200%, 4.5:1 contrast, one amenity per screen, large desk view |
| Telugu-first readers, incl. guards and domestic staff (situational/literacy) | Estimate: majority of security staff | English-only UI | English + Telugu strings in v1 **[Default]** (Q-11); icons always with text |
| Low-end Android, slow data in basements (situational) | Common for staff (P-03) | Heavy app, large bundles | PWA under 200 KB first load; works offline for "view my bookings" |
| Screen-reader users (permanent) | Estimate: small but present | Unlabelled calendar cells, colour-only availability | Each slot is a button with name, time, state; status in text |
| Motor impairment / one-handed use (permanent/situational) | P-02 situational | Drag-to-select, tiny targets | Tap-only, 44-pt targets, no drag |
| Tenants and non-owners | Varies by bylaw (Q-09) | Owner-only rules | Rules are the committee's choice; tenants are users by default |
| People without a smartphone | Estimate: small | App-only booking | Desk can book on behalf of a resident (desk view) |

### Obligations by launch market
| Market | Law / rule | Applies? (why) | Standard | Must do (statement, feedback route, alternate formats, ACR) | From |
|---|---|---|---|---|---|
| India | RPwD Act 2016; Rules 2017; mandatory ICT standards pending after *Rajive Raturi* (R19) | Likely — private service "establishment"; enforcement so far targets larger establishments; **confirm with a lawyer before selling to government-linked bodies** | GIGW 3.0 / IS 17802 (≈ WCAG 2.1 AA); kit floor WCAG 2.2 AA | Accessibility statement; feedback route (email + WhatsApp); alternate format on request; keep test records so an ACR can be produced if an RWA federation asks | Launch |
| India | DPDP Act 2023 + Rules 2025 (R12) | Yes — personal data of residents (name, phone, flat) | — | Plain-language itemised consent notice with withdrawal link; security safeguards, logs ≥ 1 year; breach notice "without delay" + 72-h report; erase when purpose ends (48-h notice); children's data not collected | Rules phase in over 18 months from 13 Nov 2025 — design for it now |
| India | Payments (RBI/NPCI via Razorpay) | Yes if amenity fees are collected | PCI handled by hosted checkout | Use hosted checkout; never store card/UPI credentials; refunds policy | Launch |
| India | Telangana Apartments Act 1987 / society registration (R14) | Indirect — the RWA's authority to charge fees and set rules | — | Rules are the committee's; app records who set them and when | Launch |
| App stores (later) | Apple accessibility labels; Play policies | Not in v1 (PWA); if native later, claim only tested features | — | Test evidence per label | Native release |
| Bengaluru (later) | Same national law; Karnataka Apartment Ownership Act | Same | Same | Same | Expansion |

### Competitors' accessibility
| Leader | Statement | ACR / VPAT | Store label / reviews | Gap we could use |
|---|---|---|---|---|
| MyGate | None found (R15) | None found | Unknown (R16) | Accessible, Telugu-capable booking and desk view |
| NoBrokerHood | None found (R15) | None found | Unknown | Same |
| ADDA | None found (R15) | None found | Unknown | Same |

### Accessibility as a strength
"Works for your parents and for the guard" — a desk view in Telugu with large text, and a booking flow usable with a screen reader — passes questions 2, 4 and 5 of the differentiator test; evidence for question 1 (do committees care?) is missing (Q-11). Treat it as a baseline that strengthens the pitch, not as the headline.

### Cheap now, expensive later
- Calendar slots as real buttons with text state (not a drawn grid); no drag-to-select; no colour-only availability; no time-limited checkout; no CAPTCHA (OTP instead); all strings in a translation file from day one; text never in images; the desk view designed for 200% text; consent and retention built into the data model.
### Ethics
- No dark patterns around fees or waitlists; rules and their reasons visible to every resident; no ranking by flat size or ownership; no selling resident data; no ads (the positioning depends on it); the desk can always override with a logged reason, so the system never traps a resident.

## 12. Cheapest validation tests (before building)
| Test | Assumption it tests (CLARITY id) | Success threshold | Kill criterion | Cost/time |
|---|---|---|---|---|
| T1 Price-card interviews with 5 committees (3 contacts + 2 referrals) | A-01, Q-03, Q-08 | ≥ 3 would pilot; ≥ 2 accept ₹8/flat or ₹1,500/month | 0 of 5 would pay anything → pivot B or learning project | 5 h, ₹0 |
| T2 Prototype test of the wireframes with 5 residents incl. 1 older adult and 1 screen-reader or large-text user | A-02, flow clarity | ≥ 4/5 book a slot unaided in < 2 min; ≥ 4/5 understand the fairness rule | < 3/5 complete | 4 h, ₹0 |
| T3 Count booking disputes in 2 WhatsApp groups for 4 weeks | A-02 | ≥ 2 disputes/week/community | < 1 per month → problem is milder than believed | 1 h/week, ₹0 |
| T4 Desk interview with 2 facility managers | A-03, Q-09 | Both would enforce app-only bookings with a desk view | Both insist on paper → design the desk view first or stop | 2 h |
| T5 Week-2 build spike: calendar + one rule end to end | A-05 | Working in ≤ 20 h | > 40 h → reduce rules or get help | 20 h |

## 13. Clarity — questions to answer next
| Question | Blocks | How to find out |
|---|---|---|
| Q-01 Accept the booking-only pivot? | Approval, design, PRD | Owner decision |
| Q-08 Will committees pay, and how much? | Approval | T1 price-card interviews |
| Q-02 PWA + WhatsApp links vs native apps? | Design, tech stack | Owner decision after T2 |
| Q-05 How many Hyderabad communities are on WhatsApp/paper? | Approval (sizing) | Desk research + 5 facility managers |
| Q-10 Is the pilot community already on a super-app? | Validation | Ask owner |
| Q-06 NoBrokerHood/ADDA complaints | Positioning | Read India store reviews, G2 |

## 14. Sources
- `research/market.md` R1–R19 (URLs there).
- Kit references: `product-standards/references/accessibility-law.md`, `inclusion.md`, `context-budget.md`.

## Revision log
| Version | Date | What changed | Score changes & why |
|---|---|---|---|
| 1 | 2026-10-19 | First evaluation, Standard mode, owner unavailable (defaults marked) | Baseline 4.95 as briefed; target 6.40 for pivot A |
