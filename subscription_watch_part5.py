# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: SubscriptionWatch
def delete_subscription(sub_id: str) -> dict:
    if not sub_id or len(sub_id.strip()) == 0:
        return {"success": False, "error": "Invalid subscription ID"}
    
    try:
        index = subscriptions.index({"id": sub_id})
        deleted_sub = subscriptions.pop(index)
        
        # Удаляем связанные записи в истории платежей и уведомлениях
        payments_to_remove = [p for p in payments if p["subscription_id"] == sub_id]
        notifications_to_remove = [n for n in notifications if n["subscription_id"] == sub_id]
        
        payments.remove_all(payments_to_remove)
        notifications.remove_all(notifications_to_remove)
        
        return {
            "success": True, 
            "deleted_subscription": deleted_sub,
            "removed_payments_count": len(payments_to_remove),
            "removed_notifications_count": len(notifications_to_remove)
        }
    except ValueError:
        return {"success": False, "error": f"Subscription with ID {sub_id} not found"}

def remove_subscription_by_name(sub_name: str) -> dict:
    if not sub_name or len(sub_name.strip()) == 0:
        return {"success": False, "error": "Invalid subscription name"}
    
    try:
        index = subscriptions.index({"name": sub_name})
        deleted_sub = subscriptions.pop(index)
        
        payments_to_remove = [p for p in payments if p["subscription_id"] == deleted_sub["id"]]
        notifications_to_remove = [n for n in notifications if n["subscription_id"] == deleted_sub["id"]]
        
        payments.remove_all(payments_to_remove)
        notifications.remove_all(notifications_to_remove)
        
        return {
            "success": True, 
            "deleted_subscription": deleted_sub,
            "removed_payments_count": len(payments_to_remove),
            "removed_notifications_count": len(notifications_to_remove)
        }
    except ValueError:
        return {"success": False, "error": f"Subscription with name {sub_name} not found"}
