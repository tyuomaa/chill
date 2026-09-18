# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: SubscriptionWatch
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "subscriptions.json")

def migrate(data):
    """Migrate data to the latest version."""
    if data.get("version") == 1:
        data["version"] = 2
        if "subscriptions" not in data:
            data["subscriptions"] = []
        if "next_subscription" not in data:
            data["next_subscription"] = None
    elif data.get("version") == 2:
        data["version"] = 3
        if "history" not in data:
            data["history"] = []
    return data

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"version": 0, "subscriptions": [], "next_subscription": None, "history": []}
