from selenium.webdriver.chrome.webdriver import WebDriver

from Core.Browser.Hacking.jsExec import jsExec


class Sanitizer:
    def __init__(self, Chrome: WebDriver):
        self.Browser = Chrome

    def removeTags(self, tagName: str) -> bool:
        if self.Browser is not None:
            code = '''
               var element = document.getElementsByTagName("$"), index;
                for (index = element.length - 1; index >= 0; index--) {
                    element[index].parentNode.removeChild(element[index]);
                }
            '''
            jsExec().execute_js(self.Browser, code.replace('$', tagName))
            return True
        return False

    def RemoveUnwantedTags(self):
        self.removeTags('script')
        #self.removeTags('link')
        #self.removeTags('style')
        return self.Browser.page_source