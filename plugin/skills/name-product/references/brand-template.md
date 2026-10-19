# Brand — {{Name}}

_Updated {{date}} · From NAMING.md (chosen name) and DESIGN_DIRECTION.md (chosen direction). Tokens: `design/tokens.json`. Assets: `design/brand/`._

## 1. Name and promise
- Name: **{{Name}}** — {{meaning / why}} · Pronunciation: {{…}} · Tagline: {{≤ 6 words}}
- Positioning in one line: {{from EVALUATION}}

## 2. Logo
- Chosen direction: {{wordmark / lettermark / symbol + wordmark}} — {{one-line idea}}
- Construction: {{grid, typeface, weight, corner radius}} · Made in: Figma file {{link}}
- Exports (`design/brand/`): `logo.svg`, `logo-mono.svg`, `logo-reversed.svg`, `mark.svg`, favicon set (16, 32, 180 apple-touch, 192/512 PWA), app icon 1024, social preview 1200×630

## 3. Logo guidelines
| Rule | Value |
|---|---|
| Clear space | {{e.g. height of the "x" on every side}} |
| Minimum size | {{e.g. 24 px digital / 12 mm print; below that use the mark only}} |
| Colour versions | full colour on light · one colour · reversed on dark |
| Allowed backgrounds | {{tokens}} — mark ≥ 3:1, text ≥ 4.5:1 |
| Don't | stretch, rotate, recolour outside the palette, add shadows/gradients, place on busy photos, rebuild in another font |

## 4. Colour
| Role | Theme | Colour | On | Contrast |
|---|---|---|---|---|
| Brand primary (button) | light | #{{hex}} | #{{hex}} | {{n}}:1 |
| Brand primary (button) | dark | #{{hex}} | #{{hex}} | {{n}}:1 |
| Body text | light | #{{hex}} | #{{hex}} | {{n}}:1 |
| Accent · Success · Warning · Danger · Info | … | | | |
One colour pair per row (the checker recomputes every ratio).
Never use colour alone to carry meaning (pair with text or an icon).

## 5. Typography
- Display: {{font}} · Text: {{font}} · Mono: {{font}} — licence {{OFL/Apache}}; scripts covered: {{Latin, Telugu, Devanagari…}}
- Fallback stack: {{system-ui, …}}
- Scale: {{12/14/16/20/24/32/40}} · body min 16 px (web) · line height {{1.5 body / 1.2 headings}} · text scales to 200% without loss

## 6. Icons
- Set: {{Lucide / Phosphor / Material Symbols}} (licence {{…}}) · style {{outline 1.5 px / filled}} · sizes 16/20/24 · tappable area ≥ 44 pt / 48 dp
- Meaningful icons have a visible label or accessible name; decorative icons are hidden from assistive tech

## 7. Voice and imagery
- Voice: {{3 words}} — do {{…}} / don't {{…}}
- Imagery: real, diverse people and contexts; no stereotypes; alt text for every meaningful image; no text inside images

## 8. Rules for code and design (enforced)
| Rule | Enforced by |
|---|---|
| Colours only via tokens, never raw hex in components | lint / review; `design.mdc` |
| Every text/background pair in `contrastPairs` ≥ AA | `npm run contrast` in CI |
| Fonts loaded from {{source}} with `font-display: swap`, fallback stack set | review |
| Icons only from {{set}}; icon-only buttons have an accessible name | lint (jsx-a11y) + review |
| Logo files only from `design/brand/`; never re-drawn in code | review |
