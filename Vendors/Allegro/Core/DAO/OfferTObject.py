from Core.DataOperations.StringBuilder import StringBuilder
from Core.Security import Global
from Logger.Logger import Logger


class OfferTObject:

    def __init__(self, offerId, title, seller, seller_rating, price, installment, buyNow, discount, description):
        self.offerId = offerId
        self.title = title
        self.seller = seller
        self.seller_link = Global.Local_Settings.ALLEGRO_config["USER_ADDR"] + seller
        self.seller_rating = seller_rating
        self.price = price
        self.installment = installment
        self.buyNow = buyNow
        self.discount = discount
        self.description = description

        self.logger = Logger()
        self.logger.Print(0, Global.levels.hackerType, message=self.__repr__(), bundler=False)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<ListingOfferTObject:")
        buffer.append(" OFFER_ID=" + str(self.offerId))
        buffer.append(", OFFER_TITLE=" + str(self.title))
        buffer.append(", SELLER_NAME=" + str(self.seller))
        buffer.append(", SELLER_LINK=" + str(self.seller_link))
        buffer.append(", SELLER_RATING=" + str(self.seller_rating))
        buffer.append(", OFFER_PRICE=" + str(self.price))
        buffer.append(", OFFER_INSTALLMENT=" + str(self.installment))
        buffer.append(", OFFER_BUY NOW=" + str(self.buyNow))
        buffer.append(", OFFER_DISCOUNT=" + str(self.discount))
        buffer.append(", OFFER_DESCRIPTION=" + str(self.description))
        buffer.append(">")
        return buffer.string

    def __str__(self):
        return self.__repr__()
