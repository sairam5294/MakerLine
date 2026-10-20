"""The menu-bar item, its menu, and the controller that ties settings, timer and windows together."""

from __future__ import annotations

import dataclasses
import logging
import time
from collections.abc import Callable
from typing import Any

from AppKit import (
    NSAboutPanelOptionApplicationName,
    NSAboutPanelOptionApplicationVersion,
    NSApplication,
    NSImage,
    NSMenu,
    NSMenuItem,
    NSObject,
    NSRunLoop,
    NSRunLoopCommonModes,
    NSStatusBar,
    NSTimer,
    NSVariableStatusItemLength,
)

from app.core import settings as settings_store
from app.core.config import DISPLAY_NAME, VERSION
from app.core.scheduler import ReminderScheduler
from app.ui import controls
from app.ui.login_item import LoginItem
from app.ui.preferences_window import PreferencesWindow
from app.ui.reminder_window import ReminderWindow, bring_app_forward

log = logging.getLogger(__name__)

# How often we check whether a reminder is due. 10 s is accurate enough for a break reminder
# and costs effectively nothing in battery.
TICK_SECONDS = 10.0


def pause_title(paused: bool) -> str:
    return "Resume Reminders" if paused else "Pause Reminders"


def build_menu(handlers: dict[str, Callable[[Any], None]], keep: list[Any], paused: bool) -> tuple[Any, dict[str, Any]]:
    """The status menu. Returned items let the controller update titles later.

    Keyboard equivalents follow Mac convention: Cmd+, opens Preferences, Cmd+Q quits.
    (They work while the menu is open; a menu-bar app has no always-on app menu.)
    """
    menu = NSMenu.alloc().initWithTitle_(DISPLAY_NAME)

    def item(key: str, title: str, shortcut: str = "") -> Any:
        mi = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(title, "fire:", shortcut)
        mi.setTarget_(controls.target(handlers[key], keep))
        menu.addItem_(mi)
        return mi

    # First line says the state in words (never by icon or colour alone). It has no action,
    # so macOS shows it greyed out and VoiceOver reads it as information, not a command.
    status = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("", None, "")
    menu.addItem_(status)
    menu.addItem_(NSMenuItem.separatorItem())
    items = {"status": status, "pause": item("pause", pause_title(paused))}
    menu.addItem_(NSMenuItem.separatorItem())
    items["preferences"] = item("preferences", "Preferences…", ",")
    items["about"] = item("about", f"About {DISPLAY_NAME}")
    menu.addItem_(NSMenuItem.separatorItem())
    items["quit"] = item("quit", f"Quit {DISPLAY_NAME}", "q")
    return menu, items


class MenuBarApp:
    def __init__(self) -> None:
        self._keep: list[Any] = []
        self.settings = settings_store.load()
        self.scheduler = ReminderScheduler(self.settings.interval_minutes, time.monotonic(), self.settings.paused)
        self.login = LoginItem()
        self.reminder = ReminderWindow(on_done=self._done, on_not_now=self._not_now)
        self.preferences: PreferencesWindow | None = None
        self.status_item: Any = None
        self.timer: Any = None

    # ----- setup -------------------------------------------------------------------------
    def start(self) -> None:
        self.status_item = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)
        handlers = {
            "pause": lambda _s: self.toggle_pause(),
            "preferences": lambda _s: self.open_preferences(),
            "about": lambda _s: self.open_about(),
            "quit": lambda _s: NSApplication.sharedApplication().terminate_(None),
        }
        menu, self.items = build_menu(handlers, self._keep, self.scheduler.paused)
        self.status_item.setMenu_(menu)
        self.timer = NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_(
            TICK_SECONDS, controls.target(lambda _t: self.tick(), self._keep), "fire:", None, True
        )
        # Common modes: keep ticking while a menu is open or a window is being dragged.
        NSRunLoop.currentRunLoop().addTimer_forMode_(self.timer, NSRunLoopCommonModes)
        self.refresh()

    # ----- state -------------------------------------------------------------------------
    def refresh(self) -> None:
        """Update the menu-bar icon, tooltip and status line after anything changes."""
        now = time.monotonic()
        text = self.scheduler.status_text(now)
        self.items["status"].setTitle_(text)
        self.items["pause"].setTitle_(pause_title(self.scheduler.paused))
        button = self.status_item.button()
        # SF Symbols are template images: macOS tints them for light/dark menu bars itself.
        symbol = "pause.circle" if self.scheduler.paused else "cup.and.saucer"
        image = NSImage.imageWithSystemSymbolName_accessibilityDescription_(symbol, f"{DISPLAY_NAME}: {text}")
        if image is not None:
            button.setImage_(image)
        else:  # very old macOS without SF Symbols: fall back to words
            button.setTitle_(DISPLAY_NAME)
        button.setAccessibilityLabel_(f"{DISPLAY_NAME}: {text}")
        button.setToolTip_(text)

    def tick(self) -> None:
        if self.reminder.visible:
            return  # one reminder at a time; never stack windows
        if self.scheduler.due(time.monotonic()):
            self.reminder.show(self.scheduler.interval_minutes, self.settings.sound_enabled)
        self.refresh()

    def _save(self, **changes: Any) -> None:
        self.settings = dataclasses.replace(self.settings, **changes)
        try:
            settings_store.save(self.settings)
        except OSError as exc:  # full disk, permissions: keep running with the in-memory value
            log.warning("Could not save settings: %s", exc)

    # ----- actions -----------------------------------------------------------------------
    def _done(self) -> None:
        self.scheduler.complete(time.monotonic())
        self.reminder.hide()
        self.refresh()

    def _not_now(self) -> None:
        self.scheduler.snooze(time.monotonic())
        self.reminder.hide()
        self.refresh()

    def toggle_pause(self) -> None:
        if self.scheduler.paused:
            self.scheduler.resume(time.monotonic())
        else:
            self.scheduler.pause()
        self._save(paused=self.scheduler.paused)
        self.refresh()

    def preferences_changed(self, changes: dict[str, Any]) -> None:
        self._save(**changes)
        if "interval_minutes" in changes:
            self.scheduler.set_interval(self.settings.interval_minutes, time.monotonic())
        self.refresh()

    def open_preferences(self) -> None:
        # Rebuilt each time it opens so it always shows the current settings.
        if self.preferences is None or not self.preferences.window.isVisible():
            self.preferences = PreferencesWindow(self.settings, self.preferences_changed, self.login)
        self.preferences.show()

    def open_about(self) -> None:
        bring_app_forward()
        NSApplication.sharedApplication().orderFrontStandardAboutPanelWithOptions_(
            {NSAboutPanelOptionApplicationName: DISPLAY_NAME, NSAboutPanelOptionApplicationVersion: VERSION}
        )

    def show_reminder_now(self) -> None:
        """Used by `--preview`: see the reminder immediately (handy for VoiceOver testing)."""
        self.reminder.show(self.scheduler.interval_minutes, self.settings.sound_enabled)


class AppDelegate(NSObject):
    """Cocoa calls this once the app has launched; that's when it's safe to add a menu-bar item."""

    def applicationDidFinishLaunching_(self, _notification: Any) -> None:
        self.controller = MenuBarApp()
        self.controller.start()
        if getattr(self, "preview", False):
            self.controller.show_reminder_now()
