from datetime import time
from datetime import date
from datetime import datetime

def  main():

    hoy = date.today()
    print("El dia es: ", hoy.day, " El mes: ", hoy.month, " El año es: ", hoy.year)

    print(" el numero del dia es ", hoy.weekday())

    hoy = datetime.today()

    print(hoy)

    hora = datetime.time(datetime.now())

    print(hora)


    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    numeroDia = date.weekday(hoy)
    print("El numero del dia es: ", numeroDia)
    print("El dia es: ", dias[numeroDia])



if __name__ == "__main__":

    main()