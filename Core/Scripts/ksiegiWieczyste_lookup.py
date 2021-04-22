import os
import sys
import time
import pdfkit

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from lxml import etree, html
from Browser.ChromeDriver import ChromeDriver
from Browser.ChromeOptions import ChromeOptions
from DAO.BotOptionsTObject import BotOptionsTObject
from DAO.BotProxyTObject import BotProxyTObject

selectors = [
    '''concat("KOD WYDZIAŁU : ", //input[1]/@value) ''',
    '''concat("NUMER KSIEGY WIECZYSTEJ : ", //input[2]/@value)''',
    '''concat("CYFRA KONTORLNA : ", //input[3]/@value)''',
    '''concat("UID : ", //input[4]/@value) '''
]

# /html/body/table[1]/tbody/tr/td[6]/form
page_css_selectors = [
    '''''',
    '''''',
    '''''',
    '''''',
    '''''',
]

input_stack = [
    "WR1K/00329384/7",
    "WR1K/00330700/9",
    "WR1K/00330724/3",
    "WR1K/00330793/7",
    "WR1K/00331136/1",
    "WR1K/00332082/4",
    "WR1K/00332082/4",
    "WR1K/00332148/5",
    "WR1K/00332148/5",
    "WR1K/00334607/5"
]
gate = 'https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW'
parametrized_objects = []


class parameters:
    def __init__(self, inputs):
        self.nrwydzialu = inputs[0]
        self.nrksiegi = inputs[1]
        self.nrkontrolny = inputs[2]


WKHTMLTOPDF_PATH = '/usr/bin/wkhtmltopdf'


def xpathParser(source, selector):
    try:
        source = html.fromstring(source)
        return source.xpath(selector)
    except etree.ParseError as ParseError:
        pass
    except etree.XPathEvalError as XpathEvalError:
        pass


class Main:

    def __init__(self):
        options = BotOptionsTObject(1, "1", "1", "LOOKUP", "", 1, 0, "0", 0, 1, "0", "0", "0", "0", "0")
        proxy = BotProxyTObject(1, "1", "1", "0", "0,", "")

        chromeOpts = ChromeOptions(options, proxy).getOptions()
        self.driver = ChromeDriver(parse_xpath_on=False)
        self.driver.setBrowser(options=chromeOpts,
                               Path='/Browser/Bin/chromedriver')

    def loadInputs(self):
        for inputs in input_stack:
            if "/" in inputs:
                parametrized_objects.append(parameters(inputs.split("/")))

        counter = 0
        for obj in parametrized_objects:
            counter += 1
            self.driver.setAddress(gate)
            self.driver.Navigate()
            self.Input("#kodWydzialuInput", obj.nrwydzialu)
            time.sleep(.5)
            self.Input("#numerKsiegiWieczystej", obj.nrksiegi)
            time.sleep(.5)
            self.Input("#cyfraKontrolna", obj.nrkontrolny)
            time.sleep(.5)
            self.Click("#wyszukaj")
            time.sleep(.5)
            self.Click("#przyciskWydrukZupelny")
            time.sleep(.5)

            self.parseNextPages()
            self.Die(1)
            # time.sleep(5)

    def countSubPages(self):
        total = xpathParser(self.driver.getBrowser().page_source, 'count(/html/body/table[1]/tbody/tr/td/form)')
        return int(total)

    def parseNextPages(self):
        counter = 1
        for i in range(1, self.countSubPages()):
            page_selector = f'/html/body/table[1]/tbody/tr/td[{str(i)}]/form/input[@type="submit"]'
            elements = self.driver.getBrowser().find_elements_by_xpath(page_selector)#.send_keys(Keys.RETURN)
            for element in elements:
                counter += 1
                print(page_selector)
                element.send_keys(Keys.ENTER)
                #self.generate_pdf(self.driver.getBrowser().page_source, 'pdf/', f"{str(counter)}.pdf")
                self.driver.getBrowser().save_screenshot(f"png/{str(counter)}.png")

    def generate_pdf(self, source, static_path, _path):
        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
        _status = pdfkit.from_string(
            source,
            os.path.join(WKHTMLTOPDF_PATH, _path),
            configuration=config,
            options={
                'page-size': 'A4',
                'margin-top': '0',
                'margin-right': '0',
                'margin-left': '0',
                'margin-bottom': '0',
                'zoom': '1.2',
                'encoding': "UTF-8",
            })
        return _path if _status else ''

    def Input(self, target, data):
        if self.Exists(target):
            self.driver.getBrowser().find_element_by_css_selector(target).send_keys(data)
        else:
            pass

    def Click(self, target):
        if self.Exists(target):
            self.driver.getBrowser().find_element_by_css_selector(target).send_keys(Keys.RETURN)
        else:
            pass

    def Exists(self, target):
        time.sleep(.4)
        try:
            self.driver.getBrowser().find_element_by_css_selector(target)
            return True
        except NoSuchElementException:
            return False

    def Die(self, line):
        self.driver.getBrowser().quit()
        sys.exit()


if __name__ == "__main__":
    _entry = Main()
    _entry.loadInputs()
