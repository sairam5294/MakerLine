# MakerLine vs your other Claude plugins

You also have the **design**, **engineering** and **product-management** plugins installed. Some of their skills do similar jobs.
When two skills match a request, Claude may pick either one, so the kit sets the rules below.

## MakerLine owns these (use the kit skill)
| Job | Use (MakerLine) | Instead of | Why |
|---|---|---|---|
| Accessibility audit | `quality-review` → accessibility-auditor | design:accessibility-review | Kit uses **WCAG 2.2** + iOS/Android rules; the other uses WCAG 2.1 |
| Code / PR review | `quality-review` | engineering:code-review | Kit checks all 5 angles against your standards and writes reviews/ |
| Test strategy | `test-plan` | engineering:testing-strategy | Maps to PRD story IDs + kit test standard |
| Spec / PRD | `write-prd` | product-management:write-spec | Gated, numbered stories feeding PLAN.md |
| Architecture / stack | `tech-stack` | engineering:architecture, engineering:system-design | Owner-fit costs + kit starters |
| Launch checklist | `ship-checklist` | engineering:deploy-checklist | Includes stores, privacy, expert review |
| Design system | `design-system` | design:design-system | Uses the project's `design/tokens.json` |
| Idea critique | `evaluate-idea` | product-management:product-brainstorming | Scored, researched, gated |

## Use these alongside the kit (they complement it)
design:ux-copy (microcopy while building) · design:research-synthesis / product-management:synthesize-research (interview notes in validate-idea) · design:user-research (research plans) · design:design-critique (early Figma feedback) · design:design-handoff · engineering:debug · engineering:incident-response · product-management:metrics-review (inside post-launch) · product-management:competitive-brief (deeper competitor dives).

## Optional: remove the overlap completely
Turn off the overlapping skills or plugins in the Claude app's plugin settings. The kit works fine either way; the rule in CLAUDE.md tells Claude which to prefer.
