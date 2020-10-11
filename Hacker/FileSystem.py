import  os
from Hacker.Logging import Logging
from Texts.Bundle import Bundle
class FileSystem:


    def Read(self,path):
        if os.path.isfile(path):
            with open(path,"r", encoding="utf-8") as reader:
                return reader.read()
        else:
            Logging("Error",'read', Bundle().getString(13))
            return ""