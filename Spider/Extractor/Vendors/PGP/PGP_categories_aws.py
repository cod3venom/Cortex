from Spider.Browser.__Chormium__ import __Chromium__
from Spider.Extractor.PyDict import PyDict
from Spider.Extractor.PyPath import *
from Spider.Network.PHP import PHP
from Hacker.ClusterClient import send


"""
    AMAZON SCRAPER LAUNCHER
"""

class PGP_categories_aws:

    def __init__(self):
        self.php = PHP()
        self.__chrome__ = __Chromium__(True,False,"",False,True,True)
        self.__FULL__ = ""
        self.__LINK__ = self.php.nextLink()

    def Start(self):
        while self.__LINK__ !="":
            self.__FORMAT__ = PyDict()
            self.__chrome__.address = self.__LINK__.replace(".co.uk//", ".co.uk/")
            self.__chrome__.Navigate()
            self.__chrome__.Scroll_V_V()
            __path__ = PyPath(self.__chrome__)
            __path__.Start(self.__chrome__.Source())
            __dict__ = self.__FORMAT__.Load()
            self.__FORMAT__.__xpath__ = __path__
            for i in range(len(__dict__['Keys'])):
                _key_ = __dict__['Keys'][i]
                _val_ = __dict__['Values'][i]
                if _key_ != "" and _val_ !="":
                    try:
                        self.STACK[_key_] = __path__.Stacked_extraction(_val_)
                    except IndexError:
                        pass
                    finally:
                        self.__FULL__+= "{}!{}~{}\n".format("AWS",_key_,self.STACK[_key_])
                        Logging(4, Bundle().getString(55), _key_)
            send(self.__FULL__)

            self.__FULL__ = ""
            self.__LINK__ = self.php.nextLink()

        self.chrome.Viewer().quit()


