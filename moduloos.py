import os
from os import path
import datetime
from datetime import date, time, timedelta
import time



def main():

    print(os.name)
    print("El archivo existe: %s" % str(path.exists("archivo.txt")))
    print("Es un archivo: %s" % str(path.isfile("archivo.txt")))
    print("Es un directorio: %s" % str(path.isdir("archivo.txt")))

    print("El directorio del archivo es: %s" % path.realpath("archivo.txt"))

    #imprimir directorio y el nombre del archivo
    print("El direcrorio y el nombre es: %s" % str(path.split(path.realpath("archivo.txt"))[0]))

    tiempo = time.ctime(path.getmtime("archivo.txt"))
    #primer formato
    print(tiempo)

    #otro tipo de formato
    print(datetime.datetime.fromtimestamp(path.getmtime("archivo.txt")))

    #tiempo transcurrido desde la ultima modificacion
    tiempotranscurrido = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("archivo.txt"))
    print("han transcurrido %s desde su ultima modificacion. " % str(tiempotranscurrido))
    print("han transcurrido %s segundos desde su ultima modificacion. " % str(tiempotranscurrido.total_seconds()))

    pass


if __name__ == '__main__':
    main()