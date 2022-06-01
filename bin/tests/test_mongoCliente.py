import unittest
from bin import mongo_connection 
from bin import getData 


class TestmongoCliente(unittest.TestCase):

    def test_2h(self):
        with mongo_connection() as connection:
            with getData(connection.connector, '2h') as data:
                pass

    def test_1d(self):
        with mongo_connection() as connection:
            with getData(connection.connector, '1d') as data:
                pass

    def test_1m(self):
        with mongo_connection() as connection:
            with getData(connection.connector, '1m') as data:
                pass

    def test_siempre(self):
        with mongo_connection() as connection:
            with getData(connection.connector, 'siempre') as data:
                pass
  
