<!-- Golden example from kit eval run 2026-09-27 (case: ai-todo). Read only when unsure of the quality bar — it is long. -->

# Idea Evaluation Report — TaskGenie

_Version 1 · 2026-09-27 · Based on PROJECT_BRIEF v1_

> **Run conditions:** No owner was available to answer questions, so assumptions are stated instead (below). Web research was done on 2026-09-27; every figure is labelled **Evidence** (sourced, numbered refs in §13), **Estimate** (math shown) or **Opinion**.

**Assumptions made in place of owner answers**
- A1. Owner is based in India (budget given in ₹); budget ₹10,000/month ≈ **US$104/month** at ₹95.8/USD [S21].
- A2. "Build a startup" means the owner wants a real business, not only a learning/portfolio project. (A learning-project reading is covered in §1.)
- A3. "AI" means calling a hosted LLM API (no in-house model).
- A4. "Launch in 4 weeks" at ~10 h/week = **~40 build hours** before launch.
- A5. No co-founder, no developer, no paid marketing beyond the ₹10k/month.

---

## 1. Verdict
**Pivot** (the brief as written scores as **Drop**) — confidence **High** for the as-written verdict, **Medium** for the pivot directions.

TaskGenie as specified is a feature-for-feature copy of a crowded, mature category (Todoist 30M+ users, TickTick, Motion, free Google Tasks / Microsoft To Do / Apple Reminders, and now ChatGPT's own scheduled tasks), aimed at "everyone", with a scope that cannot be built in 40 hours and a free-forever AI model the budget cannot pay for past a few thousand users. The underlying problem (overwhelm, forgetting) is real and the category retains well, so the owner should keep the problem but pick **one specific audience, one platform and one AI job-to-be-done** — or treat v1 openly as a **learning/portfolio project**, where a narrow version is a clear **Go**.

### Scorecard
| Dimension | Score | Why (evidence) |
|---|---|---|
| Problem severity & frequency | 5/10 | Real and daily, but already well served — free built-in apps cover "forgetting things" [S12]; people pay for Todoist/TickTick for organisation, not for the problem stated [S1][S3]. |
| Audience clarity & reach | 2/10 | Audience is "everyone … worldwide"; no named segment, community or channel in the brief. |
| Market size & growth | 7/10 | To-do app market ≈ US$1.38B (2026), 10.4% CAGR to 2032 [S6] — large and growing, but top-heavy with incumbents. |
| Differentiation | 2/10 | Every listed feature already exists: AI task breakdown + voice (Todoist Assist/Ramble) [S1][S15], habits + Pomodoro (TickTick) [S3], AI calendar scheduling (Motion) [S4], AI chat task entry (Tiimo) [S16]. |
| Feasibility for owner | 2/10 | 5+ platforms (web, iOS, Android, Watch, desktop) × 13 features in ~40 hours by a light coder; Google Play alone requires a 14-day closed test for new personal accounts [S9]. |
| Monetization | 3/10 | Willingness to pay is proven in the category (US$36–60/yr) [S1][S3][S13], but the brief is "free for everyone", and AI costs grow per user (§8). |
| Distribution & retention | 3/10 | Category retention is good (productivity D30 median 8%, best-in-class 12–18%) [S7], but the only acquisition plan is "go viral"; no loop, no channel. |
| Risk (legal, platform, trust) | 5/10 | Manageable: Gmail email-to-task needs restricted-scope verification + annual CASA assessment [S10]; calendar needs sensitive-scope review [S10]; task data sent to an LLM raises privacy questions. |
| **Weighted total** | **3.45/10** | 5×0.20 + 2×0.15 + 7×0.10 + 2×0.15 + 2×0.15 + 3×0.10 + 3×0.10 + 5×0.05 = 1.00 + 0.30 + 0.70 + 0.30 + 0.30 + 0.30 + 0.30 + 0.25 = **3.45** |

Rubric read: < 5.5 with four dimensions ≤ 3 → **Drop** as written. Because the problem is real and there are credible fixes (narrow segment, narrow scope), the verdict is **Pivot** rather than Drop. **As a learning project** (one platform, 3–4 features, no 1M-user goal): **Go** — it exercises auth, sync, notifications and LLM integration, all highly reusable skills.

---

## 2. Realistic critique

### Fatal flaws (fix before building)
- **F1. Scope is unbuildable for this owner in the time given.** ~40 hours vs. 5+ platform targets and 13 features, several of which (team collaboration, 3-way calendar sync, Slack/Notion/Jira integrations, Apple Watch) are each multi-week projects. Launching in 4 weeks is also blocked by process: Google Play's 12-tester/14-day closed test [S9] and Google OAuth verification for calendar (3–10 business days) and Gmail restricted scopes (~6 weeks + CASA) [S10]. **Fix:** one platform (web PWA or one mobile OS), 3–4 features, 10–12-week timeline.
- **F2. No reason to switch.** For "everyone", the default is a free app already on their phone (Google Tasks, Microsoft To Do, Apple Reminders — no paid tier) [S12], or Todoist (30M+ registered users, 4.8★ from 129K US ratings) [S2][S5]. "AI prioritisation" is now table stakes (Todoist Assist, Motion, Akiflow, Tiimo) [S4][S15][S16]. **Fix:** pick a segment whose needs incumbents ignore and win on that one thing (see §7 pivots).
- **F3. The 6-month goal is off by orders of magnitude.** 1M users in 182 days = **~5,500 installs/day** (Estimate). At a paid CPI of US$1.5–3.0 (APAC) [S14] that is **US$1.5M–3M**, versus a total 6-month budget of ~US$625. Virality is not a plan. **Fix:** replace with a learning-stage metric (e.g., 100 weekly active users in a niche with 25%+ D30 retention).

### Serious risks (at least 3)
| Risk | Likelihood | Impact | How to mitigate or test |
|---|---|---|---|
| R1. Free + AI costs outrun the ₹10k budget (AI ≈ US$0.015–0.08 per active user/month, §8) → at 10k MAU AI alone is US$150–800/mo | High | High | Cap AI calls on free tier; paywall the AI; use the cheapest capable model; test pricing on a landing page before building. |
| R2. "Go viral" fails; no organic channel → near-zero installs | High | High | Choose a segment with a reachable community the owner already belongs to (e.g., designers); pre-build a 300-person waitlist before coding. |
| R3. Users try once and return to their old app (switching cost: existing lists, habits) | High | High | Import from Todoist/Google Tasks; design for a daily trigger (morning plan notification); measure D7/D30 on a 50-user beta. |
| R4. Incumbents ship the same AI feature within months (Todoist already has Assist + Ramble in 38 languages) [S15] | High | Medium | Differentiate on audience-specific workflow and design, not on "AI" generally. |
| R5. Privacy/trust: tasks contain personal and work data sent to a third-party LLM; Gmail access triggers CASA [S10] | Medium | High | Avoid Gmail scopes in MVP (use forwarding-to-inbox email capture — Opinion); clear privacy copy; opt-in AI. |
| R6. LLM prioritisation is wrong or annoying (Motion users report "aggressive rescheduling" is disorienting) [S4] | Medium | Medium | Make AI suggest, never auto-move; one-tap accept/undo; test with 10 users. |
| R7. Owner time: 10 h/week sustains one product surface, not five platforms plus support | High | High | One platform; no teams/integrations until paying users ask. |

### Weak assumptions in the brief
- "**Everyone** — students, professionals, parents, businesses" → these groups have different jobs, tools and buyers (B2B teams buy per seat [S1]); no message can reach all → pick one segment and interview 10 people in it.
- "**AI-powered … makes people more productive**" → AI features are already in Todoist Pro at US$5/mo [S1][S15]; "AI" is not a differentiator in 2026 → test which specific AI job users value (brain-dump → plan? breaking tasks into steps? rescheduling?) with a Figma prototype.
- "**People have too many tasks and forget things**" → forgetting is solved by free reminders [S12]; the harder, less-served pain may be *starting* or *prioritising* (Tiimo's App-of-the-Year win for neurodivergent users suggests that [S16]) → verify via interviews.
- "**1 million users in 6 months**" → needs ~5.5k installs/day (§F3) → replace with retention-based goal.
- "**Go viral on social media**" → no content engine, audience or budget described → run a 4-week content test (e.g., 12 short videos) and measure waitlist sign-ups.
- "**Free for everyone; monetise later**" → LLM costs are per use, so free AI scales cost with growth (§8) → decide the paywall now.
- "**Launch in 4 weeks**" → Play Store testing alone takes ≥14 days [S9] → plan 10–12 weeks for a one-platform MVP.

---

## 3. Problem validation
- **Evidence the problem is real (sourced):** The category is large (US$1.38B, growing 10.4%/yr) [S6]; Todoist grew from 350K (2012) to 30M+ registered users (2024) [S5]; productivity apps show the strongest 12-month retention of any subscription category (14% at one year) and the highest 12-month LTV (US$46.97) [S13] — people keep using and paying for task tools.
- **Evidence against / unknowns:** The stated problem ("forget things") is well served by free tools [S12] and by ChatGPT scheduled tasks (3 active tasks free) [S11]. Unknown: which specific segment is under-served by existing tools — **how to find out:** 10 interviews per candidate segment + review mining of Todoist/TickTick 1–3★ reviews.
- **Current workarounds and why people tolerate them:** Built-in reminders / Google Tasks (free, zero setup) [S12]; paper and notes apps; WhatsApp "message yourself" (Opinion — common behaviour, not measured here); Todoist/TickTick for power users. People tolerate them because switching costs time and the gain from a new list app is marginal — top complaints in incumbents are price, discoverability and NLP date errors, not a missing feature category [S2].

---

## 4. User base analysis

### Segments
| Segment | Size estimate | Pain level | Willingness to pay | Reachability for this owner | Priority |
|---|---|---|---|---|---|
| Freelance / in-house designers juggling client tasks | Unknown — find via Behance/Dribbble/LinkedIn community sizes | Medium–High (Opinion) | Medium (tool-buying culture; Opinion) | **High** — owner is a senior UX designer | **1** |
| Neurodivergent adults (ADHD) needing "start/step" help | Unknown; proven niche — Tiimo was 2025 iPhone App of the Year at US$12/mo or US$54/yr [S16] | High | Proven (Tiimo pricing) [S16] | Low–Medium (competitive, sensitive audience) | 2 |
| Indian students (exam/study planning) | Unknown — needs data | Medium | Low (Opinion) | Medium (Instagram/Telegram) | 3 |
| Knowledge workers / professionals | Large (Todoist 30M+) [S5] | Medium | Proven (US$5–19/mo) [S1][S4] | Low — saturated, paid CPI US$2.5–5 in NA [S14] | 4 |
| Teams / businesses | Large | Medium | Proven per-seat [S1] | Very low (sales-led; needs collaboration features) | Drop for MVP |
| Parents / families | Unknown | Medium | Some (Any.do Family ~US$100/yr) [S8] | Low | Later |

### Personas (2–3)
**Ananya, 29, freelance product designer (Bengaluru)** — Juggles 3–4 clients; tasks arrive via email, Slack, Figma comments and WhatsApp. Goals: never miss a client revision, plan the week in 10 minutes on Monday. Frustrations: Todoist feels generic; copying tasks from five places. Devices: MacBook + Android, good connectivity. Moment: Monday 9:30 am, 23 unread Figma comments and a client call at 11. Would switch for: "paste everything → get this week's plan per client". Accessibility: none specific; dark mode, keyboard-first.

**Rahul, 34, product manager with ADHD (Pune)** — Knows what to do, struggles to start. Goals: turn a vague task into a first 10-minute step. Frustrations: long lists cause paralysis; apps nag. Devices: iPhone + work laptop. Moment: 3 pm, has avoided "write Q4 plan" for four days. Would switch for: calm, one-thing-at-a-time view with AI breakdown. Accessibility: reduced visual noise, gentle notifications, time visualisation.

**Meera, 20, engineering student (Hyderabad)** — Goals: plan revision across 6 subjects before exams. Frustrations: plans collapse after one missed day. Devices: mid-range Android, patchy data. Moment: 11 pm, realises exam is in 9 days. Would switch for: auto-rescheduling study plan that forgives missed days. Accessibility: works offline, low data, lightweight app.

### Market size
| Level | Definition | Estimate | Math & sources |
|---|---|---|---|
| TAM | Global spend on to-do list apps | **US$1.38B (2026)** → US$2.50B (2032) | Evidence, top-down analyst report [S6]. Bottom-up TAM for "everyone" is not meaningful. |
| SAM | Designers (pivot 1) who use a paid task tool, reachable in English online | **Unknown** | How to find out: sum sizes of target communities (LinkedIn/Behance/Dribbble groups, design Discords) × share paying for a task tool (survey 50 designers). |
| SOM (yr 1–2) | Realistic paying users with organic channels + ₹10k/mo | **~US$1.5k–5.5k/yr revenue** (Estimate) | 1,500–5,000 installs/yr (Estimate, organic) × 2.9% install-to-paid (9.8% install-to-trial × 29.5% trial-to-paid [S13]) × US$38/yr (median annual price [S13]) = 43–145 payers → **US$1.6k–5.5k/yr**. Paid scaling at US$1.5–3 CPI [S14] vs ~US$1.10 revenue/install (2.9% × US$38) is unprofitable in year 1. |

### Where they are & how to reach the first 100–1,000 users
- Designer pivot: the owner's own LinkedIn network and design communities (Opinion — owner's reach unknown; measure followers/groups); build-in-public posts showing the design process; Figma Community file (free template that links to the app); Product Hunt launch.
- ADHD pivot: Reddit r/ADHD-type communities and creators — high competition (Tiimo, Goblin Tools [S17]) and sensitive; only with a clear, careful angle.
- Avoid paid installs until D30 retention ≥ 15% (above productivity median of 8% [S7]).

### Retention / habit analysis
- **Trigger:** morning notification "Your plan for today (3 things)" and moments of overwhelm. **Action:** brain-dump or paste → AI turns it into today's 3 priorities. **Reward:** relief + a short, doable list; streak/completion view. **Investment:** tasks, client/project context and history live in the app, making the next plan better.
- Why they'd return weekly: a Monday planning ritual per client/project. Benchmarks: productivity D1 30% / D7 15% / D30 8% median [S7]; target ≥ 25% D30 in a niche beta.

---

## 5. Competitors & alternatives
| Name | Type | Strengths | Weaknesses (from reviews / reviewers) | Price | Rating/scale |
|---|---|---|---|---|---|
| Todoist | Direct | Mature, cross-platform (incl. watchOS, Linux), AI Assist + Ramble voice (38 languages) [S5][S15] | Price for basics, hard-to-find features, NLP date errors, no start dates/time-blocking [S2] | Free; Pro US$5/mo annual (US$7 monthly); Business US$8/user [S1] | 4.8★ (129K US ratings) [S2]; 30M+ registered users [S5] |
| TickTick | Direct | Habits + Pomodoro + calendar in one app [S3] | Habits/Pomodoro are Premium-only; minimal AI [S3][S15] | Free; US$4.99/mo or US$49.99/yr [S19] | 4.9★ (46K US ratings) [S19] |
| Motion | Direct (AI) | Auto-schedules tasks into calendar [S4] | No free plan, 7-day trial; "aggressive rescheduling" disorients users; no email task extraction [S4] | US$19/mo Pro AI; US$29/seat Business [S4] | n/a |
| Any.do | Direct | Tasks + calendar + family plan [S8] | AI only on paid tiers [S8] | Premium US$4.99/mo; Family ~US$100/yr [S8] | n/a |
| Tiimo | Niche (ADHD) | Visual planner, AI chat task entry, 2025 iPhone App of the Year [S16] | iOS-only; reviewer found it emoji-heavy with aggressive rating prompts [S16] | US$12/mo or US$54/yr [S16] | Apple award [S16] |
| Akiflow | Direct (power users) | Conversational AI assistant "Aki" [S15] | Expensive [S15] | US$19–34/mo [S15] | n/a |
| Google Tasks / Microsoft To Do / Apple Reminders | Free substitutes | Pre-installed or bundled; Gmail/Outlook/Calendar integration; no paywall [S12] | Basic; no AI planning [S12] | Free [S12] | Default for billions of devices (not quantified here) |
| ChatGPT scheduled tasks | AI substitute | Reminders and recurring tasks inside the AI people already use [S11] | Free/Go: 3 active tasks, limited scheduling [S11] | Free; paid plans raise limits [S11] | n/a |
| Goblin Tools (Magic ToDo) | Niche AI substitute | Free AI task breakdown for neurodivergent users [S17] | Reviewed as "brilliant but not enough" [S17] | Free web (app pricing not verified) | n/a |
| Paper / notes / WhatsApp self-chat / doing nothing | Substitute | Zero setup | No structure | Free | — |

**Gap / opening:** Not "AI to-do for everyone" — that space is saturated. Openings are **segment-specific workflows** incumbents treat generically: (a) client/project task intake for designers and freelancers (tasks scattered across Figma comments, email, WhatsApp); (b) calm "what do I do next" for people who struggle to start (proven by Tiimo, but competitive). Evidence for (a) is Opinion until interviews confirm it.

---

## 6. Value add
- **Core value to users (in their words — hypothesis to verify):** "Dump everything in, tell me the three things to do today."
- **Differentiators (ranked) and defensibility:**
  1. Workflow fit for one segment (e.g., designers' client work) — *moderately defensible* via community, templates and word of mouth.
  2. Design quality and calm UX — *weakly defensible*, but it is what won Tiimo App of the Year [S16] and it is the owner's core skill.
  3. AI prioritisation — *not defensible* (Todoist, Motion, Akiflow already ship it [S4][S15]).
- **Owner's unfair advantages:** ~10 years of UX design (can out-design generic tools, run interviews and usability tests cheaply); membership in designer communities (reach — to be quantified). Not an advantage: engineering capacity, marketing budget.

---

## 7. How to make it better
| Suggestion | Why | Effort | Impact |
|---|---|---|---|
| Pick one segment (recommend: designers/freelancers) | "Everyone" has no channel or message (§4) | Low | High |
| One platform: responsive web PWA first (or Android only) | Avoids Apple fee (US$99/yr ≈ ₹9.5k [S20]) and Play 14-day test [S9] for v1 | Low | High |
| Cut MVP to 4 features: quick capture (text + voice), AI "plan my day" from brain-dump, reminders, simple projects | Buildable in ~10–12 weeks at 10 h/wk (Estimate) | Medium | High |
| Drop from MVP: Apple Watch, desktop apps, team collaboration, Slack/Notion/Jira, gamification, habit tracker, Pomodoro, Outlook/Apple calendar | Each is a multi-week build and a feature incumbents already do well [S3][S5] | — | High (time saved) |
| Email-to-task via a forwarding address, not Gmail API | Avoids restricted-scope verification + annual CASA [S10] (Opinion on approach) | Low | Medium |
| Paywall AI from day one (free: capture + reminders; paid: AI planning) | Keeps AI cost ≤ revenue (§8); category WTP proven [S1][S3] | Low | High |
| Replace 1M-users goal with 100 WAU + ≥25% D30 in niche | Honest, measurable, within budget | Low | High |
| Import from Todoist / Google Tasks | Lowers switching cost (R3) | Medium | Medium |

- **Recommended positioning statement:** "For freelance designers who get tasks from five places, TaskGenie turns a messy brain-dump of client requests into a clear plan for today — unlike Todoist, it's built around clients and revisions, not generic lists." (Opinion — validate wording in interviews.)
- **Recommended MVP cut:** Web PWA · capture (text/voice) · AI "plan my day" · reminders · projects/clients. Everything else deferred.
- **Possible pivots:**
  1. **Designer/freelancer client-task planner** (best fit for owner's reach and skills).
  2. **Study planner for Indian exam students** that forgives missed days (reachable, but low WTP — validate).
  3. **Learning/portfolio project:** same narrow MVP, no revenue goal — explicitly a Go.

---

## 8. Business model check
- **Pricing benchmarks:** Todoist Pro US$5/mo annual [S1]; TickTick US$49.99/yr [S19]; Any.do US$4.99/mo [S8]; Tiimo US$54/yr [S16]; Motion US$19/mo [S4]; productivity median annual price US$38.42 [S13]. India-specific pricing: unknown — test ₹149–299/mo on landing page (Estimate range).
- **Unit economics sketch (Estimates, sources for inputs):**
  - LLM cost (GPT-5 mini at US$0.125/M input, US$1.00/M output tokens [S18]): light use (20 AI calls × 2k in + 500 out tokens) ≈ **US$0.015/user/mo**; chat-heavy use (100 messages × 3k in + 400 out) ≈ **US$0.08/user/mo**.
  - Store fees: Apple 15% under US$1M proceeds [S20b]; Apple membership US$99/yr [S20]; Google Play US$25 one-time [S20].
  - Revenue per install ≈ 2.9% × US$38 ≈ **US$1.10/yr** (from [S13] benchmarks) vs paid CPI US$1.5–3.0 APAC [S14] → paid acquisition is loss-making; organic only in year 1.
  - Free-forever at the brief's 1M-user goal: 1M × US$0.015–0.08 = **US$15k–80k/month** in AI alone (Estimate) — ~150–770× the budget.
- **Path to the 6-month success metric:** 1M users is not reachable (§F3). Realistic 6-month path: month 1–2 interviews + prototype; month 3–5 build narrow MVP; month 6 beta with 50–100 users, measure D30 and paid conversion.

---

## 9. Feasibility & cost for this owner
- **Build complexity:** **High** as written (multi-platform, real-time sync, team collaboration, 3 calendar providers, 3 third-party integrations, OAuth verifications). **Low–Medium** for the recommended one-platform MVP.
- **Estimated MVP time at 10 h/week with AI tools (Estimate):** as written: 12+ months, likely never finished solo. Recommended MVP: ~80–120 hours → **8–12 weeks**, plus 2–3 weeks beta.
- **Monthly running cost (Estimate, recommended MVP; ₹ at 95.8/USD [S21]):**

| Active users | Backend (Supabase) [S22] | AI (US$0.015–0.08/user) [S18] | Apple fee amortised (if iOS) [S20] | Total/month |
|---|---|---|---|---|
| 100 | US$0 (free: 50K MAU; pauses after 7 idle days) | US$1.5–8 | US$8.25 | **~US$10–16 (₹1k–1.6k)** |
| 1,000 | US$0–25 | US$15–80 | US$8.25 | **~US$23–113 (₹2.2k–10.8k)** |
| 10,000 | US$25+ (Pro) | US$150–800 | US$8.25 | **~US$185–835 (₹18k–80k)** — over budget unless AI is paid |

- **Skills gaps & how to cover them:** backend/auth/sync and push notifications (use Supabase + AI coding tools; keep to one platform); LLM prompt design and cost control (rate limits, caching); marketing/distribution (build-in-public in own design network); app-store submission (defer iOS). Strength: UX research and design — use it for validation first.

---

## 10. Legal, platform & ethical considerations
- **Google Play:** new personal developer accounts need 12 testers opted in for 14 continuous days before production [S9] — incompatible with a 4-week launch unless started early.
- **Google OAuth:** Calendar scopes need sensitive-scope verification (≈3–10 business days); Gmail read scopes are *restricted* → ~6-week verification and an annual CASA security assessment by an authorised lab [S10]. Avoid Gmail API in MVP.
- **Apple:** US$99/yr membership; 15% commission under US$1M proceeds [S20][S20b].
- **Privacy:** tasks can contain health, financial and client-confidential information; sending them to an LLM needs clear consent and a privacy policy. Check obligations under India's DPDP Act 2023 and GDPR if EU users (Opinion — not researched in detail here; verify before launch).
- **Ethics/trust:** AI must not silently move or delete tasks (Motion's rescheduling complaints [S4]); if targeting ADHD users, avoid medical claims and manipulative streaks/nags.

---

## 11. Cheapest validation test (before building)
| Test | What it proves | Success threshold | Cost/time |
|---|---|---|---|
| 10 interviews with freelance/in-house designers about how they track client tasks | Pain is real and under-served in this segment | ≥ 6/10 describe the scattered-intake pain unprompted and have tried ≥ 1 workaround | ₹0 · 2 weeks |
| Landing page + waitlist with price shown (₹199/mo or US$5/mo), shared in owner's network | Reach + willingness to pay | ≥ 300 visitors → ≥ 15% sign-up; ≥ 20 click "pre-order" | ≤ ₹2,000 · 2 weeks |
| Clickable Figma prototype of "brain-dump → today's plan", tested with 8 users | The AI job is valued and understandable | ≥ 6/8 say they'd use it weekly; SUS ≥ 75 | ₹0 · 1 week |
| Concierge MVP: users send their messy task list on WhatsApp/email; owner returns a plan using ChatGPT each morning for 2 weeks | Retention of the core value before code | ≥ 50% of 15 users still sending in week 2 | ₹0 · 2 weeks |

**Kill criteria:** fewer than 4/10 interviewees show the pain, OR < 5% landing-page sign-up after 300 visitors, OR < 30% of concierge users active in week 2 → park the idea (or keep as learning project only).

---

## 12. Questions to refine the brief
1. Is this primarily a business or a learning/portfolio project? (Changes the verdict from Pivot to Go.)
2. Which single segment do you personally belong to or can reach first 100 users in? How many followers/community members do you have there?
3. Which one AI job matters most: brain-dump → plan, break a task into steps, or auto-scheduling into the calendar?
4. Which one platform will you ship first (web PWA, Android or iOS)?
5. Would you charge from day one (e.g., ₹199/mo or US$5/mo) for AI features?
6. Can you extend the timeline to 10–12 weeks and replace "1M users" with a retention-based goal?

---

## 13. Sources
- [S1] Todoist pricing & AI features — https://www.morgen.so/blog-posts/todoist-pricing
- [S2] Todoist App Store ratings & reviews — https://apps.apple.com/us/app/todoist-to-do-list-calendar/id572688855?see-all=reviews
- [S3] TickTick pricing 2026 — https://vyneron.com/en/blog/ticktick-pricing-2026
- [S4] Motion pricing & user friction — https://get-alfred.ai/blog/motion-pricing
- [S5] Todoist (Wikipedia: users, platforms, history) — https://en.wikipedia.org/wiki/Todoist
- [S6] To-do list apps market forecast 2025–2032 — https://www.researchandmarkets.com/reports/6083601/to-do-list-apps-market-global-forecast
- [S7] Mobile app retention benchmarks (AppsFlyer data) — https://uxcam.com/blog/mobile-app-retention-benchmarks/
- [S8] Any.do pricing — https://lifestack.ai/blog/anydo-pricing
- [S9] Google Play testing requirements for new personal accounts — https://support.google.com/googleplay/android-developer/answer/14151465?hl=en
- [S10] Google OAuth verification & CASA — https://www.agenticfabriq.com/blog/google-oauth-verification-casa
- [S11] ChatGPT scheduled tasks — https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
- [S12] Todoist vs TickTick vs Microsoft To Do vs Google Tasks — https://www.taskspot.app/blog/todoist-vs-ticktick-vs-microsoft-to-do-vs-google-tasks
- [S13] Productivity app subscription benchmarks (Adapty) — https://adapty.io/blog/productivity-app-subscription-benchmarks/
- [S14] Cost per install benchmarks (Business of Apps) — https://www.businessofapps.com/ads/cpi/research/cost-per-install/
- [S15] Best AI task managers 2026 (Todoist Assist/Ramble, TickTick, Akiflow) — https://www.asianefficiency.com/task-management/best-ai-task-managers/
- [S16] 2025 App Store Award winners (Tiimo) — https://daringfireball.net/2025/12/2025_app_store_award_winners
- [S17] Goblin Tools review — https://thawly.ai/reviews/goblin-tools
- [S18] GPT-5 mini API pricing — https://pricepertoken.com/pricing-page/model/openai-gpt-5-mini
- [S19] TickTick App Store listing — https://apps.apple.com/us/app/ticktick-to-do-list-calendar/id626144601
- [S20] App Store publishing costs from India (Apple US$99/yr, Play US$25) — https://dev.to/preciousky_45d956626d31c3/what-it-actually-costs-to-publish-an-iphone-app-on-the-app-store-from-india-2026-numbers-1nmi
- [S20b] Apple App Store Small Business Program — https://developer.apple.com/app-store/small-business-program/
- [S21] USD/INR rate (95.82 on 2026-09-25) — https://tradingeconomics.com/india/currency
- [S22] Supabase pricing & free-tier limits — https://designrevision.com/blog/supabase-pricing

Not found / unknowns: India-specific CPI and to-do app pricing; size of designer communities reachable by owner; Goblin Tools app price; download counts for Google Tasks / Microsoft To Do.

---

## Revision log
| Version | Date | What changed | Score changes & why |
|---|---|---|---|
| 1 | 2026-09-27 | Initial evaluation from PROJECT_BRIEF v1 (no owner input; assumptions A1–A5 stated). Refinement loop and STATUS/DECISIONS updates skipped per run instructions. | Initial: 3.45/10 |
