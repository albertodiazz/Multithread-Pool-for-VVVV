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
            print('hasta aqui funciona')
            # Solo actualizamos cuando el valor sea enviado por el medialon
            c.DATAINTHREADS['modulos'] = msg 
    except ValueError:
        # print('ocurrio un error en msgModulos')
        pass


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
    except ValueError as error:
        # print('ocurrio un error en msgTemporalidad')
        pass


def msgVolumen(msg):
    try:
       _type = type(int(msg)) 
       c.DATAINTHREADS['volumen'] = _type
    except ValueError:
        # print('ocurrio un error en msgVolumen')
        pass


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
            # Sin embargo en mi red local me deja enviarlos en one per message
            # hay que revizar eso con redes 
            message = bytes.decode(bytesAddressPair[0])
            # print(type(message), len(message.replace(' ', '')), len('1m'))
            addressClient = bytesAddressPair[1] 
            msgModulos(message)
            msgTemporalidad(message)
            msgVolumen(message)
            # print('2Msg: {} IpCliente: {} '.format(message, addessClient)) 
            print('IpCliente: {} '.format(addressClient)) 
            # TODO : BUG 
            # cuando no hay conexion con el medialon el udp se queda trabado
            # esto hay que modificarlo
            # Sin embargo en mi red local no lo hace
            # udp.serverSocket.sendto('ok'.encode('utf-8'), (c.IPMEDIALON, c.PORTMEDIALON))
