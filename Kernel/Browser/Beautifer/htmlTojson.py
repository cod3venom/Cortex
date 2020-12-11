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


    def removeTags(self,tagname:str)->bool:
        if self.Browser is not None:
            code = '''
               var element = document.getElementsByTagName("$"), index;
                for (index = element.length - 1; index >= 0; index--) {
                    element[index].parentNode.removeChild(element[index]);
                }
            '''
            code = code.replace('$',tagname)
            self.Browser.execute_script(code)
            return  True
        return  False

