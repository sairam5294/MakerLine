# Quick run — the whole Quick Idea Pack in one file

<!-- Why: the Quick method condensed into one file. Mirror rule changes from new-idea, evaluate-idea and product-kickoff here. -->

**Use when** the owner says *quick*. Output in `docs/product/`: brief, CLARITY, EVALUATION, COMPETITORS Lite, ONE_PAGER, README, research file; no design direction or PRD.

## Budget (MUST)
- **Reads: 3 in all** — the start skill, this file, then one shell call (`Q` = this file's folder, `M` = launch markets as a regex, e.g. `India|EU`):
  `cat "$Q/report-template-quick.md" "$Q/competitors-lite.md"; grep -E "^\*\*(Baseline|Privacy|Solo)|^\| ($M)" "$Q/../../product-standards/references/accessibility-law-summary.md"; [ -f docs/product/OWNER.md ] && cat docs/product/OWNER.md || true`
  (no shell: read `report-template-quick.md`, `competitors-lite.md`, `../../product-standards/references/accessibility-law-summary.md`). Nothing else; never re-read your own documents.
- **≤ 12 tool calls:** 3 reads · **≤ 4 searches, sent in one turn; 0 page fetches by default** (≤ 1, step 2) · 1–2 writes ending with the checker · ≤ 1 fix (+ 1 question round if the owner is present).
- **Words incl. tables:** EVALUATION 1,400 · CLARITY 600 · brief 500 · COMPETITORS 450 · ONE_PAGER 450 · research 350.
- Out of budget → a CLARITY question, never a guess.

## Steps
1. **Ask or default.** Say "Quick mode". Owner present → one round of these 5. Unavailable (scheduled, "just do it", no reply) → write them to `docs/product/INTERVIEW_ROUND1.md`, take the recommended option for each **decision** (`[Default]`; "default (unconfirmed)" in DECISIONS), leave each **fact** open with a Q-id.
   1. (fact) A real moment someone feels this; how they cope today. 2. (fact) Who are the first 100 users, and where? 3. (decision) Goal: learning/portfolio · side income · business · impact · personal tool. 4. (decision) Platforms and launch markets for v1. 5. (fact) What do you have that others don't?
   Goal not stated by the owner or pitch → record "Assumed goal: business (unconfirmed)" as a Q-id in CLARITY; it decides the verdict (step 3).
   OWNER.md missing → ask hours/week, budget, skills, AI subscriptions and write it (unavailable: add them to INTERVIEW_ROUND1, fill OWNER.md from the pitch, *unconfirmed*); COSTS needs the budget.
2. **Research.** S1 `<category> app for <audience> <market>` → top 3 direct competitors. S2 all three in one query (`A vs B vs C reviews complaints`) → one sourced complaint each (launch-market store, Reddit, G2). S3 pricing benchmark + audience-size input. S4 only for a gap (platform/payment/legal constraint, missed competitor). Cite title + URL + "accessed <date>"; a result with no snippet is marked "(title only)". Fetch one page only when a must-have fact — a competitor's existence or price, or the launch-market law — can't be confirmed from results; never retry. Facts → `docs/product/research/<topic>.md` as `| R1 | accessed date | fact | title + URL |`; other docs cite R-ids.
3. **Think inline** (≤ 5 lines each, no section): evidence · case against · strongest honest case for · who it excludes, which law. Score the idea **as briefed**; the strongest version is the target; every score ≤ 6 gets "Raise it by…".
4. **Write all docs in one shell call** (heredocs; too big → two, brief + CLARITY + research first; no shell → one write per doc): `mkdir -p docs/product/research`, `cp` STATUS, DECISIONS, COSTS from `../../idea-pack/templates/` unread, then
   `perl -pi -e 's/^\| (1|2|✦) \|([^|]+)\| Not started \|/| $1 |$2| Waiting for owner |/; s/^\| (2a|2b) \|([^|]+)\| Not started \|/| $1 |$2| Skipped (Quick mode) |/; s/^Depth: .*/Depth: Quick/; s/^Next step:.*/Next step: owner reads ONE_PAGER.md, answers CLARITY.md, then decides./' docs/product/STATUS.md`
   (1 and 2 → `Done` only with no defaults or blocking facts left). Append rows with `>>`:
   DECISIONS: `| <date> | <decision> | <options considered> | <why; "default (unconfirmed)" if so> | <revisit when> |`
   COSTS: `| <YYYY-MM> | <tool/service> | <what for> | <amount> | <notes> |`, and set `- Monthly budget (from OWNER.md): <amount>` with `perl -pi`.
   Then write research, brief, CLARITY, COMPETITORS, EVALUATION, ONE_PAGER, README; end with `python3 "$Q/../../idea-pack/scripts/check_idea_pack.py" . --mode quick`.
5. **Fix** every FAIL and trim any length WARN in one call.
6. **Present** ≤ 10 lines: verdict · promising · top 3 risks · top 3 moves · cheapest test · defaults to confirm. End `Produced: … · Decision needed: … · Next: …`; offer Standard.

## Scoring rubric (1–10 each)
| Dimension | Weight | Strong (7–10) |
|---|---|---|
| Problem severity & frequency | 20% | painful, frequent, people pay or hack workarounds |
| Audience clarity & reach | 15% | specific segment; first 100 reachable cheaply |
| Market size & growth | 10% | large or growing |
| Differentiation | 15% | clearly better at one job; ≥ 7 only if a differentiator passes the 5-question test |
| Feasibility for this owner | 15% | MVP Musts in ≤ 8 weeks at the owner's hours |
| Monetization / sustainability | 10% | proven willingness to pay in comparables |
| Distribution & retention | 10% | habit, network, SEO or community loop |
| Risk (accessibility/privacy law, platform, content rights, trust) | 5% | low or mitigated |

Weak (1–3) is the opposite. **Weighted score** = Σ score × weight (show the sum).
- **Unknown deciding fact → that dimension ≤ 5**, evidence "Estimate — Q-xx", confidence one step lower.
- **Verdict (first that fits):** Go ≥ 7.0, no dimension ≤ 3, no fatal flaw · Go with changes 5.5–6.9 (or ≥ 7 with one fixable ≤ 3) · Drop/Park: fatal flaw without fix, or < 5.5 and no version reaches 5.5 · Pivot: < 5.5 but a real problem/audience and a named pivot reaching ≥ 5.5. Confidence Low/Medium/High.
- **Which lens sets the verdict (MUST):** the goal the owner **stated**. Learning/portfolio → portfolio lens (craft 30% · feasibility 25% · reach 20% · learning 15% · originality, crediting prior art 10%), same thresholds; personal tool → that lens, "Go as a personal tool" at ≥ 5.5. **No stated goal → the business score above decides**; never assume a goal that softens the verdict. Other lenses get one line in §1: "If this is a learning project: …".

## Accessibility and inclusion (EVALUATION §11)
Baseline: WCAG 2.2 AA, accessibility statement, barrier-feedback route, alternate formats on request. Who could be excluded: older adults (text scaling, no time pressure, no puzzle CAPTCHAs), low vision and screen-reader users, other languages and scripts, low literacy, low-end phones and slow networks, people who can't pay by card. Add the launch market's accessibility and data-protection law from the grep; uncertain + high stakes → "confirm with a lawyer" + a Q-id. Excluding a large share lowers Audience; an unmet legal duty is a Risk with a fix.

## Skeletons
Tag unconfirmed lines [Pitch] [Owner] [Default] [Assumption] [Research]; make vague answers testable.

**PROJECT_BRIEF.md** (numbers match `../../new-idea/references/brief-template.md`): `_v0 · date · Quick_` · §0 Idea card ≤ 120 words (idea, audience + markets, platforms, owner hours/budget/skills, differentiator, must-not) · §2 Problem (real moment, workarounds, unfair advantage) · §2b Alternatives (incl. doing nothing, switching cost) · §3 Goal (stated or assumed, 6-month metric, non-goals) · §4 Audience (first 100, accessibility needs, languages) · §5 Scope (core action, 3–5 Musts, out of scope) · §7 Technology (provisional + reason) · §8 Business (money, budget, hours, market, data sensitivity).

**CLARITY.md:** `**Readiness:** Evaluation can start (provisional) · n block approval · m of k blocking answered` · Phase | Ready? | Blocked by (Evaluation, Design direction, PRD draft, Approval) · **Open questions** | ID | Question | Blocks | Type | How to find out | Owner | Default if unanswered | — Decision: recommended option + why; Fact: "none — must be found out"; Assumption: → a test · **Assumptions** ranked by risk | ID | We believe… | If wrong… | Test | Status | · **Answered**.

**ONE_PAGER.md**, one line each: `_date · Verdict: **X** (confidence) · index: README.md_` · Defaults to confirm (unavailable only, ≤ 3) · The idea in one line · The problem · Who it's for first · Up against (we win / they win) · Strongest version · Reality check (3) · How to make it stronger (3) · Version 1 (provisional) · Tools and cost · Next test (go if / rethink if) · Decisions needed.

**README.md:** `# name — Idea Pack` + table Document | What it answers | Status, linking ONE_PAGER, PROJECT_BRIEF, CLARITY, EVALUATION, COMPETITORS, STATUS, DECISIONS, COSTS (+ INTERVIEW_ROUND1); design direction and PRD rows: "not yet — run Standard", no link.

## Rules
Honest coach, not judge: every weakness gets a fix or a test. Never invent competitors, reviews, prices or numbers ("Unknown + how to find out"). Never write `Evaluation: APPROVED`. Plain language for a senior UX designer who codes lightly.
