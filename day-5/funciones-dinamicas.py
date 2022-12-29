""" suma = 586 + 45

def chequear_tres_cifras (num):
   return num in range(100, 1000) # Verificar si un numero contiene 3 cifras o no

resultado = chequear_tres_cifras(suma)

print(resultado) """

""" def chequear_tres_cifras (lista):
   valid_numbers = []

   for num in lista:
      if ( num in range(100, 1000) ):
         valid_numbers.append(num)
      else:
         pass
   
   return valid_numbers

resultado = chequear_tres_cifras([10, 999, 110])

print(resultado) """

lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]

def todos_positivos(lista_numeros):
   for num in lista_numeros:
      if ( num < 0 ):
         return False
      else:
         pass
      
   return True

print(todos_positivos(lista_numeros))