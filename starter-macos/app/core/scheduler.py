"""When is the next reminder due? Pure timing logic, no clocks or windows inside.

The caller passes `now` (seconds from time.monotonic()) into every method. That keeps this
class easy to test — tests just pass numbers — and means changing the system clock (or
travelling across time zones) can never make a reminder fire early or late.
"""

from __future__ import annotations

import math

from app.core.config import SNOOZE_MINUTES


class ReminderScheduler:
    def __init__(self, interval_minutes: int, now: float, paused: bool = False) -> None:
        if interval_minutes <= 0:
            raise ValueError("interval_minutes must be positive")
        self._interval = interval_minutes * 60
        self._due_at = now + self._interval
        self._paused = paused

    @property
    def paused(self) -> bool:
        return self._paused

    @property
    def interval_minutes(self) -> int:
        return self._interval // 60

    def due(self, now: float) -> bool:
        """True when a reminder should be shown now."""
        return not self._paused and now >= self._due_at

    def complete(self, now: float) -> None:
        """The person took (or acknowledged) the break: start a full interval from now."""
        self._due_at = now + self._interval

    def snooze(self, now: float, minutes: int = SNOOZE_MINUTES) -> None:
        """'Not now': ask again shortly instead of waiting a whole interval."""
        self._due_at = now + minutes * 60

    def pause(self) -> None:
        self._paused = True

    def resume(self, now: float) -> None:
        # Restart a full interval rather than continuing the old countdown: after a pause
        # (a meeting, lunch) a reminder the moment you come back would feel like nagging.
        self._paused = False
        self._due_at = now + self._interval

    def set_interval(self, minutes: int, now: float) -> None:
        if minutes <= 0:
            raise ValueError("minutes must be positive")
        self._interval = minutes * 60
        self._due_at = now + self._interval

    def seconds_remaining(self, now: float) -> int | None:
        """Seconds until the next reminder, or None while paused."""
        if self._paused:
            return None
        return max(0, math.ceil(self._due_at - now))

    def status_text(self, now: float) -> str:
        """One line for the menu, in words — state is never shown by colour or icon alone."""
        remaining = self.seconds_remaining(now)
        if remaining is None:
            return "Reminders paused"
        if remaining == 0:
            return "Break due now"
        minutes = math.ceil(remaining / 60)
        return f"Next break in {minutes} minute" + ("" if minutes == 1 else "s")


def interval_label(minutes: int) -> str:
    """'45 minutes', '1 hour', '1 hour 30 minutes' — for the Preferences pop-up menu."""
    hours, mins = divmod(minutes, 60)
    parts = []
    if hours:
        parts.append(f"{hours} hour" + ("" if hours == 1 else "s"))
    if mins:
        parts.append(f"{mins} minute" + ("" if mins == 1 else "s"))
    return " ".join(parts) or "0 minutes"
