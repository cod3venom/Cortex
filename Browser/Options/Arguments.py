from enum import Enum
class Arguments(Enum):
    INCOGNITO = '--incognito'
    HEADLESS = True
    NO_GPU = 'disable-gpu'
    USER_DATA = '--user-data={}'
    ROOT = '--no-sandbox'
    TOR = '--proxy-server=socks5://127.0.0.1:9050'
    IGNORE_CERTIFICATE_ERROR = 'ignore-certificate-errors'
    DISABLE_EXTENSION = '--disable-extensions'
    DISABLE_DEV = '--disable-dev-shm-usage'
