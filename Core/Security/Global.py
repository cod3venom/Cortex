import requests, sys

from Core.DAO.LocalSettingsTObject import LocalSettingsTObject
from Core.DataOperations.Logger.Levels import Levels
from Core.DataOperations.Strings import EMPTY
from Core.Security.FileSystem import FileSystem
from Core.Security.Rest.http import Http

"""
    LOCAL SETTINGS
"""
Local_Settings = LocalSettingsTObject()
levels = Levels()

"""
    :var http
"""
http = Http()
http.setSession(requests.session())

'''
    :var COOKIES:DICT is the set of cookie values which are returnet from the PHP BACKEND
'''

COOKIES = {}


def setCookie(key, value):
    COOKIES[key] = value


def getCookie(key):
    if key in COOKIES.keys():
        return COOKIES[key]


def DeleteCookie(key):
    if key in COOKIES.keys():
        del COOKIES[key]


def isLogged():
    if 'CLIENT_ID' in COOKIES.keys():
        if COOKIES['CLIENT_ID'] is not None:
            return True
    return False


'''
    :param SELECTORS Is an global variable, which must be accessed from any class,
    it helps to avoid wasting time on http requests and mysql querying 
    
    @usage
        for key in indexed_js.keys():
                    __SELECTORS__.append(cls(**indexed_js[key]))
    and then retrieve objects in for loop
    for selector in __SELECTORS__:
        print(selector)
'''
__SELECTORS__: list = []

'''
    :param __THREAD_FACTORY__
'''
__THREAD_FACTORY__: list = []


def AppendToFactory(threadPool):
    if threadPool not in __THREAD_FACTORY__:
        __THREAD_FACTORY__.append(threadPool)


def ClearFactory():
    __THREAD_FACTORY__.clear()


def GetFactory():
    return __THREAD_FACTORY__


'''
    :param GLOBAL_LOG
    in this variable will stored all console outputs
'''
GLOBAL_LOG: str = ''

'''
    :param CUSTOM_HTML_LOCATORS
    is used to hover some random elements to avoid bot detection 
'''
CUSTOM_HTML_LOCATORS: list = ['img', 'p', 'button']



def report_errors(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)


sys.excepthook = report_errors
