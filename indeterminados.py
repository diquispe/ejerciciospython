def cuentaatras(num):
    num -= 1
    if num>0:
        print(num)
        cuentaatras(num)
    else:
        print("Explota")

cuentaatras(6)
