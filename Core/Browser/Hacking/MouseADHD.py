from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from Core.DataOperations.Logger.Logger import Logger
from Core.Security.Global import CUSTOM_HTML_LOCATORS, Local_Settings, levels


class MouseADHD:
    def __init__(self, Browser: webdriver.Chrome):
        self.Browser = Browser

    def loadPointerTargets(self):
        if self.Browser is not None:
            for css_selector in CUSTOM_HTML_LOCATORS:
                self.Hover(css_selector)

    def Hover(self, target):
        pass

    def Activate(self):
        self.loadPointerTargets()
