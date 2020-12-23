from selenium import webdriver

from Core.Browser.Hacking.jsExec import jsExec
from Core.Browser.JSbundler.jsLoader import jsLoader
from Core.Security.Global import Local_Settings


class Scroller:

    def __init__(self, Browser: webdriver.Chrome):
        self.Browser = Browser
        self.js_loader = jsLoader()
        self.js = jsExec()
    def scrollTo(self):
        pass

    def scrollTop(self):
        self.js.execute_js(self.Browser, self.js_loader.jsStackGet('scrollTOP'))

    def scrollBottom(self):
        self.js.execute_js(self.Browser, self.js_loader.jsStackGet('scrollBottom'))


