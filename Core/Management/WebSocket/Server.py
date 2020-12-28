import asyncio, websockets

from Core.Security.Global import Local_Settings
from Core.Management.WebSocket.Commands import Commands


class Server:

    def __init__(self):
        self.Server = None
        self.Client = None
        self.Commands = Commands()

    def Start(self):

        self.Server = websockets.serve(self.Commands.Server_listener, Local_Settings.LOCAL_HOST,
                                       Local_Settings.WSS_MANAGER_PORT)
        asyncio.get_event_loop().run_until_complete(self.Server)
        asyncio.get_event_loop().run_forever()
