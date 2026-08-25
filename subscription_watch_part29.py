# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: SubscriptionWatch
APP_CONFIG = {
    "app_name": "SubscriptionWatch",
    "version": "0.1",
    "max_subscriptions": 100,
    "renewal_reminder_days": 3,
    "payment_failed_retry_days": 5,
    "log_level": "INFO",
    "data_dir": "./data",
    "notifications": {
        "email": False,
        "console": True,
    },
    "currency": "RUB",
}
