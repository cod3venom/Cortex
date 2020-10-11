from stem import  Signal
from stem.control import EventType, Controller
from stem.control import  Controller
from stem import StreamStatus

from Hacker.Logging import Logging
from Texts.Bundle import Bundle
import socks, socket, functools

class Tor:

    #@TODO: in some sites ip's are changed but in anothers dont
    #@TODO: Example 2ip.ru on every request ip appears as new
    #@TODO: But in nordvpn site dont
    def __new_ip__(self):
        try:
            with Controller.from_port(port=9051) as controller:
                controller.authenticate(password='123')
                socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
                controller.signal(Signal.NEWNYM)
                return  True
        except Exception as ex:
            Logging(2,Bundle().getString(56), Bundle().getString(57))
            return  False

