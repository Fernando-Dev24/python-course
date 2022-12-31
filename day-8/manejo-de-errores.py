# El manejo de errores son uno de los pilares de una buena experiencia de usuario. Si bien no podemos controlar que el usuario siga la logica de la aplicacion al 100%, si podemos anticiparnos ante los errores mas comunes que el usuario puede llegar a cometer4

# Para manejar los errores, usamos las palabras try, except, y finally
# try = es la manera en que el codigo intent ejecutarse

# except = es la manera de que el codigo no se detenga en algun error, de esta forma Python no detendra la ejecucion y seguira con el flujo normal del codigo

# finally = No importa si hay error o no, tienes que ejecutar lo siguiente al final

def suma():
   n1 = int(input("Escribe el valor del num1: "))
   n2 = int(input("Escribe el valor del num2: "))
   print(n1 + n2)
   print("Gracias por sumar")


def pedir_numero():
   while ( True ):
      try:
         numero = int(input("Dame un numero: "))
      except:
         print("Ese no es un numero")
      else:
         print(f"Ingresaste el numero { numero }")
         break
   
   print("Gracias")

pedir_numero()

""" try:
   suma()
   # Codigo que queremos probar
except TypeError:
   # Codigo a ejecutar si HAY un error
   # Podemos hacer varios tipos de excepciones segun tipo de error
   print("Estas intentando concatenar tipos distintos...")
except ValueError:
   # Esta excepcion sucede cuando el valor de una variable no es el esperado
   print('Ese no es un numero')
else:
   # Codigo a ejecutar si NO hay un error
   print("Hiciste todo bien")
finally:
   # Codigo que se va a ejecutar de todos modos
   print("Eso fue todo por hoy amigos") """