import  sys, os
class ENVIRONMENT:
    CURRENT_ROOT = str(os.getcwd()) + "/"
    PATH = [
                CURRENT_ROOT + 'Spider/Browser/JSCODE/',
                CURRENT_ROOT + 'Spider/Extractor/Selectors/'
            ]




    def execute(self,__com__):
        if __com__ != None and __com__ != "":
            print(__com__)
            os.system(str(__com__))

env = ENVIRONMENT()
env.setupPath()

