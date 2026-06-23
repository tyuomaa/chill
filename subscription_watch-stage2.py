# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: SubscriptionWatch
class Subscription:
    def __init__(self, name: str, price: float, renewal_date: str):
        self.name = name
        self.price = price
        self.renewal_date = datetime.strptime(renewal_date, "%Y-%m-%d") if isinstance(renewal_date, str) else renewal_date

    def validate(self) -> bool:
        return len(self.name.strip()) > 0 and self.price >= 0 and self.renewal_date is not None


def parse_subscription_input(user_input: dict) -> Subscription | None:
    try:
        name = user_input.get("name", "").strip()
        price_str = str(user_input.get("price")).replace(",", ".")
        renewal_date = user_input.get("renewal_date", "")

        if not name or float(price_str) < 0:
            return None

        try:
            renewal_date_obj = datetime.strptime(renewal_date, "%Y-%m-%d").date()
        except ValueError:
            return None

        return Subscription(name=name, price=float(price_str), renewal_date=renewal_date_obj)
    except Exception:
        return None
