# MakerLine brand

**Idea.** The icon is an **ML monogram**: M and L drawn as one stroke, and the L's foot is the line from an idea to a shipped product. It is the clearest of seven tested directions at 16 px. **MakerLine Idea** is the same monogram with a spark in the corner — the idea at the start of the line.

**Supporting detail: the line that ends in a tick.** It runs under headlines (drawn once on the site's home page) and under the name in the signature wordmark. Use it once per page or card, never as the icon.

## Name

| Write | Never |
|---|---|
| **MakerLine** — one word, capital M and capital L | Makerline, Maker Line, MAKERLINE, makerLine |
| **MakerLine Idea** — the idea-stage plugin | Idea Pack plugin, MakerLine-Idea |
| `makerline`, `makerline-idea` — plugin IDs (lowercase, the system requires it) | in running text |
| `/makerline:start`, `/makerline-idea:start` — commands | |

**Idea Pack** stays the name of what MakerLine Idea produces (brief, evaluation, competitors, wireframes, draft PRD, one-pager): "MakerLine Idea gives you an Idea Pack."
Credit line: "Created by Sairam Mogullapalli."

## Words

| Use | Text |
|---|---|
| Tagline (both) | Know if it's worth building. Then build it right. |
| MakerLine, one line | An open-source Claude plugin that takes a product idea from first conversation to launch, with accessibility, security and testing built in. |
| MakerLine, short | MakerLine turns a product idea into an honest verdict, real competitors, wireframes and a draft PRD. Once you approve, it helps you build and ship the product, with WCAG 2.2 AA accessibility, security and tests enforced at every step. |
| MakerLine Idea, one line | Decide if a product idea is worth building, before you write any code. |
| MakerLine Idea, short | MakerLine Idea turns a product idea into an honest evaluation: a verdict, real competitors with a differentiator test, the strongest version of the idea, an accessibility and compliance check, clickable wireframes, a draft PRD and a one-page summary. No code; you decide go, change or stop. |

The long descriptions live at the top of `README.md` (MakerLine) and `standalone/makerline-idea/README.md` (MakerLine Idea). Change wording here first, then everywhere it appears.

## Logo files

| File | Use |
|---|---|
| `makerline-logo.svg` / `@4x.png` | Light backgrounds (default) |
| `makerline-logo-on-dark.svg` / `@4x.png` | Dark backgrounds |
| `makerline-mark.svg` / `-mark-512.png` | Icon alone: favicon, app icon, avatar |
| `makerline-mark-on-dark.svg` | Icon alone on dark backgrounds (the site header in dark mode) |
| `makerline-wordmark.svg` | Name alone, where the mark already appears nearby |
| `makerline-signature.svg` | Name with the line-into-tick underneath, where there's no icon (email signatures, slides) |
| `line-tick.svg` | The supporting detail on its own, under a headline |
| `makerline-idea-*` | Same set for MakerLine Idea |
| `makerline-social-preview.png`, `makerline-idea-social-preview.png` | Link previews (1280 × 640) |
| `makerline-demo.gif` | 9-second demo of a Quick run (720 px, about 80 KB), for READMEs, the directory listing and posts. Rebuilt from the home page's demo with Playwright and ffmpeg |
| `../../site/assets/` | Site favicon set: `favicon.svg`, `favicon.ico` (16/32/48), `favicon-32.png`, `apple-touch-icon.png` (180), `icon-192/512.png`, `icon-maskable-512.png`, `site.webmanifest` |

The wordmark is set in Bricolage Grotesque (weight 760, slightly tightened) and converted to outlines, so it looks the same without the font installed. Body text on the site uses Atkinson Hyperlegible Next. Both are under the SIL Open Font License.

## Colour

| Name | Hex | Where | Contrast |
|---|---|---|---|
| Ultramarine | `#2337B0` | MakerLine tile, line-into-tick, site links and buttons | white mark 9.4:1 · tile on paper 8.8:1 |
| Idea green | `#17694A` | MakerLine Idea tile | white mark 6.7:1 · tile on paper 6.3:1 |
| Ultramarine, dark mode | `#4C61DB` | tile on dark backgrounds | white mark 5.2:1 · tile on `#0D1522` 3.5:1 |
| Idea green, dark mode | `#1F8A5B` | tile on dark backgrounds | white mark 4.3:1 · tile on `#0D1522` 4.2:1 |
| Ink | `#0F1E33` | wordmark, text | 15.7:1 on paper `#F6F8FB` |

Why ultramarine: it matches the site's link and button colour, so logo and page read as one system, and it keeps its colour at 16 px where darker navies look black. Tested alternatives: ink blue `#1A2E6B`, deep teal `#0B5563`, aubergine `#3F2A6B`, graphite `#1F2430` — all pass contrast; change `BLUE` in `build_brand.py` to switch.

All logo parts meet WCAG 1.4.11 (3:1 for graphics) in both themes. Site text colours are in `docs/site/assets/site.css` and are 4.5:1 or more.

## Rebuilding the assets

1. Edit the colours or shapes at the top of `build_brand.py`, then `pip install fonttools brotli` (once) and `python3 docs/kit/brand/build_brand.py` — writes every SVG here and the site's `favicon.svg` / `mark-on-dark.svg`.
2. Render the PNGs (marks at 512, logos @4x, favicon 16/32/48, apple-touch 180, icons 192/512/maskable) and the social cards from those SVGs with a headless browser (Playwright), then `convert favicon-16.png favicon-32.png favicon-48.png favicon.ico` (ImageMagick). Ask Claude: "rebuild the MakerLine brand assets".
3. Update the colour table above and the site's `--accent` in `site.css` if the blue changed.

## Rules

- **Clear space:** at least the height of the tick (a quarter of the tile) on every side.
- **Minimum size:** the mark at 16 px, the full logo at 24 px tall. Below 24 px, use the mark alone.
- **Alt text:** "MakerLine" (or "MakerLine Idea"). If the name is already written next to it, use empty alt (`alt=""`).
- **Don't:** recolour the tile outside the four colours above, stretch it, add shadows or gradients, put the light logo on a dark background (use `-on-dark`), or rebuild the wordmark in another font.
