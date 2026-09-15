# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: SubscriptionWatch
import os, shutil, datetime, json

def backup_data_file(db_path, backup_dir=None):
    if not os.path.exists(db_path):
        return None
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(db_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"subscription_watch_{timestamp}.json")
    shutil.copy2(db_path, backup_path)
    return backup_path
