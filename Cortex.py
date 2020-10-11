from Spider.Extractor.PyPath import *
from Spider.Browser.__Chormium__ import __Chromium__
from Spider.Extractor.Vendors.Amazon import Amazon
from Spider.Network.PHP import PHP
from Hacker.Logging import Logging
from Hacker.ClusterClient import send
from Texts.Bundle import Bundle
from Spider.Extractor.PyDict import PyDict
from Cheater.Murphy import Murphy
from threading import Thread
import json,time, os,re

__chrome__ = __Chromium__(True,False,"",False,True,True)
_php = PHP()
next= _php.nextLink()
fulldata = {}
SUBLINKS= {'Links':{}}
aws = Amazon()

while next !="":
    format = PyDict()
    __chrome__.address = next.replace(".co.uk//", ".co.uk/")
    __chrome__.Navigate()
    __chrome__.Scroll_V_V()
    __path__ = PyPath(__chrome__)
    __path__.Start(__chrome__.Source())
    _dict = format.Load()
    format.__xpath__ = __path__
    req = ""
    for i in range(len(_dict['Keys'])):
        key = _dict['Keys'][i]
        val = _dict['Values'][i]
        if key != "" and val !="":
            try:
                aws.STACK[key] = __path__.Stacked_extraction(val)
            except IndexError:
                pass
            finally:
                req+= "{}!{}~{}\n".format("AWS",key,aws.STACK[key])
                Logging(4, Bundle().getString(55), key)
    send(req)
    #print(req)

    next = _php.nextLink()

__chrome__.Viewer().quit()

