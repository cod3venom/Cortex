from Spider.Network.HTTP import HTTP as __http__
from Texts.Bundle import Bundle
from Hacker.Logging import Logging
class PHP:
    def __init__(self):
        self.limit = 1
        self.start = 0
    #@TODO=LOAD LINKS FROM MYSQL USING LIMIT 1, START 0,1

    def nextLink(self):
        link = __http__(Bundle().getString(19) + "127.0.0.2","",False,False).GET()
        if len(link) > 75:
            Logging(1,Bundle().getString(27), link[:75])
        else:
            Logging(1,Bundle().getString(27), link)
        return link