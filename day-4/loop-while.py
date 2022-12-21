# La estructura de un ciclo while es el siguiente:
# while [condicion]: sin embargo, este ciclo while puede tener una declaracion else que le indicara al codigo que debe de hacerse si la condicion no se cumple

# Ademas, hay tres palabras importantes en los loops: break, continue, y pass

""" monedas = 5

while ( monedas > 0 ):
   print(f"Tengo { monedas } monedas")
   monedas -= 1
else:
   print("No tengo mas monedas") # Las sentencias dentro del bloque else de un ciclo while se ejecutaran cuando la condicion del loop while no se cumpla, independientemente el loop haya terminado o no """

""" response = 's'

while ( response == 's' ):
   pass # La palabra pass guarda el espacio, es decir, salta la iteracion de un loop en caso no tengamos claro que debemos de hacer
   break # La palabra break, rompe el loop y pasa a las sentencias siguientes, en caso las haya
   continue # La palabra continue hara que nuestro loop siga la ejecucion del mismo sin interrumpir el flujo normal de un ciclo

print("Hola Mundo") """

numero = 50

while ( numero >= 0 ):
   if( numero % 5 == 0 ):
      print(numero)
   else:
      pass
   numero -= 1