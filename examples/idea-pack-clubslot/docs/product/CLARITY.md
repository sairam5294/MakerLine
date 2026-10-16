# Clarity Log — ClubSlot

_Updated 2026-10-16 · Readiness: 0 of 5 blocking questions answered (owner unavailable this run; defaults applied where the question is a Decision)_

Every open question about the idea lives here until it is answered. Each one names the decision it blocks, so the owner can see at a glance what stands between the idea and the next step. Skills read and update this file; nothing is deleted, answered rows move to the bottom.

> Created by evaluate-idea (new-idea was skipped because PROJECT_BRIEF.md already existed and the owner asked for the whole Idea Pack in one go).

## Readiness by phase

| Phase | Ready? | Blocked by |
|---|---|---|
| Evaluation | yes (with defaults) | — |
| Design direction | yes (with defaults Q-03, Q-04) | — |
| Validation test | yes | T1–T5 in EVALUATION §12 |
| Approval | no | F-01, Q-05, A-03, Q-03, Q-04 |
| PRD (full) | no | Approval + Q-06, F-05 |

## Open questions

| ID | Question | Why it matters | Blocks | Type | How to find out | Owner | Default if unanswered |
|---|---|---|---|---|---|---|---|
| F-01 | Does the owner's community already use MyGate / NoBrokerHood / ADDA, and is its amenity booking switched on? | If yes and it works, the problem is configuration, not software | Approval | Fact | Owner checks app + asks committee (T1) | Owner | none — must be found out |
| Q-05 | Is ClubSlot a business (brief: 20 communities, ₹1.5 L MRR in 6 months) or a learning project with upside? | Target is unreachable as stated; changes verdict framing | Approval | Decision | Ask owner | Owner | Business, with the 6-month target reset to 1 own-community pilot + 2 paying pilots |
| Q-03 | Native Android + iOS apps, or a responsive web app (PWA) opened from WhatsApp? | Native triples build time and adds store review | Design, PRD, Approval | Decision | Ask owner | Owner | Web-first PWA; native later if pilots ask — fits 10 h/week |
| Q-04 | Are UPI payments in v1? | Payments add aggregator, refund and GST questions | PRD, Approval | Decision | Ask owner | Owner | No — show the fee on the booking; committee bills it with maintenance |
| Q-07 | Which modules stay out: notices, visitor passes, helpdesk? | Scope | PRD | Decision | Ask owner | Owner | All out of v1 (incumbents' core; not the differentiator) |
| Q-08 | Is "launch in 10 weeks" a hard date (event, committee meeting)? | Drives cut | Plan | Decision | Ask owner | Owner | Soft target; private pilot at ~9 weeks |
| Q-09 | Which visual direction (A Courtside calm / B Committee clear / C Festival warm)? | Design system after approval | Design system | Decision | Owner picks in DESIGN_DIRECTION §8 | Owner | A — Courtside calm |
| Q-10 | Ballot or first-come-first-served for peak slots — and who decides which slots are "peak"? | The differentiator | PRD | Decision | Committee workshop | Owner + committee | Ballot for committee-marked peak slots; FCFS for the rest |
| A-03 | Will a committee pay, how much, and from which budget? | Monetization | Approval | Assumption | T2 + T5 | Owner | none — must be found out |
| F-02 | How many 600+ flat gated communities are in Hyderabad? | Market sizing | Evaluation v2 | Fact | Telangana RERA project registry; federation lists | Claude | none — must be found out |
| F-03 | Google Play ratings, download counts and India-specific complaints for MyGate, NBH, ADDA | Competitive evidence (App Store US figures under-represent India/Android) | Evaluation v2 | Fact | Fetch Play listings (blocked this run) | Claude | none — must be found out |
| F-04 | MyGate's actual society price in Hyderabad (reported ₹20–50/flat, unverified) | Pricing benchmark | Evaluation v2 | Fact | Ask the 3 committees what they pay | Owner | none — must be found out |
| F-05 | GST / accounting treatment of amenity fees collected by an RWA through a platform | Payments later | PRD (full) | Fact | Ask a CA | Owner | none — must be found out |
| Q-06 | Language: English only at launch, or English + Telugu? | Older residents | PRD (full) | Decision | Ask owner; T4 with an older resident | Owner | English at launch; strings ready for Telugu |
| Q-11 | How does a resident prove they live in flat X? (committee approves, upload, OTP to registered number) | Trust, abuse | PRD | Decision | Committee | Owner | Committee approves each join request from the resident list |

**Type.** *Decision* — the owner chooses (goal, platform, scope, price). *Fact* — knowable about users or the market; never assume, find out. *Assumption* — a belief the idea depends on; it becomes a validation test.

## Assumptions the idea depends on (ranked by risk)

| ID | We believe… | If wrong, then… | Evidence so far | Test | Status |
|---|---|---|---|---|---|
| A-02 | Disputes concentrate on 2–3 contested amenities and existing apps' caps don't fix them | No differentiator → Drop | Owner observes weekly disputes; incumbents built caps/blacklists (suggests demand) | T1, T2 | Untested |
| A-03 | Committees will pay a single-job tool (~₹2,500/month) | No business | NBH free; ADDA Lite $0 | T5 | Untested |
| A-05 | Residents will use a ballot via a WhatsApp link | No adoption | None | T3 | Untested |
| A-04 | 20 communities in 6 months is reachable | Goal miss | 3 warm contacts only | T2 → referrals | Untested (likely wrong) |
| A-06 | Residents of all ages can book in < 60 s on the web | Exclusion of older residents | None | T4 | Untested |
| A-01 | "There are no competitors doing this" | Positioning collapses | MyGate, NBH, ADDA ship it (COMPETITORS) | Desk research | **Contradicted** |

## Answered

| ID | Answer | Source (owner, research link, test) | Date | Changed |
|---|---|---|---|---|
| A-01 | False — at least 3 established competitors offer amenity booking with rules and payments | COMPETITORS.md [1][2][7][11] | 2026-10-16 | Positioning → fair booking; brief claim dropped |
| O-01 | Owner profile: senior UX designer, light coding, ~10 h/week, ₹8,000/month, Hyderabad | PROJECT_BRIEF.md "Owner" (OWNER.md in the project is an unfilled template) | 2026-10-16 | Feasibility scored from the brief |
