import datetime

from Hacker.FileSystem import FileSystem as fs
from Texts.Bundle import Bundle
from Hacker.Logging import Logging
from Hacker.ClusterClient import send


import json, os, time

class PyDict:
    clusterized = ''
    def __init__(self,selector):
        self.delimiter = ":"
        self.delimiter2 = '~'
        self.newline = "\n"
        self.path = os.getcwd() + "/Spider/Extractor/Selectors/"+str(selector)+ ".cort"
        if os.path.isfile(self.path) == False:
            Logging(2,Bundle().getString(60),Bundle().getString(61))
            exit()

        print(self.path)
        self.stack = fs().Read(self.path)
        self.cluster = {'Keys':[], 'Values':[]}
        self.__xpath__ = None
        self.end = False

    def Load(self):
        if self.stack is not None and self.stack !="":
            return self.toStack()



    def toStack(self):
        if self.stack is not None and self.stack != "" and self.delimiter2 in self.stack and self.newline in self.stack:
            lines = self.stack.split(self.newline)
            for line in lines:
                if line is not None and line !="":
                    spl = line.split(self.delimiter2)
                    self.cluster['Keys'].append(str(spl[0]))
                    self.cluster['Values'].append(spl[1])
                else:
                    pass
            return  self.cluster


    def diffEKeyVal(self, string, index):
        if self.delimiter2 in string:
            _d = string.split(self.delimiter2)
            for i in range(len(_d)):
                if index < i:
                    return _d[index]





    def Convert(self,lst):
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return res_dct




