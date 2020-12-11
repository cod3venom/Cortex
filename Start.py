import sys
from Kernel.Classes.Bot.InitBotAuth import InitBotAuth

class Start:

    def cmain(self, identifier, password, options_id) -> int:
        InitBotAuth(identifier, password, options_id).doAuth()


if __name__ == "__main__":
    try:
        CLIENT_IDENTIFIER = sys.argv[1]
        CLIENT_PASSWORD = sys.argv[2]
        OPTIONS_ID = sys.argv[3]
        Start().cmain(CLIENT_IDENTIFIER, CLIENT_PASSWORD, OPTIONS_ID)
    except IndexError:
        print("error")
