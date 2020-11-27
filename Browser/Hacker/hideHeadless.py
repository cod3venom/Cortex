from selenium import webdriver


class hideHeadless:
    def __init__(self,Browser: webdriver.Chrome):
        if Browser is not None:
            self.Browser = Browser

    def hideHeadlessFlag(self):
        if self.Browser is not None:
            headlessAgent = self.Browser.execute_script("return navigator.userAgent")
            if headlessAgent:
                self.removeHeadlesFlag(headlessAgent)

    def removeHeadlesFlag(self, fullUserAgent : str):
        if self.Browser is not None:
            newAgent = fullUserAgent.replace("Headless","")
            self.Browser.execute_cdp_cmd(
                "Network.setUserAgentOverride",
                {"userAgent":newAgent,},
            )
