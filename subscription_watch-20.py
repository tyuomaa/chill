# === Stage 20: Добавь восстановление записей из архива ===
# Project: SubscriptionWatch
def restore_from_archive(archive_path, subscriptions_store):
    """Restore subscription records from a JSON archive file."""
    if not os.path.exists(archive_path):
        print(f"Archive not found: {archive_path}")
        return 0
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            archived = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading archive: {e}")
        return 0
    
    restored_count = 0
    for item in archived:
        if isinstance(item, dict):
            record_id = item.pop('id', None) or f"restored_{uuid.uuid4().hex[:8]}"
            subscriptions_store.add_subscription(item, record_id=record_id)
            restored_count += 1
