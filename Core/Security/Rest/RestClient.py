from Core.DAO.BotAuthTObject import BotAuthTObject
from Core.DAO.BotJavascriptTObject import BotJavascriptTObject
from Core.DAO.BotLinksTObject import BotLinksTObject
from Core.DAO.BotOptionsTObject import BotOptionsTObject
from Core.DAO.BotProxyTObject import BotProxyTObject
from Core.DAO.BotXpathSelectorTObject import BotXpathSelectorTObject
from Core.DataOperations.Logger.Logger import Logger
from Core.Security.Global import *
from Core.DataOperations.Strings import *
from Core.Texts.Bundler import Bundler


class RestClient:

    def __init__(self):
        self.__bundler = Bundler(Local_Settings)
        http.setAddress(Local_Settings.GATE_URL)

    def Authorize(self, client_identifier, client_password):
        if not isLogged():
            Request = {self.__bundler.getReq(1): EMPTY, self.__bundler.getReq(2): client_identifier,
                       self.__bundler.getReq(3): client_password}
            Response = BotAuthTObject.TO(http.Post(Request))
            self.CreateCookiePack(Response)

    def CreateCookiePack(self, Auth: BotAuthTObject):
        setCookie(Local_Settings.Bundler.getText(4), Auth.USER_ID)
        setCookie(Local_Settings.Bundler.getText(5), Auth.CLIENT_ID)
        setCookie(Local_Settings.Bundler.getText(6), Auth.CLIENT_IDENTIFIER)
        setCookie(Local_Settings.Bundler.getText(7), Auth.CLIENT_LEVEL)
        Logger(True, 8, levels.Success)

    def getBotOptions(self, options_id) -> BotOptionsTObject:
        if isLogged():
            # 9#GetBotOptions
            # 10#Option_id
            Request = {self.__bundler.getReq(14): EMPTY, self.__bundler.getReq(15): options_id}
            return BotOptionsTObject.TO(http.Post(Request))

    def getBotProxy(self, proxy_id) -> BotProxyTObject:
        if isLogged() and proxy_id != EMPTY:
            # 16#GetProxy
            # 17#Proxy_id
            Request = {self.__bundler.getReq(16): EMPTY, self.__bundler.getReq(17): proxy_id}
            Response = http.Post(Request)
            if Response:
                return BotProxyTObject.TO(Response)
        return BotProxyTObject.TO(EMPTY)

    def getLinks(self, Link_packet_id) -> BotLinksTObject:
        if isLogged() and Link_packet_id != EMPTY:
            # 18#GetNextLink
            # 19#Bot_links_packet_id
            Request = {self.__bundler.getReq(18): EMPTY, self.__bundler.getReq(19): Link_packet_id}
            Response = http.Post(Request)
            if Response:
                return BotLinksTObject.TO(Response)
        return BotLinksTObject.TO(EMPTY)

    def getXpathSelectors(self, Xpath_packet_id) -> BotXpathSelectorTObject:
        if isLogged() and Xpath_packet_id != EMPTY:
            # 18#GetNextLink
            # 19#Bot_links_packet_id
            Request = {self.__bundler.getReq(20): EMPTY, self.__bundler.getReq(21): Xpath_packet_id}
            Response = http.Post(Request)
            if Response:
                return BotXpathSelectorTObject.TO(Response)
        return BotXpathSelectorTObject.TO(EMPTY)

    def getJavascript(self, js_id) -> BotJavascriptTObject:
        if isLogged() and js_id != EMPTY:
            # 18#GetNextLink
            # 19#Bot_links_packet_id
            Request = {self.__bundler.getReq(22): EMPTY, self.__bundler.getReq(23): js_id}
            Response = http.Post(Request)
            if Response:
                return BotJavascriptTObject.TO(Response)
        return BotJavascriptTObject.TO(EMPTY)