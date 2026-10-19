# Evaluation Scoring Rubric

Score each dimension 1–10. Anchor to the descriptions; justify each score with evidence.

| Dimension | Weight | 1–3 (weak) | 4–6 (mixed) | 7–10 (strong) |
|---|---|---|---|---|
| Problem severity & frequency | 20% | Nice-to-have, rare | Real but infrequent or mild | Painful, frequent, people already pay/hack workarounds |
| Audience clarity & reach | 15% | "Everyone"; no channel to reach them | Clear segment, weak channels | Specific segment + owner can reach first 100 users cheaply |
| Market size & growth | 10% | Tiny or shrinking | Niche but stable | Large or fast-growing segment |
| Differentiation | 15% | Same as free alternatives | Better in one way that may not matter | Clear 10× better on something users care about, hard to copy |
| Feasibility for this owner | 15% | Needs skills/budget/time they don't have | Doable with significant help | Fits owner's skills; MVP Musts buildable in ≤ 8 weeks at the owner's hours |
| Monetization / sustainability | 10% | No one pays; ads-only in a low-ARPU segment | Plausible but unproven | Proven willingness to pay in comparable products |
| Distribution & retention | 10% | No reason to return; paid acquisition only | Some habit loop or channel | Built-in habit/network/SEO/community loop |
| Risk (legal incl. accessibility and privacy law in launch markets, platform, content rights incl. AI-generated content, trust) | 5% | High unmitigated risk | Manageable with effort | Low or well-mitigated |

**Weighted score** = Σ(score × weight). Show the calculation.

**Unknown deciding fact** (owner unavailable or research budget spent): score the dimension ≤ 5, write "Estimate — Q-xx" in its evidence cell, and lower the verdict's confidence one step. Never score high on a guess.

## Strengthening rule

Every dimension scored ≤ 6 gets a "Raise it by…" entry: the specific change (to audience, wedge, scope, model, channel or form), the evidence that would confirm it, and the realistic score after. Sum these into a **target weighted score**. The gap between today's score and the target is the strengthening plan; a Pivot or Drop must still show the best version worth testing, or say plainly that none was found and why.

Differentiation can only score ≥ 7 if at least one differentiator passes the 5-question test in `competitive-analysis.md` (users care, noticeably better, owner can deliver, explainable in one sentence; and either hard to copy or backed by something that makes it stick).

**Accessibility and inclusion.** A legal accessibility obligation the owner can't meet at launch (e.g. EU consumer service, public-sector buyer) is a serious risk with a fix in the strengthening plan. An idea that leaves out a large share of its own audience (older adults, a language, low-end phones) scores lower on Audience. Judge against the kit's global baseline (`../../product-standards/references/inclusion.md`), not only the launch market's law. An accessibility-led differentiator counts for Differentiation only if it passes the 5-question test.

## Verdict rules

Score the idea **as briefed**; the strongest version's score is the target. Apply the rules top to bottom and take the first that fits:

- **Go** — weighted ≥ 7.0 and no dimension ≤ 3 and no unresolved fatal flaw.
- **Go with changes** — weighted 5.5–6.9, or ≥ 7.0 with one dimension ≤ 3 that has a clear fix.
- **Drop / Park** — a fatal flaw (illegal, unbuildable, no reachable users) with no fix, or weighted < 5.5 and no version (target score) reaches 5.5.
- **Pivot** — weighted < 5.5 (or a dimension ≤ 3 without a clear fix) but the problem or audience is real and a specific pivot's target score reaches ≥ 5.5; propose 1–3 pivots and recommend one.
- Also state **confidence** (Low / Medium / High) based on evidence quality.

For learning/portfolio projects, say so and score a second lens — a "Drop" as a business can still be a "Go" as a portfolio project. Show both verdicts.

| Portfolio / learning lens | Weight |
|---|---|
| Shows the skill the owner wants to be known for (originality, depth, craft) | 30% |
| Feasibility for this owner in the stated time | 25% |
| Reach — will the right people see it (channels, community, launch plan) | 20% |
| Learning value (new skills the owner wants) | 15% |
| Differentiation from existing work in the space (credit prior art openly) | 10% |
Same verdict thresholds as the product lens.

## Market sizing method

- **TAM** (everyone who could conceivably have the problem) → **SAM** (reachable with your platform, language and geography) → **SOM** (realistic users in year 1–2 given your channels and budget).
- Prefer bottom-up: `reachable people × conversion rate × price` over top-down percentages. Cite sources for every input; mark assumptions.
