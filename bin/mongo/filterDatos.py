from collections import defaultdict
from collections import ChainMap
import re
import json 


def cuantasPreguntasTiene(data):
    '''
    Funcion para saber la cantidad maxima de preguntas por modulo
    Args:
        [data] [list] : [espera las preguntas] 
    Return:
        [max_value] [int]
    '''
    max_value = None
    for num in data:
        if max_value is None or num > max_value:
            max_value = num
    # print(type(max_value))
    return max_value 


def sortPreguntas(dic):
    '''
    Funcion para acomadar las preguntas en order de menor a mayor 
    Args:
        [dic] [dict] : [espera los datos con {preguntas: respuestas}] 
    Return:
        [max_value] [dict]
    '''
    res = {}
    for i in sorted(dict(dic)):
        res[i] = dic[i]
    # print(res)
    return res


def estructuraPreguntas(respuestas):
    '''
    Funcion para agregar todas las respuestas por pregunta 
    Args:
        [respuestas] [list] : [espera los datos con [preguntas, respuestas]] 
    Return:
        [sortData] [dict]
    '''
    temp = defaultdict(list)
    for key, val in respuestas:
        temp[key].append(val)
    '''
    Aqui acomodamos el string respuestas en su posicion despues de preguntas del json 
    '''
    res = dict((key, {'respuestas': re.sub('[\[\]]','',str((val)).replace(' ',''))}) for key, val in temp.items())
    sortData = sortPreguntas(res)
    return sortData


def filterDatos(data, modulo):
    '''
    Funcion para filtrar los datos a como los requiere VVVV 
    Args:
        [data] [list] : [espera todos los datos del request a mongo] 
        [modulo] [int] : [ponemos el numero de modulos a filtrar] 
    Return:
        [res] [dict]
    '''
    preguntas = []
    respuestas = []
    for x in range(len(data)):
        res = dict(data[x])
        if res['modulo'] == modulo:
            # print(res)
            preguntas.append(res['pregunta'])
            respuestas.append(['pregunta'+ str(res['pregunta']), res['respuesta']])
    # cantidad = cuantasPreguntasTiene(preguntas)
    '''
    Aqui acomodamos el string modulo en su posicion inicial del json 
    '''
    res = {'modulo{}'.format(modulo): estructuraPreguntas(respuestas)}
    # print(res['modulo{}'.format(modulo)])
    return res


def getJson(data):
    '''
    Funcion para obtener el json en base a la estructura acordada 
    Args:
        [data] [list] : [espera todos los datos del request a mongo] 
    Return:
        [toJson] [json]
    '''
    dataFilter = list(map(filterDatos, [data, data, data, data], [1, 2, 3, 4]))
    dataFilter.append({'modulos': '', 'temporalidad': '', 'volumen': 99})
    # Esto me genera mi lista de diccionarionos en una sola
    oneDict = dict(ChainMap(*dataFilter)) 
    toJson = json.dumps(oneDict, indent= 4)
    print(toJson)
    return toJson
