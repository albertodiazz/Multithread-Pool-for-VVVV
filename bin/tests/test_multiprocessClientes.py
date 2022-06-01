import multiprocessing
import time
import sys 
sys.path.insert(0, '/mnt/d/trabajo/cocay/muvi/futurodelaVivienda/serviciosRouter/')

from bin import mongo_connection 
from bin import getData 



def testParallelClientes(temporalidad):
    with mongo_connection() as connection:
        with getData(connection.connector, temporalidad) as data:
            print('Data con un len de {} con Temporalidad: {} '.format(len(data.data), 
                                                                    temporalidad))
            pass


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    output_async = pool.map_async(testParallelClientes,['2h', '1d', '1m', 'siempre'])
    output = output_async.get() 
    print('Output: {}'.format(output))
