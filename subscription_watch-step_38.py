# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: SubscriptionWatch
class SubscriptionError(Exception):
    pass

class SubscriptionWatch:
    def __init__(self):
        self.subscriptions = {}
        self.notifications = []

    def add_subscription(self, name, plan, amount, period_days, billing_cycle, next_billing_date):
        if not name:
            raise SubscriptionError("Name cannot be empty")
        if not plan:
            raise SubscriptionError("Plan cannot be empty")
        if amount <= 0:
            raise SubscriptionError("Amount must be positive")
        if period_days <= 0:
            raise SubscriptionError("Period must be positive")
        if billing_cycle not in ["monthly", "yearly"]:
            raise SubscriptionError("Invalid billing cycle")
        if not isinstance(next_billing_date, datetime):
            raise SubscriptionError("next_billing_date must be a datetime")
        if next_billing_date < datetime.now():
            raise SubscriptionError("next_billing_date must be in the future")
        if name in self.subscriptions:
            raise SubscriptionError(f"Subscription '{name}' already exists")
        self.subscriptions[name] = {
            "name": name,
            "plan": plan,
            "amount": amount,
            "period_days": period_days,
            "billing_cycle": billing_cycle,
            "next_billing_date": next_billing_date,
        }
        self.notifications.append({
            "type": "added",
            "subscription": name,
            "timestamp": datetime.now(),
        })

    def get_subscription(self, name):
        if name not in self.subscriptions:
            raise SubscriptionError(f"Subscription '{name}' not found")
        return self.subscriptions[name]

    def cancel_subscription(self, name):
        if name not in self.subscriptions:
            raise SubscriptionError(f"Subscription '{name}' not found")
        del self.subscriptions[name]
        self.notifications.append({
            "type": "cancelled",
            "subscription": name,
            "timestamp": datetime.now(),
        })

    def get_next_billing(self, name):
        sub = self.get_subscription(name)
        return sub["next_billing_date"]

    def get_amount(self, name):
        sub = self.get_subscription(name)
        return sub["amount"]

    def get_plan(self, name):
        sub = self.get_subscription(name)
        return sub["plan"]

    def get_billing_cycle(self, name):
        sub = self.get_subscription(name)
        return sub["billing_cycle"]

    def get_all_subscriptions(self):
        return list(self.subscriptions.values())

    def get_notifications(self, subscription=None):
        if subscription:
            return [n for n in self.notifications if n.get("subscription") == subscription]
        return self.notifications

    def get_subscription_count(self):
        return len(self.subscriptions)

    def get_notification_count(self):
        return len(self.notifications)
