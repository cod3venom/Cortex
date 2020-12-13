import json

from selenium.webdriver.chrome.webdriver import WebDriver

from Kernel.Browser.Hacker.Javascript import Javascript
from Kernel.Management.Security import Globals


# @TODO=under development
class htmlSegmentation:

    def __init__(self, Chrome: WebDriver):
        self.source = ''
        self.Browser = Chrome

    def setSource(self, source: str) -> int:
        self.source = source

    def getSource(self) -> str:
        return self.source

    def removeTags(self, tagName: str) -> bool:
        if self.Browser is not None:
            code = '''
               var element = document.getElementsByTagName("$"), index;
                for (index = element.length - 1; index >= 0; index--) {
                    element[index].parentNode.removeChild(element[index]);
                }
            '''
            Javascript().Execute_js(self.Browser, code.replace('$', tagName))
            return True
        return False

    def RemoveUnwantedTags(self):
        self.removeTags('script')
        self.removeTags('link')
        self.removeTags('style')
