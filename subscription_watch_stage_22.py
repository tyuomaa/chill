# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: SubscriptionWatch
def check_overdue_reminders():
    """Проверяет просроченные напоминания: если дата продления уже прошла, а напоминание ещё не отправлено."""
    overdue_count = 0
    for sub in subscriptions:
        if sub.renewal_date and sub.renewal_date < datetime.now() and not sub.reminder_sent:
            send_notification(f"⚠️ Подписка '{sub.name}' просрочена. Дата продления: {sub.renewal_date.strftime('%d.%m.%Y')}.")
            sub.reminder_sent = True
            overdue_count += 1
    if overdue_count == 0:
        print("✅ Все напоминания отправлены вовремя.")
