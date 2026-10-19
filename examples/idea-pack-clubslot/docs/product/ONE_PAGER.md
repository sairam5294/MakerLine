# ClubSlot — one-pager

_2026-10-16 · Verdict: **Pivot** (Medium confidence the brief as written won't work; Low for the pivot until tested) · Idea Pack index: `docs/product/README.md`_

**The idea in one line.** For residents of large gated communities who keep losing peak court and hall slots to WhatsApp races, ClubSlot is a fair-booking web app that gives every flat a fair shot at peak times. Unlike the booking module in all-in-one society apps, it uses ballots for peak slots, releases no-shows automatically and shows no ads.

**The problem.** Bookings run on WhatsApp groups and a paper register at the security desk; the owner sees double bookings and disputes weekly in a 900-flat community. Incumbents built caps, prime slots and no-show blacklists, so contention is common, but there's no resident evidence beyond the owner's own community yet.

**Who it's for first (the wedge).** Clubhouse and sports committees of 600+ flat communities in Hyderabad, starting with the owner's own community. The first 100 users are the regular court users there, reached through the sports secretary's WhatsApp group.

**Up against.** MyGate (27,000+ communities, ad-funded), NoBrokerHood (free with add-ons), ADDA (prime-slot rules) and WhatsApp plus doing nothing. The brief's "no competitors" is false. We win on fairness for contested slots, focus and no ads. They win on being installed already, on gate integration and on price (free).

**Strongest version.** A no-install fair-booking layer for the 2–3 most contested amenities. It sits beside the gate app rather than replacing it and is run hands-on by a trusted resident-designer.

**Reality check.**
- The briefed scope (2 native apps, web admin, UPI, visitor passes, helpdesk) is 4–6× what 10 h/week × 10 weeks allows.
- Committees may just switch on MyGate's booking caps, or pay nothing for a single-job tool.
- The 6-month goal (20 communities, ₹1.5 lakh MRR) needs about 10,000 flats from 3 warm contacts.

**How to make it stronger.**
1. Audit the owner's own community first.
2. Run a concierge ballot with Google Forms before writing code.
3. Cut to a web-only booking MVP without payments, priced per community (around ₹2,500/month) rather than ₹15/flat.

**Version 1.** Book a free slot within the committee's rules, with no double bookings. Musts: OTP join with roster match, rules-based booking and cancellation, peak-slot ballot, check-in with no-show release, and a committee rules editor. 12 screens · about 8–9 weeks at 10 h/week.

**Look and feel.** "Courtside calm": green-teal on warm white, large type, no ads, built for a 67-year-old on a budget Android. Wireframes are in `design/wireframes/index.html`.

**Tools and cost.** Next.js PWA + Supabase + an Indian SMS OTP provider, with payments later via Razorpay Route. About ₹4,500–5,500/month at 1,000 users (estimate), inside the ₹8,000 budget.

**Next test.** T1 is a 1-week audit of the owner's community: which app is installed, whether booking is switched on, and how many disputes there were in 8 weeks. Go if there's no working module and ≥ 4 disputes/month. Rethink if the existing booking module already works. After that, run the T3 concierge ballot: go at ≥ 40 % participation, stop below 15 %.

**Decisions needed from the owner.**
1. Accept the pivot (fair booking, web-first, no payments in v1) or keep the all-in-one brief.
2. Is this a business or learning with upside? If business, reset the 6-month target to 1 own pilot + 2 paying pilots.
3. Run T1–T3 before approval?
