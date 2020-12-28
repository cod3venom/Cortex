import datetime
import inspect

from Core.DataOperations.Colors import Colors
from Logger.Levels import Levels
from Core.DataOperations.Strings import *
import Core.Security.Global as Global


class Logger:
    def __init__(self):
        self.level = EMPTY
        self.levels = Levels()
        self.text = EMPTY
        self.color = EMPTY
        self.colors = Colors()

    def initColor(self):
        if self.level == self.levels.Info:
            self.color = self.colors.Info
        if self.level == self.levels.Success:
            self.color = self.colors.Success
        if self.level == self.levels.Warning:
            self.color = self.colors.Warning
        if self.level == self.levels.Error:
            self.color = self.colors.Error
        if self.level == self.levels.hackerType:
            self.color = self.colors.hackerType

    def Print(self, msg_num: int, level: Levels, bundler: bool = False, message: str = None):
        self.level = level
        self.initColor()

        self.caller = inspect.stack()[1][0].f_locals["self"].__class__.__name__ + DOT + inspect.stack()[
            1].function + HASHTAG + str(inspect.stack()[1].lineno)
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if bundler:
            self.text = Global.Local_Settings.Bundler.getText(msg_num)
        else:
            if message:
                self.text = str(message)

        text = Global.Local_Settings.LOG_FORMAT.format(
            self.colors.Success,
            Global.Local_Settings.TERMINAL_PREFIX,
            self.colors.Warning + self.time,
            self.color + self.caller,
            self.text
        )
        print(text)
        self.text = EMPTY
        text = EMPTY
