import json

getData = None 
modulos = None 

def setCantidadRespuestas(setCantidad):
    '''
    Args:
        [setCanitdad] [] : [Es la cantidad de repuestas por pregunta
                            en base a este wireframe:
        https://docs.google.com/spreadsheets/d/1Jn0ZBJjKI_b7tEb-VbHHrPSbshI4WQxb/edit#gid=1633676302]
    '''
    respuestas = ''
    for i in range(1, setCantidad+1):
        respuestas += str(i)+','
    return respuestas[:-1]


def setPorcentajes(sizeRespuesta, numPregunta):
    '''
    Creacion de Array en base al conteo de los numero duplicados
    colocandolos en su posicion del array
    '''
    global getData
    global modulos 
    print(type(numPregunta), 'modulo'+modulos, 'pregunta'+str(numPregunta))
    respuesta = getData['modulo'+modulos]['pregunta'+str(numPregunta)]['respuestas'].split(',')
    # ------------------------------------------------------------------
    sinRepetidos = sorted(list(dict.fromkeys(respuesta)))
    for expect in sizeRespuesta:
        if expect not in sinRepetidos:
            # Si hay alguna respuesta que no fue selecionada la agreagmos
            # al tamano del array que debe ser en base al wireframe
            sinRepetidos.append(str(expect))
    sinRepetidos = sorted(sinRepetidos)
    fixe = [x*0 for x in range(len(sinRepetidos))]
    # ------------------------------------------------------------------
    countD = ({i:respuesta.count(i) for i in respuesta})
    # Aquie es donde sacamos el porcentaje
    s = sum(countD.values())
    for k, v in countD.items():
        # TODO : DUDA
        # [] Daniel necesita los porcentajes en enteros o con decimales
        pct = v * 100 / s
        # print(k, int(pct))
        # pct = es el porcentaje
        fixe[int(k)-1] = int(pct)
    '''
    Aqui es donde agragamos los porcentajes a nuestro json
    '''
    getData['modulo'+modulos]['pregunta'+str(numPregunta)]['respuestas'] = ",".join(str(x) for x in fixe)
    print(type(fixe), fixe)


def getPorcentajes(getJson):
    '''
    Funcion para convertir las respuestas en porcentajes
    '''
    # TODO : FIX 
    # [] Areglar problemas con las pruebas

    global getData
    global modulos 

    getData = json.loads(getJson)

    # La estrucutura es el nombre del modulo mas la pregunta y la
    # catitdad de repuestas por pregunta en int
    estructuraDatos = [{'modulo1': {'1': 6, '2': 12, '3': 4}},
                       {'modulo2': {'1': 7, '2': 8}},
                       {'modulo3': {'1': 7, '2': 7}},
                       {'modulo4': {'1': 9, '2': 11}}
                       ]


    numPreguntas = [] 
    for i in range(len(estructuraDatos)):
        print('estamos ejecutando un map dentro de un loop {}'.format(estructuraDatos[i]))
        modulos = str(i+1)
        res = list(map(setCantidadRespuestas, estructuraDatos[i]['modulo'+str(i+1)].values()))
        for x in range(1,len(res)+1):
            numPreguntas.append(x)
        print('>>>>>>>>>>>>>>>>>')
        list(map(setPorcentajes, res, numPreguntas))
        numPreguntas.clear()

    print(json.dumps(getData, indent=4))
