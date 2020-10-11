from Spider.Network.HTTP import HTTP as __http__
from Texts.Bundle import Bundle as __bundle__
from Hacker.Logging import Logging
class Anonimity:
    def __get_ip__(self):
        ip = __http__(__bundle__().getString(18),"",True,True).GET()
        Logging(1,__bundle__().getString(23),ip)
