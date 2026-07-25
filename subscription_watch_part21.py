# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: SubscriptionWatch
def notify_on_date(target_date, message="Подписка истекла"):
    today = datetime.date.today()
    if target_date < today:
        print(f"⚠️  {message} — было {target_date}")
    elif target_date == today:
        print(f"🔔 {message} — сегодня!")
    else:
        days_left = (target_date - today).days
        if days_left <= 30:
            print(f"📅 {message} — через {days_left} дней")
