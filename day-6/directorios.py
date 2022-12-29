# Directorios en Python:
# Los directorios permiten acceder a archivos que estan fuera de nuestra carpeta de trabajo. Sin embargo para ello debemos de escribir toda la ruta donde se encuentran nuestro archivo.

# En Windows debemos de escribir la barra invertida dos veces para navegar dentro de directorios, para que no nos de error

# En Mac los separadores se escriben con la barra slash normal. Esto de los separadores se suele solucionar usando librerias como path y os

# Para importar os, solamente debemos de escribir import os, y ya tenemos acceso a todos los metodos
# import os

# El metodo getcwd() devuelve el directorio donde estamos trabajando (get current working directory)
# El metodo chdir() cambiar el directorio de trabajo (change directory)
# El metodo makedirs() permite crear una carpeta nueva usando un directorio ya existente

# Si nosotros accedemos a un archivo usando los metodos de os, podemos separar los dos elementos retornables, el directorio y el elemento, o archivo. Para eso usamos los metodos:
# ruta = "C:\\Users\\Fernando Ortiz\\Desktop\\courses\\python-course\\day-6\\prueba.txt"

# Con el metodo os.path.basename([ruta]) retornamos el nombre al que esta apuntando nuestra ruta.
# Con el metodo os.path.dirname([ruta]) retornamos el nombre del directorio que contiene al archivo apuntado.
# Con el metodo os.path.split([ruta]) retornamos el directorio y el nombre del archivo en una tupla, usamos el metodo
""" elemento = os.path.split(ruta)
print(elemento) """

# Con el metodo rmdir([ruta]) podemos eliminar el directorio. NOTA: Este metodo elimina directorios vacios
# os.rmdir("C:\\Users\\Fernando Ortiz\\Desktop\\courses\\python-course\\day-6\\directorios-docs\\otra")

# Abrir archivos desde otro directorio - Windows
""" otro_archivo = open("C:\\Users\\Fernando Ortiz\\Desktop\\courses\\python-course\\day-6\\prueba.txt")
print(otro_archivo.read())

otro_archivo.close() """

# Abrir archivos desde otro directorio sin importar el sistema operativo
from pathlib import Path # Path no es un modulo, es un Objeto

carpeta = Path("C:/Users/Fernando Ortiz/Desktop/courses/python-course/day-6")
archivo = carpeta / 'prueba.txt' # El slash (/) sirve como contenacion para ubicar el archivo. Otra forma es hacer la concatenacion directamente en la linea donde usamos Path, siempre usando el slash como concatenador

mi_archivo = open(archivo)
print(mi_archivo.read())

mi_archivo.close()