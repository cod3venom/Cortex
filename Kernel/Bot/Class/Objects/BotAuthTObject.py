import json

from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.Globals import Debug
from Kernel.Management.Security.JSON import JSON


class BotAuthTObject:
    def __init__(self, jsData):
        self.USER_ID: str = Constants.EMPTY
        self.USER_ID: str =  Constants.EMPTY
        self.CLIENT_ID: str =  Constants.EMPTY
        self.CLIENT_IDENTIFIER: str =  Constants.EMPTY
        self.CLIENT_LEVEL: str =  Constants.EMPTY
        self.CopyTObject(jsData)

    def CopyTObject(self, jsData):
        if JSON().isJson(jsData):
            try:
                jsData = json.loads(jsData)
                self.USER_ID: str = jsData['USER_ID']
                self.CLIENT_ID: str = jsData['CLIENT_ID']
                self.CLIENT_IDENTIFIER: str = jsData['CLIENT_IDENTIFIER']
                self.CLIENT_LEVEL: str = jsData['CLIENT_LEVEL']
            except TypeError:
                Debug(Constants.JSON_WRONG_KEY)
            except KeyError as key:
                Debug(Constants.JSON_WRONG_KEY.format(key))
