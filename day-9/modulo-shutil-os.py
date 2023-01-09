import os
import shutil
import send2trash

# Mover archivos de un directorio a otro = Para ello tenemos que importar el modulo shutil y acceder al metodo move, este metodo recibe el archivo que vamos a mover como primer parametro y el path de destino al que queremos mover dicho archivo
# shutil.move('curso.txt', "C:\\users\\Informática\\Desktop") # IMPORTANTE, este metodo solo mueve archivos que esten dentro del directorio actual

# Eliminar un archivo - metodo os
# El metodo os.unlink elimina un archivo segun la ruta especificada
# El metodo os.rmdir elimina una carpeta vacia segun la ruta
# El metodo shutil.rmtree elimina una carpeta con todos los archivos que tenga dentro y de forma permanente

# Una de las mejores opciones para eliminar archivos es con el modulo de terceros "send2trash" que necesita ser instalado e importado en nuestro proyecto
""" send2trash.send2trash('curso.txt') """ # Este metodo elimina un archivo del directorio actual y lo manda a la papelera de reciclaje

# Como recorrer todos los archivos segun la ruta especificada = El metodo walk
route = os.getcwd()

# El metodo walk primero almacena la ruta actual, luego almacena las subcarpetas y por ultimo los archivos que hayan ahi, por lo que crea tres diferentes tipos de tuplas entre archivos y carpetas
# Ademas nos permite crear condiciones para mostrar archivos solo que cumplen con determinada condicion
for carpeta, subcarpeta, archivo in os.walk(route):
   print(f"En la carpeta: { carpeta }")
   print(f"Las subcarpetas son:")
   for sub in subcarpeta:
      print(f"\t{ sub }")
   print(f"Los archivos son")
   for arch in archivo:
      print(f"\t{ arch }")
   print("\n")