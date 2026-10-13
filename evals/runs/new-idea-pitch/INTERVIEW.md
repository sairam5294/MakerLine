# Interview transcript: new-idea-pitch (first response + rounds 1 and 2)

_Skill: new-idea (Discovery). There is no critique in this phase; critique belongs to evaluate-idea._

---

## FIRST RESPONSE (to the owner)

Thanks, that's a clear pitch. Here it is in one line so we can check I have it right:

> **An Android-first order-management app for small home bakers in Hyderabad. It replaces the mess of WhatsApp and Instagram DMs so they stop losing orders, forgetting payments and double-booking. It's paid for with a monthly subscription.**

**Is that right?** If anything is off, correct me before we go on.

### What you've already told me (I won't ask again, just confirm)

| Topic | Your answer (pre-filled) | Brief section |
|---|---|---|
| Problem | Home bakers lose track of orders, forget payments and double-book | 2. Problem |
| Current workaround | Orders come in through WhatsApp and Instagram DMs | 2. Problem |
| Primary user | Small home bakers | 4. Audience |
| Launch market | Hyderabad | 8. Business |
| Platforms | Android first, maybe web later (because most bakers use Android) | 5. Scope |
| Monetization | Monthly subscription (leaning) | 8. Business |
| Design | You'll do it yourself as a UX designer | 6. Design / 7. Who builds |
| Unfair advantage (so far) | About 10 years as a professional UX designer, so no design cost and a fast prototype-to-test loop | 2. Why the owner |

I'll mark "monthly subscription" and "web later" as **leaning** rather than final. We'll confirm both when we reach business and scope.

### How this will go
We'll do **4 to 6 short rounds of 3 to 5 multiple-choice questions**, in this order: problem & goal → users → scope & platforms → design → technology → business → naming. Each question has a recommended option first. Questions marked **Optional** already have a default, so you can skip them. At the end I'll write `docs/product/PROJECT_BRIEF.md` and show you a short summary to confirm.

### Provisional technology direction (not final, and we'll revisit it)
From what you've said so far (Android first, web later, built mostly with AI tools by a designer with light coding experience), my **starting recommendation** is:

- **App:** React Native with **Expo** (TypeScript). It ships to Android now, and the same code can later run on iOS and as a web app. Claude, Cursor and Codex all work well with it.
- **Backend:** **Supabase**, which gives you a Postgres database, login (phone OTP suits Indian users), file storage for cake photos, and a free tier to start.
- **Design handoff:** Figma → a small token-based design system on NativeWind (Tailwind-style styling for React Native).
- **Alternatives we'll weigh later:** Flutter (strong on Android, but less web-friendly and a newer language to learn), or a web-first PWA (cheapest to build, but a weaker fit if "Android app on the phone" is what bakers expect).

The final stack is decided in the tech-stack step, after scope and budget are clear.

Let's start with round 1.

---

## ROUND 1: Problem & goal

