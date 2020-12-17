from selenium import webdriver

from Core.Browser.Hacking.jsExec import jsExec
from Core.DataOperations.Strings import EMPTY


class Headless:
    def __init__(self, Browser: webdriver.Chrome):
        self.Browser = Browser
        self.userAgent = EMPTY
        self.newUserAgent = EMPTY

    '''
    @Class hideHeadless USED TO REMOVE HEADLESS BROWSER INDICATOR FROM THE BROWSER UserAgent.
    WITHOUT USING THIS OPTIONS , DEFAULT UserAgent WILL LOOKS LIKE BELOW.
    
    Example:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/86.0.4240.183 Safari/537.36
    
    SOME WEBSITES LIKE AMAZON.COM CAN DETECT THIS KIND OF USERAGENT USING JAVASCRIPT
        
        return navigator.useragent;
    AND IF RETURNED VALUE CONTAINS SOMETHING LIKE 'HeadlessChrome' THAT MEANS THAT
    ACTUAL BROWSER IS AN AUTOMATED BOT AND AT LAST WE WILL GET CAPTCHA.
    '''

    def CheckUserAgent(self):
        if self.Browser is not None:
            self.userAgent = jsExec().execute_js(self.Browser, 'return navigator.userAgent')
            if self.userAgent:
                return self.ReplaceHeadlessAgent()

    def ReplaceHeadlessAgent(self):
        self.newUserAgent = self.userAgent.replace("Headless", EMPTY).replace("headless", EMPTY)
        self.Browser.execute_cdp_cmd(
            "Network.setUserAgentOverride", {"userAgent": self.newUserAgent}
        )
        return jsExec().execute_js(self.Browser, "return navigator.userAgent")

    def RemoveHeadlessIndicator(self):
        return self.CheckUserAgent()
