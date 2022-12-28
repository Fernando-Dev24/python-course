# La clase que recibe la herencia puede tener sus metodos heredados, metodos modificados, y metodos completamente nuevos

# La herencia multiple puede recibir herencia de varias clases a la vez y de igual forma esta clase puede mandar herencia a otras que sean creadas a partir de esta clase

""" class Animal:
   # Atributes
   def __init__(self, edad, color):
      self.edad = edad
      self.color = color

   def nacer(self):
      print("Este animal ha nacido")

   def hablar(self):
      print("Este animal emite un sonido")

class Pajaro(Animal):
   # Atributos nuevos
   # Metodo 1:
   def __init__(self, edad, color, altura_vuelo):
      # self.edad = edad
      # self.color = color
      # El segundo metodo 2 nos permite evitar escribir codigo nuevamente y con la ayuda de la palabra super() y su metodo __init__([atributos de clase que envia la herencia]) ya tendriamos los atributos que tiene la clase original.
      super().__init__(edad, color)
      self.altura_vuelo = altura_vuelo

   def hablar(self): # Cuando una clase crea un metodo con el mismo nombre que un metodo que recibio de herencia. Este metodo se sobrescribe y se ejecuta la ultima modificacion del metodo que se codifico
      print("Pio")
   
   def volar(self, metros):
      print(f"El pajaro vuela { metros } metros")

piolin = Pajaro(3, 'amarillo', 60)
piolin.hablar()
piolin.volar(100)

# La clase original siempre solicitara los atributos que fueron declarados la primera vez. Sin importar que otra clase haya agregado algun nuevo atributo
mi_animal = Animal(5, 'negro') """

# Herencia Multiple
class Padre:
   def hablar(self):
      print("Hola")

class Madre:
   def reir(self):
      print("JAJAJA")

   def hablar(self):
      print("Que tal?")

class Hijo(Padre, Madre):
   pass

class Nieto(Hijo):
   pass

mi_nieto = Nieto()

# En este caso el metodo que se ejecuta con el nombre hablar es el metodo que heredo de Padre ya que fue la primera herencia que tuvo. Si en lugar de Padre, hubiera heredado de Madre, entonces el metodo hubiera retornado el texto: "Que tal?"

# Para saber como Python va a buscando el metodo heredado, podemos acceder a la propiedad class.__mro__
print(Nieto.__mro__)