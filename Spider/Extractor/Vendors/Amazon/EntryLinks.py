import time

from lxml import html
from lxml import etree
from Spider.Browser.__Chormium__ import __Chromium__
from Hacker.FileSystem import FileSystem
from Texts.Bundle import Bundle
from Hacker.Logging import Logging

class EntryLinks:
    TABLE = "PGP_COFFE"
    FS = FileSystem()
    SUBSTACK = []
    OFFERS = []
    SELLERS = []
    SUBPAGES = []
    def __init__(self, category_url:str):
        self.category = category_url
        self.chrome = __Chromium__(False,False,"",False,False,False)

    def CountAllPages(self):
        xpath = '//span[@class="pagnDisabled"]/text()'
        self.chrome.address = self.category
        self.chrome.Navigate()
        self.chrome.Scroll_V_V()
        total = int(self.lxmlExtract(xpath))
        Logging(1,"AMAZON", "TOTAL FOUND " + str(total) + " PAGES")
        for i in range(int(total)):
            link = self.chrome.address.replace("page=1", "page="+str(i))
            self.SUBSTACK.append(link)
            self.FS.Append("DB/AWS_OFFERS_SUBPAGES.sql", link, False)
        self.OctopusquickLook()

    def OctopusquickLook(self):
        base = self.FS.Read('DB/AWS_OFFERS_SUBPAGES.sql')
        if "\n" in base:
            links = base.split("\n")
            for link in links:
                if link != "":
                    self.SUBSTACK.append(link)

        xpath = '//div[contains(@class,"s-result-list")]//*[contains(@class,"a-link-normal a-text-normal")]/@href'
        for link in self.SUBSTACK:
            print("INSIDE OF : " +link)
            self.chrome.address = link
            self.chrome.Navigate()
            self.chrome.Scroll_V_V()
            time.sleep(3)
            content = html.fromstring(self.chrome.Source())
            found = content.xpath(xpath)
            for f in found:
                if "https://www.amazon.de" not in f:
                    f = "https://www.amazon.de" + f
                self.FS.Append("DB/AWS_OFFER_LINKS_COFFE.json", f, False)
            print(str(found))

    def ProductWithSellerID(self):
        xpath = '//a[contains(@href,"seller=")]/@href'
        Targets = self.FS.Read('DB/AWS_OFFER_LINKS_COFFE.json')
        if "\n" in Targets:
            links = Targets.split("\n")
            for link in links:
                if link != "":
                    self.SUBSTACK.append(link)

        for link in self.SUBSTACK:
            self.chrome.address = link
            self.chrome.Navigate()
            self.chrome.Scroll_V_V()
            time.sleep(3)
            content = html.fromstring(self.chrome.Source())
            found = content.xpath(xpath)
            for f in found:
                if "https://www.amazon.de" not in f:
                    f = "https://www.amazon.de" + f
                self.FS.Append("DB/AWS_OFFER_LINKS_COFFE_WITH_SELLERID.json", f, False)
            print(str(found))

    def ConvertSellerIDToSellerLink(self):
        Targets = self.FS.Read("DB/AWS_OFFER_LINKS_COFFE_WITH_SELLERID.json")
        if "\n" in Targets:
            links = Targets.split("\n")
            for link in links:
                if link != "":
                    self.SELLERS.append(link)
        i = 0
        formated = ""
        for link in self.SELLERS:
            i+=1
            seller_id = link.split("seller=")[-1:][0]
            if "&" in seller_id:
                seller_id = seller_id.split("&")[0]
            formated = 'https://www.amazon.de/-/en/shops/{}?ref_=v_sp_storefront'.format(seller_id)
            self.FS.Append("DB/AWS_STORE_LINKS_COFFE_WITH_SELLERID.json", formated, False)


    def GetSellerAllSubLinks(self):
        xpath = '//li[@class="a-disabled"][2]/text()'
        Targets = self.FS.Read("DB/AWS_STORE_LINKS_COFFE_WITH_SELLERID.json")
        if "\n" in Targets:
            links = Targets.split("\n")
            for link in links:
                if link != "":
                    self.SUBPAGES.append(link)
        for link in self.SUBPAGES:
            self.chrome.address = link
            self.chrome.Navigate()
            self.chrome.Scroll_V_V()
            content = html.fromstring(self.chrome.Source())
            found = content.xpath(xpath)
            for total in found:
                print("\r\n\r\n\TOTAL ======== " + str(total))
                for i in range(int(total)):
                    link = self.chrome.CurrentURL() + "&page="+str(i)
                    self.SUBSTACK.append(link)
                    self.FS.Append("DB/AWS_STORE_ALL_SUBPAGES.sql", link, False)

    def GetProductsFromSubpages(self):
        xpath = '//a[@class="a-link-normal a-text-normal"][contains(@href,"-")]/@href'
        Targets = self.FS.Read('DB/AWS_STORE_ALL_SUBPAGES.sql')
        if "\n" in Targets:
            links = Targets.split("\n")
            for link in links:
                if link != "":
                    self.SUBSTACK.append(link)

        for link in self.SUBSTACK:
            self.chrome.address = link
            self.chrome.Navigate()
            self.chrome.Scroll_V_V()
            time.sleep(3)
            content = html.fromstring(self.chrome.Source())
            found = content.xpath(xpath)
            for f in found:
                if "https://www.amazon.de" not in f:
                    f = "https://www.amazon.de" + f
                self.FS.Append("DB/AWS_FINAL_OFFER_LINKS_FROM_SELLERS_WITH_SELLER_ID.json", f, False)
            print(str(found))

    def lxmlExtract(self,xpath:str):
        if xpath!=None and self.chrome.Source()!=None:
            try:
                content = html.fromstring(self.chrome.Source())
                found = content.xpath(xpath)
                for item in found:
                        try:
                            if item !=None:
                                if item != "":
                                    return item
                                else:
                                    return 1

                        except TypeError:
                            return 1

            except etree.ParseError:
                raise Bundle().getString(47)
            except etree.XPathEvalError:
                raise Bundle().getString(47) + '\r\n' + xpath


