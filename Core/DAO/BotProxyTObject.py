import json

from Core.DataOperations.Logger.Levels import Levels
from Core.DataOperations.Logger.Logger import Logger, EMPTY
from Core.Security.Global import Local_Settings, levels
from Core.DataOperations.StringBuilder import StringBuilder


class BotProxyTObject:

    def __init__(self,ID: int, USER_ID: str, PROXY_ID: str, PROXY_SERVER: str, PROXY_PORT: str, DATE: str):
        self.ID = ID
        self.USER_ID = USER_ID
        self.PROXY_ID = PROXY_ID
        self.PROXY_SERVER = PROXY_SERVER
        self.PROXY_PORT = PROXY_PORT
        self.DATE = DATE
        Logger(False,0, Levels.hackerType, self.__repr__())



    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != EMPTY:
                return cls(**json.loads(jsData))
            else:
                return cls(**{'ID': 'empty', 'USER_ID': 'empty', 'PROXY_ID': 'empty', 'PROXY_SERVER': 'empty', 'PROXY_PORT': 'empty', 'DATE': 'empty'})
        except KeyError as KeyErr:
            Logger(True, 3, levels.Error)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<BotProxyTObject:")
        buffer.append(" ID=" + str(self.ID))
        buffer.append(" USER_ID=" + self.USER_ID)
        buffer.append(" PROXY_ID=" + self.PROXY_ID)
        buffer.append(" PROXY_SERVER=" + self.PROXY_SERVER)
        buffer.append(" PROXY_PORT=" + self.PROXY_PORT)
        buffer.append(" DATE=" + self.DATE)
        buffer.append(">")
        return buffer.string

