import json
from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.Globals import Debug
from Kernel.Management.Security.JSON import JSON


class BotXpathSelectorsTObject:
    def __init__(self,  jsData=None):
        self.ID: str = Constants.EMPTY
        self.USER_ID: str = Constants.EMPTY
        self.PACKET_ID: str = Constants.EMPTY
        self.SELECTOR_ID: str = Constants.EMPTY
        self.SELECTOR_KEY: str = Constants.EMPTY
        self.SELECTOR_VALUE: str = Constants.EMPTY
        self.DATE: str = Constants.EMPTY
        self.CopyTObject(jsData)

    def CopyTObject(self, jsData):
        try:
            self.ID: str = jsData['ID']
            self.USER_ID: str = jsData['USER_ID']
            self.PACKET_ID: str = jsData['PACKET_ID']
            self.SELECTOR_ID: str = jsData['SELECTOR_ID']
            self.SELECTOR_KEY: str = jsData['SELECTOR_KEY']
            self.SELECTOR_VALUE: str = jsData['SELECTOR_VALUE']
            self.DATE: str = jsData['DATE']

        except TypeError:
            Debug(Constants.JSON_WRONG_KEY)
        except KeyError as key:
            Debug(Constants.JSON_WRONG_KEY.format(key))

    def IndexedJson(self, jsData):
        try:
            jsData = json.loads(jsData)
        except TypeError:
            Debug(Constants.JSON_WRONG_KEY)
        except KeyError as key:
            Debug(Constants.JSON_WRONG_KEY.format(key))
        finally:
            return jsData
