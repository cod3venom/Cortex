import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Kernel.Browser.Hacker.hideNavigator import hideNavigator
from Kernel.Browser.Hacker.hideHeadless import hideHeadless
from Kernel.Browser.Beautifer.htmlSegmentation import htmlSegmentation
from Kernel.Management.Security.Globals import SELECTORS


class Chromedriver:

    def __init__(self) -> int:
        self.ChromePath = os.getcwd() + "/Kernel/Browser/Bin/chromedriver"
        self.Address = None
        self.Source = None
        self.Config = None
        self.Interval = None
        self.Chrome = None

    def setAddress(self, address: str) -> int:
        self.Address = address

    def getAddress(self) -> str:
        return self.Address

    def setSource(self, source: str) -> int:
        self.Source = source

    def getSource(self) -> str:
        return self.Source

    def setInterval(self, interval: int) -> int:
        self.Interval = interval
        time.sleep(self.Interval)

    def getInterval(self) -> int:
        return self.Interval

    def setChrome(self, opt: Options, Chrome: webdriver.Chrome = None) -> int:
        if opt is not None:
            if Chrome is not None:
                self.Chrome = Chrome
            else:
                self.Chrome = webdriver.Chrome(executable_path=self.ChromePath, chrome_options=opt)

    def getChrome(self) -> webdriver.Chrome:
        return self.Chrome

    def Navigate(self):
        hideNavigator(self.getChrome()).hideWebdriverFlag()
        hideHeadless(self.getChrome()).hideHeadlessFlag()
        self.getChrome().get(self.getAddress())
        htmlSegmentation(self.getChrome()).RemoveUnwantedTags()
        print(str(SELECTORS))
