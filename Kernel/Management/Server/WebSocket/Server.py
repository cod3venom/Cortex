import asyncio
import websockets
from Kernel.Management.Security.Config import Config
from Kernel.Management.Server.WebSocket.CommandHandler import CommandHandler


class Server:

    def __init__(self):
        self.Server = None
        self.Client = None
        self.commandHandler = CommandHandler()

    def Start_server(self) -> int:
        self.Server = websockets.serve(self.commandHandler.Server_listener, Config.Server_host, Config.Web_socket_port)
        asyncio.get_event_loop().run_until_complete(self.Server)
        asyncio.get_event_loop().run_forever()




