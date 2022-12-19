# En Python podemos extraer substrings de una cadena de texto. Para esto no usamos un metodo en especifico, mas bien jugamos con el indice de la cadena de texto. La estructura es:

"""
   1. miTexto[5:10] = Esto quiere decir que el string que este guardado en miTexto se va a cortar desde el indice 5 hasta el 9, esto debido a que, no cuenta el ultimo indice proporcionado.
   
   2. miTexto[5:10:6] = Si le agregamos un tercer valor, el numero que proporcionemos servira de intervalo, es decir, cada cuantos strings, mi palabra sera cortada

   NOTA: Si el developer no agrega el indice final, Python interpreta como el indice inicial hasta el final de la cadena de texto, y viceversa, es decir si el dev no pone el indice inicial

   Si en el tercer valor el dev pone un numero negativo, esto querra decir que lo hara desde derecha a izquierda, saltando el numero de indice especificados.
"""

text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
fragment = text[::-1]

print(fragment)