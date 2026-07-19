# === Stage 17: Добавь группировку записей по категориям ===
# Project: SubscriptionWatch
def group_by_category(records):
    """Группирует записи по полю 'category'."""
    if not records:
        return {}
    grouped = {}
    for rec in records:
        cat = rec.get("category", "Uncategorized")
        grouped.setdefault(cat, []).append(rec)
    return dict(sorted(grouped.items()))

def summarize_categories(records):
    """Выводит сводку по категориям."""
    groups = group_by_category(records)
    if not groups:
        print("Нет записей.")
        return
    total = sum(len(v) for v in groups.values())
    print(f"Итого записей: {total}\n")
    for cat, subs in groups.items():
        count = len(subs)
        names = ", ".join(s.get("name", "?") for s in subs)
        dates = [s.get("renewal_date", "не указано") for s in subs]
        print(f"  [{cat}] ({count}) — {names}")
        if count == 1:
            print(f"    Дата продления: {dates[0]}")
        else:
            unique_dates = set(dates)
            if len(unique_dates) == 1:
                print(f"    Общая дата продления: {list(unique_dates)[0]}")
