import unittest
from bin import mongo_connection 
from bin import getData 
from bin import getJson
from bin import getPorcentajes 


class TestmongoCliente(unittest.TestCase):

    def test_2h(self):
        with mongo_connection() as connection:
            with getData(connection.connector, '2h') as data:
                toJson = getJson(data.data)
                getPorcentajes(toJson) 
                pass

    def test_1d(self):
        with mongo_connection() as connection:
            with getData(connection.connector, '1d') as data:
                toJson = getJson(data.data)
                getPorcentajes(toJson) 
                pass

    def test_1m(self):
        with mongo_connection() as connection:
            with getData(connection.connector, '1m') as data:
                toJson = getJson(data.data)
                getPorcentajes(toJson) 
                pass

    def test_siempre(self):
        with mongo_connection() as connection:
            with getData(connection.connector, 'siempre') as data:
                toJson = getJson(data.data)
                getPorcentajes(toJson) 
                pass
  
