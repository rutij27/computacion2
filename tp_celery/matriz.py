from tasks import pot, raiz, log
import getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'f:c:')
    if len(opt) != 2:
        print("Ingresar cantidad correcta de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'error: {error}')
    exit()

for (op,ar) in opt:
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
    nueva_matriz: list= []
    for fila in matriz:
        fila_nueva = []
        for elemento in fila:
            elemento = calculate(fun, elemento)
            fila_nueva.append(elemento)
        nueva_matriz.append(fila_nueva)
    return nueva_matriz

def calculate(fun, elemento) -> int:
    funciones = {
        'pot': pot.delay(elemento),
        'raiz': raiz.delay(elemento),
        'log': log.delay(elemento)
    }
    return funciones[fun]

def main() -> None:
    resultados = calculator(calc, read_matriz(path))
    print(resultados)

if __name__ == '__main__':
    main()