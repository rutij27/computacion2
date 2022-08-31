import getopt, sys, os

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'n:hv')
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

def hijo():     
    if not os.fork():
        suma = sum([i for i in range(os.getpid()) if i % 2 == 0])
        if modo_verboso:
            print("Inicio de la ejecucion del proceso hijo")
            print(f'{os.getpid()} - {os.getppid()}: {suma}')
            print("Fin de la ejecucion del proceso hijo")
        else:
            print(f'{os.getpid()} - {os.getppid()}: {suma}')
        os._exit(0)

def ayuda_uso() -> str:
    return f"""[Para ejecutar] python3 ejercicio1.py -n **numero_hjos**
[Modo verboso] agregar -v
[Ayuda] agregar -h"""

modo_verboso = False
for (op,ar) in opt:
    if op == '-n':
        num_hjos = int(ar)
    elif op == '-h':
        print(ayuda_uso())
    elif op == '-v':
        modo_verboso = True


for i in range(num_hjos):
    hijo()
for i in range(num_hjos):
        os.wait()