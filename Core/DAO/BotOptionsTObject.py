import json

from Core.DataOperations.Logger.Levels import Levels
from Core.DataOperations.Logger.Logger import Logger, EMPTY
from Core.DataOperations.StringBuilder import StringBuilder
from Core.Security.Global import levels


class BotOptionsTObject:

    def __init__(self, ID: int, USER_ID: str, OPTIONS_ID: str, NAME: str, DESCRIPTION: str, ARG_INCOGNITO: int,
                 ARG_HEADLESS: int, ARG_CACHE_FOLDER: str, ARG_ROOT: int, ARG_TOR: int, ARG_PROXY_ID: str,
                 ARG_LINKS_PACKET_ID: str, ARG_SELECTORS_PACKET_ID: str, ARG_CUSTOM_JAVASCRIPT_ID: str, DATE: str):
        self.ID = ID
        self.USER_ID = USER_ID
        self.OPTIONS_ID = OPTIONS_ID
        self.NAME = NAME
        self.DESCRIPTION = DESCRIPTION
        self.ARG_INCOGNITO = ARG_INCOGNITO
        self.ARG_HEADLESS = ARG_HEADLESS
        self.ARG_CACHE_FOLDER = ARG_CACHE_FOLDER
        self.ARG_ROOT = ARG_ROOT
        self.ARG_TOR = ARG_TOR
        self.ARG_PROXY_ID = ARG_PROXY_ID
        self.ARG_LINKS_PACKET_ID = ARG_LINKS_PACKET_ID
        self.ARG_SELECTORS_PACKET_ID = ARG_SELECTORS_PACKET_ID
        self.ARG_CUSTOM_JAVASCRIPT_ID = ARG_CUSTOM_JAVASCRIPT_ID
        self.DATE = DATE
        Logger(False,0, Levels.hackerType, self.__repr__())

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != EMPTY:
                return cls(**json.loads(jsData))
            else:
                return cls(**{'ID': 'empty', 'USER_ID': 'empty', 'OPTIONS_ID': 'empty', 'NAME': 'empty',
                              'DESCRIPTION': 'empty', 'ARG_INCOGNITO': 'empty', 'ARG_HEADLESS': 'empty',
                              'ARG_CACHE_FOLDER': 'empty', 'ARG_ROOT': 'empty', 'ARG_TOR': 'empty',
                              'ARG_PROXY_ID': 'empty', 'ARG_LINKS_PACKET_ID': 'empty',
                              'ARG_SELECTORS_PACKET_ID': 'empty', 'ARG_CUSTOM_JAVASCRIPT_ID': 'empty', 'DATE': 'empty'})
        except KeyError as KeyErr:
            Logger(True, 3, levels.Error)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<BotOptionsTObject:")
        buffer.append(" ID=" + str(self.ID))
        buffer.append(", USER_ID=" + self.USER_ID)
        buffer.append(", OPTIONS_ID=" + self.OPTIONS_ID)
        buffer.append(", NAME=" + self.NAME)
        buffer.append(", DESCRIPTION=" + self.DESCRIPTION)
        buffer.append(", ARG_INCOGNITO=" + str(self.ARG_INCOGNITO))
        buffer.append(", ARG_HEADLESS=" + str(self.ARG_HEADLESS))
        buffer.append(", ARG_CACHE_FOLDER=" + self.ARG_CACHE_FOLDER)
        buffer.append(", ARG_ROOT=" + str(self.ARG_ROOT))
        buffer.append(", ARG_TOR=" + str(self.ARG_TOR))
        buffer.append(", ARG_PROXY_ID=" + self.ARG_PROXY_ID)
        buffer.append(", ARG_LINKS_PACKET_ID=" + self.ARG_LINKS_PACKET_ID)
        buffer.append(", ARG_SELECTORS_PACKET_ID=" + self.ARG_SELECTORS_PACKET_ID)
        buffer.append(", ARG_CUSTOM_JAVASCRIPT_ID=" + self.ARG_CUSTOM_JAVASCRIPT_ID)
        buffer.append(" DATE=" + self.DATE)
        buffer.append(">")
        return buffer.string
