from selenium import webdriver

from Core.DataOperations.Strings import EMPTY


class jsExec:

    def execute_js(self, Browser: webdriver.Chrome, code: str):
        if Browser is not None:
            retData = Browser.execute_script(code)
            return retData

    def execute_cdp(self, Browser: webdriver.Chrome, code):
        if Browser is not None:
            retData = Browser.execute_cdp_cmd(code, EMPTY)
            if retData:
                return retData
        return EMPTY
