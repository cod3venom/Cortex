from Kernel.Management.Security.Process import Process
from Kernel.Management.Security.Constants import Constants


class CommandHandler:
    def __init__(self):
        self.Message: str = Constants.EMPTY
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
                    self.Process.RunSpider(Commands[2], Commands[3], Commands[4], Commands[5])

            if Commands[0] == Constants.STOP:
                if Commands[1] == Constants.SPIDER and Commands[2] is not None:
                    '''
                    :param Commands[2] stands for OPTIONS_ID
                    '''
                    self.Process.StopSpider(Commands[2])
        except IndexError:
            pass




        #print(str(self.Process.getAllTasks()))
