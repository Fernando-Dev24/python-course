# Hay metodos de lectura para los metodos de abrir un archivo:
# r = Metodo de solo lectura (read), este metodo NO permite modificar el contenido del archivo abierto
# w = Metodo de solo escritura (escritura), si el archivo existe se resetea, si no existe, lo crea
# a = Metodo de solo escritura posicionandose al final del archivo, en caso que no existe el archivo lo crea. En caso existe, Python se posiciona al final del archivo

# writelines = Este metodo pasa una linea de strings para escribirlas en el archivo, este metodo no escribe lineas, solo concatena los strings
archivo = open('prueba.txt', 'a')

archivo.write("Bienvenido") # Este modo de escritura es importante ya que permite llevar un log de un programa por ejemplo. Este modo, no resetea el archivo, solamente se posiciona al final y escribe desde ese punto

# Cerrar archivo
archivo.close()