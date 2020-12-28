from selenium import webdriver

from Browser.Hacking.jsExec import jsExec
from Core.DataOperations.Strings import EMPTY


class Navigator:

    def __init__(self, Browser: webdriver.Chrome):
        self.Browser = Browser
        self.userAgent = EMPTY

    def CheckUserAgent(self):
        if self.Browser is not None:
            if self.userAgent:
                self.userAgent = jsExec().execute_js(self.Browser, 'return navigator.userAgent')
                return self.RemoveFlag()

    def RemoveFlag(self):
        return jsExec().execute_cdp(
            self.Browser,
             "Page.addScriptToEvaluateOnNewDocument",
             {
                "source": """
                Object.defineProperty(window, 'navigator', {
                value: new Proxy(navigator, {
                has: (target, key) => (key === 'webdriver' ? false : key in target),
                get: (target, key) =>
                    key === 'webdriver'
                    ? undefined
                    : typeof target[key] === 'function'
                    ? target[key].bind(target)
                    : target[key]
                })
            });
        """
           + (
               "console.log = console.dir = console.error = function(){};"
           )
             },
         )

    def RemoveNavigatorIndicator(self):
        return self.CheckUserAgent()
