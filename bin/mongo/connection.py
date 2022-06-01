from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure
import os


print('.env found') if load_dotenv() else print('.env not found')


class mongo_connection(object):
    

    def __init__(self, 
                 user=os.environ['USERMONGO'], 
                 password=os.environ['PASSMONGO'],
                 ip=os.environ['IP'], 
                 port=os.environ['PORT'], 
                 db=os.environ['DB']):

        self.connection_string = 'mongodb://{}:{}@{}:{}/{}'.format(user, password, ip, port, db) 
        self.connector = None


    def __enter__(self): 
        print('Entablando conexion....')
        self.connector = MongoClient(self.connection_string)
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback): 
        print('Cerrando conexion....')
        self.connector.close()
