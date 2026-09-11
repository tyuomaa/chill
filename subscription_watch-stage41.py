# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: SubscriptionWatch
class DryRunContext:
    def __init__(self):
        self.changes = []

    def record(self, operation, data):
        self.changes.append({"operation": operation, "data": data})

    @property
    def count(self):
        return len(self.changes)

    def summary(self):
        return f"Dry-run: {self.count} change(s) pending"

    def __repr__(self):
        return f"DryRunContext({self.summary()})"
