# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: SubscriptionWatch
def weekly_stats(subscriptions, period_weeks=1):
    """Return dict {week_iso: {'new': int, 'renewed': int}} for each week in [today - n*7, today]."""
    now = datetime.now()
    stats = {}
    for i in range(period_weeks):
        w_start = now.replace(day=1) + timedelta(weeks=-i * 7)
        if w_start.day > 28:
            continue
        week_key = w_start.isoformat()
        stats[week_key] = {'new': 0, 'renewed': 0}

    for sub in subscriptions:
        # count as renewed if renewal_date is within this week
        if sub.renewal_date and sub.renewal_date >= now.replace(hour=0, minute=0, second=0):
            wd = (sub.renewal_date - now).days / 7
            wk_idx = int(wd)
            if 0 <= wk_idx < period_weeks:
                stats[f"{now.date() - timedelta(weeks=wk_idx)}"]['renewed'] += 1
        # count as new if created within this week
        if sub.created_date and sub.created_date >= now.replace(hour=0, minute=0, second=0):
            wd = (sub.created_date - now).days / 7
            wk_idx = int(wd)
            if 0 <= wk_idx < period_weeks:
                stats[f"{now.date() - timedelta(weeks=wk_idx)}"]['new'] += 1

    return stats
