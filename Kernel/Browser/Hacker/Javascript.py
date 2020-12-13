from selenium.webdriver.chrome.webdriver import WebDriver

from Kernel.Management.Security.Constants import Constants


class Javascript:

    def Execute_js(self, Browser: WebDriver, code: str):
        if Browser is not None:
            retData = Browser.execute_script(code)
            if retData:
                print(code)
                return retData
            else:
                return Constants.EMPTY

    def Execute_cdp(self, Browser: WebDriver, code: str):
        if Browser is not None:
            retData = Browser.execute_cdp_cmd(code)
            if retData:
                print(code)
                return retData
        return Constants.EMPTY
