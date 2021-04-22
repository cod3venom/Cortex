from Core.Security import Global
from Logger.Logger import Logger


class ProgressBar:
    def __init__(self, start, limit, title: str = None):
        self.start = start
        self.limit = limit

        self.logger = Logger()
        self.logger.Print(0, Global.levels.hackerType, message=self.__repr__(), bundler=False)

    def Increase(self, offset: int = None) -> bool:
        """
        This class stands for mathematical progressbar
        imitation, with increasing start point which
        offset or using plus one.
        The function output will be used to render
        real gui progressbar in client side.
        :param offset:
        :return:
        """
        if self.start < self.limit:
            if offset:
                self.start = self.start + offset
            else:
                self.start = self.start + 1

            self.logger.Print(0, Global.levels.hackerType, message=self.__repr__(), bundler=False)
            return False

        else:
            return True

    def __repr__(self):
        return str({"START": self.start, "LIMIT": self.limit})

    def __str__(self):
        return self.__repr__()
