from time import sleep
class Clock:
    secInMin = 60
    def waitM(self,minutes):
        sleep(self.secInMin * int(minutes))

    def waitS(self,seconds):
        sleep(seconds)