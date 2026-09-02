# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: SubscriptionWatch
def get_next_actions(subscriptions):
    """Return a list of human-readable next actions based on current subscription state."""
    actions = []
    for sub in subscriptions:
        if sub['status'] == 'active':
            days_left = (sub['renewal_date'] - datetime.now().date()).days
            if days_left <= 0:
                actions.append(f"Renew {sub['name']} today (expired {days_left} days ago)")
            elif days_left <= 7:
                actions.append(f"Renew {sub['name']} soon (7 days left)")
            elif days_left <= 30:
                actions.append(f"Set reminder for {sub['name']} (30 days left)")
            else:
                continue
        elif sub['status'] == 'cancelled':
            actions.append(f"Review cancellation of {sub['name']}")
        elif sub['status'] == 'on_hold':
            actions.append(f"Decide: resume or cancel {sub['name']}")
    return actions
