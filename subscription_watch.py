# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: SubscriptionWatch
from dataclasses import dataclass, field
from datetime import date, timedelta
import random
from typing import List, Optional

@dataclass
class Subscription:
    name: str
    price: float
    renewal_date: date
    last_payment: date
    notifications_sent: int = 0
    
    def is_due_soon(self, days_threshold: int = 7) -> bool:
        return self.renewal_date <= date.today() + timedelta(days=days_threshold)

def generate_demo_data(count: int = 5) -> List[Subscription]:
    base_dates = [date(2024, m, d) for m in range(1, 13) for d in range(1, 29)]
    return [
        Subscription(
            name=f"Service_{random.randint(100, 999)}",
            price=round(random.uniform(5.0, 50.0), 2),
            renewal_date=random.choice(base_dates),
            last_payment=date.today() - timedelta(days=random.randint(30, 60))
        ) for _ in range(count)
    ]

if __name__ == "__main__":
    subs = generate_demo_data()
    print(f"Загружено {len(subs)} подписок.")
    due_subs = [s for s in subs if s.is_due_soon()]
    if due_subs:
        print("Подписки, требующие внимания:")
        for s in due_subs:
            print(f"- {s.name}: продление через {(s.renewal_date - date.today()).days} дней")
