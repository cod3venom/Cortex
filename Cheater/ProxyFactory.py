from selenium.webdriver.common.proxy import Proxy, ProxyType
class ProxyFactory:
    def __tor_gen__(self):
        return {
            'http': 'socks5h://127.0.0.1:9050',
            'https':'socks5h://127.0.0.1:9050'
        }
