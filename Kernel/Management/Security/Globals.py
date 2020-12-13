import datetime, requests, urwid

from selenium.webdriver.chrome.webdriver import WebDriver

from Kernel.Bot.Class.Objects.LocalSettingsTObject import LocalSettingsTObject
from Kernel.HTTP.httpsock import httpsock

'''
    HTTPSOCK IS THE CLASS WHICH ALLOW US TO HANDLE ALL HTTP BASE REQUESTS AND AUTH SESSIONS
'''
http = httpsock()
http.setSession(requests.session())

'''
    CLASS LocalSettingsTObject STANDS FOR LOCALLY STORED JSON FORMAT CONFIG
'''
local_settings = LocalSettingsTObject()
http.setAddress(local_settings.GATE_URL)

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
    :param SELECTORS 
    THIS VARIABLE STANDS FOR XPATH SELECTORS GLOBAL STACK WHICH WILL BE USED IN MOST SPIDER BASED CLASSES
'''
SELECTORS: list = []




time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
debug_counter = 0


def Debug(data: str):
    global debug_counter
    debug_counter += 1
    formated = '[{}] [{}] $Cortex@Shell: {}'.format(str(debug_counter), time_now, data)
    print(formated)
