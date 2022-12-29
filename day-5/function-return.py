""" def multiplicar(num1, num2):
   total = num1 * num2
   return total

result = multiplicar(10, 50)

print(result) """

def invertir_palabra(palabra):
   palabra_reverso = palabra[::-1].upper() # Primera manera de dar vuelta a una palabra usando indices de strings - IMPORTANTE
   return palabra_reverso

invertir_palabra('python')