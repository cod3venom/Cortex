AMAZON                         =                         "--aws"
PARSER                         =                         "--parser"
SILICON                         =                         "--silicon"
PRODUCTS                         =                         "--products"
SELECTORS                         =                         "--selectors"
VENDOR                         =                         "VENDOR NAME WITH CAPITAL LETTERS"
ARGUMENTS                         =                          [
                                                                AMAZON,
                                                                PARSER,
                                                                SILICON,
                                                                PRODUCTS,
                                                                VENDOR,
                                                                SELECTORS
                                                               ]
from Texts.Menu import Menu
from Spider.Extractor.Vendors.PGP.PGP_AWS_EXTRACTOFFERS import PGP_AWS_EXTRACTOFFERS
from Spider.Extractor.Vendors.Expandica.Expandica_aws import Expandica_aws
from Spider.Extractor.Misc import Misc
import  sys

class Cortex:


    def c_main(self, object) ->int:
        object.Start()

if __name__ == '__main__':
    crx = Cortex()
    misc = Misc()
    try:
        if sys.argv[1]  == AMAZON and sys.argv[2] == PARSER and sys.argv[3] == SILICON and sys.argv[4] == PRODUCTS  and sys.argv[5]!="" and sys.argv[6] !="" :
            """:@PARAM = sys.argv[5] ====> SELECTOR FILE"""
            if sys.argv[5] == "PGP":
                pgp = PGP_AWS_EXTRACTOFFERS(sys.argv[6]).Start()
                crx.c_main(pgp)

            if sys.argv[5] == "EXPANDICA":
                ex = Expandica_aws(sys.argv[6])
                crx.c_main(ex)

        if sys.argv[1] == SELECTORS:
            misc.ShowArgument(SELECTORS)
            misc.ShowWithIterate(Misc().GetSelectors())



    except IndexError:
        misc.ShowArgument(" USE ARGUMENTS BELLOW")
        for arg in ARGUMENTS:
            print("         "+arg)
        exit()

    #Menu().loadMainMenu()
