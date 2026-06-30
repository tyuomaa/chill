# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: SubscriptionWatch
class SubscriptionFilter:
    def __init__(self, subscriptions):
        self.subscriptions = subscriptions
    
    def filter_by_status(self, status):
        return [s for s in self.subscriptions if s.status == status]
    
    def filter_by_category(self, category):
        return [s for s in self.subscriptions if s.category == category]
    
    def filter_by_tags(self, tags):
        return [s for s in self.subscriptions if any(tag in s.tags for tag in tags)]
    
    def filter_combined(self, status=None, category=None, tags=None):
        result = self.subscriptions
        if status:
            result = self.filter_by_status(status)
        if category:
            result = [s for s in result if s.category == category]
        if tags:
            result = [s for s in result if any(tag in s.tags for tag in tags)]
        return result
