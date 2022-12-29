# El objeto Path nos permite:
# 1. Crear o mover archivos
# 2. Ennumerar archivos
# 3. Crear rutas basadas en strings

# Una ruta relativa es aquella que puede existir en nuestra computadora y que no tenemos acceso a la ruta especifica, sin embargo Path se encarga de buscarlo en nuestro ordenador.

# Una ruta absoluta es aquella que si se desglosa la ubicacion exacta de un archivo

from pathlib import Path

# Path puede concatenar series de strings como una ruta segun el sistema operativo instalado, ademas, puede contener instancias antes creadas de Path como instancias creadas durante la misma linea de codigo de Path
""" base = Path.home() # Genera la ubicacion raiz de nuestra computadora
guia = Path(base, 'Europa', 'España', Path("Barcelona", "Sagrada Familia.txt")) """

# Este metodo nos permite tener dos referencias a dos archivos completamente diferentes que se encuentran en un directorio en comun
# guia2 = guia.with_name("La Pedrera.txt")

# El metodo PathObject.parent nos permite obtener el directorio padre de una ruta de archivos. Podemos usarlo cuantas veces queramos para obtener porciones de ruta cada vez mas alto

# Ennumerar archivos dentro de un directorio
""" guia = Path(Path.home(), "Desktop/courses/python-course", "day-6", "Europa") """

# Si iteramos cada uno de los archivos txt que se encuentran en el directorio obtendremos la ruta absoluta de cada uno de los archivos.
# **/* significa ennumerar todos los archivos con extension .txt dentro de la carpeta raiz como de subcarpetas
""" for txt in Path(guia).glob("**/*.txt"):
   print(txt) """

# Tambien podemos acceder a rutas de subcarpetas especificas que existen en un directorio, es decir que inicie la busqueda de archivos o carpetas desde un punto en especifico
guia = Path(Path.home(), "Desktop/courses/python-course", "day-6", "Europa")

day_1 = guia.relative_to(Path("day-"))

print(day_1)