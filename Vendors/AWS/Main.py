import time
from concurrent.futures.thread import ThreadPoolExecutor

from Vendors.AWS.AWS_Spider import Spider
from Core.DataOperations.Strings import EMPTY
from Core.Security.Rest.RestClient import RestClient


class AwsAuth:
    def __init__(self, client_identifier, client_password, options_id, total_process):
        self.__THREAD_FACTORY__: list = []
        self.__client_identifier = client_identifier
        self.__client_password = client_password
        self.__options_id = options_id
        self.__restClient = RestClient()

        self.Options = EMPTY
        self.Proxy = EMPTY
        self.Links = EMPTY
        self.Selectors = EMPTY
        self.Javascript = EMPTY
        self.total_process = int(total_process)

    def Login(self):
        self.__restClient.Authorize(self.__client_identifier, self.__client_password)
        self.GetOptions()

    def GetOptions(self):
        self.Options = self.__restClient.getBotOptions(self.__options_id)
        self.Proxy = self.__restClient.getBotProxy(self.Options.ARG_PROXY_ID)
        self.Links = self.__restClient.getLinks(self.Options.ARG_LINKS_PACKET_ID)
        self.Selectors = self.__restClient.getXpathSelectors(self.Options.ARG_SELECTORS_PACKET_ID)
        self.Javascript = self.__restClient.getJavascript(self.Options.ARG_CUSTOM_JAVASCRIPT_ID)

        self.Start()

    def Start(self):
        total_process = self.total_process - 1
        with ThreadPoolExecutor(max_workers=total_process) as pool:
            for index in range(total_process):
                self.AppendToFactory(
                    Spider(self.Options, self.Proxy, self.Links, self.Selectors, self.Javascript, self.total_process))

        for process in self.GetFactory():
            process.Explore()
            time.sleep(.5)

    def AppendToFactory(self, threadPool):
        if threadPool not in self.__THREAD_FACTORY__:
            self.__THREAD_FACTORY__.append(threadPool)

    def ClearFactory(self):
        self.__THREAD_FACTORY__.clear()

    def GetFactory(self):
        return self.__THREAD_FACTORY__
