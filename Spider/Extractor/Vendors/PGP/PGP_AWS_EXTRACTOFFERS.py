from Spider.Browser.__Chormium__ import __Chromium__
from Spider.Extractor.PyDict import PyDict
from Spider.Extractor.PyPath import *
from Spider.Network.PHP import PHP
from Hacker.ClusterClient import send


"""
    AMAZON SCRAPER LAUNCHER
"""

class PGP_AWS_EXTRACTOFFERS:

    def __init__(self, selector):
        """

        :rtype: object
        """
        self.php = PHP()
        self.__chrome__ = __Chromium__(True,False,"",False,False,True)
        self.__FULL__ = ""
        self.__LINK__ = self.php.nextLink()
        self.selector = str(selector)


    def Start(self):
        print("INTO PGP_AWS_EXTRACTOR")
        while self.__LINK__ !="":
            self.__FORMAT__ = PyDict(self.selector)
            self.__chrome__.address = self.__LINK__.replace(".co.uk//", ".co.uk/")
            self.__chrome__.Navigate()
            self.__chrome__.Scroll_V_V()
            time.sleep(3)
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
                        print("{}"+str(self.__FULL__).format("      "))
                    except IndexError:
                        pass
                    finally:
                        self.__FULL__+= "{}!{}~{}\n".format("PGP",_key_,self.STACK[_key_])
            send(self.__FULL__)

            self.__FULL__ = ""
            self.__LINK__ = self.php.nextLink()

        self.__chrome__.Viewer().quit()



    LINK ="LINK"
    TITLE="TITLE"
    SELLER="SELLER"
    SELLER_LINK="SELLER_LINK"
    OFFER_RATING="OFFER_RATING"
    OFFER_TOTAL_RATING="OFFER_TOTAL_RATING"
    OFFER_PRICE="OFFER_PRICE"
    OFFER_DELIVERY_INFO="OFFER_DELIVERY_INFO"
    OFFER_SHORT_DESCRIPTION="OFFER_SHORT_DESCRIPTION"
    PRODUCT_BRAND = "PRODUCT_BRAND"
    PRODUCT_MODEL_NUMBER = "PRODUCT_MODEL_NUMBER"
    PRODUCT_COLOUR = "PRODUCT_COLOUR"
    PRODUCT_DIMENSIONS = "PRODUCT_DIMENSIONS"
    PRODUCT_MATERIAL = "PRODUCT_MATERIAL"
    PRODUCT_WEIGHT="PRODUCT_WEIGHT"
    PRODUCT_ASIN="PRODUCT_ASIN"
    PRODUCT_RATINGS="PRODUCT_RATINGS"
    PRODUCT_BEST_SELLERS_RANK="PRODUCT_BEST_SELLERS_RANK"

    STACK = {
        "QUEUEID":{}, "TITLE":{}, "SELLER":{},"SELLER_LINK":{}, "OFFER_RATING":{},
        "OFFER_TOTAL_RATING":{},"OFFER_PRICE":{}, "OFFER_DELIVERY_INFO":{},
        "OFFER_SHORT_DESCRIPTION":{}, "PRODUCT_BRAND":{}, "PRODUCT_MODEL_NUMBER":{},
        "PRODUCT_COLOUR":{},"PRODUCT_DIMENSIONS":{}, "PRODUCT_MATERIAL":{},
        "PRODUCT_WEIGHT":{},"PRODUCT_ASIN":{},"PRODUCT_RATINGS":{},"PRODUCT_BEST_SELLERS_RANK":{}
    }
