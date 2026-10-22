"""Build the macOS app bundle with py2app (macOS only).

    pip install -r requirements.txt -r requirements-build.txt
    python3 setup.py py2app          → dist/BreakReminder.app
    scripts/build_dmg.sh             → dist/BreakReminder.dmg (signs ad hoc first)

py2app docs: https://py2app.readthedocs.io/ (options: plist, iconfile, packages).
"""

from setuptools import setup

from app.core.config import APP_NAME, BUNDLE_ID, DISPLAY_NAME, VERSION

OPTIONS = {
    # Include the whole app package (py2app can miss modules imported inside functions).
    "packages": ["app"],
    "plist": {
        "CFBundleName": APP_NAME,
        "CFBundleDisplayName": DISPLAY_NAME,
        "CFBundleIdentifier": BUNDLE_ID,
        "CFBundleShortVersionString": VERSION,
        "CFBundleVersion": VERSION,
        # Menu-bar only: no Dock icon, no app menu.
        "LSUIElement": True,
        # SMAppService (Open at login) and SF Symbols need macOS 13; older Macs can't run it.
        "LSMinimumSystemVersion": "13.0",
        "NSHighResolutionCapable": True,
        "NSHumanReadableCopyright": "MIT licence",
    },
    # Add "iconfile": "design/AppIcon.icns" once you have an icon (see README → Build).
}

setup(
    name=APP_NAME,
    version=VERSION,
    app=["app/main.py"],
    options={"py2app": OPTIONS},
)
