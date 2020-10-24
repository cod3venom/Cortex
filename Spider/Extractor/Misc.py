import  os
from Hacker.Logging import Logging
from Texts.Bundle import Bundle

class Misc:
    def __init__(self):
        self.CURRENT_ROOT = str(os.getcwd())
        self.path =  self.CURRENT_ROOT + '/Spider/Extractor/Selectors/'

    def ShowArgument(self, arg: str) -> int:
        print(" {}".format(arg))

    def ShowWithIterate(self, data:list) ->int:
        i:int = 0
        if data!=None:
            for dat in data:
                i+=1
                print("         [{}] {}".format(str(i),dat))

    def getString(self,num):
        if os.path.isfile(self.path):
            with open(self.path, "r") as __reader:
                for i,line in enumerate(__reader):
                    if i == int(num)-1:
                        line = line.strip()
                        if line is None:
                            return  "LINE {} IN {} IS NoneType".format(str(num),self.path)
                        else:
                            if "#" in line:
                                return line.split("#")[1]
        else:
            Logging(2,"XPATH BUNDLE", "XPATH FILE NOT FOUND")

    def GetSelectors(self):
        out = []
        for (dirpath, dirnames, filenames) in os.walk(self.path[:len(self.path)-1]):
            out.extend(filenames)
        return out