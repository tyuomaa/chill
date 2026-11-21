# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: SubscriptionWatch
class ViewManager:
    def __init__(self, subscriptions):
        self.subscriptions = subscriptions
        self.views = {}

    def register_view(self, name, func):
        self.views[name] = func

    def get_view(self, name):
        return self.views.get(name)

    def list_all(self):
        return "\n".join(f"{s.name} | до {s.renewal_date} | {s.price}" for s in self.subscriptions)

    def list_expired(self):
        expired = [s for s in self.subscriptions if s.is_expired()]
        return "\n".join(s.name for s in expired) if expired else "Нет просроченных"

    def search(self, keyword):
        found = [s for s in self.subscriptions if keyword.lower() in s.name.lower()]
        return "\n".join(s.name for s in found) if found else "Ничего не найдено"

vm = ViewManager(subscriptions)
vm.register_view("all", vm.list_all)
vm.register_view("expired", vm.list_expired)
vm.register_view("search", vm.search)
