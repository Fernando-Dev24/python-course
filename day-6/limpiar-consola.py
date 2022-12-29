# Limpiar la consola de las ejecuciones es una cosa importante mientras no tengamos una interfaz grafica donde trabajar. Para eso debemos de modificar configuraciones especificas del IDE que estemos usando.

# En PyCharm: se realiza de la siguiente manera: debugg > edit confi > execution: emulate terminal in output console

from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

# Declarar el lugar donde queremos que se limpie la consola
system('cls')

print(f"Tu nombre es { nombre }, y tienes { edad } años")