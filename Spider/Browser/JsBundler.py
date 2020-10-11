import  os
from Hacker.Logging import Logging
from Texts.Bundle import Bundle
class JsBundler:
    def __init__(self,path):
        self.path = path

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
            Logging(2,"JAVASCRIPT", "CODEFILE NOT FOUND")