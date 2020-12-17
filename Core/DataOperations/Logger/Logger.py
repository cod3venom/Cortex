import datetime
import inspect

from Core.DataOperations.Colors import Colors
from Core.DataOperations.Logger.Levels import Levels
from Core.DataOperations.Strings import *
import Core.Security.Global as Global


class Logger:

    def __init__(self, bundler: bool, msg_num: int, level: Levels, message: str = None):
        self.Level = level
        self.Color = EMPTY
        self.Log = EMPTY
        self.__caller = inspect.stack()[1][0].f_locals["self"].__class__.__name__ + DOT + inspect.stack()[
            1].function + HASHTAG + str(inspect.stack()[1].lineno)

        if bundler:
            self.Message = Global.Local_Settings.Bundler.getText(msg_num)
        else:
            self.Message = str(message) + EMPTY
        self.TIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.doLog()

    def setLevel(self, Level: Levels):
        self.Level = Level

    def getLevel(self):
        return self.Level

    def initColor(self):
        if self.getLevel() == Levels().Info:
            self.Color = Colors().Info
        if self.getLevel() == Levels().Success:
            self.Color = Colors().Success
        if self.getLevel() == Levels().Warning:
            self.Color = Colors().Warning
        if self.getLevel() == Levels().Error:
            self.Color = Colors().Error
        if self.getLevel() == Levels().hackerType:
            self.Color = Colors().hackerType

    def setMessage(self, message: str):
        self.Message = message

    def getMessage(self) -> str:
        return self.Message

    def doLog(self):
        self.initColor()
        Global.GLOBAL_LOG = Global.Local_Settings.LOG_FORMAT.format(
            Colors().Success,
            Global.Local_Settings.TERMINAL_PREFIX,
            Colors().Warning + self.TIME_NOW,
            self.Color + self.__caller,
            self.getMessage()
        )
        print('\n' + Global.GLOBAL_LOG)





