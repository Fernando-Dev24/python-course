# Los decoradores son funciones que modifican el funcionamiento de otras funciones y ayudan a acortar nuestro codigo.

# Por ejemplo, si tuviera la funcion llamada mayuscula que se encargara de retornar el string en mayusculas. Si quisiera que la funcion me salude al iniciar o terminar nuestra funcion basta con crear un decorador que active o desactive ese saludo en caso se requiera o no.

# Debido a que en Python, todo es un objeto podemos almacenar funciones a variables y acceder a ellas mediante el nombre de la variable que la contiene.

# En Python, podemos pasar funciones como argumentos de otra funcion diferente. De igual manera se puede retornar dicha funcion que se envie como argumento y a la vez guardarla como variable.

# Puedo definir funciones nuevas dentro de una funcion que las contenga.

# Crear decoradores siguiendo el ejemplo de los saludos antes y despues de una funcion.
# 1. Lo primero es crear la funcion que contendra a otra funcion y lo demas que queramos hacer. Se le envia como argumento una funcion.

# 2. Definimos adentro de la funcion padre, otra funcion que se encargara de modificar el texto que se le pase como parametro. Antes y despues se le imprime al usuario los textos "hola" y "adios". Debemos de tener en cuenta que la funcion que se pasa como argumento recibe la palabra como argumento y se ejecuta ahi mismo.

# 3. # Para encerrar una funcion dentro de un decorador basta con escribir @[nombre de la funcion decoradora]

def decorar_saludo(funcion):
   def otra_funcion(palabra):
      print("Hola")
      next(funcion(palabra))
      print("Adios")
   
   return otra_funcion


def generador(texto):
   yield texto

def minusculas(texto):
   print(texto.lower())

# Para tener las funciones con el decorador o no, solamente basta almacenar el resultado de la funcion decoradora en una variable y mandarle como argumente la funcion que queremos decorar
mayuscula_decorada = decorar_saludo(generador)
next(mayuscula_decorada('fer'))