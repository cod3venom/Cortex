from selenium import webdriver

from Kernel.Browser.Hacker.Javascript import Javascript

'''
    @Class hideHeadless USED TO REMOVE HEADLESS BROWSER INDICATOR FROM THE BROWSER UserAgent.
    WITHOUT USING THIS OPTIONS , DEFAULT UserAgent WILL LOOKS LIKE BELOW.
    
    Example:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/86.0.4240.183 Safari/537.36
    
    SOME WEBSITES LIKE AMAZON.COM CAN DETECT THIS KIND OF USERAGENT USING JAVASCRIPT
        
        return navigator.useragent;
    AND IF RETURNED VALUE CONTAINS SOMETHING LIKE 'HeadlessChrome' THAT MEANS THAT
    ACTUAL BROWSER IS AN AUTOMATED BOT AND AT LAST WE WILL GET CAPTCHA.
'''


class hideHeadless:
    def __init__(self, Browser: webdriver.Chrome):
        if Browser is not None:
            self.Browser = Browser

    def hideHeadlessFlag(self):
        if self.Browser is not None:
            headlessAgent = Javascript().Execute_js(self.Browser, "return navigator.userAgent")
            if headlessAgent:
                self.removeHeadlesFlag(headlessAgent)

    def removeHeadlesFlag(self, fullUserAgent: str):
        if self.Browser is not None:
            newAgent = fullUserAgent.replace("Headless", "")
            self.Browser.execute_cdp_cmd(
                "Network.setUserAgentOverride",
                {"userAgent": newAgent, },
            )
