import time

from lxml import html

from Hacker.Memory import Memory
from Hacker.Logging import Logging
from Cheater.Tor import Tor
from Cheater.Murphy import  Murphy
from Texts.Bundle import Bundle
from Spider.Network.Clock import Clock

#from Spider.Extractor.PyQue import PyQue
from lxml import etree

#global queue
#queue = PyQue()

class PyPath:
    def __init__(self,Viewer):
        self.source = ''
        self.viewer = Viewer
        self.__mem__ = Memory()
        #self.queue = PyQue()



    def is404(self,source):
        if Bundle().getString(31) in source:
            Logging(4,Bundle().getString(22) ,Bundle().getString(30))
            return  True
        else:
            #Logging(1,Bundle().getString(22) ,Bundle().getString(32))
            return  False
    def isBlocked(self,source):
        if Bundle().getString(33) in source:
            Logging(4,Bundle().getString(22) ,Bundle().getString(34))
            Logging(4,Bundle().getString(22) ,Bundle().getString(35))
            Tor().__new_ip__()
            Clock().waitM(.5)
            return  True
        else:
            Logging(1,Bundle().getString(22) ,Bundle().getString(32))
            return  False


    def isCaptcha(self,source):
        if Bundle().getString(36) in source:
            return True
        else:
            return False

    def getCapcha(self):
        url = self.Stacked_extraction(Bundle().getString(43))
        try:
            url = url[0]
            if Bundle().getString(44) in url or Bundle().getString(45) in url:
                return Murphy().noCapcha(url)

        except KeyError:
            pass
        except IndexError:
            pass
        except ValueError:
            pass

    def setCaptcha(self):
        captcha = self.getCapcha()
        self.viewer.setCaptcha(captcha,"XPATH")



    def Stacked_extraction(self,__target__):
        try:
            if self.is404(self.source):
                return ""
            if self.isBlocked(self.source) == False:
                content = html.fromstring(self.source)
                return content.xpath(__target__)
            else:
                return  ""
        except etree.ParseError:
            raise Bundle().getString(47)
        except etree.XPathEvalError:
            raise Bundle().getString(47) + '\r\n' + __target__

    def Start(self,source):
        if source != "" and self.isCaptcha(source) == False:
            self.source = source
            Bundle().getString(49)
        else:
            self.source = source
            self.setCaptcha()
