# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: SubscriptionWatch
def print_project_metrics():
    """Рассчитать ключевые метрики проекта SubscriptionWatch."""
    metrics = {}
    
    # Подсчёт количества классов (без учета вспомогательных)
    core_classes = ['Subscription', 'Plan', 'Payment', 'Reminder', 'Dashboard']
    class_count = sum(1 for cls in core_classes if hasattr(cls, '__dict__'))
    
    # Анализ методов в классах
    total_methods = 0
    for cls_name in core_classes:
        try:
            obj = globals()[cls_name]
            methods = [m for m in dir(obj) if not m.startswith('_')]
            metrics[f'{cls_name}_public_methods'] = len(methods)
            total_methods += len(methods)
        except KeyError:
            pass
    
    # Количество строк кода в каждом классе (примерная оценка)
    class_sizes = {}
    for cls_name in core_classes:
        try:
            obj = globals()[cls_name]
            methods = [m for m in dir(obj) if not m.startswith('_')]
            class_sizes[cls_name] = len(methods) * 5  # ~5 строк на метод
        except KeyError:
            pass
    
    metrics['total_core_methods'] = total_methods
    metrics['estimated_code_lines'] = sum(class_sizes.values())
    
    print("Метрики проекта SubscriptionWatch:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    print_project_metrics()
