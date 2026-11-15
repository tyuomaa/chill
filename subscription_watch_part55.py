# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: SubscriptionWatch
def find_duplicate(subscriptions, new_record):
    found = None
    for sub in subscriptions:
        if sub.get("id") == new_record.get("id"):
            found = sub
            break
        if _normalize(sub) == _normalize(new_record):
            if not sub.get("is_duplicate"):
                found = sub
                break
    return found

def _normalize(record):
    name = (record.get("name") or "").strip().lower()
    provider = (record.get("provider") or "").strip().lower()
    plan = (record.get("plan") or "").strip().lower()
    amount = record.get("amount") or 0
    amount = float(amount) if isinstance(amount, str) and amount.replace(".", "", 1).isdigit() else amount
    try:
        amount = round(float(amount), 2)
    except (ValueError, TypeError):
        amount = 0
    period = (record.get("period") or "").strip().lower()
    return (name, provider, plan, amount, period)
