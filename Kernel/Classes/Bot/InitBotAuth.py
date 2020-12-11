import json, requests

from Kernel.DAO.BotAuthTObject import BotAuthTObject
from Kernel.Settings.Constants import Constants
from Kernel.HTTP.httpsock import httpsock
from Kernel.Settings.Settings import Settings, SESSION, isLogged, Die

"""

    THIS CLASS IS USED TO GET ACCESS TOKEN FOR LOGGED IN BOT.
    ABOVE MENTIONED ACCESS TOKEN IS IMPORTANT IN ORDER TO GET ANY TYPE OF INFORMATION
    FROM THE BACKEND.

"""


class InitBotAuth:

    def __init__(self, identifier, password, options_id):
        self.CLIENT_IDENTIFIER = identifier
        self.CLIENT_PASSWORD = password
        self.options_id = options_id
        self.http = httpsock()
        self.http.setSession(requests.session())

    def setClientIdentifier(self, identifier: str) -> int:
        self.CLIENT_IDENTIFIER = identifier

    def getClientIdentifier(self, ) -> str:
        return self.CLIENT_IDENTIFIER

    def setClientPassword(self, password: str) -> int:
        self.CLIENT_PASSWORD = password

    def getClientPassword(self) -> str:
        return self.CLIENT_PASSWORD

    def setOptionsID(self, options_id: str) -> int:
        self.options_id = options_id

    def getOptionsID(self) -> int:
        return self.options_id

    def doAuth(self):
        self.http.setAddress(Settings().getConfig().GATE_URL)
        Request_data = {
            Constants.BOTAUTH: Constants.EMPTY,
            Constants.Client_identifier: self.getClientIdentifier(),
            Constants.Client_password: self.getClientPassword()
        }
        response = self.http.Post(Request_data).text
        if response == Constants.EMPTY or Constants.CLIENT_ID not in response:
            Die(Constants.WRONG_CREDENTIALS)
        else:
            botAuthTobject = BotAuthTObject(json.loads(response))
            SESSION.append(botAuthTobject.CLIENT_ID)
            print(self.getOptionsID())
            return True

    def Logout(self):
        if isLogged():
            self.http.setAddress(Settings().getConfig().LOGOUT_URL)
            response = self.http.Get()
            if response == Constants.LOGOUT:
                SESSION.clear()
                return True
