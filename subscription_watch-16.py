# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: SubscriptionWatch
def monthly_stats(subscriptions):
    """Расчёт месячной статистики по датам продления."""
    from collections import defaultdict
    stats = defaultdict(lambda: {'count': 0, 'total_cost': 0})
    for sub in subscriptions:
        if hasattr(sub, 'renewal_date') and isinstance(sub.renewal_date, datetime):
            key = (sub.renewal_date.year, sub.renewal_date.month)
            stats[key]['count'] += 1
            if hasattr(sub, 'price'):
                stats[key]['total_cost'] += sub.price
    return dict(stats)
