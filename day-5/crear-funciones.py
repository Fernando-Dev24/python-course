# La sintaxis de las funciones son las siguientes:
# def [nombre_funcion]([parametros]):
# Se recomienda siempre documentar la funcion antes de realizar el codigo a ejecutar en la funcion
# Para ejecutar la funcion solamente debemos escribir el nombre de la funcion y los parentesis donde podemos pasar parametros

def saludar_persona(nombre):
   '''
      Esta funcion sirve para saludar a las personas que se pasen como parametro o no, segun se necesite
   '''
   print(f"Hola { nombre }")

saludar_persona("Eli <3")