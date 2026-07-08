# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: SubscriptionWatch
import json, os

DATA_FILE = "subscriptions.json"

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return [data]
    except (json.JSONDecodeError, OSError):
        return []

def update_data(func):
    def wrapper(*args, **kwargs):
        data = load_data()
        result = func(data, *args, **kwargs)
        save_data(result)
        return result
    return wrapper
