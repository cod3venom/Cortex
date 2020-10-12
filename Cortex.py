from Spider.Extractor.Vendors.Amazon import Amazon
import  sys

class Cortex:

    def c_main(self, object) ->int:
        object.Start()



if __name__ == '__main__':
    crx = Cortex()
    try:
        __vendor__ = str(sys.argv[1]).lower()
        if __vendor__ == "aws":

            crx.c_main(Amazon())

    except IndexError:
        print("""
                                                                            AS PARAMETER INPUT SUPPORTED VENDOR NAME
                                                                            For example : python3 Cortex.py AWS
        """)
        pass