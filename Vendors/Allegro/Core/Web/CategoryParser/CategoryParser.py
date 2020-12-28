from Browser.ChromeDriver import ChromeDriver
from Browser.ChromeOptions import ChromeOptions
from Core.Spiders.Extractors.Xpath import Xpath_selector
from Vendors.Allegro.Core.DAO.CategoriesStackTObject import CategoriesStackTObject
from Vendors.Allegro.Core.DAO.CategoryTObject import CategoryTObject


class CategoryParser:
    site_map = 'https://allegro.pl/mapa-strony/kategorie'
    category_type_selector = '//div[contains(@class,"card")]/div/../h3/text()'
    subCategory_title_selector = '//h3[contains(text(),"$")]/..//li/a/text()'
    subCategory_link_selector = '//h3[contains(text(),"$")]/..//li/a/@href'
    full_report = {}

    def __init__(self, main, options):
        self.driver = ChromeDriver(parse_xpath_on=False)
        self.main = main
        self.options = options

    def Start(self):
        chromeOpts = ChromeOptions(self.options).getOptions()
        self.driver.setBrowser(chromeOpts)
        self.driver.setAddress(self.site_map)
        self.driver.Navigate(scrollBottom=True)
        self.ExtractMainCategory()

    def ExtractMainCategory(self, stackView: bool = None, fullReport: bool = None):
        extractor = Xpath_selector()
        CategoryType = extractor.Extract(self.driver.getSource(), self.category_type_selector)
        counter = 0
        for Type in CategoryType:
            counter += 1
            self.full_report[str(counter)] = {}
            subCategories = extractor.Extract(self.driver.getSource(), self.subCategory_title_selector.replace("$", Type))
            subCategoryLink = extractor.Extract(self.driver.getSource(), self.subCategory_link_selector.replace("$", Type))

            self.full_report[str(counter)][str(Type)] = {}
            for link_index in range(len(subCategoryLink)):
                self.full_report[str(counter)][str(Type)][str(link_index)] = {"TITLE": subCategories[link_index],
                                                                              "LINK": subCategoryLink[link_index]}
                CategoryTObject(str(Type), str(subCategories[link_index]), str(subCategoryLink[link_index]))

            if stackView:
                CategoriesStackTObject(Type, [subCategories, subCategoryLink])
        if fullReport:
            print(str(self.full_report))
