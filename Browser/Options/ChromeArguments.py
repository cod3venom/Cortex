from selenium.webdriver.chrome.options import Options
from Browser.Options.Arguments import Arguments
import os

class ChromeArguments:


    def getOptions(self, Incognito:bool, Headless:bool,Cache:str,Tor:bool,RandomAgent:bool):
        option = Options()
        if Incognito:
            option.add_argument('--incognito')
        if Headless:
            option.headless = True
            option.add_argument('disable-gpu')
        if len(Cache) > 3:
            option.add_argument('--user-data={}'.format(Cache))
        if Tor:
            option.add_argument('--proxy-server=socks5://127.0.0.1:9050')
            option.add_argument('ignore-certificate-errors')
        option.add_argument('window-size=1700,1500')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-extensions')
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--disable-blink-features=AutomationControlled")
        return option

