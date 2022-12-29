# La libreria Pathlib nos permite manipular archivos de una manera mas comoda y actualizada

from pathlib import Path, PureWindowsPath # Este modulo devuelve la ruta general en una ruta de Windows.

carpeta = Path("C:/Users/Fernando Ortiz/Desktop/courses/python-course/day-6/prueba.txt")

# Cuando usamos pathlib no tenemos ni que abrir ni cerrar nuestro archivo, diferente a como hemos aprendido a hacerlo antes

# Con el metodo PathObject.read_text() lee el archivo
# Con la funcion PathObject.name, sin parentesis, nos devuelve el nombre del archivo a que estamos apuntando con nuestra ruta
# Con la funcion suffix, nos devuelve la extension del archivo
# Con la funcion stem, nos devuelve el nombre del archivo sin extension
# Con el metodo PathObject.exists() retorna un valor booleano que nos indica si el archivo existe o no

ruta_windows = PureWindowsPath(carpeta) # Retorna la ruta especificada en una ruta Windows

if ( not carpeta.exists() ):
   print("Este archivo no existe")
else:
   print("Genial, si existe")