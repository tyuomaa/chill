# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: SubscriptionWatch
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_BLUE = "\033[44m"

    @staticmethod
    def enabled():
        return os.environ.get("COLOR", "1") != "0" and sys.stdout.isatty()

    @staticmethod
    def disable():
        os.environ["COLOR"] = "0"

    @staticmethod
    def enable():
        os.environ["COLOR"] = "1"

    @staticmethod
    def reset(text):
        return text + Color.RESET if Color.enabled() else text

    @staticmethod
    def red(text):
        return Color.RED + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def green(text):
        return Color.GREEN + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def yellow(text):
        return Color.YELLOW + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def blue(text):
        return Color.BLUE + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def cyan(text):
        return Color.CYAN + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def bold(text):
        return Color.BOLD + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def magenta(text):
        return Color.MAGENTA + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def underline(text):
        return Color.UNDERLINE + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def bg_red(text):
        return Color.BG_RED + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def bg_green(text):
        return Color.BG_GREEN + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def bg_blue(text):
        return Color.BG_BLUE + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def dim(text):
        return Color.DIM + text + Color.RESET if Color.enabled() else text

    @staticmethod
    def blink(text):
        return Color.BLINK + text + Color.RESET if Color.enabled() else text
