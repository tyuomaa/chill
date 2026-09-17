# === Stage 45: Добавь восстановление из резервной копии ===
# Project: SubscriptionWatch
import json, os
from datetime import datetime, timedelta

class SubscriptionBackup:
    """Управление резервными копиями подписок."""

    def __init__(self, data_dir="backup"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def save_backup(self, subscriptions, filename="backup.json"):
        """Сохраняет текущие подписки в резервную копию."""
        backup_path = os.path.join(self.data_dir, filename)
        backup_data = {
            "created_at": datetime.now().isoformat(),
            "subscriptions": subscriptions
        }
        with open(backup_path, "w", encoding="utf-8") as f:
            json.dump(backup_data, f, indent=2, ensure_ascii=False)
        return backup_path

    def load_backup(self, filename="backup.json"):
        """Загружает подписки из резервной копии."""
        backup_path = os.path.join(self.data_dir, filename)
        if not os.path.exists(backup_path):
            return None
        with open(backup_path, "r", encoding="utf-8") as f:
            backup_data = json.load(f)
        return backup_data.get("subscriptions")

    def list_backups(self):
        """Возвращает список всех доступных резервных копий."""
        backups = []
        for f in os.listdir(self.data_dir):
            if f.endswith(".json"):
                backups.append(f)
        return sorted(backups)
