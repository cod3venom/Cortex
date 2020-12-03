import requests
class httpsock:

    def __init__(self):
        self.address=''


    def setAddress(self,address:str)->int:
        self.address = address
    def getAddress(self)->str:
        return self.address

    def Post(self,data:dict)->requests.Response:
        address = self.getAddress()
        if address is not None:
            try:
                return requests.post(address,data)
            except:
                print("cant post")
        return ""

    def Get(self) ->str:
        address = self.getAddress()
        if address != '':
            try:
                return requests.get(address).json()
            except:
                print("cant get")
        return  ""





