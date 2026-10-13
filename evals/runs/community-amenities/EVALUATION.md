# Idea Evaluation Report — ClubSlot

_Version 1 · 2026-09-27 · Based on PROJECT_BRIEF v1_

> Eval-run note: there was no owner to answer questions, so assumptions are stated inline and marked **[Assumption]**. The refinement loop and STATUS/DECISIONS updates were skipped. Labels: **Evidence** = sourced fact, **Estimate** = my math on sourced inputs, **Opinion** = judgement.

## 1. Verdict
**Pivot** (as proposed: **Drop as a business**) — confidence **Medium**

The pain is real, but ClubSlot as scoped is a smaller copy of products that already do the same job at scale. Mygate says it runs 27,000+ communities and manages "2.4M+ amenity bookings annually", with UPI payments, a helpdesk and visitor management ([Mygate](https://mygate.com/community-management/)). ADDA and NoBrokerHood offer the same modules. The brief says "there are no competitors doing this", and that is false. The planned scope (Android + iOS + web admin + payments + visitor passes + helpdesk) also can't be built in 10 weeks at 10 h/week by someone with light coding skills. Build it only as a narrow, booking-only tool for communities that don't use or reject the incumbent super-apps, and test demand before writing code. It is a **Go as a learning project** if you cut it to a booking-only web app for your own community.

### Scorecard
| Dimension | Score | Why (evidence) |
|---|---|---|
| Problem severity & frequency | 5/10 | The owner sees disputes weekly in a 900-flat community (anecdote, n=1). Incumbents already solve it: Mygate reports 2.4M+ amenity bookings/yr ([Mygate](https://mygate.com/community-management/)). The pain is real where no app is used, but that group is shrinking. |
| Audience clarity & reach | 5/10 | The payer (RWA/FM) is clear and the owner knows people in 3 committees. But selling to RWAs is committee-driven B2B, and the incumbents have sales teams. |
| Market size & growth | 6/10 | Large and still growing: Hyderabad launched 58,335 units in 2024 and 43,260 in 2025 ([ANAROCK via MediaBrief](https://mediabrief.com/housing-sales-fall-14-year-on-year-in-2025-while-value-rises-6-across-top-7-cities-anarock/)). The count of Hyderabad gated communities with no app is **unknown**. |
| Differentiation | 2/10 | Mygate, ADDA, NoBrokerHood, Neighbium and Society Notebook already offer amenity booking plus payments. Society Notebook says it is "Lifetime free" ([Society Notebook](https://www.societynotebook.com/)). Nothing in the brief is 10× better. |
| Feasibility for owner | 3/10 | Two native apps + web admin + UPI payments + visitor passes + helpdesk, at ~10 h/week (~100 h in 10 weeks) with light coding. A booking-only PWA is feasible. |
| Monetization | 4/10 | RWAs do pay for this category: Mygate is quoted at ₹20–50/flat/month (weak Q&A source: [Techjockey](https://www.techjockey.com/question/20051/what-are-mygate-subscription-charges)). But free options exist, and ₹15/flat buys a product with fewer features. |
| Distribution & retention | 5/10 | RWA contracts are sticky once signed. Residents book only occasionally, so there is no strong habit loop. Word of mouth between RWAs exists, but sales cycles are slow. |
| Risk | 5/10 | Handling money needs a licensed payment aggregator, and building your own is out of reach (₹15 cr net worth: [Xflow](https://www.xflowpay.com/blog/payment-aggregators)). DPDP Rules were notified 14 Nov 2025 ([Wikipedia](https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025)). Handling resident data and disputes carries trust risk. |
| **Weighted total** | **4.25/10** | 5×0.20 + 5×0.15 + 6×0.10 + 2×0.15 + 3×0.15 + 4×0.10 + 5×0.10 + 5×0.05 = 1.00 + 0.75 + 0.60 + 0.30 + 0.45 + 0.40 + 0.50 + 0.25 = **4.25** |

Verdict logic: 4.25 < 5.5, and two dimensions score ≤ 3 (differentiation, feasibility). The rules give Drop for the idea as stated. Because the problem and the payer are real, I recommend **Pivot** (see §7) rather than a flat Drop.

## 2. Realistic critique
### Fatal flaws (fix before building)
- **No differentiation against funded incumbents that already ship the same feature.** Mygate (27,000+ communities, $67.2M raised; [Wikipedia](https://en.wikipedia.org/wiki/MyGate)), ADDA (25,000+ societies; [Play Store](https://play.google.com/store/apps/details?id=com.threefiveeight.adda&hl=en_US)) and NoBrokerHood (40 lakh households; [YourStory](https://yourstory.com/2023/08/nobrokerhood-streamlining-community-management)) all include amenity booking with payments. *Fix/test:* find out whether your 3 contact communities already use one of these apps and why booking still runs on WhatsApp. If they do, the pitch has to be "our booking module is better". If they don't, the pitch is "lighter/cheaper/private", and you need to know why they rejected the incumbents.
- **The scope can't be built with the owner's time and skills.** Native iOS + Android + web admin + payments + visitor passes + helpdesk is several products in one. Visitor management alone is the incumbents' core product and needs guard-side apps. *Fix:* cut to booking + rules + notices as a PWA (§7).

### Serious risks (at least 3)
| Risk | Likelihood | Impact | How to mitigate or test |
|---|---|---|---|
| Target communities already pay for Mygate/ADDA/NBH, so ClubSlot becomes a second app | High | High | Ask the 3 contact committees + 10 more RWAs which app they use and whether booking lives there. Kill if >70% already have an incumbent that includes booking. |
| RWA sales cycle is too slow for "20 communities in 6 months" (committees meet monthly and need votes) | High | High | Track days from first meeting to signed PO for the first 3. If it's over 60 days, reset the 6-month target. |
| Payments: money flow, refunds, disputes, 2.36% gateway fee (Razorpay 2% + GST; [Razorpay](https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/)) | Medium | High | Don't hold funds. Use a licensed PA that settles directly to the RWA's account, or start with "pay at desk/UPI QR" + mark-as-paid. |
| Unit economics at ₹15/flat can't pay for support (onboarding, WhatsApp support to RWAs, disputes) | Medium | Medium | Time-track support hours per community in the pilot. Price floor = support cost × 3. |
| Budget ₹8,000/mo is tight once you add Apple ₹8,300/yr, hosting and SMS/OTP ([Color Leaves](https://colorleaves.in/blog/app-publishing-cost-play-store-app-store-india-2026/)) | Medium | Medium | Launch as a PWA (no store fees) and use email/WhatsApp magic-link login. |
| Neutrality and trust: the app will be blamed in booking disputes and seen as taking sides with the committee | Medium | Medium | Rules are set by the RWA and every action is audit-logged. Publish the rules in-app. |

### Weak assumptions in the brief
- **"There are no competitors doing this."** → False. Mygate, ADDA, NoBrokerHood, Neighbium, Society Notebook and ApnaComplex all list facility/amenity booking (§5). → Verify: 30 minutes on the Play Store, plus asking RWAs which app they use.
- **"RWA pays ₹15/flat/month."** → Incumbent prices are not published (ADDA, NoBrokerHood and ApnaComplex all list "custom" or "on request": [SaaSworthy ADDA](https://www.saasworthy.com/product/adda), [SaaSworthy NBH](https://www.saasworthy.com/product/nobrokerhood/pricing), [ApnaComplex](https://www.apnacomplex.com/pricing)), and free options exist. → Verify: collect 5 real quotes from RWAs and ask for a written LOI at ₹15.
- **"20 communities, ₹1.5 lakh MRR in 6 months."** → ₹1.5L ÷ ₹15 = 10,000 paid flats, i.e. an average of 500 flats × 20 communities. That means a signing roughly every week, by a part-time founder with 3 warm leads. → Verify: time to close the first 3.
- **"Launch in 10 weeks" with native iOS + Android + web + payments + visitor passes** → ~100 hours of total build time. → Verify: build a booking-only PWA first and measure your real velocity.
- **"Owner has contacts in 3 committees"** → Contacts are not commitments. → Verify: ask each for a pilot with a start date.

## 3. Problem validation
- **Evidence the problem is real (sourced):** Amenity booking is common enough that Mygate reports handling 2.4M+ bookings/yr ([Mygate](https://mygate.com/community-management/)). NoBrokerHood built revenue streams around amenity fees and classes held in society facilities ([YourStory](https://yourstory.com/2023/08/nobrokerhood-streamlining-community-management)). Clubhouse use is regulated enough that the 2025 Telangana High Court guidance addresses it (liquor and DJ permissions; [Telangana Tribune](https://www.telanganatribune.com/telangana-high-court-guidelines-for-gated-communities-explained/)).
- **Evidence against / unknowns:** The evidence above shows the problem is *already solved* in many communities. Unknown: what share of Hyderabad gated communities still book by WhatsApp/register, and why (cost, privacy, committee inertia, dislike of ad-heavy apps).
- **Current workarounds and why people tolerate them:** WhatsApp group + paper register at the security desk. They are free, everyone already uses them, and they need no committee vote. Double bookings are an occasional cost, not a daily one. Opinion: that inertia is ClubSlot's real competitor.

## 4. User base analysis
### Segments
| Segment | Size estimate | Pain level | Willingness to pay | Reachability | Priority |
|---|---|---|---|---|---|
| Mid-size gated communities (200–1,000 flats) with **no** society app | Unknown (see §4 market size) | Medium–High | Medium (RWA budget) | Medium: owner's 3 contacts + referrals | **1** |
| Communities on Mygate/ADDA/NBH but unhappy with booking/ads/cost | Unknown; NBH reviews mention forced ads ([Play Store](https://play.google.com/store/apps/details?id=com.app.nobrokerhood&hl=en_IN)) | Low–Medium | Low (switching cost) | Low | 3 |
| Small buildings (<100 flats) | Large count | Low (few amenities) | Very low (free tools exist) | Medium | 4 |
| Facility-management companies running many communities | Unknown | Medium | Higher (B2B) | Low (needs sales) | 2 (later) |

### Personas (2–3)
**Ravi, 52, RWA secretary (volunteer), 700-flat community in Gachibowli [Assumption]** — Retired banker who handles committee WhatsApp late at night. Goals: fewer fights and a clean audit trail for AGM questions. Frustrations: residents escalate booking clashes to him personally, and the paper register goes missing. Uses an Android phone and desktop Excel. Moment: two families both "booked" the party hall for the same Saturday and both call him. He would switch for something the committee can approve in one meeting, cheap, with no ads, that guards can use. Accessibility: larger text, simple Telugu/English UI.

**Anjali, 34, resident, IT professional** — Wants the badminton court at 7 am on weekdays. Frustration: slots are taken by informal "regulars", and she has no visibility. iPhone, good 4G/Wi-Fi. Would switch if she could see open slots and book in two taps, with fair rules like max 2 slots/week. She won't install another app if the community already uses Mygate.

**Suresh, 40, facility manager (outsourced FM company)** — Runs 3 communities, takes calls for bookings, and collects hall fees in cash/UPI. Wants reconciliation and no disputes. Would pay (via the FM company) for a multi-community dashboard.

### Market size
| Level | Definition | Estimate | Math & sources |
|---|---|---|---|
| TAM | Flats in Indian gated communities that pay for society software | **Unknown in total.** Floor: incumbents claim ~4M households (Mygate, [Play Store](https://play.google.com/store/apps/details?id=com.mygate.user&hl=en_IN&gl=US)) + 40 lakh (NBH, [YourStory](https://yourstory.com/2023/08/nobrokerhood-streamlining-community-management)) + 25,000 societies (ADDA). | Overlap between incumbents is unknown. If you use an illustrative ₹15/flat/month for 8M flats, that's ~₹144 cr/yr (**Estimate**, illustrative only). |
| SAM | Hyderabad gated communities with **no** society app and paid amenities, in English/Telugu | **Unknown — the key number to find.** Hyderabad supply proxy: 58,335 + 43,260 units launched in 2024–25 alone ([ANAROCK](https://mediabrief.com/housing-sales-fall-14-year-on-year-in-2025-while-value-rises-6-across-top-7-cities-anarock/)). | How to find out: list ~100 Hyderabad communities with 200+ flats (Telangana RERA / property portals), then call or ask RWAs which app they use. |
| SOM (yr 1–2) | Communities the owner can realistically sign part-time | **3–8 communities**, ~₹7.5k MRR each at 500 flats × ₹15 = **₹22k–60k MRR** | **Estimate:** 3 warm contacts at ~50–100% conversion, plus 0–5 referrals. That is well short of the ₹1.5L MRR goal. |

### Where they are & how to reach the first 100–1,000 users
- First 1,000 *residents* come from one pilot community: the owner's own 900 flats. The committee announces it on the existing WhatsApp group, and a QR code goes on the clubhouse door.
- The next communities come through RWA federations and apartment association WhatsApp/Facebook groups in Hyderabad, FM companies, and referrals from pilot secretaries. Assume each sale needs 2–4 meetings.

### Retention / habit analysis
- **Trigger:** a resident wants a court or hall → **Action:** open the link and book → **Reward:** a guaranteed slot with no argument → **Investment:** booking history and recurring slots.
- The weekly return is real only for sports courts and the pool (recurring slots). Party halls get booked a few times a year. The retention that matters is the **RWA contract**, which is sticky once rules and data are in the system.

## 5. Competitors & alternatives
| Name | Type | Strengths | Weaknesses (from reviews) | Price | Rating/scale |
|---|---|---|---|---|---|
| Mygate | Society super-app | Amenity booking with payment and cancellation policies, UPI maintenance, gate security, helpdesk | Notification handling, OTP issues for international numbers ([Play Store](https://play.google.com/store/apps/details?id=com.mygate.user&hl=en_IN&gl=US)) | Custom. Q&A cites ₹20–50/flat/mo (unverified) | 4.7★ (1.02L reviews), 50L+ downloads, 27,000+ communities ([Mygate](https://mygate.com/community-management/)) |
| NoBrokerHood | Society super-app | Amenity booking with automatic % to society, classes and brand revenue shared with the society | Hidden payment-method charges, forced ads ([Play Store](https://play.google.com/store/apps/details?id=com.app.nobrokerhood&hl=en_IN)) | Custom ([SaaSworthy](https://www.saasworthy.com/product/nobrokerhood/pricing)) | 4.7★ (35.2K), 50L+ downloads, 40 lakh households |
| ADDA | Society ERP + app | Amenity reservations, accounting, DPDP compliance claims | Visitor approvals not showing for guards ([Play Store](https://play.google.com/store/apps/details?id=com.threefiveeight.adda&hl=en_US)) | Custom ([SaaSworthy](https://www.saasworthy.com/product/adda)) | 4.7★ (43.7K), 1M+ downloads, 25,000+ societies |
| Neighbium | Budget society app | Amenity booking with admin-defined slots, accounting | Slow payment processing, slow support ([Play Store](https://play.google.com/store/apps/details?id=com.neighbium.app&hl=en_IN)) | Not public | 3.4★ (744), 1M+ downloads |
| Society Notebook | Free society app | "Lifetime free", amenities and event booking, payments ([site](https://www.societynotebook.com/)) | Not verified | Free | Not verified |
| ApnaComplex | Society ERP | Facility management across plans, including a Free plan ([pricing](https://www.apnacomplex.com/pricing)) | Not verified | Free tier; paid on request | Not verified |
| WhatsApp group + paper register | Substitute | Free, universal, no vote needed | Double bookings, no audit trail | ₹0 | Default in the owner's community |
| Google Sheets/Forms/Calendar | DIY substitute | Free, a committee member can set it up in an hour | No payments, easy to edit or abuse | ₹0 | Unknown |

**Gap / opening:** Few options sit between WhatsApp and a full super-app. There may be room for a **lightweight, ad-free, booking-only tool** that a committee can adopt without replacing its gate/accounting system. It could also work as an add-on for communities whose incumbent's booking module goes unused. This gap is Opinion until the interviews in §11 confirm it.

## 6. Value add
- **Core value to users (in their words, hypothesised):** "No more fighting over the hall." "I can see which court slots are free." "The committee doesn't get blamed."
- **Differentiators (ranked) and how defensible each is:**
  1. *Booking-only simplicity with fairness rules* (quotas, lottery for peak slots, no-show penalties). Defensibility: low, since incumbents can copy it. But the UX quality, which is the owner's strength, can be a real edge.
  2. *No ads, privacy-first, no gate-hardware lock-in.* Defensibility: low–medium. NBH's ad complaints are evidence users want this.
  3. *Local, founder-led support in Hyderabad (Telugu/English).* Defensibility: medium at small scale, but doesn't scale.
- **Owner's unfair advantages:** 10 years in UX (booking UX and admin rule-setting are UX-heavy problems), lives in a 900-flat community (pilot + access), and knows people in 3 committees.

## 7. How to make it better
| Suggestion | Why | Effort | Impact |
|---|---|---|---|
| Cut to **booking + rules + notices** only. Drop visitor passes and helpdesk. | Visitor mgmt is the incumbents' core product and needs guard devices; helpdesk is commodity. | Lowers effort | High |
| **PWA instead of native iOS + Android** | Saves the ₹8,300/yr Apple fee and a 2nd codebase, and avoids store review | Low | High |
| **No money handling in v1**: "pay by UPI QR, admin marks paid". Later, Razorpay Route/split settlement direct to the RWA. | Avoids PA regulation and refund disputes (PA authorisation needs ₹15 cr net worth: [Xflow](https://www.xflowpay.com/blog/payment-aggregators)) | Low | Medium |
| Fairness features incumbents lack: peak-slot lottery, per-flat quotas, waitlist, no-show strikes, public audit log | This is the actual source of disputes, and something to be 10× better at | Medium | High |
| Position as "works alongside Mygate/ADDA" (a link from their notice board) | Removes the "second super-app" objection | Low | Medium |
| Price as a flat community fee (₹999–2,999/mo) or free for the pilot | ₹15/flat needs flat-count verification and scares committees; flat fees are easier to approve | Low | Medium |

- **Recommended positioning statement:** "For RWA committees tired of clubhouse and court booking fights, ClubSlot is an ad-free booking desk with fair-use rules and a public log. It is set up in a day and works with whatever gate app you already use."
- **Recommended MVP cut (what to remove):** native apps, UPI collection, visitor passes, complaints/helpdesk, multi-city. Keep: amenity catalog, slot calendar, rules (quota, advance window, blackout), approvals, notices, audit log, admin CSV export.
- **Possible pivots:**
  1. **Booking-only add-on** for communities without an app or with an unused booking module (recommended).
  2. **FM-company tool:** multi-community booking + fee reconciliation, sold to facility-management firms (fewer, larger buyers).
  3. **Amenity monetisation:** manage coaches/classes using society facilities, with revenue share to the RWA. Note that NBH already does this ([YourStory](https://yourstory.com/2023/08/nobrokerhood-streamlining-community-management)).

## 8. Business model check
- **Pricing benchmarks:** Incumbents don't publish prices (ADDA, NBH and ApnaComplex list custom or on request). One unverified Q&A source puts Mygate at ₹20–50/flat/mo ([Techjockey](https://www.techjockey.com/question/20051/what-are-mygate-subscription-charges)). Society Notebook is free, and ApnaComplex has a Free plan. Anchor: the RWA already pays for gate security. Booking-only is an add-on budget line, not a replacement.
- **Unit economics sketch (Estimate):** a 500-flat community at ₹15/flat = ₹7,500/mo. With a PWA, the extra hosting cost per community is near ₹0 on a free/low tier. The real cost is support time: if onboarding takes ~6 h and upkeep ~2 h/mo per community **[Assumption]**, 20 communities need ~40 h/mo, which is 4× the owner's available time. If payments go through Razorpay at 2% + GST = 2.36% ([Razorpay](https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/)), decide who absorbs it (pass it to the resident). Store fees are ~0 with a PWA and B2B invoicing.
- **Path to the 6-month success metric:** ₹1.5L MRR = 10,000 paid flats = 20 × 500-flat communities. Realistic 6-month outcome (**Estimate**): 2–5 communities, ₹15k–40k MRR. Revised success metric: 3 paying pilots, with 60%+ of bookings in pilot communities made through ClubSlot by month 6.

## 9. Feasibility & cost for this owner
- **Build complexity:** as briefed, **High** (2 native apps + admin + payments + visitor passes + helpdesk + multi-tenant). A booking-only PWA is **Low–Medium** (auth, calendar, rules engine, admin, multi-tenant).
- **Estimated MVP time at 10 h/week with AI tools:** booking-only PWA ~6–10 weeks (**Estimate**). The full brief scope is 6+ months and probably won't reach production quality for payments or security.
- **Monthly running cost at 100 / 1,000 / 10,000 users (rough, Estimate):** ~₹0–500 / ~₹1,500–3,000 / ~₹5,000–10,000 (managed Postgres/Supabase-class backend + hosting + email/WhatsApp notifications). Add ₹700/mo if you ship on iOS (₹8,300/yr) and ₹2,100 one-time for Google Play ([Color Leaves](https://colorleaves.in/blog/app-publishing-cost-play-store-app-store-india-2026/)). This fits in ₹8,000/mo only if you avoid SMS OTP at scale and native apps.
- **Skills gaps & how to cover them:** backend/multi-tenant data model and auth (use a BaaS like Supabase, with AI-assisted code), payments (defer), sales to RWAs (the owner must do this personally; it is the biggest gap), and security review before handling any money or ID data (pay for a one-off review).

## 10. Legal, platform & ethical considerations
- **Payments:** a non-bank entity collecting money on behalf of merchants needs RBI PA authorisation (₹15 cr net worth). Use a licensed PA with settlement directly to the RWA and never pool funds ([Xflow](https://www.xflowpay.com/blog/payment-aggregators); [RBI PA Directions 2025 text](https://www.fidcindia.org.in/wp-content/uploads/2025/09/RBI-PAYMENT-AGGREGATORS-DIRECTIONS-15-09-25.pdf)).
- **Data protection:** DPDP Rules 2025 were notified 14 Nov 2025 with phased obligations ([Wikipedia](https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025)). Resident names, flat numbers, phone numbers and visitor logs are personal data. You would be a processor for the RWA (or a fiduciary), so you need a data-processing agreement, consent notices, and deletion on request. Visitor passes add data about third parties, which is another reason to cut them.
- **GST:** RWA maintenance is GST-exempt up to ₹7,500/member/month where RWA turnover is ≤ ₹20 lakh. Above that, 18% applies (disputed scope: [TaxGuru](https://taxguru.in/goods-and-service-tax/gst-rwa-maintenance-charges-residents.html)). "Maintenance-linked fees" in the brief pulls the product into RWA tax matters. Keep ClubSlot as a booking tool, not a billing system. ClubSlot's own SaaS invoices need GST registration once its turnover crosses the threshold.
- **Clubhouse rules:** the Telangana HC guidance says liquor and DJ events need excise/police permissions ([Telangana Tribune](https://www.telanganatribune.com/telangana-high-court-guidelines-for-gated-communities-explained/)). Add a party-hall booking checkbox/disclaimer and let RWAs attach their rules.
- **Governance:** the Telangana Apartments Act 1987 governs common areas and associations ([India Code](https://www.indiacode.nic.in/bitstream/123456789/8604/1/act_29_of_1987.pdf)). RWAs set the rules and ClubSlot enforces them, so the app should never be the arbiter.
- **Ethics:** fairness in slot allocation, so committee members and regulars don't get priority. A transparent audit log helps.

## 11. Cheapest validation test (before building)
| Test | What it proves | Success threshold | Cost/time |
|---|---|---|---|
| Incumbent census: ask 20 Hyderabad RWAs (3 contacts + referrals) which app they use and how booking actually happens | Size of the "no-app / booking unused" segment | ≥ 8 of 20 book via WhatsApp/register **and** name booking as a top-3 pain. **Kill if** ≥ 14 of 20 already book in an incumbent app. | ₹0, 2 weeks |
| 5 RWA problem interviews (secretaries/FMs) | Willingness to pay and the decision process | ≥ 3 would take a paid pilot; you learn the approval steps | ₹0, 1–2 weeks |
| Concierge MVP in the owner's community: Google Calendar/Sheet + form + rules, run by the owner for 4 weeks | Residents use a structured system and disputes drop | ≥ 50% of bookings go through it by week 4, and disputes are logged down | ₹0, 4 weeks at ~2 h/week |
| Figma prototype of fairness rules shown to 3 committees | Differentiation over incumbents | 2 of 3 say "we'd switch from WhatsApp for this" and give a start date | ₹0, 1 week (the owner's core skill) |
| Paid-pilot LOI at a flat ₹999–1,999/mo | Real willingness to pay | ≥ 2 signed LOIs before writing production code | ₹0, 3–4 weeks |

**Kill criteria overall:** most target RWAs already have booking in an incumbent, **or** fewer than 2 LOIs after 20 conversations.

## 12. Questions to refine the brief
1. Does your own 900-flat community use Mygate/ADDA/NoBrokerHood today? If yes, why is booking still on WhatsApp? **[Assumption: no app, or the booking module is unused]**
2. What do your 3 contact committees use today, and have they seen a demo of an incumbent's booking module?
3. Is the goal really ₹1.5L MRR in 6 months, or would 3 paying pilots + a proven product count as success?
4. Will you accept a PWA-only v1, no payments and no visitor passes?
5. Who handles RWA sales and support at 10 h/week? Can you give more time, or bring in a co-founder for sales?
6. Is this also a learning/portfolio project? If so, the booking-only MVP is worth building even if the business stays small.

## 13. Sources
- Mygate feature & scale page — https://mygate.com/community-management/
- Mygate (Wikipedia: funding, scale, layoffs) — https://en.wikipedia.org/wiki/MyGate
- Mygate Play Store — https://play.google.com/store/apps/details?id=com.mygate.user&hl=en_IN&gl=US
- Mygate price Q&A (weak source) — https://www.techjockey.com/question/20051/what-are-mygate-subscription-charges
- SoftwareSuggest Mygate (quote-based pricing) — https://www.softwaresuggest.com/mygate
- NoBrokerHood Play Store — https://play.google.com/store/apps/details?id=com.app.nobrokerhood&hl=en_IN
- NoBrokerHood scale & revenue model (YourStory, Aug 2023) — https://yourstory.com/2023/08/nobrokerhood-streamlining-community-management
- NoBrokerHood pricing (SaaSworthy) — https://www.saasworthy.com/product/nobrokerhood/pricing
- ADDA Play Store — https://play.google.com/store/apps/details?id=com.threefiveeight.adda&hl=en_US
- ADDA pricing (SaaSworthy) — https://www.saasworthy.com/product/adda
- Neighbium Play Store — https://play.google.com/store/apps/details?id=com.neighbium.app&hl=en_IN
- Society Notebook — https://www.societynotebook.com/
- ApnaComplex pricing — https://www.apnacomplex.com/pricing
- ANAROCK Hyderabad sales/launches 2024–25 (via MediaBrief) — https://mediabrief.com/housing-sales-fall-14-year-on-year-in-2025-while-value-rises-6-across-top-7-cities-anarock/
- Razorpay pricing — https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/
- Payment aggregator rules (Xflow) — https://www.xflowpay.com/blog/payment-aggregators
- RBI PA Directions 2025 (PDF) — https://www.fidcindia.org.in/wp-content/uploads/2025/09/RBI-PAYMENT-AGGREGATORS-DIRECTIONS-15-09-25.pdf
- DPDP Rules 2025 — https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025
- GST on RWA maintenance (TaxGuru) — https://taxguru.in/goods-and-service-tax/gst-rwa-maintenance-charges-residents.html
- Telangana HC gated community guidelines — https://www.telanganatribune.com/telangana-high-court-guidelines-for-gated-communities-explained/
- Telangana Apartments Act 1987 — https://www.indiacode.nic.in/bitstream/123456789/8604/1/act_29_of_1987.pdf
- App store fees India 2026 (Color Leaves) — https://colorleaves.in/blog/app-publishing-cost-play-store-app-store-india-2026/

**Could not find / not verified:** the number of Hyderabad gated communities or how many use no society app; published per-flat prices for any incumbent; the market share split between Mygate, ADDA and NBH in Hyderabad.

## Revision log
| Version | Date | What changed | Score changes & why |
|---|---|---|---|
| 1 | 2026-09-27 | Initial evaluation (eval run, no owner input; assumptions stated) | — |
