import sys

from Kernel.Browser.Chromedriver import Chromedriver
from Kernel.Browser.Options.ChromeArguments import ChromeArguments


def main()->int:
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

if __name__ == '__main__':
    #CLIENT_IDENTIFIER = sys.argv[1]
    #CLIENT_PASSWORD = sys.argv[2]
    main()