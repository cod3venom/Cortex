from selenium.webdriver.chrome.options import Options
import os
class __Config__:
    JSCODE = os.getcwd() + "/JSCODE/jslist.init"
    def __init__(self,incognito, headless, cache,root,tor,randomAgent):
        self.incognito = incognito
        self.headless = headless
        self.cahe = cache
        self.root = root
        self.tor = tor
        self.random = randomAgent


    def __GET_OPTION__(self):
        option = Options()
        if self.incognito:
            option.add_argument('--incognito')
        if self.headless:
            option.headless = True
            option.add_argument('disable-gpu')
        if len(self.cahe) > 3:
            option.add_argument('--user-data={}'.format(self.cahe))
        if self.root:
            option.add_argument("--no-sandbox")
        if self.tor:
            option.add_argument('--proxy-server=socks5://127.0.0.1:9050')
            option.add_argument('ignore-certificate-errors')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-extensions')
        #option.add_argument('--log-level=3')
        return option