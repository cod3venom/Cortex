from fake_useragent import UserAgent
from Hacker.Logging import  Logging
from Texts.Bundle import Bundle as __bundle__
class AgencyFactory:
    def __gen__(self):
        agent = UserAgent(verify_ssl=False).random
        Logging(1,__bundle__().getString(24), agent)
        return agent