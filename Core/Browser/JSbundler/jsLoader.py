import glob

from Core.DAO.LocalSettingsTObject import LocalSettingsTObject
from Core.DataOperations.Logger.Levels import Levels
from Core.Security.FileSystem import FileSystem
from Core.Security.Global import Local_Settings


class jsLoader:

    def __init__(self):
        self.local_settings = Local_Settings
        self.path = Local_Settings.JS_PATH
        self.__fileSystem = FileSystem()
        self.JS_STACK = {}

        self.loadFiles()

    def loadFiles(self):
        files = glob.glob(f"{self.path}*.js")
        for file in files:
            self.jsStackAdd(self.__fileSystem.getFilename(file), self.__fileSystem.readfile(file))

    def jsStackExists(self, key):
        for k in self.JS_STACK.keys():
            if k == key:
                return True
        return False

    def jsStackAdd(self, key, value):
        if not self.jsStackExists(key):
            self.JS_STACK[key] = value

    def jsStackRemove(self, key):
        if self.jsStackExists(key):
            del self.JS_STACK[key]


    def jsStackGet(self,key):
        if self.jsStackExists(key):
            from Core.DataOperations.Logger.Logger import Logger
            Logger(False,0,self.local_settings.Bundler.getText(15).format(self.JS_STACK[key]), Levels.Info)
            return self.JS_STACK[key]