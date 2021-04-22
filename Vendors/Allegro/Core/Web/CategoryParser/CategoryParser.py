import json
import time
from API.Progress.ProgressBar import ProgressBar
from Browser.ChromeDriver import ChromeDriver
from Browser.ChromeOptions import ChromeOptions
from Core.Security.FileSystem import FileSystem
from Core.Spiders.Extractors.Xpath import Xpath_selector
from Vendors.Allegro.Core.DAO.CategoriesStackTObject import CategoriesStackTObject
from Vendors.Allegro.Core.DAO.CategoryTObject import CategoryTObject
import Core.Security.Global as Global
from Vendors.Allegro.Core.DAO.ListingOfferTObject import ListingOfferTObject
from Vendors.Allegro.Core.DAO.OfferTObject import OfferTObject


class CategoryParser:
    full_report = {}
    listing_links = []
    offers_links = {}

    def __init__(self, main, options):
        self.driver = ChromeDriver(parse_xpath_on=False)
        self.main = main
        self.options = options
        self.extractor = Xpath_selector()

        chromeOpts = ChromeOptions(self.options).getOptions()
        self.driver.setBrowser(chromeOpts)
        self.driver.setAddress(Global.Local_Settings.ALLEGRO_CategoryParser["URL"])
        self.driver.Navigate(scrollBottom=True)

    def GetCategoryScheme(self, stackView: bool = None, fullReport: bool = None):
        """
        This method is used to create some kind of json based report to view
        how many categories are available in Allegro's platform and get such
        a information like TITLE and LINK
        :param stackView:
        :param fullReport:
        :return:
        """

        CategoryType = self.extractor.Extract(self.driver.getSource(),
                                              Global.Local_Settings.ALLEGRO_CategoryParser["CATEGORY_TYPE_SELECTOR"])
        counter = 0
        for Type in CategoryType:
            counter += 1
            self.full_report[str(counter)] = {}
            subCategories = self.extractor.Extract(self.driver.getSource(),
                                                   Global.Local_Settings.ALLEGRO_CategoryParser[
                                                       "CATEGORY_TITLE_SELECTOR"].replace("$", Type))
            subCategoryLink = self.extractor.Extract(self.driver.getSource(),
                                                     Global.Local_Settings.ALLEGRO_CategoryParser[
                                                         "CATEGORY_LINK_SELECTOR"].replace("$", Type))

            self.full_report[str(counter)][str(Type)] = {}
            for link_index in range(len(subCategoryLink)):
                self.full_report[str(counter)][str(Type)][str(link_index)] = {"TITLE": subCategories[link_index],
                                                                              "LINK": subCategoryLink[link_index]}
                CategoryTObject(str(Type), str(subCategories[link_index]), str(subCategoryLink[link_index]))

            if stackView:
                CategoriesStackTObject(Type, [subCategories, subCategoryLink])
        if fullReport:
            print(str(self.full_report))

    def GenerateCategoryListingPages(self):
        """
        This method is used to generate offer listing
        pages for all Allegro categories, and those
        links in future will be used to extract all
        offer private links
        :return:
        """
        self.GetCategoryScheme(fullReport=True)
        objects = []
        for firstIndex in self.full_report.keys():
            for secondIndex in self.full_report[firstIndex]:
                for thirdIndex in self.full_report[firstIndex][secondIndex]:
                    copy = CategoryTObject("", self.full_report[firstIndex][secondIndex][thirdIndex]["TITLE"],
                                           self.full_report[firstIndex][secondIndex][thirdIndex]["LINK"])
                    objects.append(copy)

        fSys = FileSystem()
        progressBar = ProgressBar(0, len(objects))

        for progress, Category in enumerate(objects):
            progressBar.Increase()

            self.driver.setAddress(Category.categoryLink)
            self.driver.Navigate()
            total_pages = int(self.extractor.Extract(self.driver.getSource(),
                                                     Global.Local_Settings.ALLEGRO_CategoryListingPages[
                                                         "TOTAL_PAGES_COUNTER_SELECTOR"]))
            for index in range(1, total_pages):
                listing_link = f"{Category.categoryLink}{Global.Local_Settings.ALLEGRO_config['PAGE_LINK_PARAMS']}{str(index)}"
                fSys.append(f"{Global.Local_Settings.TXT_EXPORT_PATH} ALLEGRO_LISTING_PAGES.txt", listing_link)
                self.listing_links.append(listing_link)
            return

    def ExtractOfferLinks(self):
        self.GenerateCategoryListingPages()

        for Link in self.listing_links:
            if Link != self.driver.getBrowser().current_url:
                self.driver.setAddress(Link)
                self.driver.Navigate(scrollBottom=True)
                category_name = self.extractor.Extract(self.driver.getBrowser().page_source,
                                                       Global.Local_Settings.ALLEGRO_CategoryExtractLinks[
                                                           "CATEGORY_NAME"])
                offer_title = self.extractor.Extract(self.driver.getBrowser().page_source,
                                                     Global.Local_Settings.ALLEGRO_CategoryExtractLinks["OFFER_TITLE"])
                offer_link = self.extractor.Extract(self.driver.getBrowser().page_source,
                                                    Global.Local_Settings.ALLEGRO_CategoryExtractLinks["OFFER_LINK"])
                offer_price = self.extractor.Extract(self.driver.getBrowser().page_source,
                                                     Global.Local_Settings.ALLEGRO_CategoryExtractLinks["OFFER_PRICE"])
                offer_total_sold = self.extractor.Extract(self.driver.getBrowser().page_source,
                                                          Global.Local_Settings.ALLEGRO_CategoryExtractLinks[
                                                              "OFFER_TOTAL_SOLD"])

                if type(offer_title) == list:
                    for index, title in enumerate(offer_title):
                        try:
                            ListingOfferTObject(category_name, title, offer_link[index], offer_price[index],
                                                offer_total_sold[index])
                            self.ExtractOffer(offer_link[index])
                        except IndexError as ex:
                            pass

    def ExtractOffer(self, link: str):
        self.driver.setAddress(link)
        self.driver.Navigate(scrollBottom=False, sanitize=False)

        offers = self.extractor.Extract(self.driver.getSource(), Global.Local_Settings.ALLEGRO_OfferExtractor["OFFER_JSON"])

        for offer in offers:
            try:
                copy = json.loads(offer)
                OfferTObject(
                    copy["notifyAndWatch"]["offerId"], copy["offerTitle"]["title"], copy["offerTitle"]["sellerName"], copy["offerTitle"]["sellerRating"],
                    copy["price"]["priceInteger"], f'{copy["price"]["priceFraction"]} {copy["price"]["priceFraction"]}'
                    f'{copy["price"]["installments"]["installmentsDetails"]["price"]} {copy["price"]["installments"]["installmentsDetails"]["multiplierDescription"]}',
                    copy["notifyAndWatch"]["sellingMode"]["buyNow"]["active"], copy["notifyAndWatch"]["sellingMode"]["buyNow"]["discount"],
                    str(self.extractor.Extract(self.driver.getSource(), Global.Local_Settings.ALLEGRO_OfferExtractor["OFFER_DESCRIPTION"]))
                )

            except KeyError:
                pass
        time.sleep(5)