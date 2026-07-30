# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: SubscriptionWatch
def print_subscription_record(sub):
    """Print a compact human-readable record for one subscription."""
    lines = []
    lines.append(f"Subscription: {sub.name}")
    lines.append(f"  Plan:       {sub.plan_name}")
    lines.append(f"  Provider:   {sub.provider}")
    lines.append(f"  Status:     {'ACTIVE' if sub.is_active else 'EXPIRED'}")
    lines.append(f"  Renewal:    {sub.next_renewal.strftime('%Y-%m-%d') if sub.next_renewal else 'N/A'}")
    if sub.last_payment_date:
        lines.append(f"  Last paid:  {sub.last_payment_date.strftime('%Y-%m-%d')}")
    lines.append(f"  Total cost: {format_cost(sub.total_cost)}")
    print("\n".join(lines))


if __name__ == "__main__":
    sub = Subscription(
        name="Netflix", plan_name="Standard", provider="netflix.com",
        is_active=True, next_renewal=next_renewal, last_payment_date=datetime(2024, 10, 1),
        total_cost=15.99)
    print_subscription_record(sub)
