#!/usr/bin/env python3
"""Build every MakerLine logo SVG from one place.

Why a script: the brand has ~12 SVGs plus PNGs, favicons and social cards. Changing a colour or the mark
by hand in each file drifts; change the constants below and re-run instead.

    pip install fonttools brotli          # once (dev only; the site and plugins don't need it)
    python3 docs/kit/brand/build_brand.py # writes the SVGs here and the favicon SVGs into docs/site/assets/
    # then render PNGs, favicon.ico and social cards: see README.md → "Rebuilding the assets"

The wordmark is Bricolage Grotesque (OFL) at weight 760, converted to outlines so it looks the same
everywhere, even where the font isn't installed.
"""
import pathlib

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
FONT = ROOT / "docs/site/assets/fonts/bricolage-grotesque-latin-wght-normal.woff2"
SITE = ROOT / "docs/site/assets"

# Colours (contrast for each is recorded in README.md; white on all four tiles ≥ 4.3:1).
BLUE, BLUE_DARK = "#2337B0", "#4C61DB"      # MakerLine tile; lighter tile for dark backgrounds
GREEN, GREEN_DARK = "#17694A", "#1F8A5B"    # MakerLine Idea tile
INK = "#0F1E33"                              # wordmark on light backgrounds

# The mark: M and L drawn as one stroke; the L's foot is the line from idea to launch.
ML = ('<path d="M15 44V20l10.5 14L36 20v24h14" fill="none" stroke="#fff" stroke-width="7" '
      'stroke-linecap="round" stroke-linejoin="round"/>')
# MakerLine Idea: the same monogram with a spark — the idea at the start of the line.
SPARK = ('<path d="M49.5 9.5c.7 4.1 2.3 5.7 6.4 6.4-4.1.7-5.7 2.3-6.4 6.4-.7-4.1-2.3-5.7-6.4-6.4 '
         '4.1-.7 5.7-2.3 6.4-6.4Z" fill="#fff"/>')
# Supporting detail: the line that turns into a tick (used under headlines and the signature wordmark).
TICK_LINE = "M2 10H{x1}L{x2} 17L{x3} 3"

SCALE = 30 / 660  # wordmark cap height 30 units inside a 64-unit-tall lockup


def outline(text: str, wght: int) -> tuple[str, float]:
    font = instancer.instantiateVariableFont(TTFont(FONT), {"wght": wght})
    glyphs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
    x, paths = 0, []
    for ch in text:
        name = cmap[ord(ch)]
        if ch == " ":
            x += hmtx[name][0]
            continue
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        paths.append(f'<path transform="translate({x} 0)" d="{pen.getCommands()}"/>')
        x += hmtx[name][0] - 12  # slight tightening for display sizes
    return "".join(paths), x


def svg(view_w: float, view_h: float, title: str, body: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {view_w:.0f} {view_h:.0f}" role="img" '
            f'aria-label="{title}"><title>{title}</title>{body}</svg>\n')


def tile(fill: str, glyph: str) -> str:
    return f'<rect width="64" height="64" rx="14" fill="{fill}"/>{ML}{glyph}'


def main() -> None:
    word, word_w = outline("MakerLine", 760)
    idea, idea_w = outline("Idea", 520)
    ww, iw = word_w * SCALE, idea_w * SCALE

    def wordmark(fill: str, x: float, opacity: str = "") -> str:
        op = f' opacity="{opacity}"' if opacity else ""
        return f'<g fill="{fill}"{op} transform="translate({x:.1f} 47) scale({SCALE:.5f} -{SCALE:.5f})">{word}</g>'

    def idea_word(fill: str, x: float) -> str:
        return f'<g fill="{fill}" opacity=".78" transform="translate({x:.1f} 47) scale({SCALE:.5f} -{SCALE:.5f})">{idea}</g>'

    files = {
        "makerline-mark.svg": svg(64, 64, "MakerLine", tile(BLUE, "")),
        "makerline-mark-on-dark.svg": svg(64, 64, "MakerLine", tile(BLUE_DARK, "")),
        "makerline-idea-mark.svg": svg(64, 64, "MakerLine Idea", tile(GREEN, SPARK)),
        "makerline-idea-mark-on-dark.svg": svg(64, 64, "MakerLine Idea", tile(GREEN_DARK, SPARK)),
        "makerline-logo.svg": svg(82 + ww, 64, "MakerLine", tile(BLUE, "") + wordmark(INK, 82)),
        "makerline-logo-on-dark.svg": svg(82 + ww, 64, "MakerLine", tile(BLUE_DARK, "") + wordmark("#FFFFFF", 82)),
        "makerline-idea-logo.svg": svg(82 + ww + 14 + iw, 64, "MakerLine Idea",
                                       tile(GREEN, SPARK) + wordmark(INK, 82) + idea_word(INK, 82 + ww + 14)),
        "makerline-idea-logo-on-dark.svg": svg(82 + ww + 14 + iw, 64, "MakerLine Idea",
                                               tile(GREEN_DARK, SPARK) + wordmark("#FFFFFF", 82)
                                               + idea_word("#FFFFFF", 82 + ww + 14)),
        "makerline-wordmark.svg": svg(ww, 34, "MakerLine",
                                      f'<g fill="{INK}" transform="translate(0 31) scale({SCALE:.5f} -{SCALE:.5f})">{word}</g>'),
    }
    # Signature: the wordmark with the line-into-tick underneath, for places without the icon.
    x1, x2, x3 = ww - 26, ww - 19, ww - 4
    tick = TICK_LINE.format(x1=f"{x1:.0f}", x2=f"{x2:.0f}", x3=f"{x3:.0f}")
    files["makerline-signature.svg"] = svg(
        ww + 2, 58, "MakerLine",
        f'<g fill="{INK}" transform="translate(1 31) scale({SCALE:.5f} -{SCALE:.5f})">{word}</g>'
        f'<path transform="translate(0 38)" d="{tick}" fill="none" stroke="{BLUE}" stroke-width="5" '
        'stroke-linecap="round" stroke-linejoin="round"/>')
    # The bare line-into-tick, used under the site's headline.
    files["line-tick.svg"] = svg(240, 24, "", f'<path transform="translate(0 2)" d="{TICK_LINE.format(x1=200, x2=208, x3=226)}" '
                                 f'fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')

    for name, text in files.items():
        (HERE / name).write_text(text, encoding="utf-8")
    (SITE / "favicon.svg").write_text(files["makerline-mark.svg"], encoding="utf-8")
    (SITE / "mark-on-dark.svg").write_text(files["makerline-mark-on-dark.svg"], encoding="utf-8")
    print(f"Wrote {len(files)} SVGs to {HERE.relative_to(ROOT)} and the favicon SVGs to {SITE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
