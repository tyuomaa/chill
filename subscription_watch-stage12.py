# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: SubscriptionWatch
import json, os, glob

def load_subscriptions_from_file(file_pattern="subscriptions*.json"):
    files = sorted(glob.glob(file_pattern))
    if not files:
        print(f"Файлы подписок не найдены по шаблону: {file_pattern}")
        return []
    
    all_subs = []
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            if isinstance(data, list):
                all_subs.extend(data)
            elif isinstance(data, dict):
                all_subs.append(data)
            print(f"Загружено из {f}: {len(all_subs)} записей")
        except (json.JSONDecodeError, OSError) as e:
            print(f"Ошибка чтения {f}: {e}")
    
    if not all_subs:
        return []
    
    with open("subscriptions_data.json", "w", encoding="utf-8") as fh:
        json.dump(all_subs, fh, ensure_ascii=False, indent=2)
    
    print(f"Все данные сохранены в subscriptions_data.json ({len(all_subs)} записей)")
    return all_subs
