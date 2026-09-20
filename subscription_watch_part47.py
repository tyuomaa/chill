# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: SubscriptionWatch
def demo():
    """Показывает основной пользовательский сценарий: создание, добавление, обновление, списание и удаление подписок."""
    watch = SubscriptionWatch()
    watch.add_subscription("Netflix", "Premium", "2025-12-31", 1899, "monthly")
    watch.add_subscription("Spotify", "Individual", "2026-06-15", 1099, "monthly")
    watch.add_subscription("Adobe Photoshop", "All Apps", "2025-09-20", 5499, "annual")
    watch.add_subscription("GitHub Pro", "Pro", "2026-03-10", 4000, "annual")
    watch.add_subscription("Canva Pro", "Pro", "2025-11-01", 1300, "monthly")

    print("=== Подписки до списания ===")
    for s in watch.subscriptions:
        print(f"  {s.name}: {s.plan} — до {s.renewal_date}, баланс: {s.balance}₽")

    watch.charge("Netflix", 1899)
    watch.charge("Spotify", 1099)
    watch.charge("Adobe Photoshop", 5499)
    watch.charge("GitHub Pro", 4000)
    watch.charge("Canva Pro", 1300)

    print("\n=== Подписки после списания ===")
    for s in watch.subscriptions:
        print(f"  {s.name}: {s.plan} — до {s.renewal_date}, баланс: {s.balance}₽")

    watch.cancel("Canva Pro")
    watch.cancel("GitHub Pro")

    print("\n=== Оставшиеся активные подписки ===")
    for s in watch.subscriptions:
        print(f"  {s.name}: {s.plan} — до {s.renewal_date}, баланс: {s.balance}₽")

    print("\n=== Отчёт ===")
    total_spend = sum(s.total_spent for s in watch.subscriptions)
    print(f"  Потрачено всего: {total_spend}₽")
    print(f"  Активных подписок: {len(watch.subscriptions)}")
    print(f"  Отменённых: {len(watch.subscriptions) - len(watch.subscriptions) + 0}")
    print("Demo завершена.")
