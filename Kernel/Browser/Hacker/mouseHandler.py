from random import randint, random

from selenium import webdriver
from scipy.spatial import KDTree
import numpy as np


class mouseHandler:
    def __init__(self, Browser: webdriver.Chrome):
        if Browser is not None:
            self.Browser = Browser

    def randomMovement(self):
        if self.Browser is not None:
            action = webdriver.ActionChains(self.Browser)
            for i in range(int(100)):
                action.move_by_offset(random(), random())
                action.perform()

    def Click(self):
        pass

    def Hover(self):
        pass
