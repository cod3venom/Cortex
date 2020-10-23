from Texts.Menu import Menu
from Spider.Extractor.Vendors.PGP.PGP_AWS_EXTRACTOFFERS import PGP_AWS_EXTRACTOFFERS
import  sys

class Cortex:

    def c_main(self, object) ->int:
        object.Start()



if __name__ == '__main__':
    crx = Cortex()
    try:
        selector = sys.argv[1]
        pgp = PGP_AWS_EXTRACTOFFERS(selector)
        crx.c_main(pgp)

    except IndexError:
        pass

    #Menu().loadMainMenu()
