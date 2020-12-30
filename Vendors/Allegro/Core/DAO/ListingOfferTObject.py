from Core.DataOperations.StringBuilder import StringBuilder
from Core.Security import Global
from Logger.Logger import Logger


class ListingOfferTObject:

    def __init__(self, category,  title, link, price, total_sold):
        if type(category) == list:
            self.category = category[len(category)]
        else:
            self.category = str(category)
        self.title = title
        self.link = link
        if type(price) == list:
            self.price = str(f"{price[0]} zł")
        else:
            self.price = f"{str(price)} zł"
        self.total_sold = total_sold

        self.logger = Logger()
        self.logger.Print(0, Global.levels.hackerType, message=self.__repr__(), bundler=False)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<ListingOfferTObject:")
        buffer.append(" CATEGORY_TYPE=" + str(self.category))
        buffer.append(", OFFER_TITLE=" + str(self.title))
        buffer.append(", OFFER_LINK=" + str(self.link))
        buffer.append(", OFFER_PRICE=" + str(self.price))
        buffer.append(", OFFER_TOTALLY SOLD=" + str(self.total_sold))
        buffer.append(">")
        return buffer.string

    def __str__(self):
        return self.__repr__()
