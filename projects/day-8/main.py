import generador_decorador
from os import system

# Show menu function
def show_menu(user_selection):
   system('cls')
   print("¡Bienvenido! Por favor, selecciona el servicio que quieres usar para tomar tu turno \n")
   print("P. Perfumería")
   print("F. Farmaceutica")
   print("C. Cosmetica")
   print("S. Salir \n")
   user_selection = input("Escribe la letra del servicio que deseas usar para asignarte un turno: ").lower()

   while ( user_selection not in ['p', 'f', 'c', 's'] ):
      user_selection = input("Escribe la letra del servicio que deseas usar para asignarte un turno: ").lower()
   
   return user_selection

user_selection = show_menu(None)

while ( user_selection != 's' ):
   system('cls')
   match ( user_selection ):
      case 'p':
         print("Ha escogido P. Perfumeria")
         generador_decorador.decorador(user_selection)
         user_selection = show_menu(user_selection)
      case 'f':
         print("Ha escogido F. Farmaceutica")
         generador_decorador.decorador(user_selection)
         user_selection = show_menu(user_selection)
      case 'c':
         print("Ha escogido C. Cosmeticos")
         generador_decorador.decorador(user_selection)
         user_selection = show_menu(user_selection)
else:
   print("\n¡Nos vemos luego!")