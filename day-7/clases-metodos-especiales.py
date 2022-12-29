# Estos metodos especiales nos permiten obtener informacion o realizar procesos que no se pueden lograr con un metodo normal. Algunos ejemplos son el metodo __init__, __mro__ entre otros. Se caracterizan por tener doble guion bajo al principio y al final del nombre

class CD:
   def __init__(self, autor, titulo, canciones):
      self.autor = autor
      self.titulo = titulo
      self.canciones = canciones

   # El metodo especial __str__ es cambiar la forma en que se muestran en consola el contenido de la clase
   def __str__(self):
      return f"Album: { self.titulo } de { self.autor }"

   def __len__(self):
      return self.canciones

   def __del__(self):
      print("Se ha eliminado el CD")

mi_CD = CD('Pink Floyd', 'The Wall', 24)

# El metodo del elimina alguna instancia de un Objeto
del mi_CD