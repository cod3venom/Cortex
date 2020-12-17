import os

from Core.Browser.Hacking.ExploitPack import ExploitPack
from Core.DataOperations.Strings import EMPTY
from Core.Security.Global import Local_Settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Core.Spiders.XpathPicker import XpathPicker

counter = 0


class ChromeDriver:

    def __init__(self, parse_xpath_on=False):
        self.BrowserPath = os.getcwd() + Local_Settings.BINARY_PATH
        self.Address = EMPTY
        self.Browser: webdriver.Chrome = EMPTY
        self.Source = EMPTY
        self.exploitPack = ExploitPack()

        self.parse_xpath_on = parse_xpath_on
        self.xpathPicker = XpathPicker()

    # setter
    def setAddress(self, address: str):
        self.Address = address

    # getter
    def getAddress(self) -> str:
        return self.Address

    # setter
    def setSource(self):
        self.Source = self.Browser.page_source

    # getter
    def getSource(self) -> str:
        return self.Source

    # setter
    def setBrowser(self, options: Options, Browser: webdriver.Chrome = None):
        if options is not None:
            if Browser is not None:
                self.Browser = Browser
            else:
                self.Browser = webdriver.Chrome(executable_path=self.BrowserPath, chrome_options=options)

    # getter
    def getBrowser(self) -> webdriver.Chrome:
        return self.Browser

    def Navigate(self, screenshot=False):
        global counter
        self.exploitPack.RemoveHeadless(self.getBrowser())
        self.exploitPack.HideNavigator(self.getBrowser())
        self.getBrowser().get(self.getAddress())
        self.exploitPack.CrazyMouse(self.Browser)
        self.setSource()

        if screenshot:
            counter += 1
            self.Browser.save_screenshot(f'Image_{str(counter)}.png')

        if self.parse_xpath_on:
            self.parseXpath()



    def parseXpath(self):
        self.xpathPicker.start(self.getSource(),indexed=True, identifier=self.getAddress())
