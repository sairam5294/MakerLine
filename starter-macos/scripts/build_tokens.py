#!/usr/bin/env python3
"""Generate app/ui/palette.py from design/tokens.json (the kit's single source of design tokens).

    python3 scripts/build_tokens.py           write app/ui/palette.py
    python3 scripts/build_tokens.py --check   exit 1 if palette.py is out of date (CI uses this)

Why generate instead of hand-copying hex values: designers change tokens.json (or sync it from
Figma); this script turns it into Python, and --check fails CI if someone edits one without the
other ("token drift"). Pure Python, so it runs on Linux CI too.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "design" / "tokens.json"
PALETTE = ROOT / "app" / "ui" / "palette.py"
_REF = re.compile(r"^\{([^}]+)\}$")


def load_tokens(path: Path = TOKENS) -> dict[str, Any]:
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return data


def resolve(tokens: dict[str, Any], value: Any) -> Any:
    """Follow W3C token references like "{color.palette.blue600}" to the real value."""
    seen = set()
    while isinstance(value, str) and (match := _REF.match(value)):
        ref = match.group(1)
        if ref in seen:
            raise ValueError(f"circular token reference {ref}")
        seen.add(ref)
        node: Any = tokens
        for part in ref.split("."):
            node = node[part]
        value = node["$value"]
    return value


def _px(value: str) -> int:
    # Token dimensions are written in px. On macOS 1 px in a design file = 1 pt on screen.
    return int(round(float(value.removesuffix("px"))))


def mode_colors(tokens: dict[str, Any], mode: str) -> dict[str, str]:
    group = tokens["color"][mode]
    return {name: resolve(tokens, group[name]["$value"]).upper() for name in sorted(group) if not name.startswith("$")}


def render(tokens: dict[str, Any]) -> str:
    """The exact text of palette.py. Formatted the way `ruff format` would, so lint stays green."""
    light = mode_colors(tokens, "light")
    dark = mode_colors(tokens, "dark")
    pairs = tokens["$extensions"]["productKit"]["contrastPairs"]
    space = {k: _px(v["$value"]) for k, v in tokens["space"].items() if not k.startswith("$")}
    min_target = _px(tokens["size"]["minTouchTarget"]["$value"])

    def dict_block(name: str, kind: str, values: dict[str, Any]) -> list[str]:
        lines = [f"{name}: dict[str, {kind}] = {{"]
        lines += [f'    "{k}": {json.dumps(v)},' for k, v in values.items()]
        return lines + ["}"]

    out = [
        '"""Design tokens for the AppKit layer. GENERATED from design/tokens.json — do not edit.',
        "",
        "Change design/tokens.json, then run: python3 scripts/build_tokens.py",
        "Plain Python (no AppKit), so the contrast check and tests run on any OS.",
        '"""',
        "",
        "# Semantic colours, light appearance (sRGB hex).",
        *dict_block("LIGHT", "str", light),
        "",
        "# Semantic colours, dark appearance (sRGB hex).",
        *dict_block("DARK", "str", dark),
        "",
        "# (foreground, background, minimum WCAG contrast ratio) — checked in light and dark.",
        "CONTRAST_PAIRS: tuple[tuple[str, str, float], ...] = (",
        *[f'    ("{p["fg"]}", "{p["bg"]}", {float(p["min"])}),' for p in pairs],
        ")",
        "",
        "# Spacing scale in points.",
        *dict_block("SPACE", "int", space),
        "",
        "# Smallest clickable target in points (WCAG 2.5.8 asks 24; Apple and the kit ask 44+).",
        f"MIN_TARGET_PT = {min_target}",
        "",
    ]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    text = render(load_tokens())
    if "--check" in argv:
        current = PALETTE.read_text(encoding="utf-8") if PALETTE.exists() else ""
        if current != text:
            print("✗ app/ui/palette.py is out of date with design/tokens.json.")
            print("  Run: python3 scripts/build_tokens.py")
            return 1
        print("✓ palette.py matches design/tokens.json")
        return 0
    PALETTE.write_text(text, encoding="utf-8")
    print(f"✓ wrote {PALETTE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
