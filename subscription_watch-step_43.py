# === Stage 43: Добавь пагинацию длинных списков ===
# Project: SubscriptionWatch
def paginate(items, page_size=20):
    """Compact pagination helper: yields page_index and page items in chunks."""
    for start in range(0, len(items), page_size):
        page = items[start:start + page_size]
        yield start // page_size, page
