from random import *
from os import system

# Person object that have only two attributes: name and last name
class Person:
   # Attributes
   def __init__(self, name, last_name):
      self.name = name
      self.last_name = last_name

# Costumer class that will inherit the Person class and will have the following requirements:
# 1. Name and last name values that will inherit from Person class
# 2. Create a account number, and balance, which is the full amount of money the user has
# 3. Print method to show all values or attributes
# 4. Account income or transference to create a income to balance value
# 5. Account outcome to get out money from account balance value

class Costumer(Person):
   # Attributes:
   def __init__(self, name, last_name, account_number, balance):
      super().__init__(name, last_name) # Write just the inherited attributes from Person class.
      self.account_number = account_number
      self.balance = int(balance)

   # Income method
   def new_income(self, amount):
      self.balance = self.balance + round(int(amount), 2)
   
   # Outcome method
   def new_outcome(self, amount):
      self.balance = self.balance - round(int(amount), 2)
   
   # Special Method
   def __str__(self):
      system('cls')
      return f"Propietario: { self.name } { self.last_name }\nN° cuenta: { self.account_number }\nEstado de cuenta: ${ self.balance }"

# Create user function: This function will create the user bank account, using the following info:
# 1. Request user's name and last name
# 2. Create a random number configured by 10 digits
# 3. Create a new Costumer instance using the info and return it, it is important to know that balance value will be $0 at the beginning.

def create_user():
   # First, we need to request user's name and last name
   print("¡Bienvenid@!")
   name = input("Para comenzar, ingresa tus nombres: ")
   last_name = input("Por favor, ingresa tus apellidos: ")

   # Second, we need to create a number formed by 10 digits using random built-in library
   random_numbers = []
   while ( len(random_numbers) < 10 ):
      number = randint(1, 9)
      random_numbers.append(str(number))
   
   account_number = "".join(random_numbers)

   # Finally, we need to create a new instance from Costumer class
   new_user = Costumer(name, last_name, account_number, round(0, 2))
   print("Nuevo usuario creado correctamente \n")
   print(new_user)
   print("\n")
   input("Presiona Enter para continuar: ")
   return new_user

# Function to show menu that have the following options
# 1. Create a new income
# 2. Create a new outcome
# 3. Exit

def show_menu(user_option):
   system('cls')
   print("Por favor selecciona una de las siguientes opciones: \n")
   print("1. Depositar dinero")
   print("2. Retirar dinero")
   print("3. Salir \n")

   user_option = input("Escribe el numero de la opcion que desees por favor: ")

   while ( user_option not in ['1', '2', '3'] ):
      user_option = input("Has escrito una opcion invalida, vuelve a intentarlo: ")
   
   return user_option

# Function to request income amount, but first, function will do the validations to check if amount is a valid value or not
def create_income(new_user):
   # Request income amount
   amount = input("Ingresa la cantidad que deseas depositar a tu cuenta: ")

   while ( amount.isnumeric() == False ):
      amount = input("Parece que has ingresado un dato invalido, vuelve a intentarlo: ")

   # Now, execute new_income() method on Costumer class
   new_user.new_income(int(amount))

   # Clean logs on screen
   system('cls')

   # Show account bank with the changes user did
   print(new_user)
   
   input("\nDeposito realizado correctamente, presiona Enter para volver al menu principal: ")

   return

# Function to request a outcome amount, but first, function will validate if amount entered is less that user has on its balance value
def create_outcome(new_user):
   # Request income amount
   amount = input("Ingresa la cantidad que deseas retirar de tu cuenta: ")
   user_balance = new_user.balance

   while ( amount.isnumeric() == False ):
      amount = (input("Parece que el dato ingresado no es un numero, por favor, asegurate de ingresar una cantidad valida: "))
   
   while ( amount.isnumeric() == True ):
      if ( int(amount) <= 0 ):
         amount = input("No puedes hacer un retiro de $0, ingresa otra cantidad: ")
         pass
      elif ( user_balance < int(amount) ):
         amount = input(f"Actualmente cuentas con ${ user_balance }, por lo que no puedes hacer el retiro. Intenta con otra cantidad, o presiona Ctrl + C para salir: ")
         pass
      else:
         break
   
   # Send amount to new_outcome() method on Costumer class
   new_user.new_outcome(amount)

   # Clean logs on screen
   system('cls')

   # Show account bank with the changes user did
   print(new_user)

   input("Presione Enter para volver al menu principal: ")

   return

# Function start_cashier will be the init funct that will complete the followin tasks:
# 1. Create a new instance of Costumer class using create_user function
# 2. Show options menu and request user selects one of the options
# 3. Unless user select 3, there is going to be a infinite loop while to request user selects one option
# 4. If user wants to create a new income, income function will be executed, the same applies to outcome method

def start_cashier(create_user):
   system('cls')
   new_user = create_user()
   user_option = None

   # Show menu to select one of them
   user_option = int(show_menu(user_option))

   while ( int(user_option) != 3 ):
      match ( user_option ):
         case 1:
            system("cls")
            print(f"Has seleccionado: { user_option }. Depositar \n")
            create_income(new_user)
            system('cls')
            user_option = int(show_menu(user_option))
         case 2:
            system("cls")
            print(f"Has seleccionado: { user_option }. Retirar dinero \n")
            create_outcome(new_user)
            system('cls')
            user_option = int(show_menu(user_option))
   else:
      print("\n¡Nos vemos luego!")

start_cashier(create_user)