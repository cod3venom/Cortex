from Core.Browser.ChromeDriver import ChromeDriver
from Core.Browser.ChromeOptions import ChromeOptions
from Core.DAO.BotJavascriptTObject import BotJavascriptTObject
from Core.DAO.BotLinksTObject import BotLinksTObject
from Core.DAO.BotOptionsTObject import BotOptionsTObject
from Core.DAO.BotProxyTObject import BotProxyTObject
from Core.DAO.BotXpathSelectorTObject import BotXpathSelectorTObject
from Core.Security.Rest.RestClient import RestClient


class Spider:

    def __init__(self, Options: BotOptionsTObject, Proxy: BotProxyTObject, Link: BotLinksTObject, Xpath: BotXpathSelectorTObject, Javascript: BotJavascriptTObject, TOTAL_PROCESS: int):
        self.Options = Options
        self.Proxy = Proxy
        self.Link = Link
        self.Xpath = Xpath
        self.Javascript = Javascript
        self.Total_process = TOTAL_PROCESS
        self.__rest = RestClient()

    def Explore(self):
        driver = ChromeDriver(parse_xpath_on=True)
        chromeOpts = ChromeOptions(self.Options, self.Proxy).getOptions()
        driver.setBrowser(chromeOpts)

        while self.Link.Link:
            driver.setAddress(self.Link.Link)
            driver.Navigate(screenshot=True)
            self.Link = self.__rest.getLinks(self.Options.ARG_LINKS_PACKET_ID)

