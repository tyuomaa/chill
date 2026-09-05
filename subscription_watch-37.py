# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: SubscriptionWatch
import unittest


class TestSubscription(unittest.TestCase):
    def test_create_subscription(self):
        s = Subscription("Netflix", "Premium", 15.99, "2025-12-01")
        self.assertEqual(s.name, "Netflix")
        self.assertEqual(s.plan, "Premium")
        self.assertEqual(s.price, 15.99)
        self.assertEqual(s.renewal_date, "2025-12-01")

    def test_add_payment(self):
        s = Subscription("Spotify", "Individual", 9.99, "2025-06-15")
        s.add_payment("2025-06-15", 9.99)
        self.assertEqual(len(s.payments), 1)
        self.assertEqual(s.payments[0].amount, 9.99)

    def test_total_spent(self):
        s = Subscription("GitHub", "Pro", 4.00, "2025-01-01")
        s.add_payment("2025-01-01", 4.00)
        s.add_payment("2025-02-01", 4.00)
        self.assertAlmostEqual(s.total_spent(), 8.00, places=2)

    def test_is_expired(self):
        s = Subscription("OldService", "Basic", 2.99, "2024-01-01")
        self.assertTrue(s.is_expired())

    def test_not_expired(self):
        s = Subscription("NewService", "Basic", 2.99, "2026-01-01")
        self.assertFalse(s.is_expired())

    def test_notify_expiring(self):
        s = Subscription("Upcoming", "Basic", 2.99, "2025-06-01")
        s.add_payment("2025-06-01", 2.99)
        self.assertTrue(s.should_notify("2025-05-25"))
        self.assertFalse(s.should_notify("2025-07-01"))

    def test_notify_soon(self):
        s = Subscription("AlmostDue", "Basic", 2.99, "2025-06-01")
        s.add_payment("2025-06-01", 2.99)
        self.assertTrue(s.should_notify("2025-05-28"))

    def test_notify_late(self):
        s = Subscription("Overdue", "Basic", 2.99, "2025-06-01")
        s.add_payment("2025-06-01", 2.99)
        self.assertTrue(s.should_notify("2025-06-05"))


if __name__ == "__main__":
    unittest.main()
