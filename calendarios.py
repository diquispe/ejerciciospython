import calendar

calendario = calendar.TextCalendar(calendar.SUNDAY)

calendarioTexto = calendario.formatmonth(2013,10,0,0)

#muestra el calendario en formato de tabulaciones
print(calendarioTexto)
calendarioHTML = calendar.HTMLCalendar(calendar.MONDAY)

calendarHTML = calendarioHTML.formatmonth(2013,10)


#muestra el calnedario en formato html
print(calendarHTML)


#devuelve en una lista los dias de un mes de un año determnado en parametros
for i in calendario.itermonthdays(2013,10):
    print(i)


# imprime los nombres de los meses en ingles
for nombre in calendar.month_name:
    print(nombre)

#imprime los dias de la semana
for nombre in calendar.day_name:
    print(nombre)

#
for mes in range(1, 13):
    calendario = calendar.monthcalendar(2017, mes)
    semanauno = calendario[0]
    semanados = calendario[1]


    if semanauno[calendar.FRIDAY != 0]:
        partido = semanauno[calendar.FRIDAY]
    else:
        partido = semanados[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[mes], partido))
