# Decorative function to add to say the user the following info:
# 1. "Su turno es"
# 2. "Numero de turno"
# 3. "Aguarde y será atendido."

def numeros_perfumeria():
   for n in range(1, 10000):
      yield f"P - {n}"
      


def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"


def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorador(rubro):
   print("Su número es:")
   if rubro == "p":
      print(next(p))
   elif rubro == "f":
      print(next(f))
   else:
      print(next(c))
   print("Aguarde y será atendido \n")
   input("Presiona Enter para volver a mostrar el menu principal: ")