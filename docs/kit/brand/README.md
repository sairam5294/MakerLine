# MakerLine brand

**Idea.** MakerLine is the line from an idea to a shipped product, and it ends in a check: the mark is one stroke that runs, then turns into a tick. MakerLine Idea is the same line just starting, from a spark.

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
| `makerline-idea-*` | Same set for MakerLine Idea |
| `makerline-social-preview.png`, `makerline-idea-social-preview.png` | Link previews (1280 × 640) |
| `../../site/assets/` | Site favicon set: `favicon.svg`, `favicon.ico` (16/32/48), `favicon-32.png`, `apple-touch-icon.png` (180), `icon-192/512.png`, `icon-maskable-512.png`, `site.webmanifest` |

The wordmark is set in Bricolage Grotesque (weight 760, slightly tightened) and converted to outlines, so it looks the same without the font installed. Body text on the site uses Atkinson Hyperlegible Next. Both are under the SIL Open Font License.

## Colour

| Name | Hex | Where | Contrast |
|---|---|---|---|
| Line blue | `#1A2E6B` | MakerLine tile | white mark 12.8:1 · tile on paper 12.0:1 |
| Idea green | `#17694A` | MakerLine Idea tile | white mark 6.7:1 · tile on paper 6.3:1 |
| Line blue, dark mode | `#3B5BDB` | tile on dark backgrounds | white mark 5.7:1 · tile on `#0D1522` 3.2:1 |
| Idea green, dark mode | `#1F8A5B` | tile on dark backgrounds | white mark 4.3:1 · tile on `#0D1522` 4.2:1 |
| Ink | `#0F1E33` | wordmark, text | 15.7:1 on paper `#F6F8FB` |

All logo parts meet WCAG 1.4.11 (3:1 for graphics) in both themes. Site text colours are in `docs/site/assets/site.css` and are 4.5:1 or more.

## Rules

- **Clear space:** at least the height of the tick (a quarter of the tile) on every side.
- **Minimum size:** the mark at 16 px, the full logo at 24 px tall. Below 24 px, use the mark alone.
- **Alt text:** "MakerLine" (or "MakerLine Idea"). If the name is already written next to it, use empty alt (`alt=""`).
- **Don't:** recolour the tile outside the four colours above, stretch it, add shadows or gradients, put the light logo on a dark background (use `-on-dark`), or rebuild the wordmark in another font.
