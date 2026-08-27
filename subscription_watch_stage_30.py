# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: SubscriptionWatch
class UserProfiles:
    _profiles = {}
    _current = None

    @classmethod
    def create(cls, name, role="user"):
        cls._profiles[name] = {"name": name, "role": role}
        cls._current = name
        return cls._profiles[name]

    @classmethod
    def current(cls):
        if cls._current is None:
            cls.create("default", "user")
        return cls._profiles[cls._current]

    @classmethod
    def switch(cls, name):
        if name not in cls._profiles:
            raise ValueError(f"Профиль '{name}' не существует")
        cls._current = name

    @classmethod
    def list_profiles(cls):
        return list(cls._profiles.keys())

    @classmethod
    def reset(cls):
        cls._profiles = {}
        cls._current = None
