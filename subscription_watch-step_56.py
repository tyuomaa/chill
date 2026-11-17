# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: SubscriptionWatch
def bulk_update_records(self, field_name, new_value, record_ids=None):
    if record_ids is None:
        updated = [r for r in self.records if r.get(field_name) == new_value]
    else:
        updated = [r for r in self.records if r.id in record_ids]
    for record in updated:
        record[field_name] = new_value
    return len(updated)
