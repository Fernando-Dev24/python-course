"""
   Abrir y manipular archivos en Python se le conoce como E / S, lo cual significa: Entrada / Salida.
   En Ingles es conocido como: I / O = Input / Output

   El metodo rstrip() elimina los saltos de linea o los caracteres especiales que se le pasen como parametros
   Python, cuando lee un archivo lo hace hasta cierto punto con el metodo readline(), si nosotros sobreescribimos dicha variable, Python continuara desde el punto donde lo dejo

   Hay que tener cuidado con el metodo readline o readlines debido que estos metodos vuelven a cargr el archivo y puede que nos quedemos sin espacio
"""

# Abrir un archivo que ya existe
mi_archivo = open('prueba.txt') # Se escribe el nombre del archivo entre comillas
# print(mi_archivo.read()) # Para mostrar en pantalla lo que tiene mi archivo debemos de acceder al metodo read.

# Metodo readline() = Devuelve la primera linea del archivo abierto

# Iterar de acuerdo al archivo
#for linea in mi_archivo:
    #print(linea)

todas = mi_archivo.readlines()
print(todas)

# BUENA PRACTICA: Siempre que se trabaje con archivos, debemos de cerrar el archivo al final para eliminar ese gasto en memoria de la computadora
mi_archivo.close()