import json

from Core.DataOperations.Logger.Levels import Levels
from Core.DataOperations.Logger.Logger import Logger, EMPTY
from Core.Security.Global import  levels
from Core.DataOperations.StringBuilder import StringBuilder


class BotAuthTObject:

    def __init__(self,  USER_ID: str, CLIENT_ID: str, CLIENT_IDENTIFIER: str, CLIENT_LEVEL: str):
        self.USER_ID = USER_ID
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_IDENTIFIER = CLIENT_IDENTIFIER
        self.CLIENT_LEVEL = CLIENT_LEVEL
        Logger(False,0, Levels.hackerType, self.__repr__())

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != EMPTY:
                return cls(**json.loads(jsData))
            else:
                return cls(**{'USER_ID': 'empty', 'CLIENT_ID': 'empty', 'CLIENT_IDENTIFIER': 'empty',
                              'CLIENT_LEVEL': 'empty'})
        except KeyError as KeyErr:
            Logger(True, 3, levels.Error)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<BotAuthTObject:")
        buffer.append(" USER_ID=" + self.USER_ID)
        buffer.append(", CLIENT_ID=" + self.CLIENT_ID)
        buffer.append(", CLIENT_IDENTIFIER=" + self.CLIENT_IDENTIFIER)
        buffer.append(" CLIENT_LEVEL=" + self.CLIENT_LEVEL)
        buffer.append(">")
        return buffer.string
