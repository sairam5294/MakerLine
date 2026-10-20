"""Names and fixed choices for the app. Rename the app here (and only here).

Everything else (settings folder, bundle name, window titles, setup.py) reads these values,
so a rename is one edit instead of a search-and-replace across the project.
"""

# No spaces: used for the settings folder, the .app bundle and the DMG file name.
APP_NAME = "BreakReminder"
# What people see in the menu bar tooltip, window titles and the About panel.
DISPLAY_NAME = "Break Reminder"
# Reverse-DNS id macOS uses to tell apps apart. Change "com.example" to a domain you own.
BUNDLE_ID = "com.example.breakreminder"
VERSION = "0.1.0"

# Interval choices offered in Preferences. A short fixed list is easier to use (and to
# validate) than a free-text field, and covers the common "every 20/30/60 minutes" advice.
ALLOWED_INTERVALS: tuple[int, ...] = (15, 20, 30, 45, 60, 90)
DEFAULT_INTERVAL = 30
# "Not now" pushes the reminder back by this many minutes instead of skipping a whole cycle.
SNOOZE_MINUTES = 5
