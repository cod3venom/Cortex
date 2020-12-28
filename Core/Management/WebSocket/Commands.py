from Vendors.AWS.Main import AwsAuth
from Vendors.Ekw.Main import EkwAuth
from Vendors.Allegro.Main import AllegroAuth

from Logger.Logger import Logger
from Core.DataOperations.Strings import *
import Core.Security.Global as Global


class Commands:

    def __init__(self):
        self.__Message = EMPTY
        self.__Client = None
        self.logger = Logger()

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
        self.logger.Print(1, Global.levels.Info, bundler=True)

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
                Commands[1] = amazon
                Commands[2] = product
                Commands[3] = scraper
                Commands[4] = bot identifier
                Commands[5] = bot password 
                Commands[6] = options_id 
                Commands[7] = total process number 
            """
            # Start amazon product scraper admin pgp fcee8557690e8ce6a9292310ff02dd71 6
            if Com[0] == Start:
                if Com[1] == Amazon and Com[2] == Product and Com[3] == Scraper and Com[4] is not None and Com[5] and \
                        Com[6] is not None and Com[7] is not None:
                    AwsAuth(Com[4], Com[5], Com[6], Com[7]).Login()

                if Com[1] == Ekw and Com[2] is not None and Com[3] is not None and Com[4] is not None:
                    EkwAuth(Com[2], Com[3], Com[4], Com[5]).Login()

                if Com[1] == Allegro and Com[2] == Category and Com[3] == Crawler and Com[4] is not None and Com[5] is not None and Com[6] is not None and Com[7]:
                    AllegroAuth(Com[4], Com[5], Com[6],0).parseCategory()
                    exit()

        except IndexError as index:
            self.logger.Print(2, Global.levels.Info, bundler=True)
