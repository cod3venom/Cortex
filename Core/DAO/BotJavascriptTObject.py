import json

from Core.DataOperations.Logger.Logger import Logger, EMPTY
from Core.Security.Global import levels
from Core.DataOperations.StringBuilder import StringBuilder


class BotJavascriptTObject:

    def __init__(self, ID: int, USER_ID: str, JS_ID: str, JS_NAME: str, JS_CODE: str, IS_JQUERY: int, DATE: str):
        self.ID = ID
        self.USER_ID = USER_ID
        self.JS_ID = JS_ID
        self.JS_NAME = JS_NAME
        self.JS_CODE = JS_CODE
        self.IS_JQUERY = IS_JQUERY
        self.DATE = DATE

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != EMPTY:
                return cls(**json.loads(jsData))
            else:
                return cls(
                    **{'ID': 'empty', 'USER_ID': 'empty', 'JS_ID': 'empty', 'JS_NAME': 'empty', 'JS_CODE': 'empty',
                       'IS_JQUERY': 'empty', 'DATE': 'empty'})
        except KeyError as KeyErr:
            Logger(True, 3, levels.Error)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<BotJavascriptTObject:")
        buffer.append(" ID=" + str(self.ID))
        buffer.append(", USER_ID=" + self.USER_ID)
        buffer.append(", JS_ID=" + self.JS_ID)
        buffer.append(", JS_NAME=" + self.JS_NAME)
        buffer.append(", JS_CODE=" + self.JS_CODE)
        buffer.append(", IS_JQUERY=" + str(self.IS_JQUERY))
        buffer.append(" DATE=" + self.DATE)
        buffer.append(">")
        return buffer.string
