from datetime import date

hoy = date.today()

fecha = date(year=int(hoy.year), month=int(input("ingrese un mes: ")), day=int(input("ingrese un dia: ")))


if fecha<hoy:
    print("La fecha paso hace dias: ", (hoy - fecha).days)
