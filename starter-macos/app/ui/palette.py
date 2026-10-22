"""Design tokens for the AppKit layer. GENERATED from design/tokens.json — do not edit.

Change design/tokens.json, then run: python3 scripts/build_tokens.py
Plain Python (no AppKit), so the contrast check and tests run on any OS.
"""

# Semantic colours, light appearance (sRGB hex).
LIGHT: dict[str, str] = {
    "background": "#FFFFFF",
    "border": "#5C5C66",
    "danger": "#B42318",
    "focusRing": "#1F5FD1",
    "primary": "#1F5FD1",
    "primaryPressed": "#174CAB",
    "success": "#1E7A46",
    "surface": "#F7F7F8",
    "textOnPrimary": "#FFFFFF",
    "textPrimary": "#16161A",
    "textSecondary": "#5C5C66",
}

# Semantic colours, dark appearance (sRGB hex).
DARK: dict[str, str] = {
    "background": "#16161A",
    "border": "#C4C4CC",
    "danger": "#FF8A80",
    "focusRing": "#7AA7FF",
    "primary": "#7AA7FF",
    "primaryPressed": "#A6C4FF",
    "success": "#6FD39A",
    "surface": "#2A2A31",
    "textOnPrimary": "#16161A",
    "textPrimary": "#F7F7F8",
    "textSecondary": "#C4C4CC",
}

# (foreground, background, minimum WCAG contrast ratio) — checked in light and dark.
CONTRAST_PAIRS: tuple[tuple[str, str, float], ...] = (
    ("textPrimary", "background", 4.5),
    ("textPrimary", "surface", 4.5),
    ("textSecondary", "background", 4.5),
    ("textSecondary", "surface", 4.5),
    ("textOnPrimary", "primary", 4.5),
    ("textOnPrimary", "primaryPressed", 4.5),
    ("primary", "background", 4.5),
    ("danger", "background", 4.5),
    ("success", "background", 4.5),
    ("border", "background", 3.0),
    ("focusRing", "background", 3.0),
)

# Spacing scale in points.
SPACE: dict[str, int] = {
    "xs": 4,
    "sm": 8,
    "md": 16,
    "lg": 24,
    "xl": 32,
    "xxl": 48,
}

# Smallest clickable target in points (WCAG 2.5.8 asks 24; Apple and the kit ask 44+).
MIN_TARGET_PT = 48
