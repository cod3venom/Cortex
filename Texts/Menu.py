from Hacker.Logging import Logging
from Texts.Bundle import Bundle
from Spider.Extractor.Vendors.Amazon.Categories import Categories
from Spider.Extractor.Vendors.Amazon.EntryLinks import EntryLinks

class Menu:
    def __init__(self):
        self.colors = Logging(0,"","cl")


    def MainMenu(self) -> str:
        return  "               [0] Amazon               [1]ebay               [2] AlliExpres \n" \
                "               [3] Alibaba              [4] Allegro           [5] Olx \n"

    def loadMainMenu(self) -> int:
        #menu = self.MainMenu()
        #self.PrintMenu(menu)
        #Categories('DE').c_main(0)
        category = 'https://www.amazon.de/s?i=kitchen&bbn=3167641&rh=n%3A3167641%2Cn%3A3169011%2Cn%3A20679858031%2Cn%3A3310821%2Cn%3A3310911%2Cn%3A3098777031&page=1&language=en&qid=1602962866&ref=sr_pg_59'
        EntryLinks(category).GetProductsFromSubpages()
    def PrintMenu(self, menu : str) -> int:
        if menu!=None:
            menu = self.colors.bold + menu + self.colors.endbold
            print(menu)
            select = input(Bundle().getString(64))
            switcher = {
                0: SubMenu().Amazon()
            }


    def test(self):
        print("works")

class SubMenu:


    def Amazon(self) -> int:
        menu =  """
               [0] SCAN MAIN & SUB CATEGORIES  [1] GENERATE OFFERPAGE SUBPAGES\n
                """
        print(menu)
        select = input(Bundle().getString(65))
        switcher = {
            0:self.ChooseCountries()
        }

    def ChooseCountries(self) -> str:
        countries = '\n               [0] Germany            [1] United kingdom          [2] United states \n'
        print(countries)
        select = input(Bundle().getString(66))
        switcher = {
            0: Categories('DE').c_main(0)
        }