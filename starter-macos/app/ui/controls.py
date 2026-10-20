"""Small building blocks every window uses, so accessibility is built in once, not per screen.

- Every interactive control gets an explicit accessibility label (what VoiceOver says).
- Every clickable control is at least MIN_TARGET_PT tall and wide (WCAG 2.5.8; Apple asks 44 pt).
- Text uses Apple's text styles and Auto Layout, so longer translations or larger fonts wrap
  instead of being cut off.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import AppKit
import objc
from AppKit import (
    NSButton,
    NSControlSizeLarge,
    NSEventModifierFlagCommand,
    NSFont,
    NSObject,
    NSPopUpButton,
    NSStackView,
    NSTextField,
    NSUserInterfaceLayoutOrientationHorizontal,
    NSUserInterfaceLayoutOrientationVertical,
    NSView,
    NSWindow,
    NSWindowStyleMaskClosable,
)
from Foundation import NSMakeRect

from app.ui import palette
from app.ui.colors import token_color

# A push button whose bezel grows with its frame, so a 48 pt-tall button also LOOKS 48 pt tall.
# Apple renamed this style in macOS 14; the old name is the same value on older systems.
FLEXIBLE_PUSH = getattr(AppKit, "NSBezelStyleFlexiblePush", AppKit.NSBezelStyleRegularSquare)

RETURN_KEY = "\r"
ESCAPE_KEY = "\x1b"


class CallbackTarget(NSObject):
    """Lets a plain Python function be a Cocoa button/menu/timer target.

    Cocoa only holds a *weak* reference to a control's target, so whoever creates one must
    keep it alive (we keep them in a list on the window/controller object).
    """

    @objc.python_method
    def bind(self, callback: Callable[[Any], None]) -> CallbackTarget:
        self._callback = callback
        return self

    def fire_(self, sender: Any) -> None:
        self._callback(sender)


def target(callback: Callable[[Any], None], keep: list[Any]) -> Any:
    t = CallbackTarget.alloc().init().bind(callback)
    keep.append(t)
    return t


def min_target_size(view: Any) -> None:
    view.setTranslatesAutoresizingMaskIntoConstraints_(False)
    view.heightAnchor().constraintGreaterThanOrEqualToConstant_(palette.MIN_TARGET_PT).setActive_(True)
    view.widthAnchor().constraintGreaterThanOrEqualToConstant_(palette.MIN_TARGET_PT).setActive_(True)


def button(
    title: str,
    callback: Callable[[Any], None],
    keep: list[Any],
    key: str = "",
    help_text: str | None = None,
) -> Any:
    """A labelled push button. key=RETURN_KEY makes it the default (blue) button; ESCAPE_KEY = cancel."""
    b = NSButton.buttonWithTitle_target_action_(title, target(callback, keep), "fire:")
    b.setBezelStyle_(FLEXIBLE_PUSH)
    b.setControlSize_(NSControlSizeLarge)
    b.setKeyEquivalent_(key)
    b.setAccessibilityLabel_(title)
    if help_text:
        # VoiceOver reads the help after a pause; the tooltip shows it to mouse users.
        b.setAccessibilityHelp_(help_text)
        b.setToolTip_(help_text)
    min_target_size(b)
    return b


def checkbox(title: str, checked: bool, callback: Callable[[Any], None], keep: list[Any]) -> Any:
    c = NSButton.checkboxWithTitle_target_action_(title, target(callback, keep), "fire:")
    c.setState_(1 if checked else 0)
    c.setAccessibilityLabel_(title)
    min_target_size(c)
    return c


def popup(label: str, titles: list[str], selected: int, callback: Callable[[Any], None], keep: list[Any]) -> Any:
    p = NSPopUpButton.alloc().initWithFrame_pullsDown_(NSMakeRect(0, 0, 200, 32), False)
    p.addItemsWithTitles_(titles)
    p.selectItemAtIndex_(selected)
    p.setTarget_(target(callback, keep))
    p.setAction_("fire:")
    p.setControlSize_(NSControlSizeLarge)
    # The visible label sits next to the pop-up; VoiceOver needs it on the control itself.
    p.setAccessibilityLabel_(label)
    min_target_size(p)
    return p


def text(value: str, style: str, color_token: str, width: float = 360) -> Any:
    """A read-only, wrapping label in an Apple text style (e.g. AppKit.NSFontTextStyleBody)."""
    t = NSTextField.wrappingLabelWithString_(value)
    t.setFont_(NSFont.preferredFontForTextStyle_options_(style, {}))
    t.setTextColor_(token_color(color_token))
    # Not selectable: otherwise Tab would stop on plain text between the buttons.
    t.setSelectable_(False)
    t.setPreferredMaxLayoutWidth_(width)
    return t


def stack(views: list[Any], vertical: bool = True, spacing: float | None = None) -> Any:
    s = NSStackView.stackViewWithViews_(views)
    orientation = NSUserInterfaceLayoutOrientationVertical if vertical else NSUserInterfaceLayoutOrientationHorizontal
    s.setOrientation_(orientation)
    s.setAlignment_(AppKit.NSLayoutAttributeLeading if vertical else AppKit.NSLayoutAttributeCenterY)
    s.setSpacing_(palette.SPACE["md"] if spacing is None else spacing)
    return s


def trailing_row(views: list[Any]) -> Any:
    """Buttons pushed to the right, primary last — the macOS convention."""
    row = NSStackView.alloc().init()
    row.setOrientation_(NSUserInterfaceLayoutOrientationHorizontal)
    row.setSpacing_(palette.SPACE["sm"])
    for v in views:
        row.addView_inGravity_(v, AppKit.NSStackViewGravityTrailing)
    return row


class KeyboardWindow(NSWindow):
    """A window that closes with Esc and Cmd+W, like standard Mac windows.

    A menu-bar app has no app menu, so the usual File → Close (Cmd+W) shortcut doesn't exist;
    we handle it here. Windows without a close button ignore both (the reminder has its own
    Esc button instead).
    """

    def cancelOperation_(self, sender: Any) -> None:
        if self.styleMask() & NSWindowStyleMaskClosable:
            self.performClose_(sender)

    def performKeyEquivalent_(self, event: Any) -> bool:
        if (
            event.modifierFlags() & NSEventModifierFlagCommand
            and event.charactersIgnoringModifiers() == "w"
            and self.styleMask() & NSWindowStyleMaskClosable
        ):
            self.performClose_(self)
            return True
        return bool(objc.super(KeyboardWindow, self).performKeyEquivalent_(event))


def content(window: Any, body: Any, full_width: tuple[Any, ...] = (), width: float = 420) -> None:
    """Put a vertical stack in the window with token padding, and size the window to fit it.

    `full_width` rows (e.g. the button row) stretch across the window, so their trailing
    buttons line up with the right edge.
    """
    inset = palette.SPACE["lg"]
    body.setEdgeInsets_((inset, inset, inset, inset))
    body.setTranslatesAutoresizingMaskIntoConstraints_(False)
    # The window's content view stays a plain NSView (AppKit sizes it); the stack is pinned
    # to its four edges, so the window grows when text wraps onto more lines.
    container = NSView.alloc().initWithFrame_(NSMakeRect(0, 0, width, 100))
    window.setContentView_(container)
    container.addSubview_(body)
    for a, b in (
        (body.leadingAnchor(), container.leadingAnchor()),
        (body.trailingAnchor(), container.trailingAnchor()),
        (body.topAnchor(), container.topAnchor()),
        (body.bottomAnchor(), container.bottomAnchor()),
    ):
        a.constraintEqualToAnchor_(b).setActive_(True)
    body.widthAnchor().constraintGreaterThanOrEqualToConstant_(width).setActive_(True)
    for row in full_width:
        row.setTranslatesAutoresizingMaskIntoConstraints_(False)
        row.widthAnchor().constraintEqualToAnchor_constant_(body.widthAnchor(), -2 * inset).setActive_(True)
    window.setBackgroundColor_(token_color("background"))
    container.layoutSubtreeIfNeeded()
    window.setContentSize_(container.fittingSize())
    # Tab moves through controls in reading order (left to right, top to bottom).
    window.setAutorecalculatesKeyViewLoop_(True)
