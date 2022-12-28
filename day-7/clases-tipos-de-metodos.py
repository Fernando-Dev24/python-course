# Las clases tienen algo que se llama "decoradores" que nos permiten crear distintos tipos de metodos, estos son:

# 1. Metodos de instancia = Son los metodos que hemos estado trabajando todo este tiempo. Estos metodos permiten: Acceder y modificar atributos del objeto, acceder a otros metodos, modificar el estado de la clase

# 2. Metodos de clase = Para este tipo de metodos se usa la palabra @classmethod. Estos metodos no usan el argumento "self", si no que el argumento es "cls" que significa "class". Estan asociados a la clase en si misma, por lo que pueden ser llamados desde una instancia o desde la clase directamente. Estos metodos no pueden acceder a los atributos de instancia, pero si a los atributos de clase.

# 3. Metodos estaticos = Para este tipo de metodos se usa el decorador @staticmethod. Estos metodos no reciben argumentos, ni "self", ni "cls", por lo mismo no pueden modificar el estado de la clase, ni de la instancia. Estos tipos de metodos pueden ser usados como una funcion normal, pero con el conocimiento que estan ligados a la clase

class Pajaro:
   # Atributes
   alas = True
   def __init__(self, color, especie):
      self.color = color
      self.especie = especie
   
   # Methods
   def piar(self):
      print("pio")

   def volar(self, metros):
      print(f"El pajaro ha volado { metros } metros")
      # Para invocar a otros metodos siempre debemos de acceder al valor de self, que hace referencia a la clase
      self.piar()

   def pintar_negro(self):
      self.color = 'negro'
      print(f"Ahora el pajaro es { self.color }")

   # @classmethod
   @classmethod # El decorador se pone por encima de los metodos, de esta forma sirve de separados para Python 
   def poner_huevos(cls, cantidad):
      print(f"Puso { cantidad } huevos")
      cls.alas = False
   
   # staticmethod
   @staticmethod
   def mirar(): # los metodos estaticos no reciben ningun argumento que haga referencia a la clase, no acceden a los atributos de la clase, de instancia, ni a los metodos de la clase
      print("El pajaro mira")
      

Pajaro.poner_huevos(10) # los @classmethod se pueden llamar sin necesidad de crear una nueva instancia, sin embargo, no pueden acceder a los atributos de instancia, solamente a los atributos de clase y metodos de la clase

Pajaro.mirar()

print(Pajaro.alas)