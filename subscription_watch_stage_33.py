# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: SubscriptionWatch
def _undo_last(self):
        if not self._undo_stack:
            print("Нет откатываемых действий.")
            return
        action = self._undo_stack.pop()
        if action is None:
            print("Действие не может быть отменено.")
            return
        try:
            if isinstance(action, tuple):
                target, fn, args = action
                fn(target, *args)
            else:
                target, fn, args = action
                fn(target, *args)
            print("Действие отменено.")
        except Exception as e:
            print(f"Ошибка при откате: {e}")
