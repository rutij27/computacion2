import sys
import getopt
import subprocess as sp
import datetime as dt 

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'c:f:l:')
    if len(opt) != 3:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

command = ' '
output_file = ' '
log_file = ' '

for (op,ar) in opt:
    if op == '-c':
        command = ar
    elif op == '-f':
        output_file = open(ar, "a")
    elif op == '-l':
        log_file = ar

process = sp.Popen([command], stdout=output_file, stderr=sp.PIPE, shell=True, universal_newlines=True)
err = process.communicate()[1]

if not err:
    date = dt.datetime.now()
    to_write = f"{date}: El comando: {command}, se ha ejecutado correctamente"
    file_to_write = open(log_file, "a")
    file_to_write.write(to_write)
    file_to_write.write("\n")
    file_to_write.close() 
else:
    date = dt.datetime.now()
    to_write = f"{date}: >> {err}"
    file_to_write = open(log_file, "a")
    file_to_write.write(to_write)
    file_to_write.write("\n")
    file_to_write.close()

output_file.writelines("\n")
output_file.close()

#python3 ejercicio1 -c "ls" -f outfile.txt -l logfile.txt