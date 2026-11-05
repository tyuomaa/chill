# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: SubscriptionWatch
import datetime as dt


class ChangeLog:
    def __init__(self):
        self._log = []

    def add(self, subject, detail):
        entry = {
            "time": dt.datetime.now().isoformat(timespec="seconds"),
            "subject": subject,
            "detail": detail,
        }
        self._log.append(entry)
        return entry

    def log_subscription_change(self, sub_id, field, old_value, new_value):
        return self.add(
            f"subscription:{sub_id}",
            f"{field}: {old_value} -> {new_value}",
        )

    def log_payment_change(self, pay_id, field, old_value, new_value):
        return self.add(
            f"payment:{pay_id}",
            f"{field}: {old_value} -> {new_value}",
        )

    def log_renewal(self, sub_id, date):
        return self.add(
            f"renewal:{sub_id}",
            f"renewal date set to {date.isoformat()}",
        )

    def log_notification(self, kind, message):
        return self.add(
            f"notification:{kind}",
            message,
        )

    def get(self, subject=None):
        if subject is None:
            return list(self._log)
        return [e for e in self._log if e["subject"] == subject]


CHANGE_LOG = ChangeLog()
