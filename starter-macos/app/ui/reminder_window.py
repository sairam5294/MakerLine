"""The reminder: a small window (not a notification), built to be fully accessible.

Why a window and not a notification: notifications can be silenced by Focus modes, vanish
after a few seconds and can't hold more than one action reliably. A window stays until the
person answers it, and VoiceOver, keyboard and Switch Control can all reach it.

Keyboard: Return = Done (the default button), Esc = Not now. Tab moves between them.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import AppKit
from AppKit import (
    NSAccessibilityAnnouncementKey,
    NSAccessibilityAnnouncementRequestedNotification,
    NSAccessibilityPostNotificationWithUserInfo,
    NSAccessibilityPriorityHigh,
    NSAccessibilityPriorityKey,
    NSApplication,
    NSBackingStoreBuffered,
    NSFloatingWindowLevel,
    NSSound,
    NSWindowAnimationBehaviorDefault,
    NSWindowAnimationBehaviorNone,
    NSWindowCollectionBehaviorMoveToActiveSpace,
    NSWindowStyleMaskTitled,
    NSWorkspace,
)
from Foundation import NSMakeRect

from app.core.config import SNOOZE_MINUTES
from app.core.scheduler import interval_label
from app.ui import controls

TITLE = "Time for a break"


def bring_app_forward() -> None:
    """Make our windows able to take keyboard focus (menu-bar apps start in the background)."""
    app = NSApplication.sharedApplication()
    if hasattr(app, "activate"):
        # macOS 14+: "cooperative" activation. If you're mid-typing elsewhere macOS may keep
        # focus there — polite for an interruption; the window still appears on top.
        app.activate()
    else:
        app.activateIgnoringOtherApps_(True)


class ReminderWindow:
    def __init__(self, on_done: Callable[[], None], on_not_now: Callable[[], None]) -> None:
        self._keep: list[Any] = []  # keeps button targets alive (Cocoa holds them weakly)

        # Titled but not closable: the only ways out are the two clearly-named buttons
        # (or Return / Esc), so no reminder is ever dismissed by accident.
        self.window = controls.KeyboardWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(0, 0, 420, 200), NSWindowStyleMaskTitled, NSBackingStoreBuffered, False
        )
        self.window.setTitle_(TITLE)
        self.window.setReleasedWhenClosed_(False)  # Python owns this window; don't free it on close
        self.window.setLevel_(NSFloatingWindowLevel)  # above other apps' windows, like an alert
        self.window.setCollectionBehavior_(NSWindowCollectionBehaviorMoveToActiveSpace)

        self.heading = controls.text(TITLE, AppKit.NSFontTextStyleTitle2, "textPrimary")
        self.body = controls.text("", AppKit.NSFontTextStyleBody, "textSecondary")
        self.not_now = controls.button(
            "Not now",
            lambda _sender: on_not_now(),
            self._keep,
            key=controls.ESCAPE_KEY,
            help_text=f"Esc. Reminds you again in {SNOOZE_MINUTES} minutes.",
        )
        self.done = controls.button(
            "Done",
            lambda _sender: on_done(),
            self._keep,
            key=controls.RETURN_KEY,
            help_text="Return. Starts the next countdown.",
        )
        row = controls.trailing_row([self.not_now, self.done])
        controls.content(self.window, controls.stack([self.heading, self.body, row]), full_width=(row,))
        # Focus starts on the primary action, so Space or Return both work straight away.
        self.window.setInitialFirstResponder_(self.done)

    def message(self, interval_minutes: int) -> str:
        return (
            "Stand up, stretch and rest your eyes on something far away. "
            f"Done starts the next {interval_label(interval_minutes)} countdown; "
            f"Not now asks again in {SNOOZE_MINUTES} minutes."
        )

    @property
    def visible(self) -> bool:
        return bool(self.window.isVisible())

    def show(self, interval_minutes: int, play_sound: bool) -> None:
        self.body.setStringValue_(self.message(interval_minutes))
        self.window.contentView().layoutSubtreeIfNeeded()
        self.window.setContentSize_(self.window.contentView().fittingSize())
        # Reduce Motion: appear instantly instead of the zoom-in animation. Read every time,
        # because people change the setting while the app is running.
        reduce_motion = NSWorkspace.sharedWorkspace().accessibilityDisplayShouldReduceMotion()
        self.window.setAnimationBehavior_(
            NSWindowAnimationBehaviorNone if reduce_motion else NSWindowAnimationBehaviorDefault
        )
        self.window.center()
        bring_app_forward()
        self.window.makeKeyAndOrderFront_(None)
        self.window.makeFirstResponder_(self.done)
        if play_sound:
            sound = NSSound.soundNamed_("Glass")  # a built-in macOS sound; nothing to bundle
            if sound is not None:
                sound.play()
        # VoiceOver reads the window title and focused button; announce the message too,
        # so a screen-reader user hears the whole reminder without exploring the window.
        NSAccessibilityPostNotificationWithUserInfo(
            self.window,
            NSAccessibilityAnnouncementRequestedNotification,
            {
                NSAccessibilityAnnouncementKey: f"{TITLE}. {self.body.stringValue()}",
                NSAccessibilityPriorityKey: NSAccessibilityPriorityHigh,
            },
        )

    def hide(self) -> None:
        self.window.orderOut_(None)
