from Kernel.Bot.Class.Objects.BotJavascriptTObject import BotJavascriptTObject
from Kernel.Bot.Class.Objects.BotProxyTObject import BotProxyTObject
from Kernel.Bot.Class.Objects.BotAuthTObject import BotAuthTObject
from Kernel.Bot.Class.Objects.BotLinksTObject import BotLinksTObject
from Kernel.Bot.Class.Objects.BotOptionsTObject import BotOptionsTObject
from Kernel.Bot.Class.Objects.BotXpathSelectorsTObject import BotXpathSelectorsTObject
from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.Globals import *
from Kernel.Management.Security.JSON import JSON


class Rest:

    def Login(self, CLIENT_IDENTIFIER, CLIENT_PASSWORD) -> bool:
        if not isLogged():
            Request = {'BotAuth': Constants.EMPTY,
                       'Client_identifier': CLIENT_IDENTIFIER,
                       'Client_password': CLIENT_PASSWORD}
            Response = http.Post(Request).text
            self.CreateCookiePack(BotAuthTObject(Response))

    def CreateCookiePack(self, clazz: BotAuthTObject) -> int:
        setCookie('USER_ID', clazz.USER_ID)
        setCookie('CLIENT_ID', clazz.CLIENT_ID)
        setCookie('CLIENT_IDENTIFIER', clazz.CLIENT_IDENTIFIER)
        setCookie('CLIENT_LEVEL', clazz.CLIENT_LEVEL)

    def getOptions(self, OPTIONS_ID) -> BotOptionsTObject:
        if isLogged() and OPTIONS_ID is not None:
            Request = {'GetBotOptions': Constants.EMPTY,'Option_id': OPTIONS_ID}
            Response = http.Post(Request).text
            return BotOptionsTObject(Response)

    def getProxy(self, PROXY_ID) -> BotProxyTObject:
        if isLogged():
            Request = {'GetProxy': Constants.EMPTY,'Proxy_id': PROXY_ID}
            Response = http.Post(Request).text
            return BotProxyTObject(Response)

    def getNextLink(self, LINKS_PACKET_ID) -> BotLinksTObject:
        if isLogged():
            Request = {'GetNextLink': Constants.EMPTY,'Bot_links_packet_id': LINKS_PACKET_ID}
            Response = http.Post(Request).text
            return BotLinksTObject(Response)

    '''
        THIS FUNCTION IS USED TO GET SELECTORS FOR THE SPIDER.
        LITTLE BIT IT LOOKS LIKE AN SPAGETTI CODE BUT THERE WAS PROBLEM WITH JSON DATA.
        SELECTORS JSON DATA WAS INDEXED BY NUMBERS LIKE 1,2,3,4,5.
        {
          "1": {
            "SELECTOR_KEY": "LINK",
          },
          "2": {
            "SELECTOR_KEY": "PRODUCT_TITLE",
          }
      }
      AND BECAUSE OF THAT IN ORDER TO CONVERT JSON TO THE CLASS OBJECTS,
      AT FIRST STEP WE MUST READ ALL KEYS USING jsDATA.keys(), AND THEN
      ITERATE JSON KEYS IN THE LOOP. WHEN LOOP ENDS, JUST PUSH CONVERTED
      CLASS OBJECTS TO THE LIST ARRAY CALLED AS 'SELECTORS' AND RETURN 
      MENTIONED LIST.
      
      TO USE RETURNED SELECTORS , WRITE SOMETHING LIKE BELOW
      
      selectors = rest.getXpathSelectors(Config.ARG_SELECTORS_PACKET_ID)
        for select in selectors:
            print("{} = {}".format(select.SELECTOR_KEY, select.SELECTOR_VALUE))
    '''
    def getXpathSelectors(self, PACKET_ID) -> BotXpathSelectorsTObject:
        if isLogged():
            Request = {'GetSelectors': Constants.EMPTY,'Packet_id': PACKET_ID}
            Response = http.Post(Request).text
            jsData = BotXpathSelectorsTObject().IndexedJson(Response)
            for Index in jsData.keys():
                SELECTORS.append(BotXpathSelectorsTObject(jsData[Index]))
            return SELECTORS

    def getCustomJavascript(self, JS_ID) -> BotJavascriptTObject:
        if isLogged():
            Request = {'GetJSbyID': Constants.EMPTY,'Js_id': JS_ID}
            Response = http.Post(Request).text
            return BotJavascriptTObject(Response)

