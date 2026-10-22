#!/usr/bin/env python3
"""Fail if any token colour pair misses WCAG 2.2 AA, in light, dark and Increase Contrast.

    python3 scripts/check_contrast.py

- Text pairs (foreground token starts with "text", or the pair asks for 4.5) need >= 4.5:1
  (WCAG 1.4.3). Borders, focus rings and other graphics need >= 3:1 (WCAG 1.4.11).
- Also fails if app/ui/palette.py is out of date with design/tokens.json, because then we
  would be checking colours the app doesn't actually draw.
Pure Python: runs on Linux CI without AppKit.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import build_tokens  # noqa: E402  (needs the sys.path lines above)

from app.ui import palette, theme  # noqa: E402

TEXT_MIN = 4.5
GRAPHIC_MIN = 3.0


def required(fg: str, declared: float) -> float:
    return max(declared, TEXT_MIN if fg.startswith("text") else GRAPHIC_MIN)


def failures() -> list[str]:
    problems = []
    for dark in (False, True):
        for high_contrast in (False, True):
            mode = ("dark" if dark else "light") + (" + Increase Contrast" if high_contrast else "")
            for fg, bg, declared in palette.CONTRAST_PAIRS:
                need = required(fg, declared)
                fg_hex = theme.resolve(fg, dark, high_contrast)
                bg_hex = theme.resolve(bg, dark, high_contrast)
                ratio = theme.contrast(fg_hex, bg_hex)
                status = "✓" if ratio >= need else "✗"
                print(f"  {status} {mode:28} {fg:15} on {bg:15} {ratio:5.2f}:1 (needs {need})")
                if ratio < need:
                    problems.append(f"{mode}: {fg} {fg_hex} on {bg} {bg_hex} = {ratio:.2f}:1 < {need}")
    return problems


def main() -> int:
    if build_tokens.render(build_tokens.load_tokens()) != build_tokens.PALETTE.read_text(encoding="utf-8"):
        print("✗ app/ui/palette.py is out of date with design/tokens.json — run: python3 scripts/build_tokens.py")
        return 1
    problems = failures()
    if problems:
        print("\n✗ Contrast failures:\n  " + "\n  ".join(problems))
        return 1
    print("✓ Every colour pair meets WCAG 2.2 AA in light, dark and Increase Contrast.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
