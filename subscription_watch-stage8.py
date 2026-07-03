# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: SubscriptionWatch
def show_menu():
    print("\n=== Меню SubscriptionWatch ===")
    print("1. Список всех подписок")
    print("2. Добавить новую подписку")
    print("3. Просмотр деталей подписки по ID")
    print("4. Вывод уведомлений о продлении в ближайшие 7 дней")
    print("5. Экспорт данных в CSV")
    print("0. Выход")

def run_cli():
    subscriptions = []
    while True:
        show_menu()
        choice = input("Выберите действие (0-5): ").strip()
        if not choice.isdigit():
            print("Ошибка: введите число.")
            continue
        try:
            n = int(choice)
        except ValueError:
            print("Ошибка ввода.")
            continue

        if n == 1:
            if not subscriptions:
                print("Список подписок пуст.")
            else:
                for s in subscriptions:
                    print(f"\nID: {s['id']}, Название: {s['name']}, Тариф: {s['plan']}, Статус: {s['status']}")
        elif n == 2:
            name = input("Название подписки: ")
            plan = input("Тарифный план: ")
            price = float(input("Стоимость (₽): "))
            next_date_str = input("Дата следующего платежа (YYYY-MM-DD): ")
            from datetime import date, timedelta
            try:
                next_date = date.fromisoformat(next_date_str)
            except ValueError:
                print("Неверный формат даты.")
                continue
            subscriptions.append({
                "id": len(subscriptions) + 1,
                "name": name,
                "plan": plan,
                "price": price,
                "next_payment_date": next_date,
                "status": "active" if date.today() <= next_date else "expired",
            })
            print("Подписка добавлена.")
        elif n == 3:
            sub_id = input("Введите ID подписки для просмотра: ")
            try:
                idx = int(sub_id) - 1
                if 0 <= idx < len(subscriptions):
                    s = subscriptions[idx]
                    print(f"\nID: {s['id']}, Название: {s['name']}, Тариф: {s['plan']}")
                    print(f"Стоимость: {s['price']} ₽, Статус: {s['status']}")
                    print(f"Дата следующего платежа: {s['next_payment_date'].strftime('%d.%m.%Y')}")
                else:
                    print("Подписка с таким ID не найдена.")
            except ValueError:
                print("Ошибка ввода ID.")
        elif n == 4:
            from datetime import timedelta
            today = date.today()
            week_later = today + timedelta(days=7)
            alerts = [s for s in subscriptions if s['next_payment_date'] <= week_later and s['status'] != 'expired']
            if not alerts:
                print("Уведомлений о продлении в ближайшие 7 дней нет.")
