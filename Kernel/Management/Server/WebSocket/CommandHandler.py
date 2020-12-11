import os

from Kernel.Security.Process import Process
from Kernel.Settings.Constants import Constants


class CommandHandler:
    def __init__(self):
        self.Message: str = ''
        self.Client = None
        self.Process = Process()

    def setMessage(self, message: str) -> int:
        self.Message = message

    def getMessage(self) -> str:
        return self.Message

    def setClient(self, client) -> int:
        self.Client = client

    def getClient(self):
        return self.Client

    async def Server_listener(self, client, path):
        self.Client = client
        try:
            async for Message in self.Client:
                self.setMessage(Message)
                await self.Handler()
        except:
            pass

    async def Handler(self):
        if Constants.SPACE in self.getMessage():
            Commands = self.getMessage().split(Constants.SPACE)
            self.Switch(Commands)

    def Switch(self, Commands: list) -> int:
        try:
            """
                Commands[0] = Start with capital S
                Commands[1] = spider with lower s
                Commands[2] = Botclient username
                Commands[3] = Botclient password 
                Commands[4] = OPTIONS_ID 
                Commands[5] = TOTAL_PROCESS 
            """
            if Commands[0] == Constants.START:
                if Commands[1] == Constants.SPIDER and Commands[2] is not None:
                    self.RunSpider(Commands[2], Commands[3], Commands[4], Commands[5])
        except IndexError:
            pass

    def RunSpider(self, CLIENT_IDENTIFIER: str, CLIENT_PASSWORD: str, OPTIONS_ID: str, TOTAL_PROCESS: int) -> int:

        for process in range(int(TOTAL_PROCESS)):
            Command = Constants.BOT_LAUNCHER.format(str(process), os.getcwd(), CLIENT_IDENTIFIER, CLIENT_PASSWORD, OPTIONS_ID)
            self.Process.Execute(Command)


        #print(str(self.Process.getAllTasks()))
