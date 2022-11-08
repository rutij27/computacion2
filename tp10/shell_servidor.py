import socketserver, subprocess, getopt, sys

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

class Thread(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Process(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            if len(data) == 0 or data == "bye":
                print(f"Cliente desconectado {self.client_address[0]}")
                exit(0)
            comando = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = comando.communicate()
            if comando.returncode == 0:
                ans = "OK \n"+ stdout
                print(f'El comando {data.decode("ascii")} se ha ejecuto correctamente')
            else:
                ans = "ERROR \n"+ stderr
                print(f'El comando {data.decode("ascii")} no se ha ejecuto correctamente')

            self.request.send(ans.encode('ascii'))

if __name__ == "__main__":
    # args = 'p'
    socketserver.TCPServer.allow_reuse_address = True
    if args == "p":
        servidor = Process((host, port), MyTCPHandler)
        print(f"Servidor con procesos lanzado (Port= {port})")
        servidor.serve_forever()

    elif args == "t":
        servidor = Thread((host, port), MyTCPHandler)
        print(f"Servidor con hilos lanzado (Port= {port})")
        servidor.serve_forever()