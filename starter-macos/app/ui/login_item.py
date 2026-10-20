"""Optional "Open at login", using Apple's SMAppService (macOS 13+).

macOS keeps this setting itself (System Settings → General → Login Items), so we never store
it in settings.json — we ask macOS each time. It only works from the built .app: run from
source, the process is Python, not our app, so we report "unavailable" and the Preferences
window explains the manual route instead.
"""

from __future__ import annotations

import logging
import sys
from typing import Any

log = logging.getLogger(__name__)

# SMAppServiceStatus values from Apple's ServiceManagement framework.
STATUS_ENABLED = 1
STATUS_REQUIRES_APPROVAL = 2


def _service() -> Any | None:
    if getattr(sys, "frozen", None) != "macosx_app":  # py2app sets this inside the built .app
        return None
    try:
        from ServiceManagement import SMAppService

        return SMAppService.mainAppService()
    except (ImportError, AttributeError):  # framework missing, or macOS older than 13
        return None


class LoginItem:
    def __init__(self) -> None:
        self._service = _service()

    @property
    def available(self) -> bool:
        return self._service is not None

    def _status(self) -> int:
        return int(self._service.status()) if self._service is not None else 0

    @property
    def enabled(self) -> bool:
        return self._status() in (STATUS_ENABLED, STATUS_REQUIRES_APPROVAL)

    @property
    def requires_approval(self) -> bool:
        return self._status() == STATUS_REQUIRES_APPROVAL

    def set_enabled(self, on: bool) -> bool:
        """Returns True if macOS accepted the change. Failures are logged, never raised."""
        if self._service is None:
            return False
        if on:
            ok, error = self._service.registerAndReturnError_(None)
        else:
            ok, error = self._service.unregisterAndReturnError_(None)
        if not ok:
            log.warning("Open at login change failed: %s", error)
        return bool(ok)
