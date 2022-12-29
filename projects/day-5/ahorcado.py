from random import choice

palabras = ['panadero', 'dinosaurio', 'computadora', 'mouse', 'elizabeth']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
   palabras_elegida = choice(lista_palabras)
   letras_unicas = len(set(palabras_elegida))

   return palabras_elegida, letras_unicas

def pedir_letra():
   letra_elegida = ''
   es_valida = False
   abecedario = 'abcdefghijklmnopqrstuvwzyz'

   while ( not es_valida ):
      letra_elegida = input("Elige una letra: ").lower()
      if ( letra_elegida in abecedario and len(letra_elegida) == 1 ):
         es_valida = True
      else:
         print("No has elegido una letra correcta")
   
   return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
   lista_oculta = []

   for letra in palabra_elegida:
      if ( letra in letras_correctas ):
         lista_oculta.append(letra)
      else:
         lista_oculta.append("-")

   print(" ".join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
   fin = False

   if ( letra_elegida in palabra_oculta ):
      letras_correctas.append(letra_elegida)
      coincidencias += 1
   else:
      letras_incorrectas.append(letra_elegida)
      vidas -= 1

   if ( vidas == 0 ):
      fin = perder()
   elif ( coincidencias == letras_unicas ):
      fin = ganar(palabra_oculta)
   
   return vidas, fin, coincidencias

def perder():
   print("Te has quedado sin vidas")
   print(f"La palabra oculta era: { palabra }")

   return True

def ganar(palabra_oculta):
   mostrar_nuevo_tablero(palabra_oculta)
   print("Felicidades, has encontrado la palabra!")

   return True


palabra, letras_unicas = elegir_palabra(palabras)

while ( not juego_terminado ):
   print("\n * " * 20 + '\n')
   mostrar_nuevo_tablero(palabra)
   print("\n * " * 20 + '\n')
   print(f"Letras incorrectas { '-'.join(letras_incorrectas) } ")
   print(f"Vidas: { intentos }")
   print("\n * " * 20 + '\n')
   letra = pedir_letra()

   intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
   juego_terminado = terminado