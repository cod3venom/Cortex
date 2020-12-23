import datetime
import json

from Core.DataOperations.Strings import EMPTY
from Core.Security.FileSystem import FileSystem
from Core.Security.Global import Local_Settings


class Json:

    def __init__(self, export_name):
        self.__export_name: str = EMPTY
        self.__data: dict = {}
        self.__fileSystem = FileSystem()
        self.export_name = Local_Settings.JSON_EXPORT_PATH + export_name + ".json"



    @property
    def data(self) -> dict:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = json.dumps(data)

    def getTimeNow(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def export(self, append_mode: bool = True, duplicates=True):
        if append_mode:
            if duplicates:
                self.__fileSystem.appendToFile(self.export_name, str(self.data), True)
            else:
                self.__fileSystem.appendToFile(self.export_name, str(self.data), False)
        else:
            self.__fileSystem.writeToFile(self.export_name, str(self.data))
