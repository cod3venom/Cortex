import json

from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.FileSystem import FileSystem


class LocalSettingsTObject:
    def __init__(self):
        data = json.loads(FileSystem().ReadFile(Constants.SETTINGS_FILE))
        for jsData in data[Constants.SOFTWARE_NAME_UPPER]:
            self.GATE_URL = jsData['GATE_URL']
            self.LOGOUT_URL = jsData['LOGOUT_URL']