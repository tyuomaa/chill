# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: SubscriptionWatch
def edit_subscription(sub_id: int, **kwargs) -> dict | None:
    """Редактирует подписку по ID, возвращая обновлённую запись или None."""
    for sub in subscriptions:
        if sub['id'] == sub_id:
            updates = {k: v for k, v in kwargs.items() if k in ['name', 'plan', 'price', 'billing_cycle', 'next_renewal']}
            if not updates:
                print("Нет изменений для применения.")
                return None
            sub.update(updates)
            # Пересчёт даты следующего продления при изменении цикла или цены (упрощённо)
            if 'next_renewal' in kwargs and isinstance(kwargs['next_renewal'], str):
                try:
                    from datetime import datetime, timedelta
                    date_str = kwargs['next_renewal']
                    fmt = "%Y-%m-%d"
                    next_date = datetime.strptime(date_str, fmt)
                    sub['next_renewal'] = next_date.strftime(fmt)
                except ValueError:
                    print(f"Ошибка формата даты продления: {date_str}")
            elif 'billing_cycle' in kwargs and isinstance(kwargs['billing_cycle'], str):
                cycle_map = {'monthly': 30, 'quarterly': 91, 'yearly': 365}
                days = cycle_map.get(kwargs['billing_cycle'].lower(), 30)
                if 'next_renewal' in sub:
                    try:
                        from datetime import datetime
                        current_date = datetime.strptime(sub['next_renewal'], "%Y-%m-%d")
                        new_next = (current_date + timedelta(days=days)).strftime("%Y-%m-%d")
                        sub['next_renewal'] = new_next
                    except ValueError:
                        pass
            print(f"Подписка #{sub_id} обновлена.")
            return sub.copy()
    print(f"Подписка с ID {sub_id} не найдена.")
    return None
