"""Design tokens: palette.py matches tokens.json, and every colour pair passes WCAG AA."""

import build_tokens
import check_contrast
import pytest

from app.core.login import login_item_help
from app.ui import palette, theme


def test_palette_is_generated_from_tokens():
    assert build_tokens.render(build_tokens.load_tokens()) == build_tokens.PALETTE.read_text(encoding="utf-8")


def test_light_and_dark_define_the_same_tokens():
    assert set(palette.LIGHT) == set(palette.DARK)


def test_contrast_formula_known_values():
    assert theme.contrast("#000000", "#FFFFFF") == pytest.approx(21.0)
    assert theme.contrast("#777777", "#777777") == pytest.approx(1.0)


def test_every_pair_passes_in_every_appearance():
    assert check_contrast.failures() == []


def test_text_pairs_need_at_least_aa():
    assert check_contrast.required("textSecondary", 3.0) == 4.5
    assert check_contrast.required("border", 3.0) == 3.0


@pytest.mark.parametrize("dark", [False, True])
def test_increase_contrast_never_lowers_contrast(dark):
    for fg, bg, _ in palette.CONTRAST_PAIRS:
        normal = theme.contrast(theme.resolve(fg, dark, False), theme.resolve(bg, dark, False))
        high = theme.contrast(theme.resolve(fg, dark, True), theme.resolve(bg, dark, True))
        assert high >= normal


def test_minimum_target_size_meets_apple_guidance():
    assert palette.MIN_TARGET_PT >= 44


def test_token_references_resolve_and_loops_fail():
    tokens = {"a": {"$value": "{b}"}, "b": {"$value": "{a}"}}
    with pytest.raises(ValueError):
        build_tokens.resolve(tokens, "{a}")


def test_login_help_always_explains_a_way_forward():
    assert "System Settings" in login_item_help(available=False, requires_approval=False)
    assert "System Settings" in login_item_help(available=True, requires_approval=True)
    assert login_item_help(available=True, requires_approval=False)
