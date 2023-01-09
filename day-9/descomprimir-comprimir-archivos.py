# El modulo zipfile permite comprimir y descomprir archivos programaticamente, es decir con codigo. Esto en combinacion con shutil nos permite elevar nuestros conocimientos al siguiente nivel

import zipfile
import shutil

""" # Este modulo zipFile recibe dos argumentos:
# 1. El nombre de la carpeta que contendra nuestro archivo compreso
# 2. El modo de apertura del documento

# Con el metodo write se puede agregar nuevos valores al archivo zip que se creo.

mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

# Importante es no olvidarse de cerrar el documento
mi_zip.close() """

""" # Descomprimir archivos
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall() # Extrae todos los archivos
zip_abierto.close() """

""" # Comprimir archivos usando shutil
carpeta_origen = "C:\\Users\\Informática\\Desktop\\Carpeta"
archivo_destino = "Todo_Comprimido"

# El metodo shutil.make_archive recibe tres argumentos: (archivo_destino, 'format', 'origin')
shutil.make_archive(archivo_destino, 'zip', carpeta_origen) """

# Descomprimir archivos usando shutil
# Para eso usamos el metodo shutil.unpack_archive([filename], [folder_name], [format])
shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion Terminada', 'zip')