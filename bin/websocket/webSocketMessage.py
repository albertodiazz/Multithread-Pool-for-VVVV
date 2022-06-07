import websockets 
from bin import config as c


async def sendMessage(msg):
    '''
        [args : str]: [Puede ser cualquier cosa solo es el pretexto 
                       para activar la funcion handler]
    '''
    # Estoy seguro que esto se puede mejorar y asi poder activar el handler
    # de forma directa sin necesidad de hacer esto.
    # Se me ocurre probar con Queue
    async with websockets.connect('ws://{}:{}'.format(c.IPWEBSOCKET, c.PORTWEBSOCKET)) as websocket:
        await websocket.send(msg)
        await websocket.recv()
