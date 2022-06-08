import socket
from bin import config as c   


class udpServer(object):
    

    def __init__(self): 
        self.ip = c.IPUDP 
        self.port = c.PORTUDP 
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.bufferSize = 1024
        self.message = None
        self.addessClient = None


    def __enter__(self): 
        print('Iniciando Server UDP....')
        self.serverSocket.bind((self.ip, self.port))
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback): 
        # print('UDP....{}'.format(exc_type))
        # self.serverSocket.shutdown(socket.SOCK_DGRAM)
        pass
