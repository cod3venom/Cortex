from PIL import Image
from Spider.Network.HTTP import HTTP as __http__
from Texts.Bundle import Bundle
from Hacker.Logging import Logging
import pytesseract
class Murphy:

    def noCapcha(self,url):
        __IMG__ = __http__(url,"",True,True).getImage()
        captcha =  pytesseract.image_to_string(Image.open(__IMG__),config='--psm 7').strip().replace(" ","")
        Logging(2,Bundle().getString(58), captcha)
        return captcha