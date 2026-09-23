# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: SubscriptionWatch
def self_check():
    print("=" * 60)
    print("  Подсчётчик подписок (SubscriptionWatch) — Самопроверка")
    print("=" * 60)
    print(f"  Подписок: {len(subscriptions)}")
    print(f"  Тарифов:  {len(tariffs)}")
    print(f"  Промокодов: {len(promo_codes)}")
    print(f"  Уведомлений: {len(notifications)}")
    print(f"  Топовые категории: {top_categories}")
    print(f"  Статус: {'✅ ОК' if subscriptions else '⚠️ нет подписок'}")
    print("=" * 60)
