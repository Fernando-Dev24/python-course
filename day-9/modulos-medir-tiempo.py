# Los dos modulos para evaluar el tiempo de ejecucion en Python son:
# time = permite colocar marcas de tiempo en la ejecucion del codigo
# timeit = Su principal objetivo es medir el tiempo de ejecucion del codigo

import timeit

def prueba_for(numero):
   lista = []
   for num in range(1, numero + 1):
      lista.append(num)
   
   return lista

def prueba_while(numero):
   lista = []
   contador = 1
   while ( contador <= numero ):
      lista.append(contador)
      contador += 1
   
   return lista

""" start = time.time() # Genera una marca de tiempo
prueba_for(100000)
end = time.time() # Genera una marca de tiempo

print(end - start)

start = time.time() # Genera una marca de tiempo
prueba_while(100000)
end = time.time() # Genera una marca de tiempo

print(end - start) """

statement = '''
prueba_for(10)
'''

setup = '''
def prueba_for(numero):
   lista = []
   for num in range(1, numero + 1):
      lista.append(num)
   
   return lista
'''

duracion = timeit.timeit(statement, setup, number = 1000000)
print(duracion)

statement1 = '''
prueba_while(10)
'''

setup1 = '''
def prueba_while(numero):
   lista = []
   contador = 1
   while ( contador <= numero ):
      lista.append(contador)
      contador += 1
   
   return lista
'''

duracion1 = timeit.timeit(statement1, setup1, number = 1000000)
print(duracion1)