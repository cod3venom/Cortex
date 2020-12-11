import requests

from Kernel.Settings.Constants import Constants


class httpsock:

    def __init__(self):
        self.address = ''
        self.session = None

    def setSession(self, request):
        self.session = request

    def getSession(self) -> requests.sessions:
        return self.session

    def setAddress(self, address: str) -> int:
        self.address = address

    def getAddress(self) -> str:
        return self.address

    def Post(self, data: dict) -> requests.Response:
        return self.getSession().post(self.getAddress(), data)

    def Get(self) -> str:
        return self.getSession().get(self.getAddress()).text
