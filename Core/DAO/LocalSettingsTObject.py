import json

from Core.Security.FileSystem import FileSystem
from Core.DataOperations.Strings import EMPTY
from Core.Security.Settings import SETTINGS_JSON, SOFTWARE_NAME
from Core.Texts.Bundler import Bundler


class LocalSettingsTObject:
    def __init__(self):
        data = json.loads(FileSystem().readfile(SETTINGS_JSON))
        for JsonData in data[SOFTWARE_NAME]:
            self.VERSION = JsonData["VERSION"]
            self.GATE_URL = JsonData['GATE_URL']
            self.LOGOUT_URL = JsonData['LOGOUT_URL']
            self.en_US = JsonData['en_US']
            self.pl_PL = JsonData['pl_PL']
            self.REST_REQUESTS = JsonData['REST_REQUESTS']
            self.WSS_MANAGER_USERNAME = JsonData['WSS_MANAGER_USERNAME']
            self.WSS_MANAGER_PASSWORD = JsonData['WSS_MANAGER_PASSWORD']
            self.WSS_MANAGER_PORT = int(JsonData['WSS_MANAGER_PORT'])
            self.LOCAL_HOST = JsonData['LOCAL_HOST']
            self.TCP_SERVER_PORT = int(JsonData['TCP_SERVER_PORT'])
            self.TCP_SERVER_BUFFER = JsonData['TCP_SERVER_BUFFER']
            self.TERMINAL_PREFIX = JsonData["TERMINAL_PREFIX"].format(self.VERSION)
            self.LOG_FORMAT = JsonData["LOG_FORMAT"]
            self.BINARY_PATH = JsonData["BINARY_PATH"]
            self.JSON_EXPORT_PATH = JsonData["JSON_EXPORT_PATH"]
            self.CSV_EXPORT_PATH = JsonData["CSV_EXPORT_PATH"]
            self.Bundler = Bundler(self)
