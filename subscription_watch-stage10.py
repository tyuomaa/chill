# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: SubscriptionWatch
def export_state():
    """Export current state as a JSON-like string."""
    import json, datetime
    now = datetime.datetime.now().isoformat()
    lines = []
    for sub in subscriptions:
        lines.append(f"Subscription: {sub.name}")
        if hasattr(sub, 'plan'):
            lines.append(f"  Plan: {sub.plan.name}")
        else:
            lines.append("  Plan: (none)")
        if hasattr(sub, 'next_renewal'):
            lines.append(f"  Next renewal: {sub.next_renewal.isoformat()}")
        else:
            lines.append("  Next renewal: unknown")
    return json.dumps({"status": now, "subscriptions": "\n".join(lines)}, indent=2)
