# When to use which MakerLine skill

The product's stage and the owner's decision determine the route. Existing outputs are inputs, not work to repeat. Use the skill's own instructions for its full method.

| Situation and decision | Start here | Continue with | Example prompt |
|---|---|---|---|
| Fresh idea: worth exploring? | `start` or `new-idea` | `evaluate-idea` → `validate-idea` → `design-direction` → draft `write-prd` | `/makerline:start I have an idea for a neighbourhood tool library. Give me the Idea Pack (quick).` |
| Fresh idea: also want the HTML decision view | `product-opportunity-review` (`idea`) | Existing Idea Pack skills; save findings to review | `/makerline:product-opportunity-review Review this fresh idea and give me an HTML decision report. Market: Canada.` |
| Half-built: continue investing? | `product-opportunity-review` (`partial`) | `evaluate-idea` for refreshed market, `validate-idea` for the top risk, `plan-build` only after the decision | `/makerline:product-opportunity-review This app is half built. Compare finishing, narrowing, pivoting and stopping. Use the repo and current market.` |
| Near launch: ready and distinctive? | `product-opportunity-review` (`prelaunch`) | `quality-review`, `test-plan`, `ship-checklist`; `plan-build` for later work | `/makerline:product-opportunity-review We launch next month. Check readiness and market positioning; separate launch essentials from later ideas.` |
| Delayed: assumptions still valid? | `product-opportunity-review` (`delayed`) | Refresh `evaluate-idea`, time-box `validate-idea`, then `ship-checklist` if launch remains sensible | `/makerline:product-opportunity-review Launch slipped nine months. Recheck demand, competitors and remaining effort before we spend more.` |
| Live: what improves next? | `post-launch` for weekly pulse | `product-opportunity-review` for a strategic refresh, `validate-idea` for a bet, `plan-build` after selection | `/makerline:product-opportunity-review We have live users. Find the bottleneck and compare three ways to improve retention.` |
| Specific AI feature already chosen | `ai-feature` | `plan-build`, `build-feature`, `quality-review` | `/makerline:ai-feature Summarise support requests; compare with a non-AI workflow and price it.` |
| More than one AI tool | `tool-plan` | `handoff` at each switch | `/makerline:tool-plan I have Claude, Codex and Cursor. Assign the review, prototype and build jobs, with a fallback and handoff.` |

`start` owns the normal phase sequence and approval. `product-opportunity-review` can be invoked at any stage to answer a strategic question; its output may send the owner back to a phase skill. A combination such as "half built and delayed" uses the route for the more urgent decision and includes the other concern as a check. "Live for me, but nobody else can install it" is `prelaunch`. Every route includes an `access` step for launch-market rules. Do not interpret "near launch" as permission to publish or deploy.

Each route ends with: current recommendation, confidence, evidence gaps, options including non-build moves, cheapest decision-changing test, and next actions. A weak evidence route stops before a ranked roadmap.
