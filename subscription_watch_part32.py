# === Stage 32: Добавь журнал действий пользователя ===
# Project: SubscriptionWatch
import datetime

class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, action_type, description, user_id=None):
        entry = {
            "timestamp": datetime.datetime.now(),
            "action_type": action_type,
            "description": description,
            "user_id": user_id
        }
        self._entries.append(entry)

    def get_recent(self, limit=10):
        return self._entries[-limit:]

    def get_by_type(self, action_type):
        return [e for e in self._entries if e["action_type"] == action_type]
