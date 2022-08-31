import getopt, sys, multiprocessing as mp
from math import sqrt, log10
from functools import partial

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'p:f:c:')
    if len(opt) != 3:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-p':
       num_process = int(ar)
    if op == '-f':
        path = str(ar)
    if op == '-c':
        calc = str(ar)

def read_matriz(path) -> list:
    with open(path, 'r') as file:
        matriz = file.readlines()
        matriz = [line.split(',') for line in matriz]
        return matriz

def calculator(fun, matriz) -> list:
    matriz_nueva: list= []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            elemento = calculate(fun, elemento)
            nueva_fila.append(elemento)
        matriz_nueva.append(nueva_fila)
    return matriz_nueva

def log(elemento) -> int:
    return log10(int(elemento))

def raiz(elemento) -> int:
    return sqrt(int(elemento))

def pot(elemento) -> int:
    return int(elemento)**int(elemento)

def calculate(fun, elemento) -> int:
    functions = {
        'pot': pot(elemento),
        'raiz': raiz(elemento),
        'log': log(elemento)
    }
    return functions[fun]

def main() -> None:
    pool = mp.Pool(processes=num_process)
    results = pool.starmap(partial(calculator, calc), [[read_matriz(path=path)]])
    print(results[0])

if __name__ == '__main__':
    main()