"""Scheduler: when reminders are due, snooze, pause/resume, and the menu status words."""

import pytest

from app.core.config import SNOOZE_MINUTES
from app.core.scheduler import ReminderScheduler, interval_label


def test_due_after_one_interval():
    s = ReminderScheduler(30, now=0)
    assert not s.due(30 * 60 - 1)
    assert s.due(30 * 60)


def test_complete_starts_a_full_interval():
    s = ReminderScheduler(20, now=0)
    s.complete(now=1500)
    assert not s.due(1500 + 20 * 60 - 1)
    assert s.due(1500 + 20 * 60)


def test_snooze_asks_again_soon():
    s = ReminderScheduler(60, now=0)
    s.snooze(now=3600)
    assert s.due(3600 + SNOOZE_MINUTES * 60)
    assert not s.due(3600 + SNOOZE_MINUTES * 60 - 1)


def test_paused_is_never_due_and_resume_restarts_the_countdown():
    s = ReminderScheduler(15, now=0)
    s.pause()
    assert s.paused and not s.due(10_000)
    assert s.seconds_remaining(10_000) is None
    s.resume(now=10_000)
    assert not s.due(10_000 + 15 * 60 - 1)
    assert s.due(10_000 + 15 * 60)


def test_can_start_paused():
    assert not ReminderScheduler(15, now=0, paused=True).due(99_999)


def test_set_interval_restarts_from_now():
    s = ReminderScheduler(90, now=0)
    s.set_interval(15, now=100)
    assert s.interval_minutes == 15
    assert s.due(100 + 15 * 60)


@pytest.mark.parametrize("bad", [0, -5])
def test_rejects_non_positive_intervals(bad):
    with pytest.raises(ValueError):
        ReminderScheduler(bad, now=0)
    with pytest.raises(ValueError):
        ReminderScheduler(30, now=0).set_interval(bad, now=0)


@pytest.mark.parametrize(
    "elapsed, text",
    [(0, "Next break in 30 minutes"), (29 * 60 + 1, "Next break in 1 minute"), (30 * 60, "Break due now")],
)
def test_status_text_uses_words(elapsed, text):
    assert ReminderScheduler(30, now=0).status_text(elapsed) == text


def test_status_text_when_paused():
    s = ReminderScheduler(30, now=0, paused=True)
    assert s.status_text(0) == "Reminders paused"


@pytest.mark.parametrize(
    "minutes, label",
    [(15, "15 minutes"), (60, "1 hour"), (90, "1 hour 30 minutes"), (120, "2 hours"), (1, "1 minute")],
)
def test_interval_label(minutes, label):
    assert interval_label(minutes) == label
