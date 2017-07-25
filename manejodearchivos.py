def main():
    # abrira un archivo y si no existe se creara
    #archivo = open("archivo.txt", "w+")

    # el a+ agrega la informacion despues del final de la ultima linea
    #archivo = open("archivo.txt", "a+")

    """for i in range(10):
        archivo.write("Esta es la linea %d\n" % (i + 0))

    #despues de trabajar en el archivo lo cerrramos con este metodo en archivo
    archivo.close()
    """


    # leyendo la informacion de un archivo
    archivo = open("archivo.txt", "r")


    # si el archivo se puede leer entonces usa el metodo readLines
    # mediante el ciclo for se lee linea por linea
    if archivo.mode == "r":
        lineasArchivo = archivo.readlines()

        for linea in lineasArchivo:
            print(linea)
    archivo.close()
    pass

if __name__ == "__main__":
    main()