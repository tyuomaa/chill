# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: SubscriptionWatch
def sort_subscriptions(subs, key='renewal_date', reverse=False):
    if key == 'name':
        return sorted(subs, key=lambda x: (x['priority'] or 0) * -1 + len(x['name']), reverse=reverse)
    elif key == 'priority':
        return sorted(subs, key=lambda x: -(x.get('priority', 0)), reverse=True)
    else:
        try:
            from datetime import datetime
            def parse_date(d):
                if isinstance(d, str):
                    for fmt in ['%Y-%m-%d', '%d.%m.%Y', '%Y/%m/%d']:
                        try: return datetime.strptime(d, fmt)
                        except ValueError: pass
                    raise ValueError(f"Неизвестный формат даты: {d}")
                return d
            subs_with_date = [(parse_date(s.get(key)), s) for s in subs]
            subs_with_date.sort(reverse=reverse)
            return [s[1] for s in subs_with_date]
        except Exception as e:
            print(f"Ошибка сортировки по дате: {e}")
            return sorted(subs, key=lambda x: str(x.get(key, '')), reverse=reverse)
