from bin import mongo_connection
from bin import getData 
from bin import getJson 
from bin import getPorcentajes 
from bin import webSocketServer 
from bin import broadcast 
from bin import filterUdp 
from bin import config as c 
from flask import Flask, request 
from flask_cors import CORS 
import concurrent.futures
import json 
import asyncio 


app = Flask(__name__)
CORS(app)


@app.route('/data/<id>', methods= ['PUT'])
async def mongoRequest(id):
    with mongo_connection() as connection:
        with getData(connection.connector, 'siempre') as data:
            toJson = getJson(data.data)
            DATATOFRONT = getPorcentajes(toJson) 
            # TODO : PENDIENTE
            # [] para produccion hay que quitarle el id ya que solo me sirve
            #    para probar que los mensajes me lleguen en el orden correcto
            cliente = id
            # Esto lo podria cerrar y levantar cada que se necesite pero el problema
            # esta en que si VVVV se conecta en automatico hoy hay que manejar la desconexion
            # desde VVVV
            await broadcast(json.dumps({'cliente': cliente,'body': DATATOFRONT}))
            return json.dumps({'result': '200',
                               'cliente': cliente,
                               'body': DATATOFRONT})


async def threadsAsyncio():
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            loop = asyncio.get_running_loop()
            futures = [
                await loop.run_in_executor(pool, webSocketServer().execute_WebSocket),
                loop.run_in_executor(pool, app.run),
                loop.run_in_executor(pool, filterUdp)
            ]
            results = await asyncio.gather(*futures, return_exceptions=False)
    except KeyboardInterrupt:
        print('Se detuvieron los Threads con el Teclado')


if __name__ == '__main__':

    # TODO : PENDIENTE 
    # [x] Filtrar los datos para daniel en base al json 
    # [x] Integracion de Flask 
    # [] Hacer que cliente de udp llene los mensajes vacios:
    #    modulos, temporalidad, volumen, eso se lo enviamos a VVVV   
    # [x] Enviar por webSocket los mensajes a VVVV 
    # -------------------------------------------------------
    # mongoRequest()
    # app.run()
    try:
        asyncio.run(threadsAsyncio())
        # asyncio.run(webSocketServer().execute_WebSocket())
    except KeyboardInterrupt:
        print('Se detuvieron todos los servicios con el Teclado')
