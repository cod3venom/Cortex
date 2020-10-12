import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from urllib3 import  exceptions

from Cheater.ProxyFactory import ProxyFactory
from Cheater.Tor import  Tor as __tor__

from Spider.Browser.__Config__ import __Config__
from Spider.Browser.Javascript import Javascript
from Spider.Network.Anonimity import Anonimity
from Spider.Browser.Web import Web
from Spider.Network.Clock import Clock
from Texts.Bundle import Bundle
                    #Headles , #Incognito ,#As Root, #--user-data-dir, #Tor


class __Chromium__:
    def __init__(self,incognito, headless, cache,root,tor,randomAgent):
        self.__conf__  = __Config__(incognito,headless,cache,root,tor,randomAgent).__GET_OPTION__()
        self.chrome = getChrome(self.__conf__)
        self.address = None
        self.js = Javascript(self.chrome)
        self.element = Web(self.chrome)

    def Viewer(self):
        return self.chrome

    def Navigate(self):
        try:
            __tor__().__new_ip__()
            Anonimity().__get_ip__()
            self.chrome.get(self.address)
        except exceptions.MaxRetryError:
            Bundle().getString(51)
            time.sleep(10)
            self.Navigate()
            Bundle().getString(52)

        except WebDriverException:
            raise Bundle().getString(53)
        except NoSuchWindowException:
            print("CLOSED")


    def Source(self):
        return self.chrome.page_source

    def ScrollBottom(self):
        time.sleep(.5)
        self.js.scrollBottom()

    def ScrollTop(self):
        self.js.scrollTop()

    def Scroll_V_V(self):
        self.js.scrollV_V()

    #@TODO:Captcha is not empty but doesnt appears in webbrowser input field
    #@TODO:IN this function check if cpatcha is not null
    def setCaptcha(self,captcha,_by):
        if captcha is not None and len(captcha) > 3:
            Clock().waitS(5)
            self.element.Input(Bundle().getString(46),captcha,_by)

    def Die(self):
        self.chrome.quit()


def getChrome(__cfg__):
    return webdriver.Chrome(executable_path=r"/usr/local/share/chromedriver", chrome_options=__cfg__)
