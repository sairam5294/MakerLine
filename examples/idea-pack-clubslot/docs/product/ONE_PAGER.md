# ClubSlot — one-pager

**Defaults to confirm (owner unavailable):** D1 booking-only pivot (Q-01) · D2 PWA + WhatsApp links (Q-02) · D3 ₹8/flat/month, ₹1,500 minimum, 3 pilots free for 3 months (Q-03) · D4 direction A "Notice board" · D5 English + Telugu (Q-11) · D6 target reset to 5–8 paying communities.

_2026-10-19 · Verdict: **Pivot** (Medium-Low confidence) · Idea Pack index: `docs/product/README.md`_

**The idea in one line.** For committees of gated communities in Hyderabad who are tired of amenity-booking disputes, ClubSlot is a shared-amenity booking service that gives every flat a fair, confirmed slot from a WhatsApp link. Unlike MyGate or NoBrokerHood, it does one job, with no ads and no app to install.

**The problem.** Court, pool and hall bookings happen in WhatsApp threads and a paper register, so double bookings and disputes land on volunteer committee members weekly (owner's own 900-flat community). A vendor study claims 18% of facility bookings double-book and 71% of societies run on WhatsApp (R13, weak).

**Who it's for first (the wedge).** Committees of 100–500-flat Hyderabad communities still on WhatsApp/paper (or whose gate app's booking module sits unused). First 100 users: the owner's community plus the three committee contacts.

**Up against.** MyGate, NoBrokerHood, ADDA (each ~25k communities, booking bundled free or cheap) and WhatsApp + register — we win on fairness, quiet and no-install booking; they win on gate security, bundles and price (free with ads). "No competitors" in the brief is wrong.

**Strongest version.** The quiet, fair booking desk pinned to the top of the community WhatsApp group: three taps to a confirmed slot, rules enforced visibly, a desk view the guard reads in five seconds. Ceiling: a Hyderabad–Bengaluru niche of 50–100 communities, not a venture outcome.

**Reality check.** 1) Committees may not pay for one job when super-apps bundle it free (A-01). 2) The paper register may survive, making the app "one more place to check" (A-03). 3) As briefed (two native apps plus five modules in 10 weeks at 10 h/week) it is not buildable, and incumbents can copy any booking feature in a quarter.

**How to make it stronger.** Cut v1 to booking + rules + desk view as a web link; run five price-card interviews before writing code; make fairness visible in session one ("your turns this week") and the desk view Telugu-first at large text.

**Version 1.** Book a slot from a link · set-up with rules · OTP + flat sign-in · waitlist · confirmation with desk code · desk view · English + Telugu · 9 Must stories · 8 wireframed screens · ~8 weeks at 10 h/week, pilot by week 10.

**Look and feel.** A "Notice board": warm paper tones, one deep green, 17 px base type, slots as big buttons · wireframes: `design/wireframes/index.html`

**Tools and cost.** PWA (Next.js/SvelteKit) on Vercel + Supabase + Razorpay payment links + PostHog + SMS OTP · ~₹2,000–4,000 per month at 1,000 users; within the ₹8,000 budget.

**Next test.** Five committee conversations with a price card and the clickable wireframes — go if ≥ 3 would pilot and ≥ 2 accept ₹8/flat or ₹1,500/month; rethink if 0 of 5 would pay anything.

**Decisions needed from the owner.** Confirm D1–D3; name the pilot community and sponsor (Q-04); does the pilot already run a gate super-app (Q-10)?
