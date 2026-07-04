# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: SubscriptionWatch
import json, sys
from datetime import datetime, timedelta
INITIAL_DATA = '''
{
  "subscriptions": [
    {
      "id": "sub_001",
      "name": "Netflix Premium",
      "price_usd": 15.99,
      "billing_cycle_days": 30,
      "last_payment_date": "2024-06-01",
      "status": "active"
    },
    {
      "id": "sub_002",
      "name": "Spotify Family",
      "price_usd": 16.99,
      "billing_cycle_days": 30,
      "last_payment_date": "2024-05-28",
      "status": "active"
    },
    {
      "id": "sub_003",
      "name": "Adobe Creative Cloud",
      "price_usd": 59.99,
      "billing_cycle_days": 12,
      "last_payment_date": "2024-06-15",
      "status": "active"
    }
  ],
  "notifications_enabled": true,
  "currency_symbol": "$"
}
'''

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data.get("subscriptions"), list):
            raise ValueError("Invalid subscriptions format")
        
        now = datetime.now()
        processed_subs = []
        for sub in data["subscriptions"]:
            last_date_str = sub.get("last_payment_date", "")
            if last_date_str:
                try:
                    last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
                    next_renewal = (last_date + timedelta(days=sub.get("billing_cycle_days", 30))).date()
                    
                    sub["next_renewal"] = next_renewal.isoformat()
                    days_until_renewal = (next_renewal - now.date()).days
                    
                    if days_until_renewal < 0:
                        sub["status"] = "overdue"
                    elif days_until_renewal <= 7 and data.get("notifications_enabled"):
                        sub["notification_sent"] = True
                    else:
                        sub["notification_sent"] = False
                        
                except ValueError as e:
                    print(f"Warning: Invalid date format for subscription {sub['id']}: {e}")
                    continue
            
            processed_subs.append(sub)
        
        return {"subscriptions": processed_subs, "currency_symbol": data.get("currency_symbol", "$")}
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON initial data: {e}")

if __name__ == "__main__":
    loaded_data = load_initial_data(INITIAL_DATA)
    print(f"Loaded {len(loaded_data['subscriptions'])} subscriptions.")
