"""Pick the right token colour for the current appearance. Pure Python (tested on any OS).

macOS has four appearances: light, dark, and an Increase Contrast version of each. The
tokens already pass WCAG AA; with Increase Contrast on we go further and swap softer
colours for the strongest one, because people who turn that setting on need it.
"""

from __future__ import annotations

from app.ui import palette

# With Increase Contrast on: secondary text and borders use the primary text colour.
HIGH_CONTRAST_SUBSTITUTES: dict[str, str] = {
    "textSecondary": "textPrimary",
    "border": "textPrimary",
}


def resolve(name: str, dark: bool, high_contrast: bool) -> str:
    """Hex colour for a semantic token name, e.g. resolve("textPrimary", dark=True, ...)."""
    colors = palette.DARK if dark else palette.LIGHT
    if high_contrast:
        name = HIGH_CONTRAST_SUBSTITUTES.get(name, name)
    return colors[name]


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    if len(value) != 6:
        raise ValueError(f"expected #RRGGBB, got {value!r}")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def _linear(channel: int) -> float:
    c = channel / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color: str) -> float:
    r, g, b = (_linear(c) for c in hex_to_rgb(hex_color))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg: str, bg: str) -> float:
    """WCAG 2.x contrast ratio between two hex colours (1.0 to 21.0)."""
    lighter, darker = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)
