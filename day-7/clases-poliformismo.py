# El poliformismo es la capacidad que tiene Python de que varias instancias de un objeto puedan tener varias llamadas a un metodo, o incluso compartir ese nombre

# Este nos permite que los loops, las funciones y los bloques de codigo saben que metodo ejecutar, no importando que el nombre sea igual al de una clase que otra.

class Vaca:
   def __init__(self, nombre):
      self.nombre = nombre
   
   def hablar(self):
      print(f"La vaca { self.nombre } dice Mu")
   
class Oveja:
   def __init__(self, nombre):
      self.nombre = nombre
   
   def hablar(self):
      print(f"La oveja { self.nombre } dice beee")

mi_vaca = Vaca('Eli')
mi_oveja = Oveja('Nube')

def animal_habla(animal):
   animal.hablar()

animal_habla(mi_vaca)
animal_habla(mi_oveja)