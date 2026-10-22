"""Start the menu-bar app.

python3 -m app.main             run it (look for the cup icon in the menu bar)
python3 -m app.main --preview   also show the reminder straight away (for testing)
"""

from __future__ import annotations

import logging
import sys


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    # Logs go to stderr (and Console.app when built). We log warnings, never personal data.
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    try:
        from AppKit import NSApplication, NSApplicationActivationPolicyAccessory
        from PyObjCTools import AppHelper
    except ImportError:
        print("This app needs macOS with PyObjC: pip install -r requirements.txt", file=sys.stderr)
        return 1

    from app.ui.menu_bar import AppDelegate

    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    delegate.preview = "--preview" in argv
    app.setDelegate_(delegate)  # Cocoa keeps delegates weakly; `delegate` lives until exit
    # Accessory = menu-bar only: no Dock icon and no app menu (LSUIElement does the same in the .app).
    app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
    AppHelper.runEventLoop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
