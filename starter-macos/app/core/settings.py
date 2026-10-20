"""Load, validate and save the user's settings as a small JSON file.

Rules this module follows (see the kit's privacy and security standards):
- Minimum data: only the three preferences below are stored. No names, no usage history.
- Never crash on a bad file: anything we can't trust falls back to a safe default and a
  warning is logged, so a hand-edited or half-written file can't stop the app starting.
- Atomic save: write a temporary file, then rename it over the old one, so a crash or a
  full disk mid-save never leaves a corrupt settings.json behind.
"""

from __future__ import annotations

import json
import logging
import os
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

from app.core.config import ALLOWED_INTERVALS, APP_NAME, DEFAULT_INTERVAL

log = logging.getLogger(__name__)

SCHEMA_VERSION = 1
# A real settings file is under 200 bytes. Refusing anything huge stops a corrupted or
# hostile file from using lots of memory when we parse it.
MAX_FILE_BYTES = 64 * 1024


@dataclass(frozen=True)
class Settings:
    interval_minutes: int = DEFAULT_INTERVAL
    sound_enabled: bool = True
    paused: bool = False


def settings_path(home: Path | None = None) -> Path:
    """~/Library/Application Support/<AppName>/settings.json — Apple's place for app data."""
    base = home if home is not None else Path.home()
    return base / "Library" / "Application Support" / APP_NAME / "settings.json"


def validate(raw: object) -> tuple[Settings, list[str]]:
    """Turn untrusted JSON into Settings. Returns the settings and a list of problems found.

    Each field is checked on its own, so one bad value doesn't throw away the others.
    Unknown keys are dropped (minimum data: we never keep what we don't use).
    """
    defaults = Settings()
    if not isinstance(raw, dict):
        return defaults, ["settings file is not a JSON object"]

    problems: list[str] = []

    interval = raw.get("interval_minutes", defaults.interval_minutes)
    # bool is a subclass of int in Python, so `True` would otherwise pass as 1 minute.
    if isinstance(interval, bool) or not isinstance(interval, int) or interval not in ALLOWED_INTERVALS:
        problems.append(f"interval_minutes {interval!r} is not one of {list(ALLOWED_INTERVALS)}")
        interval = defaults.interval_minutes

    sound = raw.get("sound_enabled", defaults.sound_enabled)
    if not isinstance(sound, bool):
        problems.append(f"sound_enabled {sound!r} is not true/false")
        sound = defaults.sound_enabled

    paused = raw.get("paused", defaults.paused)
    if not isinstance(paused, bool):
        problems.append(f"paused {paused!r} is not true/false")
        paused = defaults.paused

    unknown = sorted(set(raw) - {"version", "interval_minutes", "sound_enabled", "paused"})
    if unknown:
        problems.append(f"ignored unknown keys {unknown}")

    return Settings(interval_minutes=interval, sound_enabled=sound, paused=paused), problems


def load(path: Path | None = None) -> Settings:
    """Read settings. First run (no file) is normal and silent; anything broken is logged."""
    path = path or settings_path()
    if not path.exists():
        return Settings()
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            log.warning("Settings file %s is too large; using defaults", path)
            return Settings()
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        log.warning("Could not read settings file %s (%s); using defaults", path, exc)
        return Settings()

    settings, problems = validate(raw)
    for problem in problems:
        log.warning("Settings file %s: %s; using the default for it", path, problem)
    return settings


def save(settings: Settings, path: Path | None = None) -> None:
    """Write settings atomically, readable only by the current user."""
    path = path or settings_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {"version": SCHEMA_VERSION, **asdict(settings)}
    # mkstemp creates the file with 0600 permissions, so other accounts on the Mac can't read it.
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=".settings-", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(tmp_name, path)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise
