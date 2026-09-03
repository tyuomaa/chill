# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: SubscriptionWatch
def check_and_repair():
    """Проверка целостности и минимальный ремонт данных."""
    issues = []
    for sub in subscriptions:
        if sub.expiry is None:
            issues.append(f"Нет даты окончания для {sub.name}")
        if not sub.plan:
            issues.append(f"Нет тарифа для {sub.name}")
        if sub.amount is None and not sub.is_free:
            issues.append(f"Нет суммы для {sub.name}")
    if issues:
        print("Обнаружено {0} проблем:".format(len(issues)))
        for i in issues:
            print(" - " + i)
        return False
    print("Все данные в порядке.")
    return True
