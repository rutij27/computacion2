import getopt, sys, os, mmap, signal

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'f:')
    if len(opt) != 1:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-f':
       path = str(ar)

memoria = mmap.mmap(-1, 100)

def handler_padre(s, f):
    global continuar
    if s == signal.SIGUSR1:
        linea = memoria.readline()
        print(f'El padre acaba de recibir desde H1: {linea.decode()}')
        os.kill(pidh2, signal.SIGUSR1) # enviar
    if s == signal.SIGUSR2:
        print('El padre le avisa a h2 que tiene que terminar')
        continuar = False
        os.kill(pidh2, signal.SIGUSR2)

def handler_h2(s, f):
    if s == signal.SIGUSR1:
        linea = memoria.readline()
        print(f'El H2 acaba de recibir la señal del padre y lee la linea para guardarla en el archivo: {linea.decode()}')
        with open(path, 'a') as archivo:
            archivo.write(linea.decode())
            archivo.flush()
    if s == signal.SIGUSR2:
        print('H2 terminando y avisando al padre')
        os._exit(0)

pidh1 = os.fork()
if pidh1 == 0:
    print(f'Soy H1 mi pid es: {pidh1} y mi ppid es: {os.getppid()}\n')
    for linea in sys.stdin:
        if linea == 'bye\n':
            print('H1 terminando y avisandole al padre')
            os.kill(os.getppid(), signal.SIGUSR2)
            os._exit(0)
        else:
            print(f'H1 acaba de recibir la linea: {linea}')
            memoria.write(linea.encode('ascii'))
            os.kill(os.getppid(), signal.SIGUSR1)

pidh2 = os.fork()
if pidh2 == 0:
    print(f'Soy H2 y mi pid es: {pidh2} y mi ppdid es: {os.getppid()}\n')
    signal.signal(signal.SIGUSR1, handler_h2)
    signal.signal(signal.SIGUSR2, handler_h2)
    while True:
        signal.pause()

# esto es el padre
continuar = True
print(f'Soy el padre y mi pid es: {os.getpid()}\n')
signal.signal(signal.SIGUSR1, handler_padre)
signal.signal(signal.SIGUSR2, handler_padre)
while continuar:
    signal.pause()
else:
    for i in range(2):
        os.wait()
    print('Padre espero y ahora termina')

