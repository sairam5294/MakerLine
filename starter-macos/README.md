# MakerLine macOS Starter — Python + PyObjC menu-bar app

Use for: **small Mac utilities that live in the menu bar** — reminders, timers, status
monitors, quick toggles. (Use the Expo starter for iOS/Android apps, the web starter for sites.)

What's in it: a generic "take a break" reminder that shows the patterns, not a product.
A menu-bar icon with a menu (status in words · Pause/Resume · Settings… Cmd+, · About ·
Quit Cmd+Q), an accessible reminder window, and a Settings window (interval, sound,
optional Open at login). Settings are a small JSON file. No network, no analytics, no account.

## First run (on a Mac)
```bash
python3 -m venv .venv && source .venv/bin/activate      # Python 3.11 or newer
pip install -r requirements.txt -r requirements-dev.txt
python3 -m app.main                 # look for the cup icon in the menu bar
python3 -m app.main --preview       # also shows the reminder right away (for testing)
```
Rename the app in **one place**: `app/core/config.py` (name, bundle id, intervals).

## Quality commands
| Command | What it does |
|---|---|
| `scripts/check.sh` | everything CI runs: ruff lint + import order, ruff format check, mypy, token drift, contrast, pytest |
| `scripts/check.sh --fix` | apply ruff fixes and formatting first |
| `python3 scripts/build_tokens.py` | regenerate `app/ui/palette.py` after editing `design/tokens.json` |
| `python3 scripts/check_contrast.py` | WCAG AA check of every colour pair, light + dark + Increase Contrast |
| `pytest` | tests; the AppKit UI tests **skip on Linux** and **run on a Mac** |

CI (`.github/workflows/macos-app.yml`): lint, types, tokens and core tests on Linux (cheap);
UI accessibility tests and the app + DMG build on macOS.

## Build the app
```bash
pip install -r requirements-build.txt
python3 setup.py py2app             # → dist/BreakReminder.app
scripts/build_dmg.sh                # → dist/BreakReminder.dmg (signs the app ad hoc first)
```
Icon: make a 1024 px PNG, turn it into `design/AppIcon.icns` (`iconutil`, macOS only) and add
`"iconfile"` to `OPTIONS` in `setup.py`.

### First launch on another Mac (Gatekeeper)
The DMG is signed **ad hoc** — fine for you and friends, but macOS doesn't know who made it,
so the first launch is blocked with "can't be opened". To open it once:
- **Right-click (or Control-click) the app → Open → Open**, or
- try to open it, then **System Settings → Privacy & Security → scroll down → Open Anyway**.

After that it opens normally. To remove the warning for everyone you need **notarisation**,
which requires a **paid Apple Developer account** (Developer ID certificate + `notarytool`).

### Open at login
Uses Apple's `SMAppService` (macOS 13+), so it only works in the **built app**. When you run
from source the checkbox is disabled and explains the manual route: System Settings → General
→ Login Items → + → choose the app. The setting lives in macOS, not in our settings file.

## Accessibility checklist (run by hand before each release)
The UI tests check labels, roles, target sizes and keyboard shortcuts automatically. These
need a person:
- [ ] **VoiceOver** (Cmd+F5): the menu-bar icon is announced with its state; the reminder
      is announced in full when it appears; every control says what it is.
- [ ] **Keyboard only**: Return = Done, Esc = Not now, Tab reaches every control (turn on
      System Settings → Keyboard → Keyboard navigation), Cmd+, and Cmd+Q in the menu,
      Esc and Cmd+W close Settings.
- [ ] **Reduce Motion** (Accessibility → Display): the reminder appears without animating.
- [ ] **Increase Contrast** (Accessibility → Display): secondary text and borders get stronger.
- [ ] **Dark Mode**: switch while the reminder is open — colours update live.
- [ ] **Larger text**: Zoom (Accessibility → Zoom) and long translations — text wraps,
      nothing is cut off. (AppKit has no system text-size setting for third-party apps; we
      use Apple's text styles so we follow any AppKit applies.)
- [ ] Nothing flashes; nothing relies on colour alone; sound is optional.

Update `ACCESSIBILITY.md` (statement + barrier-report contact) with what you found.

## Where things live
```
app/core/        pure Python — NO AppKit import (runs and is tested on any OS)
  config.py        app name, bundle id, interval choices
  settings.py      load/validate/save ~/Library/Application Support/<AppName>/settings.json
  scheduler.py     when the next reminder is due; status text in words
  login.py         wording for the Open at login setting
app/ui/          AppKit layer (macOS only)
  palette.py       GENERATED from design/tokens.json — don't edit
  theme.py         picks light/dark/high-contrast colours; WCAG contrast maths (pure Python)
  colors.py        dynamic NSColors that follow Dark Mode + Increase Contrast live
  controls.py      accessible buttons, checkboxes, pop-ups, labels, Esc/Cmd+W window
  reminder_window.py · preferences_window.py · menu_bar.py · login_item.py
app/main.py      entry point (python3 -m app.main)
design/tokens.json  the kit's design tokens (same file as Figma and the other starters)
scripts/         check.sh · build_tokens.py · check_contrast.py · build_dmg.sh
tests/           core, settings, tokens (anywhere) + UI accessibility (macOS)
setup.py         py2app build settings (menu-bar only: LSUIElement)
```

## Built in
One design-token source → generated palette (drift fails CI) · contrast checked in four
appearances · dynamic colours · 44 pt+ targets · labelled controls · Return/Esc/Tab/Cmd+,/Cmd+Q ·
Reduce Motion · state in words · schema-validated settings (bad file → safe defaults + a
warning, never a crash) · atomic, owner-only settings file · minimum data, no network.

PyObjC tips for AI agents: selectors become Python names with `_` for each `:`
(`initWithTitle:action:keyEquivalent:` → `initWithTitle_action_keyEquivalent_`); Cocoa keeps
targets and delegates **weakly**, so keep a Python reference; helper methods on `NSObject`
subclasses need `@objc.python_method`. Check APIs in Apple's docs, not from memory.
