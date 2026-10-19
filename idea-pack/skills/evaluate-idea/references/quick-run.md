# Quick run — the whole Quick Idea Pack in one file

<!-- Why this file exists: a Quick run used to read ~8 skill and reference files (~80k characters) before writing a word. This is the same method, condensed, so Quick reads one guide plus the templates it fills. Standard and Deep still use the full skills. If you change a rule in new-idea, evaluate-idea or product-kickoff, check whether it belongs here too. -->

**Use when** the owner asks for *quick* ("give me everything, quick", "is this worth a weekend?"). Output: brief, CLARITY, short EVALUATION, COMPETITORS Lite, ONE_PAGER, README index. No design direction or PRD.

## Read only these (each once)
- This file.
- Templates you fill: `../../new-idea/references/brief-template.md`, `../../new-idea/references/clarity-template.md`, `report-template-quick.md`, `competitors-lite.md`, and `../../idea-pack/templates/` (STATUS, DECISIONS, COSTS, ONE_PAGER, IDEA_PACK_README).
- Law: `../../product-standards/references/accessibility-law-summary.md`.
- `docs/product/OWNER.md` if it exists.
Nothing else — not the SKILL.md files, the question bank or the full standards.

## Budget
≤ 8 searches, ≤ 4 page reads (bare-link results: two unused searches buy one read; search in two batches) · ≤ 25 tool calls · caps: EVALUATION 2,000 words incl. tables, COMPETITORS 600, CLARITY 800, ONE_PAGER 550. Facts go to `docs/product/research/<topic>.md` as R1, R2… (snippet + URL + date); other docs cite the R-id. Out of budget → a CLARITY question, never a guess.

## Steps
1. **Set up.** Create `docs/product/`; copy STATUS, DECISIONS, COSTS from the kickoff templates. Say "Quick mode" in one line.
2. **Brief (phase 1).** Fill the brief from the pitch, §0 Idea card first (≤ 120 words). Tag every line [Pitch], [Owner], [Default], [Assumption] or [Research]. Make vague answers testable ("everyone" → "first 100 users, where?"). Give a provisional tech suggestion with a one-line reason (brief §7).
3. **Ask or default.** Owner present → one round of the 5 questions below, then continue. Owner unavailable (scheduled, "just do it", no reply) → write them to `INTERVIEW_ROUND1.md` (with an "About you" block if OWNER.md has gaps), take the recommended option for every **decision**, mark it `[Default]` and "default (unconfirmed)" in DECISIONS; leave every **fact** blank with a Q-id. STATUS Discovery → `Waiting for owner`.
   1. (fact) Describe a real moment someone feels this problem. How do they solve it today?
   2. (fact) Who exactly are the first 100 users, and where will you find them?
   3. (decision — recommend one) Goal: learning/portfolio · side income · business · social impact · personal tool.
   4. (decision) Platforms and launch markets for version 1.
   5. (fact) What do you have that others don't — access, skills, content, lived experience?
   About you (only if missing): hours/week, budget, skills, AI subscriptions.
4. **CLARITY.** Every open question: the phase it blocks, type (decision / fact / assumption), how to find out, a default only for decisions. Rank the assumptions the idea depends on.
5. **Research (phase 2).** Two search batches: competitors (top 3 direct + "doing nothing", one sourced complaint each — launch-market store or forum) and market (pricing benchmark, audience size input, any platform/payment/legal constraint). Write the research file.
6. **COMPETITORS Lite** from `competitors-lite.md`, including the 5-question differentiator test.
7. **Perspectives inline**, ≤ 5 lines each, as notes (not a section): evidence · strongest case against · strongest honest case for (best version) · who it excludes and which law applies. They feed EVALUATION §2–3.
8. **Score and write EVALUATION** from `report-template-quick.md` (rubric below). Score the idea **as briefed**; the strongest version is the target. Every score ≤ 6 gets "Raise it by…".
9. **One-pager and index** from the kickoff templates: verdict, *Defaults to confirm* (≤ 3, owner unavailable only), the idea in one line, problem, wedge, up against, strongest version, reality check, how to make it stronger, version 1 (provisional), tools and cost. README rows for design and PRD say "not yet — run Standard". STATUS 2a/2b → `Skipped (Quick mode)`.
10. **Check.** `python3 <kickoff or idea-pack folder>/scripts/check_idea_pack.py <project> --mode quick`; fix every FAIL. Don't re-read your own documents.
11. **Present** ≤ 10 lines: verdict · what's promising · top 3 risks · top 3 strengthening moves · cheapest test · the defaults to confirm. End: `Produced: … · Decision needed: … · Next: …`. Offer Standard.

## Scoring rubric (1–10 each)
| Dimension | Weight | Strong (7–10) looks like |
|---|---|---|
| Problem severity & frequency | 20% | painful, frequent, people already pay or hack workarounds |
| Audience clarity & reach | 15% | specific segment; owner can reach the first 100 cheaply |
| Market size & growth | 10% | large or growing segment |
| Differentiation | 15% | clearly better at one job users care about — only ≥ 7 if a differentiator passes the 5-question test |
| Feasibility for this owner | 15% | MVP Musts buildable in ≤ 8 weeks at the owner's hours |
| Monetization / sustainability | 10% | proven willingness to pay in comparable products |
| Distribution & retention | 10% | built-in habit, network, SEO or community loop |
| Risk (legal incl. accessibility and privacy law, platform, content rights, trust) | 5% | low or mitigated |

Weak (1–3): nice-to-have · "everyone" · tiny · same as free tools · skills/time missing · nobody pays · no reason to return · high unmitigated risk. **Weighted score** = Σ score × weight (show the sum).
- **Unknown deciding fact → that dimension ≤ 5**, evidence cell "Estimate — Q-xx", confidence one step lower.
- **Verdict (first that fits):** Go ≥ 7.0, no dimension ≤ 3, no fatal flaw · Go with changes 5.5–6.9 (or ≥ 7 with one fixable ≤ 3) · Drop/Park: fatal flaw without fix, or < 5.5 and no version reaches 5.5 · Pivot: < 5.5 but a real problem/audience and a specific pivot's target ≥ 5.5 (recommend one). State confidence Low/Medium/High.
- Learning or portfolio project → also score the portfolio lens (shows the owner's craft 30% · feasibility 25% · reach 20% · learning 15% · originality, crediting prior art 10%); personal tool → "Go as a personal tool" at ≥ 5.5.

## Accessibility and inclusion (EVALUATION §11)
Baseline everywhere: WCAG 2.2 AA, accessibility statement, barrier-feedback route, alternate formats on request. Who could be excluded — older adults (text scaling, no time pressure, no puzzle CAPTCHAs), low vision and screen-reader users, other languages and scripts, low literacy, low-end phones and slow networks, people who can't pay by card. Add the launch market's accessibility law and data-protection law from the summary; uncertain + high stakes → "confirm with a lawyer" + a Q-id. Leaving out a large share of the audience lowers Audience; an unmet legal duty is a Risk with a fix.

## Rules
- Honest coach, not judge: every weakness comes with a fix or a test. No hype, no cynicism.
- Never invent competitors, reviews, prices or numbers; "Unknown + how to find out" instead.
- Never write `Evaluation: APPROVED`; only the owner approves.
- Plain language — the owner is a senior UX designer, light coding.
