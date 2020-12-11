from selenium import webdriver

class hideNavigator:
    def __init__(self,Browser: webdriver.Chrome):
        if Browser is not None:
            self.Browser = Browser


    def hideWebdriverFlag(self):
        if self.Browser is not None:
            if self.Browser.execute_script("return navigator.webdriver"):
                self.removeFlag(self.Browser)

    def removeFlag(self, Browser: webdriver.Chrome):
        if Browser is not None:
            Browser.execute_cdp_cmd(
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
