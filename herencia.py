class miClase():
    def metodo1(self):
        print("metodo 1")

    def metodo2(self, texto):
        print("el metodo 2 recib e una cadena : ", texto)

class clase2(miClase):
    def metodo2(self):
        print("Metodo 2 de la clase2")

def main():
    objeto = miClase()
    objeto.metodo1()
    objeto.metodo2(input("Ingrese un texto> "))

if __name__ == "__main__":
    main()
