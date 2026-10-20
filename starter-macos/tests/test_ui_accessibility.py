"""Build the real windows and menu and check they are accessible. macOS only.

On Linux (no AppKit) the whole file is skipped; the macOS CI job runs it.
"""

import pytest

AppKit = pytest.importorskip("AppKit", reason="AppKit UI tests run on macOS only")

from app.core.config import ALLOWED_INTERVALS  # noqa: E402
from app.core.settings import Settings  # noqa: E402
from app.ui import palette  # noqa: E402
from app.ui.login_item import LoginItem  # noqa: E402
from app.ui.menu_bar import build_menu  # noqa: E402
from app.ui.preferences_window import PreferencesWindow  # noqa: E402
from app.ui.reminder_window import ReminderWindow  # noqa: E402


@pytest.fixture(scope="module", autouse=True)
def application():
    # Windows need an NSApplication to exist; we never start its event loop.
    return AppKit.NSApplication.sharedApplication()


def all_views(view):
    yield view
    for sub in view.subviews():
        yield from all_views(sub)


def interactive(window):
    window.contentView().layoutSubtreeIfNeeded()
    return [
        v
        for v in all_views(window.contentView())
        if isinstance(v, AppKit.NSControl) and not isinstance(v, AppKit.NSTextField)
    ]


def assert_accessible(window):
    controls = interactive(window)
    assert controls, "window has no controls"
    for control in controls:
        name = control.accessibilityLabel()
        assert name, f"{control} has no accessibility label"
        assert control.accessibilityRole(), f"{name} has no accessibility role"
        size = control.frame().size
        assert size.height >= palette.MIN_TARGET_PT, f"{name} is {size.height} pt tall"
        assert size.width >= palette.MIN_TARGET_PT, f"{name} is {size.width} pt wide"
    for label in (v for v in all_views(window.contentView()) if isinstance(v, AppKit.NSTextField)):
        assert label.accessibilityRole() == AppKit.NSAccessibilityStaticTextRole
        assert not label.isSelectable(), "plain text should not be a Tab stop"


def test_reminder_window_is_accessible():
    w = ReminderWindow(on_done=lambda: None, on_not_now=lambda: None)
    assert w.window.title()
    assert_accessible(w.window)


def test_reminder_keyboard_return_is_done_and_esc_is_not_now():
    calls = []
    w = ReminderWindow(on_done=lambda: calls.append("done"), on_not_now=lambda: calls.append("not now"))
    assert w.done.keyEquivalent() == "\r"
    assert w.not_now.keyEquivalent() == "\x1b"
    assert w.window.initialFirstResponder() == w.done
    w.done.performClick_(None)
    w.not_now.performClick_(None)
    assert calls == ["done", "not now"]


def test_reminder_roles_are_buttons():
    w = ReminderWindow(on_done=lambda: None, on_not_now=lambda: None)
    assert w.done.accessibilityRole() == AppKit.NSAccessibilityButtonRole
    assert w.not_now.accessibilityRole() == AppKit.NSAccessibilityButtonRole


def test_reminder_message_is_words_not_colour():
    w = ReminderWindow(on_done=lambda: None, on_not_now=lambda: None)
    assert "Done" in w.message(30) and "Not now" in w.message(30)


def test_preferences_window_is_accessible_and_saves_changes():
    changes: list[dict] = []
    p = PreferencesWindow(Settings(), changes.append, LoginItem())
    assert_accessible(p.window)
    assert p.interval.accessibilityLabel() == "Remind me every"
    assert p.interval.numberOfItems() == len(ALLOWED_INTERVALS)
    p.interval.selectItemAtIndex_(0)
    p.interval.sendAction_to_(p.interval.action(), p.interval.target())
    assert changes[-1] == {"interval_minutes": ALLOWED_INTERVALS[0]}
    p.sound.performClick_(None)
    assert changes[-1] == {"sound_enabled": False}


def test_open_at_login_is_disabled_and_explained_when_running_from_source():
    p = PreferencesWindow(Settings(), lambda _c: None, LoginItem())
    assert not p.login_box.isEnabled()
    assert "System Settings" in p.login_help.stringValue()


def test_status_menu_items_have_titles_and_conventional_shortcuts():
    handlers = {k: (lambda _s: None) for k in ("pause", "preferences", "about", "quit")}
    menu, items = build_menu(handlers, [], paused=False)
    for mi in menu.itemArray():
        if not mi.isSeparatorItem() and mi is not items["status"]:
            assert mi.title(), "every menu item needs a visible (and spoken) title"
    assert items["preferences"].keyEquivalent() == ","
    assert items["quit"].keyEquivalent() == "q"
    assert items["pause"].title() == "Pause Reminders"
