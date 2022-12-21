# La estructura de un loop for se escribe asi: for element in [list]
# Los datos iterables en Python son: Strings, Listas, Tuples
# El loop for puede almacenar dos variables que accederan a listas u objetos dentro de un objeto padre. Si nosotros imprimimos las dos variables accederá al objeto y luego al valor de dicho objeto

dic = {
   'clave1': 'a',
   'clave2': 'b',
   'clave3': 'c',
}

for a, b in dic.items():
   print(a, b)