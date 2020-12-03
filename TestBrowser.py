from datetime import datetime
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Browser.Chromedriver import Chromedriver
from Browser.Options.ChromeArguments import ChromeArguments


driver = Chromedriver()
args = ChromeArguments()
config = args.getOptions(True,True,"",False,False)
driver.setChrome(config)
links = [
            "https://www.amazon.co.uk//Alfresia-Turin-Seater-Garden-Reclining/dp/B06XT2M7KF/ref=sr_1_5"
]

counter = 0
for link in links:
    print(link)
    driver.setAddress(link)
    driver.Navigate()

while True:
    pass