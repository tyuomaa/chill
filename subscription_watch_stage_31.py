# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: SubscriptionWatch
def switch_profile(current_profile, profiles):
    """Switch the active profile and return the new one."""
    if not profiles:
        return None
    if not current_profile:
        return profiles[0]
    if isinstance(current_profile, Profile):
        for p in profiles:
            if p.name == current_profile.name:
                current_profile = p
                break
    if isinstance(current_profile, str):
        if current_profile not in profiles:
            return None
        current_profile = profiles[profiles.index(current_profile)]
    if isinstance(current_profile, int):
        if current_profile < 0 or current_profile >= len(profiles):
            return None
        current_profile = profiles[current_profile]
    return current_profile
