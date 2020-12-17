from Core.DataOperations.Strings import EMPTY


class StringBuilder:
    def __init__(self):
        self.string = EMPTY

    def append(self, string):
        self.string += string

    def __str__(self):
        return str(self.string)
