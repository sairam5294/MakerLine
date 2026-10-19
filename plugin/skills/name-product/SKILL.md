---
name: name-product
description: Name the product and build a lightweight brand kit — 12–15 contextual product names scored and conflict-checked (NAMING.md), then BRAND.md with a logo concept and an easy way to make it, logo usage guidelines, colour theme, font pairing and icon style, each with rules the code and design must follow. Trigger with "name ideas", "what should I call it?", "logo", "brand", "colours and fonts", or after approval.
argument-hint: "<naming constraints or chosen name, or nothing to start from the brief>"
---

# /name-product

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Give the owner a shortlist of names they can check and pick from, then a one-person, free-tools brand kit built on the chosen name.

## Usage

```
/name-product                          # Part 1: names from the brief and evaluation
/name-product avoid English words      # add a criterion
/name-product brand for "Wisp"         # Part 2: brand kit for the picked name
```

## How it works

```
┌──────────────────────────────────────────────────────────────┐
│                     NAME PRODUCT                             │
├──────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                   │
│  ✓ 12–15 names from the idea's own context, scored 1–5       │
│  ✓ Conflict check for the top 6 (stores, domains, marks)     │
│  ✓ Brand kit: logo concept + how to make it, guidelines,     │
│    colour theme, typography, icon style, voice, rules        │
├──────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                  │
│  + Design (Figma): build the logo on a grid, export assets   │
└──────────────────────────────────────────────────────────────┘
```

## Inputs

- Gate: STATUS `Evaluation: APPROVED`.
- `docs/product/PROJECT_BRIEF.md` (audience, languages, feel, naming preferences), `EVALUATION.md` (positioning, wedge), `DESIGN_DIRECTION.md` (chosen visual direction and its contrast-checked palette).
- `../product-standards/references/inclusion.md`.
- Ask the owner only for missing criteria: languages and scripts, words or tones to avoid, domain/app-store needs.

## Workflow

### Part 1 — Names (`NAMING.md`)

1. **Confirm criteria** only if missing: languages and scripts, words or tones to avoid, domain/app-store needs.
2. **Generate 12–15 names from the idea's own context** — its users' words for the problem, the moment of use, the core action, the outcome, local language roots (give script and accurate meaning), metaphors from the positioning. Styles: descriptive, evocative, invented/compound, culture/language-rooted. Skip excluded styles.
3. **Score 1–5** on: memorable · easy to say and spell for the audience (incl. non-native speakers and screen-reader pronunciation) · meaning fit · distinctive · ≤ 12 characters for the icon label · no negative meaning in target languages.
4. **Conflict-check the top 6** by web search: App Store/Play clashes, domain signals (.com/.in/.app), same-category companies and trademarks (IP India, USPTO, WIPO if reachable). Report what was checked vs not; never claim "available".
5. **Write `docs/product/NAMING.md`**: a table (name · style · meaning · scores · conflicts · risk) + top 3 with a ≤ 6-word tagline each. Owner picks.

### Part 2 — Brand kit (`BRAND.md`), after the owner picks a name

Follow `references/brand-template.md`; keep it a one-person, free-tools brand.

6. **Logo concept:** 2–3 directions that fit the name and positioning — wordmark, lettermark/monogram, or a simple symbol + wordmark. For each: the idea in one line, why it fits, and how it reads at 16 px (favicon) and 1024 px (app icon).
7. **Easy way to make it** (`references/logo-guide.md`): the owner is a designer, so default to Figma (free): build on a grid with one typeface from Part 2's pairing, export SVG + PNG sizes. Optional AI image tools only for mood exploration, never as the final mark (licensing and consistency). List every export the product needs (favicon set, app icons, social preview 1200×630, store assets).
8. **Logo guidelines:** clear space, minimum size, colour versions (full colour, one-colour, reversed on dark), backgrounds it may sit on (with contrast ≥ 3:1 for the mark, 4.5:1 for any text in it), misuse examples (stretching, recolouring, effects, busy photos), file names and where they live (`design/brand/`).
9. **Colour theme:** start from DESIGN_DIRECTION's chosen palette — brand primary, secondary/accent, neutrals, semantic (success, warning, danger, info), light and dark. Every text/background pair with its contrast ratio (≥ 4.5:1 body, ≥ 3:1 large text and UI boundaries); never colour alone for meaning. These become primitive tokens in `design-system`.
10. **Typography:** a pairing of open-licence fonts (e.g. Google Fonts) with script coverage for every launch language (check Indic, Arabic, CJK as needed), a fallback system stack, a type scale, minimum body size (16 px web / platform default on mobile), line height, and that text must scale to 200%.
11. **Icon style:** one open-licence set (e.g. Lucide, Phosphor, Material Symbols — check the licence), stroke or fill weight, corner style, sizes (16/20/24), target ≥ 44 pt/48 dp around tappable icons, every meaningful icon has a text label or accessible name, decorative icons are hidden from assistive tech.
12. **Voice in one line + imagery rules** (diverse, real-looking people; no stereotypes; alt text for every meaningful image).
13. **Rules:** write the enforceable version of steps 9–11 into BRAND.md §8 ("Rules for code and design"); `project-setup` turns them into `.cursor/rules/design.mdc` and `design-system` turns them into tokens. Update STATUS and DECISIONS.

## Output

| File | What | Size |
|---|---|---|
| `docs/product/NAMING.md` | scored, conflict-checked table of 12–15 names + top 3 with taglines | one table + 3 lines |
| `docs/product/BRAND.md` | logo concept and how to make it, guidelines, colours, type, icons, voice, §8 rules | per template |
| `design/brand/` | logo exports (SVG + PNG sizes, favicon set, app icons, social preview) | — |

Present: the top 3 names with taglines and what was (not) conflict-checked; after the pick, the recommended logo direction and the §8 rules in ≤ 10 lines.

## If connectors available

If **~~design** (Figma) is connected:
- Build the chosen logo direction on a grid in Figma and export the asset set listed in step 7.

## Rules

- Never claim a name is "available" — report exactly what was checked and what wasn't.
- Avoid crowded dictionary words, near-clones of big brands, imitating another brand's identity, and disrespectful use of religious or cultural terms.
- Contrast: mark ≥ 3:1; text ≥ 4.5:1 body, ≥ 3:1 large text and UI boundaries; never colour alone for meaning.
- Open-licence fonts and icon sets only; check script coverage for every launch language.
- AI image tools are for mood exploration only, never the final mark.

## Tips

1. Say which languages and scripts matter up front — it changes the shortlist and the font pairing.
2. Pick the name before asking for the brand kit; Part 2 depends on it.
3. The §8 rules are what code and Cursor rules will enforce — read them with that in mind.

## Related

- Before: approval, `design-direction` · After: `tech-stack`, `design-system` (palette → tokens), `project-setup` (§8 → `.cursor/rules/design.mdc`)
- Reads: `references/brand-template.md`, `references/logo-guide.md`; `../product-standards/references/inclusion.md`
