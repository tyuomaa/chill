# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: SubscriptionWatch
def search_subscriptions(query, field="name"):
    """Search subscriptions by multiple fields case-insensitively."""
    if not query:
        return []
    results = [sub for sub in _subs if any(
        query.lower() == str(getattr(sub, f)).lower() or
        (field != "name" and hasattr(sub, f) and getattr(sub, field).lower().startswith(query.lower()))
        for f in ("name", "provider", "status")
    )]
    return results
