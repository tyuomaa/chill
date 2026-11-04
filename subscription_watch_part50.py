# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: SubscriptionWatch
def format_subscription(sub):
    """Формирует аккуратное описание подписки с ключевыми параметрами."""
    name = sub["name"] or "безымянная подписка"
    status = "активна" if sub.get("active", True) else "отключена"
    plan = sub["plan"] or "без тарифа"
    lines = [
        f"• {name} ({plan})",
        f"  Статус: {status}",
        f"  Стоимость: {sub.get('price', 0)} {sub.get('currency', '₽')}",
        f"  Дата продления: {sub.get('renewal_date', 'не указана')}",
        f"  Последний платёж: {sub.get('last_payment', 'не выполнен')}",
    ]
    return "\n".join(lines)


def format_notification(notification):
    """Формирует аккуратное уведомление о событии подписки."""
    when = notification.get("timestamp", "не указано")
    text = notification.get("message", "Уведомление")
    channel = notification.get("channel", "email")
    return f"Уведомление [{channel}] ({when}): {text}"


def format_payment(payment):
    """Формирует аккуратное описание платежа за подписку."""
    amount = payment.get("amount", 0)
    currency = payment.get("currency", "₽")
    status = payment.get("status", "неизвестен")
    when = payment.get("timestamp", "не указано")
    return f"Платёж: {amount} {currency} ({status}) — {when}"
