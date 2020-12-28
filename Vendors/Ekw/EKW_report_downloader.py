import os
import time

from selenium.webdriver.common.keys import Keys

from Browser.ChromeDriver import ChromeDriver
from Browser.ChromeOptions import ChromeOptions
from Browser.HTML.Elements import Elements
from DAO.BotJavascriptTObject import BotJavascriptTObject
from DAO.BotOptionsTObject import BotOptionsTObject
from DAO.EkwNumbersListTObject import EkwNumbersListTObject
from Vendors.Ekw.EkwConfig import EkwConfig
from Core.DataOperations.Strings import EMPTY
from Core.Security.FileSystem import FileSystem
from Core.Security.Rest.RestClient import RestClient
from Core.Spiders.Extractors.Xpath import Xpath_selector

from Core.Security.Global import Local_Settings


class Report_downloader:
    def __init__(self, Options: BotOptionsTObject, Javascript: BotJavascriptTObject, Ekw_numbers: EkwNumbersListTObject,
                 TOTAL_PROCESS: int):
        self.Options = Options
        self.Javascript = Javascript
        self.Total_process = TOTAL_PROCESS
        self.Ekw_numbers = Ekw_numbers
        self.EKw_config = EkwConfig()
        self.__rest = RestClient()
        self.Elements = Elements()
        self.XpathSelector = Xpath_selector()
        self.browser: ChromeDriver = EMPTY
        self.ReportFolder = EMPTY
        self.FSystem = FileSystem()

    def Explore(self):
        self.browser = ChromeDriver(parse_xpath_on=False)
        chromeOpts = ChromeOptions(self.Options).getOptions()
        self.browser.setBrowser(chromeOpts)

        while self.Ekw_numbers.FIRST_PART:
            self.browser.setAddress(self.EKw_config.Gate)
            self.browser.Navigate(screenshot=False)

            self.MakePause()
            self.Elements.SetBrowser(self.browser.getBrowser())
            self.Elements.Input(self.EKw_config.First_code_css, self.Ekw_numbers.FIRST_PART)
            self.Elements.Input(self.EKw_config.Second_code_css, self.Ekw_numbers.SECOND_PART)
            self.Elements.Input(self.EKw_config.Third_code_css, self.Ekw_numbers.THIRD_PART)
            self.HitSearch()
            self.OpenReport()

            self.Ekw_numbers = self.__rest.getEkwNumbers(self.Ekw_numbers.EKW_NUMBERS_PACK_ID)

    def HitSearch(self):
        self.Elements.Click(self.EKw_config.Form_submit_css)
        self.MakePause()
        self.OpenReport()

    def RecordWasFound(self):
        source = str(self.browser.getBrowser().page_source).strip()
        if self.EKw_config.record_not_found in source or self.EKw_config.wrong_third_number in source:
            return False
        return True

    def OpenReport(self):
        if self.RecordWasFound():
            self.Elements.Click(self.EKw_config.Report_view_css)
            self.MakePause()
            self.ReportFolder = "{}{}_{}_{}".format(Local_Settings.HTML_EXPORT_PATH, self.Ekw_numbers.FIRST_PART,
                                                    self.Ekw_numbers.SECOND_PART, self.Ekw_numbers.THIRD_PART)
            if not os.path.exists(self.ReportFolder):
                self.OpenNextPage()

    def CountPages(self):
        total = self.XpathSelector.Extract(self.browser.getBrowser().page_source, self.EKw_config.Pages_count_xpath)
        return int(total)

    def OpenNextPage(self):
        total = self.CountPages()
        if total is not None and type(total) == int:
            self.FSystem.Create_dir(self.ReportFolder)
            total += 1  # TO HOOK THE LAST PAGE
            for index in range(0, total):
                page_selector = self.EKw_config.Page_selector_xpath.replace('$', str(index))
                page_buttons = self.Elements.FindByXpath(page_selector)
                if type(page_buttons) == list:
                    for button in page_buttons:
                        button.send_keys(Keys.ENTER)
                        self.SavePage(str(index), self.browser.getBrowser().page_source)

    def SavePage(self, name: str, content):
        document_path = f"{self.ReportFolder}/{name}.html"
        self.FSystem.writeToFile(document_path, content)

    def MakePause(self):
        time.sleep(.5)
