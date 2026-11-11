# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: SubscriptionWatch
def parse_file(path, sep="\t"):
    subs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(sep)]
            if len(parts) < 6:
                print("Ошибка: недостаточно полей в строке:", line)
                continue
            subs.append({
                "name": parts[0],
                "plan": parts[1],
                "price": parts[2],
                "next_renewal": parts[3],
                "last_payment": parts[4],
                "notes": parts[5] if len(parts) > 6 else "",
            })
    return subs

def import_records(path, sep="\t"):
    subs = parse_file(path, sep)
    for sub in subs:
        add_subscription(sub)
    return subs
