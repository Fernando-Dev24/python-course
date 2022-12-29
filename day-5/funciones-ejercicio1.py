def devolver_distintos(lista_numeros):
   total = 0

   for num in lista_numeros:
      total += num
   
   # Conditionals
   if ( total > 15 ):
      print(f"El numero mayor es { max(lista_numeros) }")
      return max(lista_numeros)
   elif ( total < 10 ):
      print(f"El numero menor es { min(lista_numeros) }")
      return min(lista_numeros)
   else:
      lista_numeros.sort()
      print(f"El numero intermedio es { lista_numeros[1] }")
   
      
devolver_distintos([10, 1, 2])