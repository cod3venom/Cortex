import json
from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.Globals import Debug
from Kernel.Management.Security.JSON import JSON
class BotOptionsTObject :
    def __init__(self, jsData):
        self.ID: str = Constants.EMPTY
        self.USER_ID: str = Constants.EMPTY
        self.OPTIONS_ID: str = Constants.EMPTY
        self.NAME: str = Constants.EMPTY
        self.DESCRIPTION: str = Constants.EMPTY
        self.ARG_INCOGNITO: str = Constants.EMPTY
        self.ARG_HEADLESS: str = Constants.EMPTY
        self.ARG_CACHE_FOLDER: str = Constants.EMPTY
        self.ARG_ROOT: str = Constants.EMPTY
        self.ARG_TOR: str = Constants.EMPTY
        self.ARG_PROXY_ID: str = Constants.EMPTY
        self.ARG_LINKS_PACKET_ID: str = Constants.EMPTY
        self.ARG_SELECTORS_PACKET_ID: str = Constants.EMPTY
        self.ARG_CUSTOM_JAVASCRIPT_ID: str = Constants.EMPTY
        self.DATE: str = Constants.EMPTY
        self.CopyTObject(jsData)

    def CopyTObject(self, jsData):
        if JSON().isJson(jsData):
            try:
                jsData = json.loads(jsData)
                self.ID: str = jsData['ID']
                self.USER_ID: str = jsData['USER_ID']
                self.OPTIONS_ID: str = jsData['OPTIONS_ID']
                self.NAME: str = jsData['NAME']
                self.DESCRIPTION: str = jsData['DESCRIPTION']
                self.ARG_INCOGNITO: str = jsData['ARG_INCOGNITO']
                self.ARG_HEADLESS: str = jsData['ARG_HEADLESS']
                self.ARG_CACHE_FOLDER: str = jsData['ARG_CACHE_FOLDER']
                self.ARG_ROOT: str = jsData['ARG_ROOT']
                self.ARG_TOR: str = jsData['ARG_TOR']
                self.ARG_PROXY_ID: str = jsData['ARG_PROXY_ID']
                self.ARG_LINKS_PACKET_ID: str = jsData['ARG_LINKS_PACKET_ID']
                self.ARG_SELECTORS_PACKET_ID: str = jsData['ARG_SELECTORS_PACKET_ID']
                self.ARG_CUSTOM_JAVASCRIPT_ID: str = jsData['ARG_CUSTOM_JAVASCRIPT_ID']
                self.DATE: str = jsData['DATE']

            except TypeError:
                Debug(Constants.JSON_WRONG_KEY)
            except KeyError as key:
                Debug(Constants.JSON_WRONG_KEY.format(key))
