import json

from Kernel.DAO.SettingsTObject import SettingsTObject
from Kernel.Security.FileSystem import FileSystem
from Kernel.Settings.Constants import Constants


class Settings:

    def __init__(self):
        self.CONFIG_CONTENT = str(FileSystem().ReadFile(Constants().SETTINGS_FILE))

    def getConfig(self) -> SettingsTObject:
        jsData = json.loads(self.CONFIG_CONTENT)
        return SettingsTObject(jsData)



SESSION = []

def isLogged():
    for CLIENT_ID in SESSION:
        if CLIENT_ID is not None:
            print(CLIENT_ID)
            return True
        return False
    return False

def Die(msg):
    print(msg)
    exit(1)

