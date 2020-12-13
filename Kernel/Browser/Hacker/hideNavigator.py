from selenium import webdriver

from Kernel.Browser.Hacker.Javascript import Javascript


class hideNavigator:
    def __init__(self, Browser: webdriver.Chrome):
        if Browser is not None:
            self.Browser = Browser

    def hideWebdriverFlag(self):
        if self.Browser is not None:
            if Javascript().Execute_js(self.Browser, "return navigator.webdriver"):
                self.removeFlag(self.Browser)

    def removeFlag(self, Browser: webdriver.Chrome):
        if Browser is not None:
            Javascript().Execute_cdp(Browser,
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
