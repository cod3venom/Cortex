from Kernel.Bot.Class.Objects.BotXpathSelectorsTObject import BotXpathSelectorsTObject
from Kernel.Management.Security.Globals import COOKIES, http, SELECTORS, Debug
from Kernel.Management.Security.REST import Rest
class BotAuth:
    def __init__(self, client_identifier, client_password, options_id):

        self.client_identifier = client_identifier
        self.client_password = client_password
        self.options_id = options_id
        self.Login()


    def Login(self):
        Rest().Login(self.client_identifier, self.client_password)
        self.GET_OPTIONS()

    def GET_OPTIONS(self):
        rest = Rest()
        Config = rest.getOptions(self.options_id)
        proxies = rest.getProxy(Config.ARG_PROXY_ID)
        #next_link = rest.getNextLink(clazz.ARG_LINKS_PACKET_ID).Link
        selectors = rest.getXpathSelectors(Config.ARG_SELECTORS_PACKET_ID)
        for select in selectors:
            Debug("{} = {}".format(select.SELECTOR_KEY, select.SELECTOR_VALUE))
        javascript = rest.getCustomJavascript('d8a7ad3291c5d94e8606d89f7dee13de')
        Debug(javascript.JS_CODE)



