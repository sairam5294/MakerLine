# Figma ↔ design/tokens.json ↔ code

```
Figma variables (Light/Dark modes)  ⇄  design/tokens.json  →  npm run tokens  →  src/theme/tokens.generated.ts  →  components
```

## Kit Figma library
A ready library matching the starters, "Product Kit — Design System" (Primitives, Semantic Light/Dark, Dimensions, type styles; Button, TextField, ScreenState), is published on Figma Community: https://www.figma.com/community/file/1692097443572763844/product-kit-design-system Duplicate it per product, then sync tokens.json from the copy. (Maintainers: see design/FIGMA-COMMUNITY.md.)
Code Connect templates (`starter/figma/*.figma.ts`) link these components to code in Dev Mode — needs a Figma Organization/Enterprise plan.

## tokens.json structure (W3C Design Tokens format)
- `color.palette.*` — raw colours (primitives). Figma collection **Primitives**.
- `color.light.*` / `color.dark.*` — semantic colours referencing the palette, e.g. `"{color.palette.blue600}"`. Figma collection **Semantic** with modes **Light** and **Dark** (same variable names in both).
- `space`, `radius`, `size`, `duration`, `typography` — Figma number variables / text styles.
- `$extensions.productKit.contrastPairs` — pairs the contrast test checks (code-only).

## Option A — Claude + Figma connector (no plugin needed)
Ask: "Sync design/tokens.json to Figma variables in <file URL>" (or the reverse). Claude loads the figma-use skill, then creates/updates the collections: variable names = token paths (`color/light/textPrimary` style), Light/Dark as modes, semantic variables **alias** primitives (don't copy hex). Reverse sync: read the variables, update tokens.json, run `npm run tokens && npm run contrast`, and show the diff before committing.

## Option B — Tokens Studio plugin (in Figma)
Tokens Studio reads/writes W3C-format JSON: point it at `design/tokens.json` in your GitHub repo (sync provider: GitHub), push changes from Figma as a pull request → CI regenerates and contrast-checks.

## Rules
- Designers change tokens in Figma or tokens.json — never in `tokens.generated.ts` or component code.
- Every token change runs `npm run contrast`; a failure blocks the PR.
- Renaming a semantic token = breaking change → search the codebase and update in the same PR.
