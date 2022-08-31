import getopt, sys, os

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'f:')
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-f':
        file_to_read = ar

def leer_archivo():
    file = open(file_to_read, 'r')
    return file.readlines()

lineas_recibidas = []
def crear_hijo(line):
    if not os.fork():
        os.write(w, line[::-1].encode('ascii'))
        os._exit(0)
    #Hay que poner a todos los hijos a trabajar y despues leer, las lineas se la envio por otro pipep
    else:
        value = os.read(r, 100)
        lineas_recibidas.append(value.decode())


if __name__ == '__main__':
    lines = leer_archivo()
    r, w = os.pipe()
    for line in lines:
        crear_hijo(line)
    
    for line in lines:
        os.wait()

    for line in lineas_recibidas:
        print(line)