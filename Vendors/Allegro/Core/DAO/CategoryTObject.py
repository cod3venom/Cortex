from Core.DataOperations.StringBuilder import StringBuilder
from Core.Security import Global
from Logger.Logger import Logger


class CategoryTObject:
    def __init__(self, categoryType: str, categoryTitle: str, categoryLink: str):
        self.categoryType = categoryType
        self.categoryTitle = categoryTitle
        self.categoryLink = Global.Local_Settings.ALLEGRO_config["ROOT_PATH"] + categoryLink
        self.logger = Logger()
        self.logger.Print(0, Global.levels.hackerType, message=self.__repr__(), bundler=False)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<CategoryTObject:")
        buffer.append(" CATEGORY TYPE=" + self.categoryType)
        buffer.append(", CATEGORY NAME=" + self.categoryTitle)
        buffer.append(", CATEGORY LINK=" + self.categoryLink)
        buffer.append(">")
        return buffer.string

    def __str__(self):
        return self.__repr__()