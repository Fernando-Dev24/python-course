# La herencia permite crear una clase hija, que herede de una clase padre sus atributos y herencias. Ademas, la clase hija puede sobreescribir los atributos heredados, y definir atributos nuevos

# La herencia puede servirnos para ahorrarnos codigo e inicializar una nueva clase que se parezca a la clase original

class Animal:
   # Atributes
   def __init__(self, edad, color):
      self.edad = edad
      self.color = color

   def nacer(self):
      print("Este animal ha nacido")

class Pajaro(Animal):
   pass

piolin = Pajaro(2, 'amarillo')
print(piolin.color)

# El atributo __bases__ nos ayuda a identificar si una clase esta recibiendo herencia de otra
# El atributo __subclasses__ nos ayuda a saber si una clase esta hererando sus atributos y propiedades
# print(Animal.__subclasses__)