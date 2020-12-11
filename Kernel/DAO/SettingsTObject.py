from Kernel.Settings.Constants import Constants


class SettingsTObject:

    def __init__(self,data):
        for jsData in data[Constants.SOFTWARE_NAME_UPPER]:
            self.GATE_URL = jsData['GATE_URL']
            self.LOGOUT_URL = jsData['LOGOUT_URL']