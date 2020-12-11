import  socket
from Kernel.Management.Manager.Config.Config import Config

class TCPserver:

    def __init__(self):
        self.Server = socket.socket(family=socket.AF_INET, type= socket.SOCK_STREAM)
        self.machine = None
        self.ServerAction = False
        self.Connection = None
    def setMachine(self, machinie) ->int:
        self.machine = machinie
    def getMachine(self):
        return self.machine

    def Start_server(self):
        try:
            self.Server.bind((Config.Server_ip, Config.Server_port))
            self.Start_listening()
        except socket.error as ex:
            print(ex)

    def Start_listening(self):
        self.Server.listen(10)
        while True:
            self.Connection, addr = self.Server.accept()
            print('Connected with ' + addr[0] + ':' + str(addr[1]))
            self.Connection.sendto(b'hello',addr)
            Receive = self.Connection.recvfrom(Config.Server_tcp_buffer)
            print(Receive[0])
