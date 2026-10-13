---
name: design-qa
description: Compares a built screen with its Figma design (or DESIGN_SYSTEM.md) — spacing, tokens, type, states, responsive, a11y — and lists fixes. Use for "design QA", "does it match Figma?", "pixel check".
---

# Design QA

1. Get the design (start from the kit library file or the product's duplicate; if Code Connect is published, use its component mapping to name the exact code component): Figma frame via Figma MCP (screenshot + design context/variables) or the spec in DESIGN_SYSTEM.md.
2. Get the build: run the app (web or Expo web) and screenshot the same screen at the same viewport via Playwright MCP / Playwright; mobile → owner-provided simulator screenshots.
3. Compare in this order: layout & hierarchy → spacing (token scale) → typography (style, weight, line height, truncation) → colour (semantic token used, not just similar hex) → components & variants → states (loading/empty/error/disabled/focus) → responsive breakpoints → dark mode → a11y (contrast, targets, focus visible).
4. Output table: severity (Blocker / Visible / Nit) · screen/element · design · build · fix (file:line, token name). Include the two screenshots side by side when possible.
5. Fix Blockers/Visible issues if asked; re-screenshot to confirm.

Differences caused by platform conventions (iOS vs Android controls) are not bugs — note them.
