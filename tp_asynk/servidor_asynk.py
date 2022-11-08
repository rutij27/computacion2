import asyncio, subprocess, getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'h:p:')
    if len(opt) != 2:
        print("Ingresar la cantidad correcta argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-h':
       host = str(ar)
    if op == '-p':
        port = int(ar)

async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        data = data.decode('ascii')
        addr = writer.get_extra_info('peername')
        if data == "bye":
            print(f"Cliente desconectado.. {addr}")
            writer.close()
            await writer.wait_closed()
            return
        print(f"Recibido {data} de {addr}") 
        comando = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = comando.communicate()
        if comando.returncode == 0:
            ans = "OK \n"+ stdout
            print(f'El comando {data} se ha ejecutado correctamente')
        else:
            ans = "ERROR \n"+ stderr
            print(f'El comando {data} no se ha ejecutado correctamente')

        writer.write(ans.encode('ascii'))
        await writer.drain()

async def main():
    servidor = await asyncio.start_server(
        handle_echo,
        host,
        port
    )

    print(f'Server lanzado...')
    await servidor.serve_forever()

asyncio.run(main())