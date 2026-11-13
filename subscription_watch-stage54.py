# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: SubscriptionWatch
import json
from datetime import datetime

class FavoritesManager:
    def __init__(self, storage):
        self.storage = storage
        self.favorites = self._load_favorites()

    def _load_favorites(self):
        try:
            data = self.storage.read("favorites")
            return data.get("items", [])
        except Exception:
            return []

    def _save_favorites(self):
        self.storage.write("favorites", {"items": self.favorites})

    def toggle_favorite(self, subscription_id):
        if subscription_id in self.favorites:
            self.favorites.remove(subscription_id)
        else:
            self.favorites.append(subscription_id)
        self._save_favorites()

    def is_favorite(self, subscription_id):
        return subscription_id in self.favorites

    def get_favorite_subscriptions(self, subscriptions):
        result = []
        for sub in subscriptions:
            if self.is_favorite(sub["id"]):
                result.append(sub)
        return result

    def get_favorite_ids(self):
        return self.favorites

    def quick_access_panel(self):
        favorites = self.get_favorite_subscriptions(
            self.storage.read("subscriptions").get("subscriptions", [])
        )
        lines = ["=== Избранные подписки ==="]
        if not favorites:
            lines.append("Нет избранных записей")
        else:
            for sub in favorites:
                lines.append(f"[★] {sub.get('name', 'unknown')}")
        return "\n".join(lines)
