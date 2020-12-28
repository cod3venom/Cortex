import time

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Core.DataOperations.Strings import EMPTY


class Elements:

    def __init__(self):
        self.browser: webdriver.Chrome = EMPTY

    def SetBrowser(self, browser: webdriver.Chrome):
        self.browser = browser

    def GetBrowser(self):
        return self.browser

    def Exists(self, target, selector_type):
        time.sleep(.4)
        try:
            if selector_type == 'css':
                self.browser.find_element_by_css_selector(target)
                return True
            if selector_type == 'xpath':
                self.browser.find_element_by_css_selector(target)
                return True
            return False
        except NoSuchElementException:
            return False

    def Input(self, target, value):
        if self.Exists(target, 'css'):
            self.browser.find_element_by_css_selector(target).send_keys(value)

    def Click(self, target):
        if self.Exists(target, 'css'):
            self.browser.find_element_by_css_selector(target).send_keys(Keys.RETURN)

    def FindByXpath(self, target):
        try:
            return self.browser.find_elements_by_xpath(target)
        except NoSuchElementException:
            ## print ()
            pass

    def FindByCss(self, target):
        try:
            return self.browser.find_element_by_css_selector(target)
        except NoSuchElementException:
            pass
