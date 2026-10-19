# Competitive Analysis — method and template

Output: `docs/product/COMPETITORS.md`. The evaluation summarises it in one section; this file holds the evidence. Re-use `docs/product/research/` (research-cache format) and cite every fact.

## Method

1. **Map the landscape in four rings.** Users never compare you only to look-alike apps.
   - **Direct** — same job, same audience, same form (the obvious apps).
   - **Indirect** — same job, different form or audience (a broader tool that also does this; an enterprise product used informally).
   - **Substitutes** — how people actually cope today: WhatsApp groups, spreadsheets, paper, YouTube, a person they pay or ask.
   - **Doing nothing** — tolerating the problem. Always a competitor; often the strongest.
   Aim for 3–6 direct, 2–4 indirect, 2–3 substitutes. "No competitors" is never a finding — it means the research isn't done.
2. **Profile the leaders** (top 3–5 by scale or mindshare): positioning in their own words, audience, price and model, scale signals (downloads, ratings count, funding, users claimed), strengths, and the **top 3 complaints mined from real reviews** (app stores, Reddit, G2, Play reviews — quote short phrases, link the source). Ratings: use the store for the launch market (e.g. the India App Store `apps.apple.com/in/…`) and state the country next to every rating. If a store page can't be fetched, search for it and open the result link, then try a public app tracker; otherwise write "Unknown" and add a CLARITY question. **B2B2C** (a payer different from the user, e.g. a committee pays, residents use): profile both — user complaints from app reviews, payer complaints from G2/Capterra, forums and sales conversations.
3. **Job matrix.** Rows = the 5–8 jobs or capabilities users care about most (from the brief and the review complaints, not a feature checklist). Columns = leaders + this idea. Cells: ● strong · ◐ partial · ○ missing · ? unknown. Add a row "Usable with a screen reader / large text / in {{language}}" when the audience needs it.. A matrix where this idea wins every row is a red flag, not a result.
4. **Positioning map.** Pick the two axes that matter most to the target user and on which competitors actually spread out (e.g. *simple ↔ powerful*, *self-serve ↔ done-for-you*, *generic ↔ made for this audience*, *free ↔ premium*). Place each competitor and the idea. The empty quadrant is a candidate opening — say whether it's empty because nobody wants it.
5. **Head-to-head for each leader.** Where they win · where we'd win · parity · why a user would switch · why they'd stay.
6. **Differentiator test.** For each claimed differentiator, answer all five:
   1. Do users care? — evidence: complaints, searches, interviews, willingness to pay.
   2. Is it noticeably better? — would a user see it in the first session? (aim for clearly better at one important job, not a bit better at many)
   3. Can the leader copy it in a quarter? — if yes, it's a feature, not a moat; say so.
   4. Can this owner deliver it? — skills, time, budget, content, access.
   5. Can it be explained in one sentence?
   Keep differentiators that pass 1, 2, 4 and 5; for those that fail 3, name what makes them stick (community, data, distribution, local knowledge, trust, speed, focus).
7. **Why hasn't anyone done this?** One honest paragraph: too small for incumbents, needs local or domain knowledge, regulation, they tried and stopped (find out why), or someone is doing it and research missed them.
8. **Opening and positioning.** The gap worth taking, the wedge (narrowest audience × job where this idea can be clearly best), and a positioning statement.

## Template — COMPETITORS.md

```markdown
# Competitive Analysis — {{working name}}
_Version {{n}} · {{date}} · Sources at the end; Evidence / Estimate / Opinion labelled_

## Summary
{{3–4 sentences: who leads, where the gap is, the wedge, and how defensible it is.}}

## Landscape
| Ring | Name | What it is | Audience | Price / model | Scale signal | Source |
|---|---|---|---|---|---|---|
| Direct | | | | | | |
| Indirect | | | | | | |
| Substitute | | | | | | |
| Doing nothing | Tolerating the problem | | | Free | | |

## Lite (Quick mode)
Required: the landscape table with the top 3 direct competitors + "doing nothing" (name, link, price, one-line positioning, one sourced complaint each) · the differentiator test · the wedge and positioning statement · sources. Skip: indirect and substitute rings beyond one line each, full leader profiles, job matrix, positioning map, head-to-head, "why hasn't anyone done this". Say "Lite — run Standard for the full analysis" at the top.

## Leader profiles
### {{Leader}}
- Positioning (their words):
- Strengths:
- Top complaints from reviews: "…" ([source](url)) · "…" · "…"
- Accessibility signals: statement · ACR/VPAT · app-store accessibility label · review mentions (screen reader, text size, older users):
- Where they're heading (recent launches, pricing changes):

## Job matrix
| Job / capability users care about | {{Leader A}} | {{Leader B}} | {{Substitute}} | **This idea** |
|---|---|---|---|---|
| | ● | ◐ | ○ | |

● strong · ◐ partial · ○ missing · ? unknown

## Positioning map
Axes: {{X: … ↔ …}} · {{Y: … ↔ …}} — chosen because {{why these matter to the user}}.
(Diagram: a 2×2 with each competitor placed; the idea marked.)

## Head-to-head
| Leader | They win on | We'd win on | Parity | Why a user would switch | Why they'd stay |
|---|---|---|---|---|---|

## Differentiator test
| Differentiator | Users care? (evidence) | Noticeably better? | Copyable in a quarter? | Owner can deliver? | One sentence? | Keep / reframe / drop |
|---|---|---|---|---|---|---|

## Why hasn't anyone done this?

## Opening, wedge and positioning
- Opening:
- Wedge (audience × job where we can be clearly best):
- Positioning: For {{audience}} who {{need}}, {{name}} is a {{category}} that {{key benefit}}. Unlike {{main alternative}}, it {{differentiator that passed the test}}.
- What would make the moat stronger over time:

## Sources
```

## Rules
- Real, named products with links; prices and ratings with the date checked. Never invent a competitor, a number or a review.
- Mark anything unverified as Unknown and add it to CLARITY.md with how to find out.
- Respect incumbents: say plainly what they do well. Users chose them for reasons.
