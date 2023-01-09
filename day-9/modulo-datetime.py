# El modulo datetime nos permite almacenas hora y fecha dentro de variables, calcular el tiempo, mostrarlo en diferentes formatos, entre muchas otras cosas

from datetime import *

# El objeto datetime se define en estas partes: datetime es fecha y hora, date es fecha, y time es hora
# La horas se miden en un formato de 24 horas
# El objeto date recibe valores de year-month-day
# Con el metodo ctime de una fecha podemos obtener el dia y la hora de la fecha proporcionada
# El metodo today obtiene la fecha actual
""" mi_date = datetime.date(2025, 12, 18)
print(mi_date.today()) """

""" mi_fecha = datetime(2025, 12, 18, 20, 15, 10, 2500)
# Con el metodo replace podemos cambiar los valores que queramos de mi objeto de fecha
mi_fecha = mi_fecha.replace(month = 11) """

# Calcular tiempo con el objeto datetime
# Para hacer el calculo primero debemos de almacenar el punto inicial en el tiempo, luego el punto final y hacerlo como una resta normal
""" nacimiento = date(1995, 3, 5)
fallecimiento = date(2095, 6, 19)

vida = fallecimiento - nacimiento
print(vida.days) """

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta
print(despierta.today().minute)