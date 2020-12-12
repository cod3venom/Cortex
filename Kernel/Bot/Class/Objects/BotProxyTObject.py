import json
from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.Globals import Debug
from Kernel.Management.Security.JSON import JSON


class BotProxyTObject:
    def __init__(self, jsData):
        self.ID: str = Constants.EMPTY
        self.USER_ID: str = Constants.EMPTY
        self.PROXY_ID: str = Constants.EMPTY
        self.PROXY_SERVER: str = Constants.EMPTY
        self.PROXY_PORT: str = Constants.EMPTY
        self.DATE: str = Constants.EMPTY
        self.CopyTObject(jsData)

    def CopyTObject(self, jsData):
        if JSON().isJson(jsData):
            try:
                jsData = json.loads(jsData)
                self.ID: str = jsData['ID']
                self.USER_ID: str = jsData['USER_ID']
                self.PROXY_ID: str = jsData['PROXY_ID']
                self.PROXY_SERVER: str = jsData['PROXY_SERVER']
                self.PROXY_PORT: str = jsData['PROXY_PORT']
                self.DATE: str = jsData['DATE']

            except TypeError:
                Debug(Constants.JSON_WRONG_KEY)
            except KeyError as key:
                Debug(Constants.JSON_WRONG_KEY.format(key))