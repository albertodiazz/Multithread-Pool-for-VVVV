from bin import udpServer 
from bin import config as c


def msgModulos(msg):
    '''
    Return:
            [res] [str] : [regresa el nombre para el atributo modulos] 
    '''
    res = ['todas','derechos','vivienda','bienestar','desarrollo','academico']
    try:
        _index = type(res.index(msg))
        if _index == int:
            # Solo actualizamos cuando el valor sea enviado por el medialon
            c.DATAINTHREADS['modulos'] = res[_index] 
            return res[_index] 
        else:
            return None 
    except ValueError:
        return None 


def msgTemporalidad(msg):
    '''
    Return:
            [res] [str] : [regresa el nombre para el atributo temporalidad] 
    '''
    res = ['2h','1d','1m','siempre']
    try:
        _index = type(res.index(msg))
        if _index == int:
            # Solo actualizamos cuando el valor sea enviado por el medialon
            c.DATAINTHREADS['temporalidad'] = msg 
        else:
            return None 
    except ValueError as error:
        return None 

def msgVolumen(msg):
    try:
       _type = type(int(msg)) 
       c.DATAINTHREADS['volumen'] = _type
       return _type
    except ValueError:
        print('no me estas enviando un valor valido para convertilos a int')
        return None


def filterUdp():
    # TODO : BUG 
    # [] Arreglar problema de excepcion al cerrar con teclado
    with udpServer() as udp:
        while(True):
            print('UDP Listening...')
            bytesAddressPair = udp.serverSocket.recvfrom(udp.bufferSize)
            # TODO : IMPORTANTE
            # Los mensajes me los tiene que mandar en bytes ya que si no el len
            # del string no corresponde al del array
            message = bytes.decode(bytesAddressPair[0])
            # print(type(message), len(message.replace(' ', '')), len('1m'))
            addessClient = bytesAddressPair[1] 
            # TODO : TEST
            # [] Testear esto, hay que irlo cambiando mientras se hacen las peticiones
            msgModulos(message)
            msgTemporalidad(message)
            msgVolumen(message)
            # print('2Msg: {} IpCliente: {} '.format(message, addessClient)) 
            print('IpCliente: {} '.format(addessClient)) 
