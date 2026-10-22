"""Settings: validation, safe defaults on bad input, atomic private saves."""

import json
import logging
import stat

import pytest

from app.core import settings as store
from app.core.config import ALLOWED_INTERVALS, APP_NAME
from app.core.settings import Settings


def test_path_is_in_application_support(tmp_path):
    assert store.settings_path(tmp_path) == tmp_path / "Library" / "Application Support" / APP_NAME / "settings.json"


def test_missing_file_gives_defaults_without_warning(tmp_path, caplog):
    with caplog.at_level(logging.WARNING):
        assert store.load(tmp_path / "nope.json") == Settings()
    assert caplog.records == []


def test_round_trip(tmp_path):
    path = tmp_path / "sub" / "settings.json"
    wanted = Settings(interval_minutes=45, sound_enabled=False, paused=True)
    store.save(wanted, path)
    assert store.load(path) == wanted
    assert json.loads(path.read_text())["version"] == store.SCHEMA_VERSION


def test_saved_file_is_private_and_no_temp_files_left(tmp_path):
    path = tmp_path / "settings.json"
    store.save(Settings(), path)
    assert stat.S_IMODE(path.stat().st_mode) == 0o600
    assert [p.name for p in tmp_path.iterdir()] == ["settings.json"]


@pytest.mark.parametrize("content", ["{not json", "[]", '"text"', "null", "\xff\xfe"])
def test_unreadable_or_wrong_shape_gives_defaults_and_warns(tmp_path, caplog, content):
    path = tmp_path / "settings.json"
    path.write_bytes(content.encode("latin-1"))
    with caplog.at_level(logging.WARNING):
        assert store.load(path) == Settings()
    assert caplog.records, "a broken file must be logged, not silently ignored"


def test_oversized_file_is_refused(tmp_path, caplog):
    path = tmp_path / "settings.json"
    path.write_text('{"x": "' + "a" * store.MAX_FILE_BYTES + '"}')
    with caplog.at_level(logging.WARNING):
        assert store.load(path) == Settings()
    assert "too large" in caplog.text


@pytest.mark.parametrize(
    "raw, field",
    [
        ({"interval_minutes": 7}, "interval_minutes"),
        ({"interval_minutes": "30"}, "interval_minutes"),
        ({"interval_minutes": True}, "interval_minutes"),  # bool is an int in Python
        ({"interval_minutes": 30.0}, "interval_minutes"),
        ({"sound_enabled": "yes"}, "sound_enabled"),
        ({"paused": 1}, "paused"),
    ],
)
def test_each_bad_field_falls_back_on_its_own(raw, field):
    good = {"interval_minutes": 60, "sound_enabled": False, "paused": True}
    settings, problems = store.validate({**good, **raw})
    assert getattr(settings, field) == getattr(Settings(), field)
    assert any(field in p for p in problems)
    # The other, valid fields are kept.
    for name, value in good.items():
        if name != field:
            assert getattr(settings, name) == value


def test_unknown_keys_are_dropped_and_reported():
    settings, problems = store.validate({"interval_minutes": 20, "email": "a@b.c"})
    assert settings.interval_minutes == 20
    assert not hasattr(settings, "email")
    assert any("email" in p for p in problems)


def test_every_allowed_interval_is_valid():
    for minutes in ALLOWED_INTERVALS:
        assert store.validate({"interval_minutes": minutes}) == (Settings(interval_minutes=minutes), [])
