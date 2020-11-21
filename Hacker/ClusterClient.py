import socket
SERVER = ("127.0.0.1",1337)
CONNECTED = False
_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def send(data):
    _client.sendto(str.encode(data),SERVER)
