from colorama import Fore, Back, Style
from colorama import init


class Colors:
    @property
    def Default(self):
        return Fore.WHITE

    @property
    def Success(self):
        return Fore.GREEN

    @property
    def Error(self):
        return Fore.RED

    @property
    def Warning(self):
        return Fore.YELLOW

    @property
    def Info(self):
        return Fore.BLUE

    @property
    def hackerType(self):
        return Fore.LIGHTCYAN_EX
