# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: SubscriptionWatch
class SubscriptionWatch:
    def __init__(self):
        self.subscriptions = []
    
    def add_subscription(self, name, plan, price, billing_cycle, next_renewal_date=None):
        if not next_renewal_date:
            from datetime import date, timedelta
            today = date.today()
            cycle_days = {'monthly': 30, 'weekly': 7, 'yearly': 365}.get(billing_cycle.lower(), 30)
            next_renewal_date = today + timedelta(days=cycle_days)
        self.subscriptions.append({
            "name": name,
            "plan": plan,
            "price": price,
            "billing_cycle": billing_cycle,
            "next_renewal_date": next_renewal_date
        })
        return self.subscriptions[-1]

    def get_subscription(self, name):
        for sub in self.subscriptions:
            if sub["name"].lower() == name.lower():
                return sub
        return None
