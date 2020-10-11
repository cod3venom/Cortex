from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from lxml import  html

class Web:
    def __init__(self,chrome):
        self.chrome = chrome
        self.source = self.chrome.page_source

    def Exists(self,__target__,_by):
        try:
            if _by == "CSS":
                if self.chrome.find_elements(By.CSS_SELECTOR,__target__):
                    return  True
            if _by == "XPATH":
                if self.chrome.find_elements(By.XPATH,__target__):
                    return True
        except NoSuchElementException:
            return  False

    def Input(self,__target__,__value__, _by):
        if self.Exists(__target__, _by):
            if _by == 'CSS':
                self.chrome.find_element_by_css_selector(__target__).send_keys(__value__)
            if _by == "XPATH":
                self.chrome.find_element(By.XPATH,__target__).send_keys(__value__)
            return  True
        return  False

    def Click(self,__target__):
        if self.Exists(__target__):
            self.chrome.find_element_by_css_selector(__target__).send_keys(Keys.RETURN)
            return  True
        return  False


