# Lifecycle and growth — {{product}}

_Updated {{date}} · Where the project is, what "done" means for this stage, and what changes when it moves on. Current stage: **{{stage}}**._

## Stages
| Stage | Goal | Exit criteria (all true to move on) | Key metric | Typical cost | What changes in the repo / docs |
|---|---|---|---|---|---|
| 1. Idea | decide if it's worth testing | Idea Pack done; owner decision logged | — | ₹0 | docs/product only |
| 2. Validation | prove the riskiest assumption | VALIDATION.md thresholds met (e.g. ≥ 4/5 complete the prototype task; {{n}} sign-ups) | test success | ₹0–{{…}} | wireframes, landing page |
| 3. MVP build | ship the Musts to a few real users | PLAN M0–Mn done; quality-review "Ready"; TEST_PLAN exit met | core action completed | free tiers | full engineering docs; CI green |
| 4. Private beta | learn with 10–50 users | {{n}} weekly active; top 5 issues fixed; no P0/P1 | week-2 retention | free tiers | feedback log; analytics live |
| 5. Public launch | open the doors | RELEASE checklist ✅; accessibility statement; privacy docs; store approval | sign-ups / activation | {{first paid tier?}} | release tags; on-call basics |
| 6. Growth | find a repeatable channel | {{CAC/LTV or activation target}} for 2 months | {{north-star}} | {{…}} | experiments (`exp/` branches), feature flags |
| 7. Scale | stay fast and safe as usage grows | p95 latency, error rate and cost per user within budget at {{10×}} | cost per active user | paid tiers | perf budgets, backups tested, expert reviews |
| 8. Mature / sunset | keep, sell, open-source or close well | owner decision | — | — | export for users; deletion; archive |

## Growth plan
- **North-star metric:** {{the one number that means users get value, e.g. "docs published per week"}} · inputs: {{activation, retention, referral}}.
- **First 100 users:** {{channels from EVALUATION §5}} · **First 1,000:** {{…}}.
- **Growth loops:** {{e.g. shared docs carry a "made with" link; invites from editors}} — each measured by an event in PRD §11.
- **Experiments:** one hypothesis per `exp/` branch, a metric and a stop date; result logged in `docs/product/METRICS.md`.

## Upgrade triggers (free tier → paid)
| Service | Free-tier limit (checked {{date}}) | Upgrade when | Next tier cost |
|---|---|---|---|
| {{Vercel}} | | {{80% of bandwidth for 2 months}} | |
| {{Supabase}} | | {{DB size / egress / paused project risk}} | |
| {{AI provider}} | | {{cap reached by real use}} | |

## Kill or pivot criteria
- {{From EVALUATION §12 and VALIDATION: e.g. "< 20% week-2 retention after 3 iterations → rethink the core action"}}

## Review cadence
- Weekly in beta and growth (`post-launch`): metrics, feedback, one decision. Quarterly: this file, costs, `standards-refresh`.
