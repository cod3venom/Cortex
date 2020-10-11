from selenium import webdriver
from selenium.common.exceptions import TimeoutException, JavascriptException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Spider.Browser.JsBundler import JsBundler
from Spider.Network.Clock import Clock
from Hacker.Logging import Logging
from Texts.Bundle import Bundle
import time

class Javascript:
    def __init__(self, Viewer):
        self.chrome = Viewer
        self.__jslist_path__ = '/home/venom/Desktop/Cortex/Spider/Browser/JSCODE/jslist.init'
        self.bundler = JsBundler(self.__jslist_path__)

    def __execute__(self, command):
        Logging(1,Bundle().getString(28),str(command))
        try:
            self.chrome.execute_script(str(command))
        except JavascriptException:
            self.__execute__(command)
            raise Bundle().getString(48)
        except TypeError:
            pass



    def scrollTop(self):
        self.__execute__(self.bundler.getString(1))

    def scrollBottom(self):
        self.__execute__(self.bundler.getString(2))

    def scrollV_V(self):
        self.scrollBottom()
        Clock().waitS(.1)
        self.scrollTop()

