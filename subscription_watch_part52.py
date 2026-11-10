# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: SubscriptionWatch
def export_report(subs, path):
    lines = ["=== SubscriptionWatch Report ===",
             f"Generated: {datetime.now().isoformat()}",
             f"Total subscriptions: {len(subs)}"]
    total_spend = 0.0
    for s in subs:
        status = s.get_status()
        total_spend += s.monthly_cost
        lines.append(f"- {s.name} | {status} | {s.monthly_cost} | "
                     f"Renews: {s.renewal_date.strftime('%Y-%m-%d')}")
    lines.append(f"Total monthly spend: {total_spend:.2f}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path
