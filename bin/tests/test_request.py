import requests
import unittest

class TestrequestFlask(unittest.TestCase):

    def test_UnCliente(self):
        res = requests.put('http://localhost:5000/data')
        print('Response: {}'.format(res.json()['result']))
        self.assertEqual(res.json()['result'], '200')
