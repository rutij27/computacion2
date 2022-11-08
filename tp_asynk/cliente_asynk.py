import socket, getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'h:p:')
    if len(opt) != 2:
        print("Ingresar la cantidad correcta de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-h':
       host = str(ar)
    if op == '-p':
        port = int(ar)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

print("Ingresar uncomando")
while True:
    comando = input('> ')
    if len(comando) == 0 or comando == "bye":
        print("Saliendo...")
        s.send(comando.encode("ascii"))
        break
    else:
        s.send(comando.encode("ascii"))
        recv = str(s.recv(1024).decode("ascii"))
        print(recv)