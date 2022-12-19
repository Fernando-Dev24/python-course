# Hay dos manera de crear un set:
# Manera 1: Llamar con la palabra reservada set() y encerrar los elementos en corchetes
# Manera 2: Usar llaves y crear los elementos separados por comas.

# NOTA: Los sets no contienen valores repetidos, por lo que Python elimina aquellos valores duplicados automaticamente. Ademas, no estan organizados en indices

# NOTA 2: Los sets son elementos inmutables, al igual que los tuples y los strings. LOS TUPLES NO ACEPTAN LISTAS Y DICCIONARIOS

s1 = { 1, 2, 3, 5, 6 }
s1.add(4) # Agrega un elemento al set al final
s1.remove(3) # Elimina el elemento que se ha declarado en parentesis, si no hay un elemento que no existe arroja error

s1.discard(6) # El metodo discard, descarta el elemento declarado en los parentesis, si se intenta descartar un elemento que no existe, este no arroja error

s1.pop() # El metodo pop en los sets elimina un numero aleatorio de los sets. Es de tener mucho CUIDADO

s1.clear() # Vacia la coleccion de datos

print(s1)