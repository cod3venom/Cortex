import requests

from Core.DataOperations.Strings import EMPTY, NOLIST


class Http:
    def __init__(self):
        self.address = EMPTY
        self.session = None

    def setSession(self, request):
        self.session = request

    def getSession(self) -> requests.sessions:
        return self.session

    def setAddress(self, address: str):
        self.address = address

    def getAddress(self) -> str:
        return self.address

    def Post(self, data: dict) -> requests.Response:
        Response = self.getSession().post(self.getAddress(), data).text
        if Response == NOLIST:
            return EMPTY
        return Response

    def Get(self) -> str:
        return self.getSession().get(self.getAddress()).text
