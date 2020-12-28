import json

from Core.DataOperations.Strings import EMPTY
from Logger.Levels import Levels
from Logger.Logger import Logger
import Core.Security.Global as Global
from Core.DataOperations.StringBuilder import StringBuilder


class BotLinksTObject:

    def __init__(self, ID: int, USER_ID: str, BOT_LINKS_PACKET_ID: str, LINK_ID: str, Link: str):
        self.ID = ID
        self.USER_ID = USER_ID
        self.BOT_LINKS_PACKET_ID = BOT_LINKS_PACKET_ID
        self.LINK_ID = LINK_ID
        self.Link = Link
        self.logger = Logger()
        self.logger.Print(0, Global.levels.hackerType, message=self.__repr__(), bundler=False)

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != EMPTY:
                return cls(**json.loads(jsData))
            else:
                return cls(**{'ID': 'empty', 'USER_ID': 'empty', 'BOT_LINKS_PACKET_ID': 'empty', 'LINK_ID': 'empty',
                              'Link': 'empty'})
        except KeyError as KeyErr:
            Logger().Print(3, Global.levels, bundler=True)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<BotLinksTObject:")
        buffer.append(" ID=" + str(self.ID))
        buffer.append(", USER_ID=" + self.USER_ID)
        buffer.append(", BOT_LINKS_PACKET_ID=" + self.BOT_LINKS_PACKET_ID)
        buffer.append(", LINK_ID=" + self.LINK_ID)
        buffer.append(" Link=" + self.Link)
        buffer.append(">")
        return buffer.string
