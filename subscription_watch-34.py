# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: SubscriptionWatch
class SubscriptionTemplate:
    def __init__(self, name, duration_days, payment_interval_days, category, default_amount):
        self.name = name
        self.duration_days = duration_days
        self.payment_interval_days = payment_interval_days
        self.category = category
        self.default_amount = default_amount

    def create_subscription(self, user_id, amount=None, note=None):
        amount = amount or self.default_amount
        renewal_date = datetime.now() + timedelta(days=self.duration_days)
        next_payment = datetime.now() + timedelta(days=self.payment_interval_days)
        return Subscription(
            user_id=user_id,
            name=self.name,
            amount=amount,
            renewal_date=renewal_date,
            next_payment_date=next_payment,
            payment_interval_days=self.payment_interval_days,
            category=self.category,
            note=note,
            source="template",
        )

TEMPLATES = [
    SubscriptionTemplate("Netflix", 30, 30, "streaming", 599),
    SubscriptionTemplate("Spotify", 30, 30, "music", 499),
    SubscriptionTemplate("GitHub Pro", 365, 365, "dev", 4000),
    SubscriptionTemplate("Adobe CC", 365, 365, "design", 12000),
    SubscriptionTemplate("Mail.ru Premium", 30, 30, "communication", 199),
]
