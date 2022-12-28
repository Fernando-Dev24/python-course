# Para crear metodos, usamos igualmente la palabra clave def, seguido del nombre del metodo y siempre, de manera obligatoria, se le pasa el argumento self, que hace referencia a cada una de las instancias de esa clase u objeto.

# Es importante recalcar que los metodos no son mas que funciones. Igualmente si el metodo necesita mas argumentos, podemos declararlos luego del argumento obligatorio self

class Pajaro:
   # Atributes
   alas = True
   def __init__(self, color, especie):
      self.color = color
      self.especie = especie
   
   # Methods
   def piar(self):
      # Para incluir los valores de atributos dentro de los metodos, debemos de hacerlo con la palabra self.[nombre_atributo] su valor esta definido en los atributos por lo que no debemos de pasarle ningun valor cuando ejecutemos el metodo
      print(f'Pío, mi color es { self.color }')
   
   def volar(self, metros):
      print(f"El pajaro ha volado una cantidad de { metros } metros")

piolin = Pajaro('amarillo', 'canario')

# Para ejecutar metodos, accedemos al nombre del metodo y, en esta ocasion, si ponemos los parentesis
piolin.piar()
piolin.volar(50)