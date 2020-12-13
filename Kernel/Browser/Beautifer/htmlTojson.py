import json

from selenium import webdriver


class htmlTojson:

    def __init__(self,Browser: webdriver.Chrome):
        if Browser is not None:
            self.Browser = Browser
        self.source = ''

    def setSource(self,source:str) ->int:
        self.source = source
    def getSource(self)->str:
        return self.source


    def Serialize(self):
        source = self.getSource()
        if source is not None:
            return json.dumps(source,indent=4, sort_keys=True)




