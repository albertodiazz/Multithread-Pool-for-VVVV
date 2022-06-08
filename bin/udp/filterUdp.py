from bin import udpServer 


def msgModulos(msg):
    msgModulos = ['todas','derechos','vivienda','bienestar','desarrollo','academico']
    try:
        # TODO : FIRE
        # [] Agregar la eleccion al json del con el atributo modulos
        # [] contestar ok
        # [] Agregar la temporalidad al json y a la solicitud de la info en la base
        #    de datos
        if type(msgModulos.index(msg)) == int:
            return True 
        else:
            return False
    except ValueError:
        return False 


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
            # print(type(message), len(message.replace(' ', '')), len('vivienda'))
            addessClient = bytesAddressPair[1] 
            res = msgModulos(message)
            print('Msg: {} IpCliente: {} Modulos: {}'.format(message, addessClient, res))
