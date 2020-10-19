from Spider.Browser.__Chormium__ import __Chromium__
from Spider.Extractor.PyDict import PyDict
from Spider.Extractor.PyPath import *
from Spider.Network.PHP import PHP
from Hacker.ClusterClient import send


"""
    AMAZON SCRAPER LAUNCHER
"""

class Expandica_aws:

    def __init__(self, selector):
        self.php = PHP()
        self.__chrome__ = __Chromium__(True,False,"",False,True,True)
        self.__FULL__ = ""
        self.__LINK__ = self.php.nextLink()
        self.selector = str(selector)


    def Start(self):
        while self.__LINK__ !="":
            self.__FORMAT__ = PyDict(self.selector)
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

        self.__chrome__.Viewer().quit()



    LINK ="LINK"
    TITLE="TITLE"
    SELLER="SELLER"
    SELLER_LINK="SELLER_LINK"
    OFFER_RATING="OFFER_RATING"
    OFFER_TOTAL_RATING="OFFER_TOTAL_RATING"
    OFFER_PRICE="OFFER_PRICE"
    OFFER_PRICE_IS="OFFER_PRICE_IS"
    OFFER_PRICE_WAS="OFFER_PRICE_WAS"
    OFFER_SHIPPING_INFO="OFFER_SHIPPING_INFO"
    OFFER_SHORT_DESCRIPTION="OFFER_SHORT_DESCRIPTION"
    CUSTOMERS_WHO_REVIEWED_TITLE="CUSTOMERS_WHO_REVIEWED_TITLE"
    CUSTOMERS_WHO_REVIEWED_LINK="CUSTOMERS_WHO_REVIEWED_LINK"
    CUSTOMERS_WHO_REVIEWED_IMAGE="CUSTOMERS_WHO_REVIEWED_IMAGE"
    CUSTOMERS_WHO_REVIEWED_STARS="CUSTOMERS_WHO_REVIEWED_STARS"
    CUSTOMERS_WHO_REVIEWED_PRICE="CUSTOMERS_WHO_REVIEWED_PRICE"
    PRODUCT_INFO_TABLE_KEY="PRODUCT_INFO_TABLE_KEY"
    PRODUCT_INFO_TABLE_VALUE="PRODUCT_INFO_TABLE_VALUE"
    PRODUCT_DESCRIPTION="PRODUCT_DESCRIPTION"
    PRODUCT_FROM_MANUFACTURER="PRODUCT_FROM_MANUFACTURER"

    STACK = {
        "QUEUEID":{}, "TITLE":{}, "SELLER":{},"SELLER_LINK":{}, "OFFER_RATING":{},
        "OFFER_TOTAL_RATING":{},"OFFER_PRICE":{}, "OFFER_SHIPPING_INFO":{},
        "OFFER_SHORT_DESCRIPTION":{},"CUSTOMERS_WHO_REVIEWED_TITLE":{},
        "CUSTOMERS_WHO_REVIEWED_LINK":{},"CUSTOMERS_WHO_REVIEWED_IMAGE":{},
        "CUSTOMERS_WHO_REVIEWED_STARS":{},"CUSTOMERS_WHO_REVIEWED_PRICE":{},
        "PRODUCT_INFO_TABLE_KEY":{},"PRODUCT_INFO_TABLE_VALUE":{},
        "PRODUCT_DESCRIPTION":{}, "PRODUCT_FROM_MANUFACTURER":{}
    }
