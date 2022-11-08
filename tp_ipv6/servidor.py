import socketserver, subprocess, socket, threading, getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'h:p:a:')
    if len(opt) != 3:
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
    if op == '-a':
        args = str(ar)

class Thread(socketserver.ThreadingMixIn, socketserver.TCPServer): pass

class Process(socketserver.ForkingMixIn, socketserver.TCPServer): pass

class ThreadIPV6(socketserver.ThreadingMixIn, socketserver.TCPServer):
    ip_type = socket.AF_INET6

class ProcessIPV6(socketserver.ForkingMixIn, socketserver.TCPServer):
    ip_type = socket.AF_INET6

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            if len(data) == 0 or data == "exit":
                print(f"Cliente desconectado {self.client_address[0]}")
                exit(0)
            command = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = command.communicate()
            if command.returncode == 0:
                ans = "OK \n"+ stdout
                print(f'Comando {data.decode("ascii")} ejecutado correctamente')
            else:
                ans = "ERROR \n"+ stderr
                print(f'Comando {data.decode("ascii")} no ejecutado correctamente')

            self.request.send(ans.encode('ascii'))

# Lanzamos un hilo para contectar a los clientes
def servidor(direccion, port):
    if direccion[0] == socket.AF_INET and args == "t":
        print("Levantando en IPv4 con hilos")
        servidor = Thread((host,port), MyTCPHandler)
    elif direccion[0] == socket.AF_INET and args == "p":
        print("Levantando en IPv4 con procesos")
        servidor = Process((host,port), MyTCPHandler)
    elif direccion[0] == socket.AF_INET6 and args == "t":
        print("Levantando en IPv6 con hilos")
        server = ThreadIPV6((host,port), MyTCPHandler)
    elif direccion[0] == socket.AF_INET6 and args == "p":
        print("Levantando en IPv6 con procesos")
        servidor = ProcessIPV6((host,port), MyTCPHandler)
    else:
        print("Error con algun argumento")
    servidor.serve_forever()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    direcciones = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    print(direcciones, 'DIRECTIONS')
    connections = []
    for direction in direcciones:
        connections.append(threading.Thread(target=servidor, args=(direction, port)))

    for coneccion in connections:
        print(coneccion, 'conecion')
        coneccion.start()