from bin import mongo_connection
from bin import getData 


if __name__ == '__main__':

    # TODO : TEST 
    # [] Testear esto con peticiones simultaneas
    # [] Filtrar los datos para daniel 
    with mongo_connection() as connection:
        with getData(connection.connector, 'siempre') as data:
            # print(data.data)
            pass
