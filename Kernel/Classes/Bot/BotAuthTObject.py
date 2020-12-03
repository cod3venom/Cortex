class BotAuthTObject:
    def __init__(self,JSON) ->int:
        try:
            self.USER_ID = JSON['USER_ID']
            self.CLIENT_ID = JSON['CLIENT_ID']
            self.CLIENT_IDENTIFIER = JSON['CLIENT_IDENTIFIER']
        except IndexError:
            pass


    def getUserID(self) ->str:
        return  self.USER_ID
    def getClientID(self)->str:
        return self.CLIENT_ID
    def getClientIdentifier(self)->str:
        return self.CLIENT_IDENTIFIER