# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: SubscriptionWatch
def print_table(data, headers):
    """Отображает список подписок в виде отформатированной таблицы."""
    widths = [len(str(h)) for h in headers]
    for row in data:
        for i, v in enumerate(row):
            widths[i] = max(widths[i], len(str(v)))

    def fmt_row(cells):
        return " | ".join(f"{c:<{w}}" for c, w in zip(cells, widths))

    print(fmt_row(headers))
    print("-" * sum(widths) + "-")
    print(fmt_row(data))


if __name__ == "__main__":
    subs = [
        ("Netflix", 1200, "2025-12-31", True),
        ("Spotify", 499, "2026-01-15", False),
        ("GitHub Pro", 800, "2025-08-20", True),
    ]
    print_table(subs, ["Название", "Цена (₽)", "Продление", "Активна"])
