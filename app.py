from bin import mongo_connection
from bin import getData 
from bin import getJson 
from bin import getPorcentajes 
from flask import Flask 
from flask_cors import CORS 
import concurrent.futures
import json 


app = Flask(__name__)
CORS(app)


@app.route('/data', methods= ['PUT'])
def mongoRequest():
    with mongo_connection() as connection:
        with getData(connection.connector, 'siempre') as data:
            toJson = getJson(data.data)
            res = getPorcentajes(toJson) 
            return json.dumps({'result': '200',
                               'data': res)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        future = pool.submit(app.run())
        print('Termino: {}'.format(future.result()))


if __name__ == '__main__':

    # TODO : PENDIENTE 
    # [x] Filtrar los datos para daniel en base al json 
    # [] Integracion de Flask 
    # [] Hacer cliente de udp que responda y reciba los mensajes 
    # [] Enviar por webSocket los mensajes a VVVV 
    # -------------------------------------------------------
    # mongoRequest()
    # app.run()
    main()
