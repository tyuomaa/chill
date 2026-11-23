# === Stage 59: Добавь диагностику производительности основных операций ===
# Project: SubscriptionWatch
import timeit

def bench(func, n=3):
    best = float('inf')
    for _ in range(n):
        best = min(best, timeit.timeit(func, number=1))
    return best

def diag():
    subs = [
        {'name': 'Spotify', 'tier': 'premium', 'price': 9.99, 'renewal': '2025-12-01', 'paid': True},
        {'name': 'Netflix', 'tier': 'standard', 'price': 15.5, 'renewal': '2025-11-15', 'paid': True},
        {'name': 'GitHub', 'tier': 'pro', 'price': 4.0, 'renewal': '2026-01-10', 'paid': True},
        {'name': 'Adobe', 'tier': 'cc', 'price': 54.99, 'renewal': '2025-10-05', 'paid': False},
    ]
    by_name = {s['name']: s for s in subs}
    totals = sum(s['price'] for s in subs)
    paid = [s for s in subs if s['paid']]
    upcoming = [s for s in subs if s['renewal'] <= '2025-12-31']
    print(f"subs: {len(subs)}, unique: {len(by_name)}, total: {totals:.2f}, "
          f"paid: {len(paid)}, renewing: {len(upcoming)}")
    print(f"bench(dict): {bench(lambda: by_name.get('Netflix', {}).get('price', 0)) * 1e6:.1f} µs")
    print(f"bench(sum): {bench(lambda: sum(s['price'] for s in subs)) * 1e6:.1f} µs")
    print(f"bench(filter): {bench(lambda: [s for s in subs if s['paid']]) * 1e6:.1f} µs")
