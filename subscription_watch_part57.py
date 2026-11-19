# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: SubscriptionWatch
def confirm_bulk_delete(subscriptions):
    print(f"Найдено подписок: {len(subscriptions)}")
    if not subscriptions:
        print("Нет подписок для удаления")
        return
    print("Список подписок для удаления:")
    for i, sub in enumerate(subscriptions, 1):
        print(f"  {i}. {sub.name} (до {sub.renewal_date})")
    print()
    choice = input("Введите номер через запятую или 'all' для всех, или 'c' для отмены: ").strip().lower()
    if choice in ('c', 'отмена', 'отменить'):
        print("Отмена операции")
        return
    if choice == 'all':
        selected = list(range(1, len(subscriptions) + 1))
    else:
        selected = []
        for part in choice.split(','):
            part = part.strip()
            if not part:
                continue
            if not part.isdigit():
                print(f"Неверный номер: {part}")
                return
            num = int(part)
            if num < 1 or num > len(subscriptions):
                print(f"Нет подписки с номером {num}")
                return
            selected.append(num)
    if not selected:
        print("Ничего не выбрано")
        return
    subs_to_delete = [subscriptions[i - 1] for i in selected]
    for sub in subs_to_delete:
        print(f"Удалено: {sub.name}")
    print(f"Удалено подписок: {len(subs_to_delete)}")
