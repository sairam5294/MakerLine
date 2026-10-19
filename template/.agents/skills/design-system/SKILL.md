---
name: design-system
description: Product Kit design system: defines the framework and tokens.json — HIG/Material/custom approach, tokens (light+dark, contrast-checked), component inventory with states, Figma↔code mapping → DESIGN_SYSTEM.md + token files. Use for "design system", "tokens", "theme", "design framework".
---

# Design System

Owner is a senior UX designer: act as a design-systems partner; they lead aesthetics.

1. Read brief (feel, audience, platforms, brand), evaluation personas, TECH_STACK UI library, BRAND.md (colours, fonts, icon set and their rules become primitive tokens and component rules), and DESIGN_DIRECTION.md — start from the visual direction the owner chose and its contrast-checked palette, and turn its screen inventory into the component inventory.
2. Agree approach: platform-native (HIG/Material 3) · unified brand system on a component library (still honour platform navigation/back) · existing brand system.
3. Tokens in 3 tiers — primitive → semantic (`color.text.primary`) → component (`button.primary.bg`). The starters' `build-tokens.mjs` generates primitives and semantic tokens; component tokens live in DESIGN_SYSTEM.md component specs (as references to semantic tokens) until the generator supports them. Tokens cover: colour light+dark, type scale (+ Indic fallbacks if needed), 4-pt spacing, radius, elevation, motion, breakpoints.
4. Write tokens to **`design/tokens.json`** (W3C Design Tokens format — the single source for Figma and code; see `references/tokens-figma-sync.md`). Add every text/background and boundary pair to `$extensions.productKit.contrastPairs`, run `npm run tokens && npm run contrast` (CI fails below AA), fix failures.
5. MVP component inventory: variants, sizes, states (default/hover/focus/pressed/disabled/loading/error/selected), a11y (role, label, keyboard/gesture), content rules.
6. Write `docs/product/DESIGN_SYSTEM.md` (principles, component specs — reference token names, never raw values). `npm run tokens` generates `src/theme/tokens.generated.ts`; never hand-edit it.
7. Figma: sync `design/tokens.json` ↔ Figma variables (Light/Dark modes) via the Figma connector or Tokens Studio — `references/tokens-figma-sync.md`. Figma is where the owner designs; tokens.json is what code reads; keep them equal.
8. Update DECISIONS + STATUS.

Rules: semantic tokens only in components; design dark mode now; specs include empty/loading/error behaviour.
