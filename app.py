from bin import mongo_connection
from bin import getData 
from bin import getJson 
from bin import getPorcentajes 
from bin import webSocketServer 
from flask import Flask 
from flask_cors import CORS 
import concurrent.futures
import json 
import asyncio 


app = Flask(__name__)
CORS(app)


@app.route('/data', methods= ['PUT'])
def mongoRequest():
    with mongo_connection() as connection:
        with getData(connection.connector, 'siempre') as data:
            toJson = getJson(data.data)
            res = getPorcentajes(toJson) 
            # print(res)
            # TODO : FIRE
            # [] Aqui hay que agreger un await para que cada que se termine el proceso
            #    mandamos la data a VVVV
            return json.dumps({'result': '200',
                               'body': res})


async def threadsAsyncio():
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            loop = asyncio.get_running_loop()
            futures = [
                await loop.run_in_executor(pool, webSocketServer().execute_WebSocket),
                loop.run_in_executor(pool, app.run)
            ]
            results = await asyncio.gather(*futures, return_exceptions=False)
    except KeyboardInterrupt:
        print('Se detuvieron los Threads con el Teclado')


if __name__ == '__main__':

    # TODO : PENDIENTE 
    # [x] Filtrar los datos para daniel en base al json 
    # [x] Integracion de Flask 
    # [] Hacer cliente de udp que responda y reciba los mensajes 
    # [] Enviar por webSocket los mensajes a VVVV 
    # -------------------------------------------------------
    # mongoRequest()
    # app.run()
    try:
        asyncio.run(threadsAsyncio())
        # asyncio.run(webSocketServer().execute_WebSocket())
    except KeyboardInterrupt:
        print('Se detuvieron todos los servicios con el Teclado')
