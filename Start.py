import sys, urwid

from Kernel.Bot.Class.Actions.BotAuth import BotAuth


class Start:




    def cmain(self, identifier, password, options_id) -> int:
         BotAuth(identifier, password, options_id)



if __name__ == "__main__":
    try:

        CLIENT_IDENTIFIER = sys.argv[1]
        CLIENT_PASSWORD = sys.argv[2]
        OPTIONS_ID = sys.argv[3]


        Start().cmain(CLIENT_IDENTIFIER, CLIENT_PASSWORD, OPTIONS_ID)



    except IndexError:
        print("error")
