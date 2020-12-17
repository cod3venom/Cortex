from Core.Actions.Auth.Auth import Auth
from Core.DataOperations.Logger.Logger import Logger
from Core.DataOperations.Strings import *
from Core.Security.Global import *
from Core.Texts.Bundler import Bundler
from concurrent.futures import ThreadPoolExecutor


class Commands:

    def __init__(self):
        self.__Message = EMPTY
        self.__Client = None
        self.__bundler = Bundler(Local_Settings)

    def setMessage(self, message: str):
        self.__Message = message.lower()

    def getMessage(self):
        return self.__Message

    def setClient(self, Client):
        self.__Client = Client

    def getClient(self):
        return self.__Client

    async def Server_listener(self, client, path):
        self.setClient(client)

        Logger(True, 1, levels.Info)

        async for Message in self.__Client:
            self.setMessage(Message)
            await self.Handler()


    async def Handler(self):
        if SPACE in self.getMessage():
            Com = self.getMessage().split(SPACE)
            await self.Switch(Com)

    async def Switch(self, Com: list):
        try:
            """
                Commands[0] = Start with capital S
                Commands[1] = scraper with lower s
                Commands[2] = Botclient username
                Commands[3] = Botclient password 
                Commands[4] = OPTIONS_ID 
                Commands[5] = TOTAL_PROCESS 
            """
            if Com[0] == Start:
                if Com[1] == Scraper and Com[2] is not None and Com[3] is not None and Com[4] is not None and Com[5] is not None:
                    Auth(Com[2], Com[3], Com[4], Com[5]).Login()


        except IndexError as index:
            Logger(True, 2,levels.Warning)
