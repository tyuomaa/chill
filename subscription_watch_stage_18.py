# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: SubscriptionWatch
def add_tag(sub_id: str, tag: str) -> bool:
    sub = find_subscription(sub_id)
    if not sub or tag in sub.tags:
        return False
    sub.tags.append(tag)
    save_data()
    print(f"Added tag '{tag}' to subscription {sub_id}")
    return True


def remove_tag(sub_id: str, tag: str) -> bool:
    sub = find_subscription(sub_id)
    if not sub or tag not in sub.tags:
        return False
    sub.tags.remove(tag)
    save_data()
    print(f"Removed tag '{tag}' from subscription {sub_id}")
    return True


def list_tags(sub_id: str) -> List[str]:
    sub = find_subscription(sub_id)
    if not sub:
        return []
    return sorted(sub.tags)
