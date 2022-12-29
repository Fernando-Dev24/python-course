# *args puede usarse para recibir todos los parametros que sea posible en la funcion, si no sabemos cuantos va a recibir. Ademas, es iterable

def suma (*args):
   total = 0

   for arg in args:
      total += arg

   return total

print(suma(10, 50, 5))