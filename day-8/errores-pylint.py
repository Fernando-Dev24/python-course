# Los archivos de prueba nos ayudan a asegurarnos que el codigo, en un equipo de trabajo, se sigue ejecutando correctamente. Ya que, debido al constante cambio que puede tener un proyecto, este podria arrojar algun error por algun cambio realizado. Para evitar estos errores inesperados sirven los archivos de prueba.

# Pylint es una biblioteca que analiza el codigo y arroja errores o advertencias sobre: Forma de escribir el codigo, o codigo no valido

# Unittest es una biblioteca integrada en Python para analizar el codigo y arrojar algunos errores o advertencias sobre la ejecucion del mismo.

# Para analizar el codigo debemos de ir al simbolo del sistema, o la terminal. Y realizar lo siguiente:
# 1. Navegar hasta el archivo que queremos analizar
# 2. Escribir el comando: pylint [archivo_a_analizar] -r (report) y (yes)

# Los errores que comienzan con C son aquellos errores de estilo.
# Los errores que comienzan con E si son aquellos que son errores de ejecucion


# Por convencion se espera que haya un comentario de bloque explicando que hara nuestro archivo
"""
   Este es un modulo que imprime algo
"""

# Ademas, se espera que nuestro codigo se ejecute en una funcion
def una_funcion():
   numero1 = 500
   print(numero1)


una_funcion()
