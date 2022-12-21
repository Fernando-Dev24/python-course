""" list = [ letter for letter in 'python' ] # La compresion de listas nos ayuda a ahorrar menos codigo y decirle a Python que nos almacene valores directamente desde la lista y no acceder a metodos externos de listas. Esto anterior se lee: letter [variable interna] de letter [variable interna] in palabra [variable externa]

print(list) """

# Si la compresion de valores tiene un condicional if que no tiene la sentencia else, este if se pondra al final de mi sentencia, caso contrario, se pone al principio

pies = [10, 20, 30, 40, 50]

metros = [ p * 3.281 for p in pies ]

print(metros)