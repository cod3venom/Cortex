from Core.DAO.BotOptionsTObject import BotOptionsTObject
from Core.DAO.BotProxyTObject import BotProxyTObject
from selenium.webdriver.chrome.options import Options


class ChromeOptions:
    def __init__(self, BOT_OPTIONS: BotOptionsTObject, BOT_PROXY: BotProxyTObject):
        self.BOT_OPTIONS = BOT_OPTIONS
        self.BOT_PROXY = BOT_PROXY

    def getOptions(self):
        option = Options()
        if self.BOT_OPTIONS.ARG_INCOGNITO == 1:
            option.add_argument('--incognito')
        if self.BOT_OPTIONS.ARG_HEADLESS == 1:
            option.headless = True
            option.add_argument('disable-gpu')

        if len(self.BOT_OPTIONS.ARG_CACHE_FOLDER) > 3:
            option.add_argument('--user-data={}'.format(self.BOT_OPTIONS.ARG_CACHE_FOLDER))
        if self.BOT_OPTIONS.ARG_TOR == 1:
            #option.add_argument('--proxy-server=socks5://127.0.0.1:9050')
            #option.add_argument('ignore-certificate-errors')
            pass
        option.add_argument('window-size=1700,1500')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-extensions')
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--disable-blink-features=AutomationControlled")
        return option
