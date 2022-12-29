user_number = int(input("Digite un numero para marcar el final del loop: "))

def contar_primos(end_number):
   total_primos = [2]
   iteracion = 3

   if ( end_number < 2 ):
      return 0

   while ( iteracion <= end_number ):
      for n in range(3, iteracion, 2):
         if( iteracion % n == 0 ):
            iteracion += 2
            break
      else:
         total_primos.append(iteracion)
         iteracion += 2
   
   print(total_primos)
   return len(total_primos)


print(contar_primos(user_number))