import getopt, sys, os, time

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'n:r:hf:v')
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

modo_verboso = False
for (op,ar) in opt:
    if op == '-n':
        num_hjos = int(ar)
    if op == '-f':
        file = ar
    if op == '-r':
        len_letra = int(ar)
    if op == '-h':
        print("Para ejecutar: [python3 fork_fd.py -n 3 -r 4 -f log.txt]")
    if op == '-v':
        modo_verboso = True
    
ABC = 'ABCDEFGHIJK'

def hijo(letra: str):
    if not os.fork():
        print("Hijo escribiendo...")
        if modo_verboso:
            print(f'PROCESO: {os.getpid()} escribiendo letra: {letra}')
        for i in range(len_letra):
            fd.write(letra)
            fd.flush()
            time.sleep(1)
        print("Hijo termino de escribir")
        os._exit(0)

def escribir_archivo(name: str):
    fd = open(str(name), "w+")
    return fd

def leer_archivo(name: str):
    fd = open(str(name), "r")
    lines = fd.readlines()
    print(f"[Archivo] -> {lines[0]}")


if __name__ == '__main__':

    fd = escribir_archivo(file)
    for i in range(num_hjos):
        hijo(ABC[i])

    for i in range(num_hjos):
        os.wait()

    leer_archivo(file)