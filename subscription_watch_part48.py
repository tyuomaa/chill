# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: SubscriptionWatch
from datetime import date, timedelta

def next_occurrence(due_date: date, period_days: int) -> date:
    """Return the next date >= due_date that falls on a day matching the subscription period."""
    if period_days <= 0:
        raise ValueError("period_days must be positive")
    delta = timedelta(days=period_days)
    next_val = due_date + delta
    while next_val < due_date:
        next_val += delta
    return next_val
