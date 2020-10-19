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

    def Write(self,path:str,data:str) -> int:
        if os.path.isfile(path):
            with open(path,"w", encoding="utf-8") as writer:
                writer.write(data)
                writer.close()

    def Append(self, path:str, data:str, duplicate:bool) -> int:
        if os.path.isfile(path) == False:
            self.Write(path,"")
        data = str(data)
        with open(path, "a") as appender:
            if data != None and data != "None" and len(data) > 10:
                if duplicate == False:
                    if data not in self.Read(path):
                        appender.write("\n" +data)
                    else:
                        appender.write("\n"+data)
