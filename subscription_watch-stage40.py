# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: SubscriptionWatch
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="SubscriptionWatch CLI")
    sub = parser.add_subparsers(dest="command")

    list_parser = sub.add_parser("list", help="Show all subscriptions")
    list_parser.set_defaults(func=list_subscriptions)

    add_parser = sub.add_parser("add", help="Add a new subscription")
    add_parser.add_argument("name", help="Subscription name")
    add_parser.add_argument("--price", required=True, help="Price in rubles")
    add_parser.add_argument("--period", required=True, help="Billing period (e.g., monthly)")
    add_parser.add_argument("--next_renewal", required=True, help="Next renewal date (YYYY-MM-DD)")
    add_parser.add_argument("--auto_renew", action="store_true", help="Auto-renew")
    add_parser.add_argument("--contact", help="Contact info")
    add_parser.set_defaults(func=add_subscription)

    remove_parser = sub.add_parser("remove", help="Remove a subscription by name")
    remove_parser.add_argument("name", help="Subscription name to remove")
    remove_parser.set_defaults(func=remove_subscription)

    search_parser = sub.add_parser("search", help="Search subscriptions")
    search_parser.add_argument("query", help="Search term")
    search_parser.set_defaults(func=search_subscriptions)

    return parser.parse_args()
