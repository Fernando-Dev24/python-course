# Los tuples ocupan menos espacio de memoria, se procesan mas rapido en Python
# Los tuples no se pueden modificar
# Los tuples van indexados como las listas y los strings

## x, y, z = t # Al tener los mismos elementos que variables, estos tomando el valor de dicha posicion del tuple. Asi como una desestructuracion en Javascript. NOTA: Esto solamente funciona cuando hay la misma cantidad de valores que de valores en el tuple.

t = (1, 2, 3, 1)

print(t.count(1)) # El metodo count permite contar la cantidad de apariciones de un valor dentro del tuple
print(t.index(2)) # El metodo index permite retornar el indice de un valor especifico dentro del tuple