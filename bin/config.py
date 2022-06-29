IPWEBSOCKET = '10.90.125.20'
PORTWEBSOCKET = 8765
# Aqui es donde recive el udp
IPUDP = '10.90.125.20'
PORTUDP = 1234 

IPFLASK = '10.90.125.20'
PORTFLASK = 5000 
# Le ponemos la Ip del medialon
IPMEDIALON = 'localhost'
PORTMEDIALON = 1234
# En esta varible es donde seteamos el json que le llega a VVVV
DATATOFRONT = None
# Estos son los valores iniciales del json cada que se abre la app para que cambien
# el medialon tiene que enviar los mensajes
DATAINTHREADS = {'modulos': 'todas', 'temporalidad': 'siempre', 'volumen': 99}
# La estructura de datos esta basada en el nombre del modulo[str]
# el numero de pregunta[str] y la cantidad de respuestas[int]
# IMPORTANTE en caso de que cambien el numero de respuestas o aumenten
# preguntas y modulos tienes que mover aqui
ESTRUCTURADATOS = [{'modulo1': {'1': 6, '2': 12, '3': 4}},
                   {'modulo2': {'1': 7, '2': 8}},
                   {'modulo3': {'1': 7, '2': 7}},
                   {'modulo4': {'1': 9, '2': 11}}
                   ]

