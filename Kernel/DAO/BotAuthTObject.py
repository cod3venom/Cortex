from Kernel.Settings.Constants import Constants


class BotAuthTObject:

    def __init__(self,json):
        try:
            self.USER_ID: str = json[Constants.USER_ID]
            self.CLIENT_ID: str = json[Constants.CLIENT_ID]
            self.CLIENT_IDENTIFIER: str = json[Constants.CLIENT_IDENTIFIER]
            self.CLIENT_LEVEL: str = json[Constants.CLIENT_LEVEL]
        except KeyError as ex:

             print(str(ex))





