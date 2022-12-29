# La convencion kwargs nos permite no solo mandar parametros a la funciones, tanto como queramos, si no que tambien, mandar dichos argumentos o parametros con algun tipo de clave para lograr identificarlos. Los kwargs se almacenan como diccionarios

# Asi mismo podemos tener listas y diccionarios antes de ejecutar nuestra funcion y lograr que la funcion ejecute correctamente el codigo solicitado. Solamente que para lograr esto debemos pasar los argumentos con *args y **kwargs

def prueba(numero1, numero2, *args, **kwargs):
   print(f"El primer valor es { numero1 }")
   print(f"El segundo valor es { numero2 }")
   
   for arg in args:
      print(f"arg es igual a { arg }")

   for clave, valor in kwargs.items():
      print(f"{ clave } es igual a { valor }")

print(prueba(15, 50, 100, 50, 78, 85, x = "8", y = "9", z = "Buenas"))