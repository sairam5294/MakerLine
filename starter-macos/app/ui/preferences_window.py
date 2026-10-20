"""Preferences: reminder interval, sound, and the optional Open at login.

Every change is saved the moment it's made (Mac convention: no Save button), so closing the
window — Done, Return, Esc, Cmd+W or the red close button — never loses anything.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import AppKit
from AppKit import (
    NSBackingStoreBuffered,
    NSWindowStyleMaskClosable,
    NSWindowStyleMaskTitled,
)
from Foundation import NSMakeRect

from app.core.config import ALLOWED_INTERVALS, DISPLAY_NAME
from app.core.login import login_item_help
from app.core.scheduler import interval_label
from app.core.settings import Settings
from app.ui import controls
from app.ui.login_item import LoginItem
from app.ui.reminder_window import bring_app_forward


class PreferencesWindow:
    def __init__(self, settings: Settings, on_change: Callable[[dict[str, Any]], None], login: LoginItem) -> None:
        self._keep: list[Any] = []
        self._on_change = on_change
        self._login = login

        self.window = controls.KeyboardWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(0, 0, 420, 260),
            NSWindowStyleMaskTitled | NSWindowStyleMaskClosable,
            NSBackingStoreBuffered,
            False,
        )
        self.window.setTitle_(f"{DISPLAY_NAME} Preferences")
        self.window.setReleasedWhenClosed_(False)

        label = "Remind me every"
        self.interval = controls.popup(
            label,
            [interval_label(m) for m in ALLOWED_INTERVALS],
            ALLOWED_INTERVALS.index(settings.interval_minutes),
            self._interval_changed,
            self._keep,
        )
        interval_row = controls.stack(
            [controls.text(label, AppKit.NSFontTextStyleBody, "textPrimary", width=160), self.interval],
            vertical=False,
        )
        self.sound = controls.checkbox(
            "Play a sound with each reminder", settings.sound_enabled, self._sound_changed, self._keep
        )
        self.login_box = controls.checkbox("Open at login", login.enabled, self._login_changed, self._keep)
        self.login_box.setEnabled_(login.available)
        self.login_help = controls.text("", AppKit.NSFontTextStyleCallout, "textSecondary")
        self._refresh_login_help()
        self.done = controls.button("Done", lambda _s: self.window.performClose_(None), self._keep, controls.RETURN_KEY)
        row = controls.trailing_row([self.done])
        body = controls.stack([interval_row, self.sound, self.login_box, self.login_help, row])
        controls.content(self.window, body, full_width=(row,))
        self.window.setInitialFirstResponder_(self.interval)

    def _refresh_login_help(self) -> None:
        self.login_help.setStringValue_(login_item_help(self._login.available, self._login.requires_approval))

    def _update(self, **changes: Any) -> None:
        # Send only what changed: the controller owns the full settings (e.g. "paused" is
        # changed from the menu), so this window can never overwrite them with stale values.
        self._on_change(changes)

    def _interval_changed(self, sender: Any) -> None:
        self._update(interval_minutes=ALLOWED_INTERVALS[int(sender.indexOfSelectedItem())])

    def _sound_changed(self, sender: Any) -> None:
        self._update(sound_enabled=bool(sender.state()))

    def _login_changed(self, sender: Any) -> None:
        self._login.set_enabled(bool(sender.state()))
        sender.setState_(1 if self._login.enabled else 0)  # show what macOS actually did
        self._refresh_login_help()

    def show(self) -> None:
        bring_app_forward()
        self.window.center()
        self.window.makeKeyAndOrderFront_(None)
