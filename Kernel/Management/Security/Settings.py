import json

from Kernel.Bot.Class.Objects.LocalSettingsTObject import LocalSettingsTObject
from Kernel.Management.Security.FileSystem import FileSystem
from Kernel.Management.Security.Constants import Constants


class Settings:

    def __init__(self):
        self.CONFIG_CONTENT = str(FileSystem().ReadFile(Constants().SETTINGS_FILE))

    def getConfig(self) -> LocalSettingsTObject:
        jsData = json.loads(self.CONFIG_CONTENT)
        return LocalSettingsTObject(jsData)


