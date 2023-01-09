# Como se menciono al inicio del curso algunos tipos de datos nos permiten coleccionar o almacenar una gran cantidad de datos. El modulo collections nos ayuda a mejorar la forma de usar estos tipos de datos
# Vamos a saber usas las siguientes herramientas: counter, defaultdict, namedtuple

from collections import Counter, defaultdict, namedtuple

frase = "Al pan pan, y al vino vino"

# Counter = Al pasar como argumento la lista que de numeros o datos al Objeto Counter, este se encargara de contar cuantas veces aparece cada numero en la lista
# Para contar palabras de una frase combinamos el string con el metodo split()
""" serie = Counter([1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,4])
print(list(serie))
print(Counter(frase.split())) """

# defaultdict = Esto sirve para que al momento de que el diccionario no encuentre una clave se le aplique el valor que especificamos en la clave "lambda"
""" mi_dict = defaultdict(lambda: 'nada')

mi_dict['uno'] = 'verde'
print(mi_dict['dos'])
print(mi_dict) """

# namedtuple = Este nuevo metodo nos permite darle nombre a los datos que vamos a guardar en una tupla. Esto sigue la siguiente sintaxis = namedtuple([nombre_de_tuple], [[valor1], [valor2], ...])
# Una vez creada la tupla podemos acceder a sus valores de acuerdo al nombre que le dimos o por su indice, como se harias normalmente
""" Persona = namedtuple("Persona", ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

print(ariel.altura) """

import collections

lista_ciudades = collections.deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.appendleft("San Salvador")