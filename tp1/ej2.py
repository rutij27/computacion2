mport argparse

parser = argparse.ArgumentParser(description="ejemplo parser")

parser.add_argument("-f", "--file", type=str, required=False, help="string")
parser.add_argument("-o", "--other", type=str, required=False, help="string")
args = parser.parse_args()

try:
    file = open(args.file,  'r')
except FileNotFoundError as error:
    print(f"El archivo {args.file} no existe en el disco, error: {error}")
    exit()

lines = file.readlines()
file.close()

def write_file():
    file_to_write = open(args.other, "w")
    file_to_write.writelines(lines)
    file_to_write.close()
    print(f"El archivo {args.other}, fue sobreescrito correctamente")

write_file()