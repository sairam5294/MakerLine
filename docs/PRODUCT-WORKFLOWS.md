# Choose the right MakerLine workflow

MakerLine starts with the decision you need to make, then uses the parts of the kit that answer it. You can enter at any product stage. Existing work is read and reused; a review does not reset a project to phase 1.

The example commands below use Claude's `/makerline:<skill>` syntax. In ChatGPT, select the installed skill with `@`; in Codex, mention it with `$`; in Cursor, use `/<skill>`. You can also say the same request in plain language. See [installation and invocation](INSTALL-AI-TOOLS.md).

## Start with these four facts

Tell MakerLine: (1) what exists today, (2) the decision you need, (3) your launch markets, and (4) any deadline, budget or team limit. If you have a project folder, open that folder in the AI tool first. Add customer evidence and analytics only if you have permission to use them with that tool. Numbers without a source are labelled estimates.

| Your situation | First skill | Then use | Paste this example prompt |
|---|---|---|---|
| A fresh idea; need an early verdict | `start` (Quick Idea Pack) | `evaluate-idea`, then `validate-idea` if the idea survives | `/makerline:start I want to help small clinics fill cancelled appointments. Give me the Idea Pack (quick). Launch market: Canada.` |
| Fresh idea; want the full plan and visual review | `product-opportunity-review` (`idea`) | `start` for the Idea Pack, `design-direction`, draft `write-prd` | `/makerline:product-opportunity-review This is a fresh idea. Assess whether it is worth building and create the HTML decision report. Market: Canada.` |
| Half-built product; unsure whether to finish | `product-opportunity-review` (`partial`) | Refresh `evaluate-idea`; `validate-idea` for the largest unknown; `plan-build` only after choosing to continue | `/makerline:product-opportunity-review This product is half built. Read the repo and plan, refresh the market, then compare finish, narrow, pivot and stop. Show value and effort ranges.` |
| Product close to launch | `product-opportunity-review` (`prelaunch`) | `quality-review`, `test-plan`, `ship-checklist`; `plan-build` for post-launch work | `/makerline:product-opportunity-review We plan to launch in six weeks. Check readiness, positioning and the launch markets. Separate must-fix items from later opportunities.` |
| Launch delayed; market may have moved | `product-opportunity-review` (`delayed`) | Refresh `evaluate-idea`; time-box `validate-idea`; `ship-checklist` if launch is still justified | `/makerline:product-opportunity-review Launch slipped eight months. Recheck demand, competitors, remaining effort and what would make us stand out before we spend more.` |
| Live product; need a next bet | `post-launch` for the weekly pulse | `product-opportunity-review` for a strategic refresh; `validate-idea` for the proposed bet; `plan-build` after choosing it | `/makerline:product-opportunity-review We have live users. Use usage and feedback to find the bottleneck and compare build and non-build ways to improve retention.` |
| A specific AI feature is already chosen | `ai-feature` | `plan-build`, `build-feature`, `quality-review` | `/makerline:ai-feature Summarise support requests. Compare a non-AI workflow, show data and approval needs, cost per use and an eval plan.` |

For combinations, state both conditions: “half built **and** delayed,” or “live **but** launching in a new market.” The review chooses the route for the decision with the highest immediate cost of being wrong and adds checks for the other condition. An urgent launch does not erase weak demand evidence; it changes the test you can run in time.

## Choose the review depth

| Depth | Use it when | What you should receive |
|---|---|---|
| Quick | A decision is urgent or only public evidence is available | Current facts, unknowns, a provisional recommendation and the cheapest decision-changing test; no ranked roadmap on weak demand evidence |
| Standard | You can inspect the product, plan, customer feedback and current market | Compared options with value/effort ranges, evidence, an action plan and a challenge to the preferred option |
| Deep | Code, designs, analytics and customer research are available and the investment is substantial | A full baseline and opportunity scan, market and launch checks, test design and a staged roadmap if the evidence supports one |

For a later review, keep the existing `REVIEW.json`, mark `mode` as `refresh`, record what changed in the product, market and customer evidence, and update the recommendation. Recheck prior “declined” or “parked” ideas only if new evidence explains why they deserve another look. A standing competitor watch or monthly refresh is an optional follow-up; set a cadence only if the owner requests one.

## What the new review does

`product-opportunity-review` creates `docs/product/opportunity/REVIEW.json` and `index.html` in your project. The HTML starts with the current recommendation and confidence, shows the route and saved progress, then presents options, actions, AI-tool responsibilities, sources and open questions. Expand a step to see its finding and a prompt for that skill. Open `index.html` directly in a browser, or run MakerLine's local dashboard and open the review from the project page. The dashboard is a reader; it does not call an AI or approve decisions.

The skill updates `REVIEW.json` after each completed step and regenerates the HTML. A completed step must have a finding; sources have IDs and dates. Weak evidence yields a hypothesis and test plan instead of a ranked investment roadmap. Compare building with pricing, distribution, onboarding, reliability, partnerships and simplification when relevant. If an idea is already in the product plan, label it accordingly.

The review does not change MakerLine's owner approval gate. It can research before approval. `plan-build` and `build-feature` still follow the normal [phase workflow](../plugin/skills/product-kickoff/SKILL.md).

## A practical multi-tool sequence

| Job | Suggested owner | Handoff material |
|---|---|---|
| Evidence and market review | One research-capable tool chosen in `tool-plan` | Dated source notes, `REVIEW.json`, unknowns |
| Wireframe or prototype | Tool with the design environment you use | `DESIGN_DIRECTION.md`, task success criteria |
| Code and tests | Tool with local repo and test access | `PLAN.md`, relevant source files, `HANDOFF.md` |
| Independent challenge or quality review | A separate reviewer when available | The recommendation, evidence, assumptions and changed files |

Run `/makerline:tool-plan` with your actual subscriptions and limits; it writes the primary and fallback for your project. One tool owns each output at a time. Before a switch, run `/makerline:handoff` so the next tool receives what is done, what remains, decisions and a quick verification step. A browser-only tool without repo access gets `CONTEXT_PACK.md` and the relevant review files, never secret files.

## What good looks like

A complete review answers: What should we do next? How sure are we? What evidence supports that? What would change the answer? What can we test cheaply? Who does what over the next 2–4 weeks? It names launch-market requirements separately from MakerLine's WCAG 2.2 AA design baseline. For legal or regulated decisions, verify current official sources for the actual market and product type and seek specialist review when applicability is unclear.

The HTML is accessible by design, but automated accessibility checks cannot establish full conformance. The report renderer should be checked with keyboard-only use, screen readers, zoom/reflow, light/dark contrast and automated rules. MakerLine's cockpit test already uses axe and checks 320 px reflow; extend that test to the review page.
