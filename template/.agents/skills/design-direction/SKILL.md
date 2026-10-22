---
name: design-direction
description: Sketch the design direction and wireframes for an idea. Covers experience principles, competitor UX teardown, information architecture, core flows, screen inventory with states, content and voice, 2–3 visual directions, accessibility plan and clickable low-fi wireframes (HTML, optionally Figma) → DESIGN_DIRECTION.md + design/wireframes/. Trigger with "design direction", "wireframes", "what would it look like?", "user flows", or after evaluate-idea.
argument-hint: "<focus (e.g. 'phone-first'), or nothing to use docs/product/EVALUATION.md>"
---

# /design-direction

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Give the owner a draft design direction and clickable wireframes before any code — groundwork and options, not the design system.

**Stance: design partner, not lead.** The owner is a senior UX designer: do the groundwork and propose options; they lead taste and make the calls. This is a **draft direction**, not the design system (that comes after approval, in `design-system`).

## Usage

```
/design-direction                     # uses PROJECT_BRIEF, EVALUATION, COMPETITORS, CLARITY
/design-direction phone-first         # state the assumption up front
/design-direction what would it look like?
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                     DESIGN DIRECTION                         │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ Principles · competitor UX teardown · IA · core flows     │
│  ✓ Screen inventory with states · content and voice          │
│  ✓ 2–3 visual directions with contrast-checked palettes      │
│  ✓ Accessibility and inclusion plan                          │
│  ✓ Clickable HTML wireframes (design/wireframes/index.html)  │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Design (Figma): wireframes mirrored into a Figma file     │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- `docs/product/PROJECT_BRIEF.md` (feel, references, platforms), `EVALUATION.md` (personas, positioning, wedge, MVP cut), `COMPETITORS.md` (leaders, complaints), `CLARITY.md`.
- Gate: none — allowed before approval. Everything lands in `docs/` and `design/`, which the approval gate permits.
- Ask ≤ 3 questions only if something blocks direction (e.g. "phone-first or desktop-first?"); otherwise state the assumption and log it in `CLARITY.md`.
- Depth: Standard ≤ 8 wireframe screens, Deep 12+.

## Workflow

1. **Read** the inputs above; ask or assume as described in Inputs.
2. **Experience principles** — 3–5, derived from positioning and personas. Each: one line, "this means…", "this doesn't mean…". They're the tie-breakers for every later design decision.
3. **Competitor UX teardown** — for the 2–3 leaders in `COMPETITORS.md`: first-run steps, steps to the core action, patterns worth borrowing, and the pain points from their review complaints this design must avoid. Cite.
4. **Information architecture** — navigation model (tabs, sidebar, single flow) with the reason, and a sitemap (Mermaid).
5. **Core flows** — 2–4 journeys as Mermaid flowcharts: first run → first value (the "aha"), the core action, and one recovery path (error, offline, permission denied). Count the steps to the core action; compare with the leaders.
6. **Screen inventory** — every MVP screen: purpose · primary action · key content · states (empty, loading, error, offline, success) · MVP or later.
7. **Content and voice** — tone in 3 words with do/don't, a terminology list (one word per concept), and real microcopy for the key moments: onboarding promise, empty states, the main error, the success moment.
8. **Visual directions** — 2–3 distinct options. Recommend one and say why; follow platform conventions (Apple HIG / Material 3) where the brief targets native apps. Never imitate a specific brand's identity. Each option has:
   - name, mood words, one reference product
   - palette with text/background pairs and contrast ratios (text ≥ 4.5:1; borders, icons, focus ring ≥ 3:1; both themes)
   - type pairing, shape and spacing feel, imagery and iconography, motion
9. **Accessibility and inclusion plan** — from personas and EVALUATION §11. State the conformance target (WCAG 2.2 AA everywhere, plus what launch markets add) and lock in the "cheap now, expensive later" choices. Add accessibility notes to each wireframe (heading, focus order, what the screen reader says for icons and status). Cover:
   - the persona spectrum (permanent, temporary, situational), languages and scripts, text scaling
   - low vision and screen readers; motor (targets, one-handed, no drag-only)
   - cognitive (plain language, one task per screen, no time pressure — W3C COGA); low connectivity; older adults or children if relevant
   - `../product-standards/references/inclusion.md` (global baseline: accessible worldwide, no discrimination — names, gender, languages, low-end devices, cost)
10. **Wireframes** — copy (`cp`) `references/wireframe-template.html` to `design/wireframes/index.html`; read it once in full (its CSS kit and script contract are needed), then fill it (Standard ≤ 8 screens, Deep 12+; delete the comment when done). Phone frames for mobile products, desktop width for web tools. Keep the markup accessible (landmarks, labels, real buttons). Then run `check_idea_pack.py` (product-kickoff/scripts) for labels, links and states; if a browser is available, also open it, check every screen renders and the core flow clicks through, and fix what's broken. Each file has:
   - one section per MVP screen in grey-box fidelity with real content (no lorem ipsum)
   - a "Product at a glance" block at the top: what it is in one line, problem → what it does → outcome, goal and how it's measured, value add over the alternative, and who it helps and how — filled from the brief, evaluation and one-pager (write "Not decided yet" rather than guess)
   - at least one empty and one error state
   - links that click through the core flow
   - a designer note per screen (what it's for, open questions)
11. **Figma** — if ~~design (Figma) is connected and the owner says yes, mirror the wireframes into `<Product> — Wireframes v<n>` (new file or their URL) — see If connectors available. HTML stays the checker's source of truth. No connector: mention html.to.design import once.
12. **Write** `docs/product/DESIGN_DIRECTION.md` from `references/design-direction-template.md`, then present (see Output).
13. **Update** `CLARITY.md` (new questions, especially ones a prototype test could answer) and STATUS (`Design direction: Waiting for owner` → `Done` once they pick a direction). Offer `validate-idea` (prototype test with these wireframes) or the approval gate.

## Output

| File | What | Size |
|---|---|---|
| `docs/product/DESIGN_DIRECTION.md` | principles, teardown, IA, flows, screens, voice, visual directions, accessibility plan | per template |
| `design/wireframes/index.html` | clickable low-fi wireframes, one section per MVP screen | Standard ≤ 8 screens, Deep 12+ |
| `docs/product/CLARITY.md` | new questions and logged assumptions | — |

Present in ≤ 12 lines:

```
principles · the recommended visual direction · steps to the core action vs leaders
the wireframe link · 2–4 design decisions for the owner
```

The wireframes double as the prototype for `validate-idea`.

## If connectors available

If **~~design** (Figma) is connected — follow `references/figma-wireframes.md` (tools, seat, limits):
- Load the Figma skills first (`figma-create-new-file`, `figma-use`, `figma-generate-design`, `figma-generate-diagram`).
- A page per platform (Phone 360×800, Tablet 768×1024, Desktop 1024×768 — the HTML wireframe widths); an auto-layout frame per screen, named by screen ID, real content.
- Greyscale `wf/` colour and text styles (text ≥ 4.5:1), targets ≥ 44pt/48dp; states as sibling frames or in the screen note.
- Build and screenshot-check one screen at a time; flows as prototype links or a FigJam diagram.
- Frames: Standard ≤ 8, Deep 12+ (Figma calls are large). Write the file link into `DESIGN_DIRECTION.md`.

## Rules

- Draft direction only — tokens and components come after approval, in `design-system`.
- Text contrast ≥ 4.5:1 in every palette; state ratios for every text/background pair.
- Follow Apple HIG / Material 3 for native targets; never imitate a specific brand's identity.
- Real content in wireframes (no lorem ipsum); accessible markup (landmarks, labels, real buttons).
- Conformance target is WCAG 2.2 AA everywhere, plus whatever the launch markets add.

## Tips

1. Answer the blocking question up front (*"phone-first"*, *"desktop-first"*) to skip the clarification round.
2. Compare the step count to the core action against the leaders — it's the most persuasive line in the doc.
3. Use the wireframes for a `validate-idea` prototype test before approval.

## Related

- Before: `evaluate-idea` · After: `validate-idea`, approval, `design-system` (turns the chosen visual direction into tokens and components), `write-prd` (links screens to stories)
- Reads: `references/design-direction-template.md`, `references/wireframe-template.html`, `references/figma-wireframes.md` (Figma only); `../product-standards/references/inclusion.md`; `check_idea_pack.py` in `../product-kickoff/scripts/`
