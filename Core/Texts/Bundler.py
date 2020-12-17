import locale
from Core.Security.FileSystem import FileSystem
from Core.DataOperations.Strings import *


class Bundler:

    def __init__(self, Local_Settings):
        self.Local_settings = Local_Settings

        region_language = locale.getdefaultlocale()
        if "en_US" in region_language:
            self.target_region_file = Local_Settings.en_US
        if "pl_PL" in region_language:
            self.target_region_file = Local_Settings.pl_PL
        else:
            self.target_region_file = Local_Settings.en_US

        self.Texts = {}
        self.Requests = {}
        self.LoadTexts(self.target_region_file, self.Texts)
        self.LoadTexts(Local_Settings.REST_REQUESTS, self.Requests)

    def LoadTexts(self, file, packet: dict):
        content = FileSystem().readfile(file)
        if content is not None:
            if NEWLINE in content:
                Lines = content.split(NEWLINE)
                for Line in Lines:
                    if HASHTAG in Line:
                        spl = Line.split(HASHTAG)
                        packet[spl[0]] = spl[1]

    def getAsset(self, number: int, target: dict) -> str:
        if self.Texts is not None:
            try:
                if str(number) in target.keys():
                    return target[str(number)]
            except KeyError:
                print("Text not found")
                return EMPTY
        return EMPTY

    def getText(self, number: int):
        return self.getAsset(number, self.Texts)

    def getReq(self, number: int) -> str:
        return self.getAsset(number, self.Requests)
