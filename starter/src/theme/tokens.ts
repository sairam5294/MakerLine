/**
 * Design tokens — the ONLY place raw values (hex colours, sizes) live.
 * Source of truth: design/tokens.json (W3C Design Tokens format, shared with Figma).
 * Edit tokens.json → run `npm run tokens` → this file's exports update everywhere.
 * Three tiers (see DESIGN_SYSTEM.md):
 *   1. palette   – raw colours, never used directly in components
 *   2. semantic  – lightColors / darkColors (textPrimary, danger…) — what components use
 *   3. component – build from semantic tokens where needed (e.g. button.primary.bg)
 * The contrast test (npm run contrast) fails if any pair in contrastPairs breaks WCAG AA.
 */
export * from './tokens.generated';
