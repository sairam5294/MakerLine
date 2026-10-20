"""Words for the optional "Open at login" setting. Pure Python, so the copy is tested anywhere."""

MANUAL_STEPS = "System Settings → General → Login Items → + (then choose the app)"


def login_item_help(available: bool, requires_approval: bool) -> str:
    """Explain the setting in plain words, including what to do when the switch can't be used.

    Why it can be unavailable: macOS only lets a real, built .app register itself to open at
    login (Apple's SMAppService, macOS 13 or later). Running from source (python3 -m app.main)
    is a Python process, not an app, so we explain the manual route instead of failing silently.
    """
    if not available:
        return f"Available in the built app on macOS 13 or later. You can also add it yourself: {MANUAL_STEPS}."
    if requires_approval:
        return "macOS needs your OK first: open System Settings → General → Login Items and allow it."
    return "Starts the app quietly in the menu bar when you log in. Turn off any time."
