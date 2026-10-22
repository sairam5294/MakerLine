"""Token colours as AppKit dynamic colours.

A dynamic NSColor asks "which appearance am I drawn in?" every time it is drawn, so the
window follows Dark Mode and Increase Contrast live — no restart, no observers to wire up.
The hex values come from palette.py (generated from design/tokens.json), never typed here.
"""

from __future__ import annotations

from typing import Any

from AppKit import (
    NSAppearanceNameAccessibilityHighContrastAqua,
    NSAppearanceNameAccessibilityHighContrastDarkAqua,
    NSAppearanceNameAqua,
    NSAppearanceNameDarkAqua,
    NSColor,
)

from app.ui import theme

# Listing the high-contrast names makes macOS tell us when Increase Contrast is on.
_APPEARANCES = [
    NSAppearanceNameAqua,
    NSAppearanceNameDarkAqua,
    NSAppearanceNameAccessibilityHighContrastAqua,
    NSAppearanceNameAccessibilityHighContrastDarkAqua,
]
_DARK = (NSAppearanceNameDarkAqua, NSAppearanceNameAccessibilityHighContrastDarkAqua)
_HIGH_CONTRAST = (
    NSAppearanceNameAccessibilityHighContrastAqua,
    NSAppearanceNameAccessibilityHighContrastDarkAqua,
)


def _srgb(hex_color: str) -> Any:
    # WCAG contrast is defined in sRGB and the tokens are sRGB, so draw them as sRGB too.
    r, g, b = theme.hex_to_rgb(hex_color)
    return NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255, g / 255, b / 255, 1.0)


def token_color(name: str) -> Any:
    """An NSColor for a semantic token (e.g. "textPrimary") that adapts to the appearance."""

    def provider(appearance: Any) -> Any:
        match = appearance.bestMatchFromAppearancesWithNames_(_APPEARANCES)
        return _srgb(theme.resolve(name, dark=match in _DARK, high_contrast=match in _HIGH_CONTRAST))

    return NSColor.colorWithName_dynamicProvider_(name, provider)
