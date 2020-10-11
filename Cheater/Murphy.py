from PIL import Image
from Spider.Network.HTTP import HTTP as __http__
from Texts.Bundle import Bundle
import pytesseract
class Murphy:

    def noCapcha(self,url):
        __IMG__ = __http__(url,"",True,True).getImage()
        captcha =  pytesseract.image_to_string(Image.open(__IMG__),config='--psm 7')
        print("CAPTCHA IS   " + captcha)
        return captcha