import multiprocessing
import requests 
import time
import sys 
sys.path.insert(0, '/mnt/d/trabajo/cocay/muvi/futurodelaVivienda/serviciosRouter/')



def testParallelClientes(cliente):
        res = requests.put('http://localhost:5000/data/{}'.format(cliente))
        print('Response to Cliente{}: {}'.format(cliente,res.json()['result']))


if __name__ == '__main__':
    clientes = [1,2,3,4,5,6,7,8,9,10,11,12]
    pool = multiprocessing.Pool(processes=4)
    output_async = pool.map_async(testParallelClientes,clientes)
    output = output_async.get() 
    print('Output: {}'.format(output))
