import json
from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.Globals import Debug
from Kernel.Management.Security.JSON import JSON


class BotLinksTObject:
    def __init__(self, jsData):
        self.ID: str = Constants.EMPTY
        self.USER_ID: str = Constants.EMPTY
        self.BOT_LINKS_PACKET_ID: str = Constants.EMPTY
        self.LINK_ID: str = Constants.EMPTY
        self.Link: str = Constants.EMPTY
        self.CopyTObject(jsData)

    def CopyTObject(self, jsData):
        if JSON().isJson(jsData):
            try:
                jsData = json.loads(jsData)
                self.ID: str = jsData['ID']
                self.USER_ID: str = jsData['USER_ID']
                self.BOT_LINKS_PACKET_ID: str = jsData['BOT_LINKS_PACKET_ID']
                self.LINK_ID: str = jsData['LINK_ID']
                self.Link: str = jsData['Link']

            except TypeError:
                Debug(Constants.JSON_WRONG_KEY)
            except KeyError as key:
                Debug(Constants.JSON_WRONG_KEY.format(key))
