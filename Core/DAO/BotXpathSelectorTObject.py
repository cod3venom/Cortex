import json

from Core.DataOperations.Logger.Levels import Levels
from Core.DataOperations.Logger.Logger import Logger, EMPTY
from Core.Security.Global import levels, __SELECTORS__
from Core.DataOperations.StringBuilder import StringBuilder


class BotXpathSelectorTObject:

    def __init__(self, ID: int, USER_ID: str, PACKET_ID: str, SELECTOR_ID: str, SELECTOR_KEY: str, SELECTOR_VALUE: str,
                 DATE: str):
        self.ID = ID
        self.USER_ID = USER_ID
        self.PACKET_ID = PACKET_ID
        self.SELECTOR_ID = SELECTOR_ID
        self.SELECTOR_KEY = SELECTOR_KEY
        self.SELECTOR_VALUE = SELECTOR_VALUE
        self.DATE = DATE
        Logger(False,0, Levels.hackerType, self.__repr__())

    @classmethod
    def TO(cls, jsData: str):
        global __SELECTORS__
        try:
            if jsData != EMPTY:
                indexed_js = json.loads(jsData)
                if len(__SELECTORS__) > 0:
                    __SELECTORS__.clear()
                for key in indexed_js.keys():
                    __SELECTORS__.append(cls(**indexed_js[key]))
                return __SELECTORS__
            else:
                return cls(**{'ID': 'empty', 'USER_ID': 'empty', 'PACKET_ID': 'empty', 'SELECTOR_ID': 'empty',
                              'SELECTOR_KEY': 'empty', 'SELECTOR_VALUE': 'empty', 'DATE': 'empty'})
        except KeyError as KeyErr:
            Logger(True, 3, levels.Error)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<BotXpathSeletorTObject:")
        buffer.append(" ID=" + str(self.ID))
        buffer.append(", USER_ID=" + self.USER_ID)
        buffer.append(", PACKET_ID=" + self.PACKET_ID)
        buffer.append(", SELECTOR_ID=" + self.SELECTOR_ID)
        buffer.append(", SELECTOR_KEY=" + self.SELECTOR_KEY)
        buffer.append(", SELECTOR_VALUE=" + self.SELECTOR_VALUE)
        buffer.append(" DATE=" + self.DATE)
        buffer.append(">")
        return buffer.string
