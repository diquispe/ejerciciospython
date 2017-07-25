import os
from os import path


def main():

    if(path.exists("file.txt")):
        src = path.realpath("file.txt")

        #split devuelve: 1.- la ruta del archivo; 2.- el nombre del archivo; y se elmacenan respectivamente en cada variable que han sido separados por comas
        ruta, nombreArchivo = path.split(src)
        print("La ruta es: %s" % ruta)
        print("el nombre es %s" % nombreArchivo)

        os.rename("file.txt", "archivo.txt")

        nuevonombre = path.split(src)[1]

        print("El nuevo nombre del arvhico es: %s " % nuevonombre)

    pass

if __name__ == '__main__':
    main()