# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: SubscriptionWatch
def generate_summary(subscriptions):
    now = datetime.now()
    active = [s for s in subscriptions if s["status"] == "active"]
    expiring_soon = []
    overdue = []
    total_monthly = sum(s.get("price", 0) / 30.44 for s in active)

    for s in active:
        days_left = (s["renewal_date"] - now).days
        if days_left <= 7:
            expiring_soon.append(f"{s['name']} — продление через {days_left} дн.")
        elif days_left < 0:
            overdue.append(f"{s['name']} — просрочено на {-days_left} дн.")

    result = [f"📊 Сводка по подпискам ({len(active)} активных)", f"💰 Средний расход: {total_monthly:.2f} руб/мес"]
    if expiring_soon:
        for line in expiring_soon:
            result.append(f"⚠️  {line}")
    if overdue:
        for line in overdue:
            result.append(f"🔴 {line}")
    return "\n".join(result)
