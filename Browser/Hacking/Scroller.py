from selenium import webdriver

from Browser.Hacking.jsExec import jsExec
from Browser.JSbundler.jsLoader import jsLoader


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


