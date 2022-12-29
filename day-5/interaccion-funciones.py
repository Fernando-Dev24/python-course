""" from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']

# Mezclar palitos
def mezclar(lista):
   shuffle(lista)
   return lista

# Pedir usuario que eliga un numero del 1 - 4
def probar_suerte():
   intento = ''
   
   while( intento not in ['1', '2', '3', '4'] ): # Una forma de obligar al usuario a escribir un numero
      intento = input("Elige un numero del 1 - 4: ")
   
   return int(intento)

# Validar si fallo o acerto
def chequear_intento(lista, intento):
   if ( lista[intento - 1] == "-" ):
      print("A lavar los platos")
   else:
      print("Esta vez te has salvado")
   
   print(f"Te ha tocado { lista[intento - 1] }")


palitosMezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitosMezclados, seleccion) """

""" ------------------------------------------------------------------------------ """

""" from random import randint

# Programa genera dos valores aleatorios
def lanzar_dados():
   num1 = randint(1,6)
   num2 = randint(1,6)
   return [num1, num2]

# Evaluar tirada de dados segun la suma de estos valores
def evaluar_jugada(lista):
   suma_dados = 0
   for num in lista:
      suma_dados += num
   
   if ( suma_dados <= 6 ):
      print(f"La suma de tus dados es { suma_dados }. Lamentable")
   elif ( suma_dados >= 6 and suma_dados < 10 ):
      print(f"La suma de tus dados es { suma_dados }. Tienes buenas chances")
   elif ( suma_dados >= 10 ):
      print(f"La suma de tus dados es { suma_dados }. Parece una buena ganadora")

tirada_de_dados = lanzar_dados()
evaluar_jugada(tirada_de_dados) """

""" # Reducir lista si hay valores repetidos y eliminado el valor mas alto
lista_numeros = [1, 2, 15, 7, 2]

def reducir(lista):
   # Eliminar valor mayor de la lista
   lista.remove(max(lista))

   # Eliminar valores repetidos en la lista
   result = []
   for num in lista:
      if ( num not in result ):
         result.append(num)
   

   return result

# Calcular el promedio de la lista devuelta
def promedio (lista):
   promedio = 0
   for num in lista:
      promedio += num / len(lista)

   return promedio

lista_reducida = reducir(lista_numeros)
promedio(lista_reducida) """

from random import choice

# Elegir cara o cruz
opciones_moneda = ["Cara", "Cruz"]
lista_numeros = [10, 5, 8, 500]

def lanzar_moneda(opciones):
   seleccion_moneda= choice(opciones)
   return seleccion_moneda


# Probar suerte para ver si elimina el contenido de la lista o no
def probar_suerte(seleccion, lista):
   if ( seleccion == 'Cara' ):
      lista.clear()
      print(f"La lista se ha autodestruido: { lista }")
      return lista
   else:
      print(f"La lista se ha salvado: { lista }")
      return lista

seleccion_moneda = lanzar_moneda(opciones_moneda)
probar_suerte(seleccion_moneda, lista_numeros)