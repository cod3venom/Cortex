import json

from Core.DataOperations.Strings import EMPTY
from Logger.Levels import Levels
from Logger.Logger import Logger
import Core.Security.Global as Global

from Core.DataOperations.StringBuilder import StringBuilder


class BotAuthTObject:

    def __init__(self,  USER_ID: str, CLIENT_ID: str, CLIENT_IDENTIFIER: str, CLIENT_LEVEL: str):
        self.USER_ID = USER_ID
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_IDENTIFIER = CLIENT_IDENTIFIER
        self.CLIENT_LEVEL = CLIENT_LEVEL
        self.logger = Logger()
        self.logger.Print(0, Global.levels.hackerType, message=self.__repr__(), bundler=False)

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != EMPTY:
                return cls(**json.loads(jsData))
            else:
                return cls(**{'USER_ID': 'empty', 'CLIENT_ID': 'empty', 'CLIENT_IDENTIFIER': 'empty',
                              'CLIENT_LEVEL': 'empty'})
        except KeyError as KeyErr:
            Logger().Print(3, Global.levels, bundler=True)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<BotAuthTObject:")
        buffer.append(" USER_ID=" + self.USER_ID)
        buffer.append(", CLIENT_ID=" + self.CLIENT_ID)
        buffer.append(", CLIENT_IDENTIFIER=" + self.CLIENT_IDENTIFIER)
        buffer.append(" CLIENT_LEVEL=" + self.CLIENT_LEVEL)
        buffer.append(">")
        return buffer.string
