from Core.DataOperations.StringBuilder import StringBuilder
from Core.Security import Global
from Logger.Logger import Logger


class CategoriesStackTObject:

    def __init__(self, categoryType: str, subCategories: list):
        self.categoryType = categoryType
        self.subCategories = subCategories
        self.logger = Logger()
        self.logger.Print(0, Global.levels.hackerType, message=self.__repr__(), bundler=False)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<CategoriesStackTObject:")
        buffer.append(" CATEGORY TYPE=" + self.categoryType)
        buffer.append(", SUB CATEGORY=" + str(self.subCategories))
        buffer.append(">")
        return buffer.string

    def __str__(self):
        return self.__repr__()
