import requests as req
from requests import exceptions

from Cheater.HeadersFactory import HeadersFactory
from Cheater.ProxyFactory import ProxyFactory
from Cheater.Tor import  Tor

from Texts.Bundle import Bundle
from Hacker.Logging import  Logging

class HTTP:
    def __init__(self, address,data,PROXY_ROTATION,AGENT_ROTATION):
        if address !="":
            Logging(1,Bundle().getString(22),address)
            self.address = address
        self.data = data
        self.PROXY_ROTATION = PROXY_ROTATION
        self.AGENT_ROTATION = AGENT_ROTATION
        self.OUTPUT = ''





    def GET(self):
        try:
            with req.Session() as __session__:
                if self.PROXY_ROTATION:
                    __tor__ = Tor()
                    __tor__.__new_ip__()
                    __session__.proxies = ProxyFactory().__tor_gen__()
                if self.AGENT_ROTATION:
                    __session__.headers = HeadersFactory().__aws_random__()
                self.OUTPUT = __session__.get(self.address).text
        except exceptions.URLRequired:
            raise Bundle().getString("1")
        except exceptions.URLRequired:
            raise Bundle().getString("2")
        except exceptions.MissingSchema:
            raise Bundle().getString("3")
        except exceptions.InvalidSchema:
            raise Bundle().getString("4")
        except exceptions.TooManyRedirects:
            raise Bundle().getString("5")
        except exceptions.ConnectTimeout:
            raise Bundle().getString("6")
        except exceptions.Timeout:
            raise Bundle().getString("7")
        except exceptions.HTTPError:
            raise Bundle().getString("8")
        except exceptions.SSLError:
            raise Bundle().getString("9")
        except exceptions.ProxyError:
            raise Bundle().getString("10")
        except exceptions.ConnectionError:
            raise Bundle().getString("11")
        finally:
            if self.OUTPUT is not None and self.OUTPUT != "":
                return self.OUTPUT
            else:
                Logging(1,Bundle().getString(26),Bundle().getString(25))
                return ""

    def getImage(self):
        try:
            with req.Session() as __session__:
                if self.PROXY_ROTATION:
                    __tor__ = Tor()
                    __tor__.__new_ip__()
                    __session__.proxies = ProxyFactory().__tor_gen__()
                if self.AGENT_ROTATION:
                    __session__.headers = HeadersFactory().__aws_random__()
                self.OUTPUT = __session__.get(self.address, stream=True).raw
        except exceptions.URLRequired:
            raise Bundle().getString("1")
        except exceptions.URLRequired:
            raise Bundle().getString("2")
        except exceptions.MissingSchema:
            raise Bundle().getString("3")
        except exceptions.InvalidSchema:
            raise Bundle().getString("4")
        except exceptions.TooManyRedirects:
            raise Bundle().getString("5")
        except exceptions.ConnectTimeout:
            raise Bundle().getString("6")
        except exceptions.Timeout:
            raise Bundle().getString("7")
        except exceptions.HTTPError:
            raise Bundle().getString("8")
        except exceptions.SSLError:
            raise Bundle().getString("9")
        except exceptions.ProxyError:
            raise Bundle().getString("10")
        except exceptions.ConnectionError:
            raise Bundle().getString("11")
        finally:
            if self.OUTPUT is not None and self.OUTPUT != "":
                return self.OUTPUT
            else:
                Logging(1,Bundle().getString(26),Bundle().getString(25))
                return ""