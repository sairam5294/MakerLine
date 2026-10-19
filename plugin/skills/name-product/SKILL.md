---
name: name-product
description: Product Kit naming and brand — 12–15 contextual product names scored and conflict-checked (NAMING.md), then a lightweight brand kit (BRAND.md) — logo concept and an easy way to make it, logo usage guidelines, colour theme, font pairing and icon style, each with rules the code and design must follow. Use for "name ideas", "what should I call it?", "logo", "brand", "colours and fonts".
---

# Name and brand

Gate: STATUS `Evaluation: APPROVED`. Inputs: PROJECT_BRIEF (audience, languages, feel, naming preferences), EVALUATION (positioning, wedge), DESIGN_DIRECTION (chosen visual direction and its contrast-checked palette), `../product-standards/references/inclusion.md`.

## Part 1 — Names (NAMING.md)
1. Confirm criteria only if missing: languages and scripts, words or tones to avoid, domain/app-store needs.
2. Generate 12–15 names **from the idea's own context** — its users' words for the problem, the moment of use, the core action, the outcome, local language roots (give script and accurate meaning), metaphors from the positioning. Styles: descriptive, evocative, invented/compound, culture/language-rooted. Skip excluded styles.
3. Score 1–5: memorable, easy to say and spell for the audience (incl. non-native speakers and screen-reader pronunciation), meaning fit, distinctive, ≤ 12 characters for the icon label, no negative meaning in target languages.
4. For the top 6, web-search App Store/Play clashes, domain signals (.com/.in/.app), same-category companies and trademarks (IP India, USPTO, WIPO if reachable). Report what was checked vs not; never claim "available".
5. Table (name · style · meaning · scores · conflicts · risk) + top 3 with a ≤ 6-word tagline each → `docs/product/NAMING.md`. Owner picks.

## Part 2 — Brand kit (BRAND.md), after the owner picks a name
Follow `references/brand-template.md`; keep it a one-person, free-tools brand.
6. **Logo concept:** 2–3 directions that fit the name and positioning — wordmark, lettermark/monogram, or a simple symbol + wordmark. For each: the idea in one line, why it fits, and how it reads at 16 px (favicon) and 1024 px (app icon).
7. **Easy way to make it** (`references/logo-guide.md`): the owner is a designer, so default to Figma (free): build on a grid with one typeface from Part 2's pairing, export SVG + PNG sizes. Optional AI image tools only for mood exploration, never as the final mark (licensing and consistency). List every export the product needs (favicon set, app icons, social preview 1200×630, store assets).
8. **Logo guidelines:** clear space, minimum size, colour versions (full colour, one-colour, reversed on dark), backgrounds it may sit on (with contrast ≥ 3:1 for the mark, 4.5:1 for any text in it), misuse examples (stretching, recolouring, effects, busy photos), file names and where they live (`design/brand/`).
9. **Colour theme:** start from DESIGN_DIRECTION's chosen palette — brand primary, secondary/accent, neutrals, semantic (success, warning, danger, info), light and dark. Every text/background pair with its contrast ratio (≥ 4.5:1 body, ≥ 3:1 large text and UI boundaries); never colour alone for meaning. These become primitive tokens in design-system.
10. **Typography:** a pairing of open-licence fonts (e.g. Google Fonts) with script coverage for every launch language (check Indic, Arabic, CJK as needed), a fallback system stack, a type scale, minimum body size (16 px web / platform default on mobile), line height, and that text must scale to 200%.
11. **Icon style:** one open-licence set (e.g. Lucide, Phosphor, Material Symbols — check the licence), stroke or fill weight, corner style, sizes (16/20/24), target ≥ 44 pt/48 dp around tappable icons, every meaningful icon has a text label or accessible name, decorative icons are hidden from assistive tech.
12. **Voice in one line + imagery rules** (diverse, real-looking people; no stereotypes; alt text for every meaningful image).
13. **Rules:** write the enforceable version of 9–11 into BRAND.md §8 ("Rules for code and design"); project-setup turns them into `.cursor/rules/design.mdc` and design-system turns them into tokens. Update STATUS and DECISIONS.

Avoid crowded dictionary words, near-clones of big brands, imitating another brand's identity, and disrespectful use of religious or cultural terms.
