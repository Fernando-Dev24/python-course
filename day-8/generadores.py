# Son un tipo especial de funcion que en lugar de devolver un tipo terminado. Va produciendo ese valor segun lo vamos requeriendo

# Este tipo de funcion genera el valor que queremos, se queda esperando cuando necesitemos el siguiente, de esta forma no hacemos una carga masiva a la memoria del programa y podemos trabajar de la mano con la funcion.

# Para lograr este funcionamiento, sustituimos la palabra clave "return" por la palabra "yield", la cual quiere decir producir

# A diferencia de una funcion, este tipo de funcion genera un objeto para producir. Sin embargo no devuelve como tal el valor ya producido, si no que para hacerlo necesitamos hacer uso de una variable para guardar el valor o bien pasarlo por el metodo next([funcion_generadora]), esta funcion produce el nuevo valor

# La ejecucion del yield no detiene la ejecucion de una funcion

def mi_funcion():
   lista = []

   for x in range(1, 5):
      lista.append(x * 10)
   
   return lista

def mi_generador():
   for x in range(1, 5):
      yield x * 10

print(mi_funcion())
print(next(mi_generador()))