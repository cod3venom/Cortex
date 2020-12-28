from DAO.BotAuthTObject import BotAuthTObject
from DAO.BotJavascriptTObject import BotJavascriptTObject
from DAO.BotLinksTObject import BotLinksTObject
from DAO.BotOptionsTObject import BotOptionsTObject
from DAO.BotProxyTObject import BotProxyTObject
from DAO.BotXpathSelectorTObject import BotXpathSelectorTObject
from DAO.EkwBotOptionsTObject import EkwBotOptionsTObject
from DAO.EkwNumbersListTObject import EkwNumbersListTObject
from Logger.Logger import Logger
import Core.Security.Global as Global
from Core.DataOperations.Strings import *
from Core.Texts.Bundler import Bundler


class RestClient:

    def __init__(self):
        self.logger = Logger()
        Global.http.setAddress(Global.Local_Settings.GATE_URL)

    def Authorize(self, client_identifier, client_password):
        if not Global.isLogged():
            Request = {Global.Local_Settings.Bundler.getReq(1): EMPTY, Global.Local_Settings.Bundler.getReq(2): client_identifier,
                       Global.Local_Settings.Bundler.getReq(3): client_password}
            Response = BotAuthTObject.TO(Global.http.Post(Request))
            self.CreateCookiePack(Response)

    def CreateCookiePack(self, Auth: BotAuthTObject) -> bool:
        if Auth:
            Global.setCookie(Global.Local_Settings.Bundler.getText(4), Auth.USER_ID)
            Global.setCookie(Global.Local_Settings.Bundler.getText(5), Auth.CLIENT_ID)
            Global.setCookie(Global.Local_Settings.Bundler.getText(6), Auth.CLIENT_IDENTIFIER)
            Global.setCookie(Global.Local_Settings.Bundler.getText(7), Auth.CLIENT_LEVEL)
            self.logger.Print(2, Global.levels.Info, bundler=True)
            return True
        return False

    def getBotOptions(self, options_id) -> BotOptionsTObject:
        if Global.isLogged():
            # 14#GetBotOptions
            # 15#Option_id
            Request = {Global.Local_Settings.Bundler.getReq(14): EMPTY, Global.Local_Settings.Bundler.getReq(15): options_id}
            return BotOptionsTObject.TO(Global.http.Post(Request))

    def getEkwBotOptions(self, options_id) -> EkwBotOptionsTObject:
        if Global.isLogged():
            # 26#GetEkwBotOptions
            # 15#Option_id
            Request = {Global.Local_Settings.Bundler.getReq(26): EMPTY, Global.Local_Settings.Bundler.getReq(15): options_id}
            return EkwBotOptionsTObject.TO(Global.http.Post(Request))

    def getBotProxy(self, proxy_id) -> BotProxyTObject:
        if Global.isLogged() and proxy_id != EMPTY:
            # 16#GetProxy
            # 17#Proxy_id
            Request = {Global.Local_Settings.Bundler.getReq(16): EMPTY, Global.Local_Settings.Bundler.getReq(17): proxy_id}
            Response = Global.http.Post(Request)
            if Response:
                return BotProxyTObject.TO(Response)
        return BotProxyTObject.TO(EMPTY)

    def getLinks(self, Link_packet_id) -> BotLinksTObject:
        if Global.isLogged() and Link_packet_id != EMPTY:
            # 18#GetNextLink
            # 19#Bot_links_packet_id
            Request = {Global.Local_Settings.Bundler.getReq(18): EMPTY, Global.Local_Settings.Bundler.getReq(19): Link_packet_id}
            Response = Global.http.Post(Request)
            if Response:
                return BotLinksTObject.TO(Response)
        return BotLinksTObject.TO(EMPTY)

    def getXpathSelectors(self, Xpath_packet_id) -> BotXpathSelectorTObject:
        if Global.isLogged() and Xpath_packet_id != EMPTY:
            # 18#GetNextLink
            # 19#Bot_links_packet_id
            Request = {Global.Local_Settings.Bundler.getReq(20): EMPTY, Global.Local_Settings.Bundler.getReq(21): Xpath_packet_id}
            Response = Global.http.Post(Request)
            if Response:
                return BotXpathSelectorTObject.TO(Response)
        return BotXpathSelectorTObject.TO(EMPTY)

    def getJavascript(self, js_id) -> BotJavascriptTObject:
        if Global.isLogged() and js_id != EMPTY:
            # 18#GetNextLink
            # 19#Bot_links_packet_id
            Request = {Global.Local_Settings.Bundler.getReq(22): EMPTY, Global.Local_Settings.Bundler.getReq(23): js_id}
            Response = Global.http.Post(Request)
            if Response:
                return BotJavascriptTObject.TO(Response)
        return BotJavascriptTObject.TO(EMPTY)

    def getEkwNumbers(self, Ekw_numbers_pack_id):
        if Global.isLogged() and Ekw_numbers_pack_id != EMPTY:
            # 24#GetNextEkwNumbers
            # 25#Ekw_numbers_pack_id
            Request = {Global.Local_Settings.Bundler.getReq(24): EMPTY, Global.Local_Settings.Bundler.getReq(25): Ekw_numbers_pack_id}
            Response = Global.http.Post(Request)
            if Response:
                return EkwNumbersListTObject.TO(Response)
        return EkwNumbersListTObject.TO(EMPTY)
