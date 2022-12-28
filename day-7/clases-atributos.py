# Existen dos tipos de atributos:
# Atributos de clase: Estos atributos son permanentes y todas las instancias tendran por defecto estos atributos
# Atributos de Instancia: Estos atributos particulares que son distintos entre cada instancia de la clase

# Para definir atributos de instancia primeramente debemos de escribir la palabra clave def seguido de __init__(self, [nombres_atributos])
# Para darle valor a esos atributos debemos de escribir primeramente self.[nombre_atributo] = valor_aotributo. self es bligatorio, y hace referencia al objeto que se esta creando
# __init__ es el constructor de la clase, es decir la herramienta que construira los atributos que tendra nuestra clase

# Para definir atributos de clase solamente ponemos el nombre del atributo = valor del atributo, tal como si fuera una variable
class Pajaro:
   alas = True
   def __init__(self, color, especie):
      self.color = color
      self.especie = especie

# Para pasar el valor del atributo lo hacemos como pasariamos argumentos a una funcion
mi_pajaro = Pajaro('negro', 'Tucan')

# Para acceder a los atributos de los objetos accedemos a el nombre de atributo que le proporcionamos. Sin parentesis debido a que no es un metodo del objeto, solamente un atributo
# print(mi_pajaro.color, mi_pajaro.especie)

print(f"Mi pajaro es un { mi_pajaro.especie } y es de color { mi_pajaro.color }")

# Para acceder a los atributos de clase no necesariamente debemos de hacer una instancia del objeto, esta disponible llamando a la clase, o a la instancia de la clase y ambos valores tendran acceso al atributo de clase 
# print(Pajaro.alas)
# print(mi_pajaro.alas)