import json
from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.Globals import Debug
from Kernel.Management.Security.JSON import JSON


class BotJavascriptTObject:
    def __init__(self, jsData):
        self.ID: str = Constants.EMPTY
        self.USER_ID: str = Constants.EMPTY
        self.JS_ID: str = Constants.EMPTY
        self.JS_NAME: str = Constants.EMPTY
        self.JS_CODE: str = Constants.EMPTY
        self.IS_JQUERY: str = Constants.EMPTY
        self.DATE: str = Constants.EMPTY
        self.CopyTObject(jsData)

    def CopyTObject(self, jsData):
        if JSON().isJson(jsData):
            try:
                jsData = json.loads(jsData)
                self.ID: str = jsData['ID']
                self.USER_ID: str = jsData['USER_ID']
                self.JS_ID: str = jsData['JS_ID']
                self.JS_NAME: str = jsData['JS_NAME']
                self.JS_CODE: str = jsData['JS_CODE']
                self.IS_JQUERY: str = jsData['IS_JQUERY']
                self.DATE: str = jsData['DATE']

            except TypeError:
                Debug(Constants.JSON_WRONG_KEY)
            except KeyError as key:
                Debug(Constants.JSON_WRONG_KEY.format(key))
