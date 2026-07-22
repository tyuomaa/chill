# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: SubscriptionWatch
def archive_old_records(db, cutoff_days=365):
    """Archive records older than cutoff_days into a separate table."""
    import datetime
    cutoff = datetime.date.today() - datetime.timedelta(days=cutoff_days)
    archived = db.execute("SELECT id FROM subscriptions WHERE renewal_date < ?", (cutoff,)).fetchall()
    for row in archived:
        rec_id = row[0]
        try:
            db.execute("INSERT INTO subscription_archive SELECT * FROM subscriptions WHERE id = ?", (rec_id,))
            db.execute("DELETE FROM subscriptions WHERE id = ?", (rec_id,))
        except Exception as e:
            print(f"Archive warning for {rec_id}: {e}")
    db.commit()