**Q1.1 (Core): Which of these problems hurts bakers the most?** _(pre-filled from your pitch; I'm asking which one ranks first so the core feature targets it)_
- **Double-booking / overcommitting on a day's capacity (Recommended).** Trade-off: missing an order date hurts a baker's reputation most visibly, and an order calendar with daily capacity is a clear, demo-able core feature.
- **Forgotten or untracked payments (advance / balance).** Trade-off: direct money loss, but many bakers already rely on UPI screenshots, so the app has to beat that habit.
- **Order details lost in chats (flavour, size, message on cake, pickup time).** Trade-off: a very frequent irritation, but on its own it's closer to a notes app, so harder to charge for.
- **All three about equally.** Trade-off: honest, but it makes version 1 bigger. We'd still need to pick one "core action".

**Q1.2 (Core): Describe one real moment a baker felt this problem.** (Pick the closest option, or tell the story in "Other".)
- **I've seen it happen to a baker I know personally, and can describe it (Recommended).** Trade-off: a first-hand story is the best evidence and gives us a concrete test scenario.
- **I've heard about it from bakers, but not in detail.** Trade-off: fine for now. I'll add "interview 5 bakers" to the open questions.
- **It's an assumption from watching Instagram/WhatsApp ordering.** Trade-off: I'll label it as an assumption in the brief.

**Q1.3 (Core): Besides WhatsApp and Instagram DMs, what else do bakers use today?** (multi-select)
- **Paper notebook / diary (Recommended guess).** Trade-off: common and "free", and the thing the app must feel simpler than.
- **Google Forms / Google Sheets.** Trade-off: shows some bakers already want structure, so they're the easiest early adopters.
- **Generic tools (Dukaan, Instamojo, WhatsApp Business catalog).** Trade-off: these are the real alternatives your app will be compared against.
- **Nothing: memory and chat scroll-back only.** Trade-off: the biggest pain, but also the least habit of paying for tools.
- **Not sure.** Trade-off: added to open questions.

**Q1.4 (Core): What is the goal of this project for you?**
- **Side income that could grow into a business (Recommended).** Trade-off: fits a monthly subscription and keeps the pressure realistic while you validate.
- **Full business / startup from day one.** Trade-off: needs more time, budget and sales effort (onboarding bakers one by one).
- **Learning / portfolio (a shipped product as a UX designer).** Trade-off: lowest pressure, and the subscription becomes optional.
- **Community / social impact (help home bakers, many of them women-run businesses).** Trade-off: could mean a free tier or sponsorship instead of a subscription.

**Q1.5 (Core): In 6 months, which one number would tell you "keep going"?**
- **Paying bakers (e.g. 20 to 30 on a subscription) (Recommended).** Trade-off: proves the subscription works, which is the riskiest part of your plan.
- **Active bakers (e.g. 100 using it weekly, free or paid).** Trade-off: proves usefulness but not willingness to pay.
- **Orders managed per week through the app.** Trade-off: a strong engagement signal, but harder to set a target for yet.
- **Monthly revenue (₹ amount).** Trade-off: clearest financially, same idea as paying bakers.

_Vague answers get made testable. For example, "lots of bakers" becomes "what number of paying bakers in 6 months would make you continue?"_

---

## ASSUMED ANSWERS (round 1, simulated owner)

- **Q1.1:** Double-booking is the worst, with forgotten balance payments a close second.
- **Q1.2:** "My cousin bakes custom cakes from home in Kondapur. Last Diwali she accepted two big cake orders for the same evening from Instagram and WhatsApp, didn't notice until the day before, and had to cancel one. She also regularly forgets who has paid the balance."
- **Q1.3:** Paper notebook, plus Google Sheets for some. A few use a WhatsApp Business catalog.
- **Q1.4:** Side income that could grow into a business.
- **Q1.5:** Paying bakers, 25 on a subscription in 6 months.

**Captured unfair advantages (so far):** a 10-year UX designer (design in-house) + **direct access to a working home baker (cousin)** who can serve as the first user, test partner and bridge into her baker network. I'll ask about that network next.

---

## ROUND 2: Target audience

_Already confirmed: primary user = small home bakers in Hyderabad, mostly on Android; the baker pays (subscription). I won't re-ask these, only sharpen them._

**Q2.1 (Core): Which home bakers are version 1 for? (Let's make "small home bakers" specific.)**
- **Solo custom-cake / dessert bakers taking pre-orders (1 to 20 orders a week) (Recommended).** Trade-off: the most order-detail heavy and date-sensitive, so they feel double-booking the most. Matches your cousin, so easy to test.
- **Bakers doing daily or bulk items (cookies, breads, brownie boxes).** Trade-off: more volume and less customisation, so inventory and batch quantity matter more than a calendar.
- **Small teams (2 to 5 people, a home kitchen or cloud kitchen).** Trade-off: will pay more, but needs roles and sharing, so version 1 gets bigger.
- **All home food sellers (bakers, tiffin, pickles).** Trade-off: a wider market, but the product gets generic and loses the baker-specific edge.

**Q2.2 (Core): Who are the first 100 bakers, and where do they already spend time?** (multi-select, needed for distribution)
- **Instagram (their own baking pages, #hyderabadbakers, home-baker hashtags) (Recommended).** Trade-off: easy to find and DM, but cold outreach converts slowly.
- **WhatsApp / Facebook groups of home bakers and baking-class alumni.** Trade-off: high trust and word of mouth. Needs an insider, like your cousin, to get in.
- **Baking supply stores and classes in Hyderabad.** Trade-off: offline partnerships; slower, but a trusted referral.
- **Local events (flea markets, pop-ups, food festivals).** Trade-off: good for face-to-face demos, but only now and then.

Follow-up if needed: *"Of those first 100, how many could your cousin personally introduce you to?"*

**Q2.3 (Core): Does the baker's customer ever touch the product, or is it baker-only?**
- **Baker-only in version 1; customers keep ordering on WhatsApp/Instagram (Recommended).** Trade-off: the smallest build and no change in customer behaviour, but the baker still re-types order details.
- **Baker app + a shareable order-form link for customers (no customer app).** Trade-off: saves the baker typing and captures clean details, but it's a web page to build and customers must use it.
- **Full customer app / marketplace.** Trade-off: a very large scope, and it competes with Swiggy/Zomato-style discovery. Probably not version 1.

**Q2.4 (Optional): How comfortable are these bakers with technology?** _Default if skipped: "comfortable with WhatsApp, Instagram and UPI, but not with spreadsheets or complex apps"_
- **WhatsApp/Instagram/UPI-comfortable, not "app power users" (Recommended default).** Trade-off: design for very few steps, big tap targets and WhatsApp-like patterns.
- **Comfortable with Google Sheets / business apps.** Trade-off: we can offer richer features (reports, filters) earlier.
- **Mixed, including older bakers.** Trade-off: needs extra accessibility work (larger text, simpler flows).

**Q2.5 (Optional): Which languages at launch?** _Default if skipped: "English UI at launch, Telugu and Hindi later"_
- **English at launch, Telugu + Hindi later (Recommended default).** Trade-off: fastest to ship. Most Instagram-selling bakers read English, but we should build so translation can be added easily from the start.
- **English + Telugu at launch.** Trade-off: a warmer fit for local bakers, but more copy work and testing.
- **English + Telugu + Hindi at launch.** Trade-off: the widest reach, but the most effort before first users.

---

## Provisional technology note after round 2 (updated suggestion)

If the answers go as assumed (solo custom-cake bakers, baker-only version 1, WhatsApp-level tech comfort), the **Expo (React Native) + Supabase** recommendation still holds. Two points to note for the tech-stack step:
- If Q2.3 becomes "shareable order-form link", Expo's web output (or a small Next.js page on Vercel) can serve that link from the same Supabase backend.
- Build with translation support from day one (e.g. i18next), even if the UI launches English-only.

**Next round (3): Scope & platforms.** We'll confirm Android-first, choose the ONE core action (likely "add an order to a date, checked against my capacity"), and settle the version 1 features.
