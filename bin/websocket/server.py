from websockets import connect
from websockets import serve 
from bin import config as c
import websockets 
import asyncio
import json 
import requests 

CLIENTS = set()

async def handler(websocket):
    try:
        CLIENTS.add(websocket)
        print('>>>>>>>>>>>>>>>>>>')
        print('Cliente Conectado')
        print('>>>>>>>>>>>>>>>>>>')
        # Esto se lo pongo para que conecte en automatico con la base de datos
        # recuerda que en produccion va sin el 1 que es el id
        requests.put('http://{}:{}/data/1'.format(c.IPFLASK, c.PORTFLASK))
        async for message in websocket:
            try:
                if message == 'sendToVVVV':
                    print('Estamos mandando los mensajes a vvvv')
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    await broadcast(json.dumps({'result': 200,
                                                'body': json.dumps(c.DATATOFRONT)}))
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            except TypeError as error:
                await websocket.send(json.dumps({'result': 400}))
                # print(error)
                pass
    except websockets.exceptions.ConnectionClosedError as e:
        # Esto suele ocurrir cuando reinicio la conexion en TouchDesigner
        # ya que al reiniciar me da un nuevo cliente
        print('>>>>>>>>>>>>>>>>>>')
        print(f'Sesion Terminada Handler', e)
        print('>>>>>>>>>>>>>>>>>>')
        pass
    except websockets.exceptions.ConnectionClosedOK as e:
        print('>>>>>>>>>>>>>>>>>>')
        print(f'ConnectionClosedOk Handler', e)
        print('>>>>>>>>>>>>>>>>>>')

async def broadcast(message):
    # En esta funcion obtenemos la cantidad de clientes conectados y es donde
    # les enviamos el mensaje a todos los cliente 
    # Hay una mejor manera de hacer esto en la documentacion The concurrent way
    # https://websockets.readthedocs.io/en/stable/topics/broadcast.html
    for websocket in CLIENTS.copy():
        try:
            await websocket.send(message)
        except websockets.exceptions.ConnectionClosedError as e:
            print('>>>>>>>>>>>>>>>>>>')
            print(f'Sesion Terminada en Broadcast', e)
            print('>>>>>>>>>>>>>>>>>>')
            pass

class webSocketServer():

    async def execute_WebSocket(self):
        print('Inciando WebSocket')
        async with serve(handler, c.IPWEBSOCKET, c.PORTWEBSOCKET):
            await asyncio.Future()  # run forever

