from types import SimpleNamespace

from Kernel.HTTP.httpsock import  httpsock
from Kernel.Classes.Bot.BotAuthTObject import BotAuthTObject
import json
sock = httpsock()
sock.setAddress('http://localhost/Silicon/index.php')
credits = {'BotAuth':'', 'Client_identifier':'dadada', 'Client_password':'admin'}
JSONIZED = json.loads(sock.Post(credits).text)

list = []
list.append(BotAuthTObject(JSONIZED))

for obj in list:
    print(obj.getUserID())