# random es una libreria de Python que hay que importar para utilizar sus metodos. Para importar librerias debemos de seguir la siguiente sintaxis: from [libreria] import [metodo]

# NOTA: Los archivos de Python que tienen importaciones no deben de tener los mismos nombres que las librerias puesto que eso genera una importacion circular

from random import *

colores = ['azul', 'rojo', 'verde']
numeros = list(range(5, 50, 5))

aleatorio = randint(1, 50) # Genera un numero entero aleatorio
aleatorio = round(uniform(1, 5), 1) # Genera un numero decimal aleatorio
aleatorio = round(random()) # Genera un numero decimal entre 0 y 1
aleatorio = choice(colores) # Elige un valor aleatorio de una coleccion de datos
shuffle(numeros) # NOTA: shuffle genera una mezcla dentro de una coleccion de datos, importante es saber que shuffle no retorna nada por lo que su valor no puede guardarse en una variable

print(numeros)