from bin import mongo_connection
from bin import getData 
from bin import getJson 
from bin import getPorcentajes 
import json 



def mongoRequest():
    with mongo_connection() as connection:
        with getData(connection.connector, 'siempre') as data:
            toJson = getJson(data.data)
            getPorcentajes(toJson) 
            pass


if __name__ == '__main__':

    # TODO : PENDIENTE 
    # [x] Filtrar los datos para daniel en base al json 
    # [] Integracion de Flask 
    # [] Hacer cliente de udp que responda y reciba los mensajes 
    # [] Enviar por webSocket los mensajes a VVVV 
    # -------------------------------------------------------
    # NOTAS
    # mongoRequest() se tiene que levantar un proceso por peticion
    mongoRequest()
