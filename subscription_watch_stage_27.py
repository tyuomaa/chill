# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: SubscriptionWatch
def reset_demo_data():
    """Сбрасывает демо-данные: удаляет все подписки, платежи и уведомления."""
    global subscriptions, payments, notifications
    subscriptions = []
    payments = []
    notifications = []


def clear_state():
    """Очищает состояние приложения: сбрасывает демо-данные и показывает приветственное сообщение."""
    reset_demo_data()
    print("Состояние успешно очищено. Все данные сброшены.")
