from random import randint

# Game variables
name = input("Digita tu nombre ")
lifes_available = 8

# Select a random number between 1 to 100
secret_number = randint(1,100)

# Output to init the game
print(f"Bienvenido { name }, he pensado un número entre 1 al 100 y tienes solamente 8 intentos para adivinar el numero")

# Ask user to enter a number to try guess the secret number
user_number = int(input("Digita un numero entre el 1 - 10 "))

# While loop to init the game
while ( user_number != secret_number ):
   if ( user_number < 1 and user_number > 100 ):
      print("\n")
      print("Has elegido un numero que no está permitido")
   elif ( user_number < secret_number and lifes_available > 0 ):
      lifes_available = lifes_available - 1
      print("\n")
      print("Respuesta incorrecta, has elegido un número menor al número secreto")
      print("\n")
      user_number = int(input(f"Te quedan { lifes_available } vidas, vuelve a intentarlo "))
   elif ( user_number > secret_number and lifes_available > 0 ):
      lifes_available = lifes_available - 1
      print("\n")
      print("Respuesta incorrecta, has elegido un número mayor al número secreto")
      print("\n")
      user_number = int(input(f"Te quedan { lifes_available } vidas, vuelve a intentarlo "))
   elif ( user_number != secret_number and lifes_available == 0 ):
      print("\n")
      print(f"Te has quedado con { lifes_available } intentos, lo siento :(")
      break

if ( user_number == secret_number ):
   print("\n")
   print(f"Has adivinado el número secreto, intento realizados: { 8 - lifes_available }")
