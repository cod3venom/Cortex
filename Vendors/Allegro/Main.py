import time
from concurrent.futures.thread import ThreadPoolExecutor

from Vendors.AWS.AWS_Spider import Spider
from Core.DataOperations.Strings import EMPTY
from Core.Security.Rest.RestClient import RestClient
from Vendors.Allegro.Core.Web.CategoryParser.CategoryParser import CategoryParser


class AllegroAuth:
    def __init__(self, client_identifier, client_password, options_id, total_process):
        self.THREAD_FACTORY__: list = []
        self.RestClient = RestClient()

        self.RestClient.Authorize(client_identifier, client_password)
        self.Options = self.RestClient.getBotOptions(options_id)

    def parseCategory(self):
        CategoryParser(self, self.Options).Start()

    def AppendToFactory(self, threadPool):
        if threadPool not in self.THREAD_FACTORY__:
            self.THREAD_FACTORY__.append(threadPool)

    def ClearFactory(self):
        self.THREAD_FACTORY__.clear()

    def GetFactory(self):
        return self.THREAD_FACTORY__
