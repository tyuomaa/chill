# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: SubscriptionWatch
import sys, os
from datetime import datetime

def demo_subscription_watch():
    """Демо-команды для ручного тестирования SubscriptionWatch."""

    # --- Демо: создание подписок ---
    subs = [
        {"name": "Netflix", "plan": "Standard", "price": 15.99, "cycle": "monthly", "next_renewal": datetime(2025, 8, 15).date()},
        {"name": "Spotify Premium", "plan": "Individual", "price": 9.99, "cycle": "monthly", "next_renewal": datetime(2025, 7, 20).date()},
        {"name": "GitHub Pro", "plan": "Pro", "price": 4.00, "cycle": "annual", "next_renewal": datetime(2026, 1, 1).date()},
        {"name": "Adobe CC", "plan": "Photography", "price": 54.99, "cycle": "monthly", "next_renewal": datetime(2025, 8, 30).date()},
    ]

    print("=" * 60)
    print("DEMO: SubscriptionWatch — ручное тестирование")
    print("=" * 60)

    # --- Список подписок ---
    print("\n[1] Текущие подписки:")
    for i, s in enumerate(subs, 1):
        days_left = (s["next_renewal"] - datetime.now().date()).days
        status = "⚠️ Скоро истечёт!" if days_left < 30 else ("✅ Активна" if days_left > 0 else "❌ Просрочена")
        print(f"   {i}. {s['name']} — ${s['price']:.2f}/мес, продление через {days_left} дней → {status}")

    # --- Уведомления (симуляция) ---
    print("\n[2] Симуляция уведомлений:")
    for s in subs:
        days = (s["next_renewal"] - datetime.now().date()).days
        if days <= 7:
            print(f"   🔔 {s['name']} — продление через {days} дн. (срочно!)")
        elif days > 0 and days <= 30:
            print(f"   ℹ️ {s['name']} — продление через {days} дней.")

    # --- Итого ---
    total = sum(s["price"] for s in subs)
    print("\n[3] Итого: ", f"${total:.2f}/мес")

    # --- Поиск по названию (демо) ---
    query = input("Искать подписку? (или Enter чтобы продолжить): ").strip() or "Netflix"
    found = next((s for s in subs if query.lower() in s["name"].lower()), None)
    print(f"\n[4] Поиск «{query}» → {found['name'] if found else 'не найдена'}")

    # --- Сортировка
