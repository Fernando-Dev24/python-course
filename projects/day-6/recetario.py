import os
from os import system
from pathlib import Path

username = input("Digite su nombre: ")
user_selection = None
directory_root = Path(Path.home(), "desktop", "courses", "python-course", "projects", "day-6", "Recetas")
receipts_names = []

# Functions
# Greet the user and show the following information: Directory route and total of receipts in directory
def greet_user(username, directory_root, receipts_names):
   total_receipts = len(count_receipts(directory_root, receipts_names))
   
   system('cls')
   print(f"Hola { username }")
   print(f"Actualmente las recetas se encuentran en: { directory_root }")
   print(f"Hay un total de { total_receipts} recetas para elegir")

# Count how many receipts are in the parent directory
def count_receipts(directory_root, receipts_names):
   for receipt in Path(directory_root).glob("**/*.txt"):
      receipts_names.append(receipt.stem)
   
   return receipts_names

# Function to create the menu and show it to the user, also, user will decide how to do next
def show_menu(user_selection):
   print("1. Leer una receta")
   print("2. Crear una receta en una categoria existente")
   print("3. Crear una categoria nueva")
   print("4. Eliminar una receta")
   print("5. Eliminar una categoria")
   print("6. Salir\n")

   user_selection = input("Digite el numero de acción para continuar: ")

   while user_selection not in ['1', '2', '3', '4', '5', '6']:
      user_selection = input("Digite el numero de acción para continuar: ")

   return int(user_selection)

# Function to select a category
def choose_category(directory_root):   
   categories = os.listdir(directory_root)
   categorie_selection = ''
   
   for categorie in categories:
      print(f"{ categories.index(categorie) + 1 }. { categorie }")
   
   while ( categorie_selection not in ['1', '2', '3', '4'] ):
      categorie_selection = input("Digite el numero de la categoria: ")
   
   return categories[int(categorie_selection) - 1]

# Function to select a receipt
def choose_receipt(directory_root, category_selection):
   system('cls')
   print(f"Escogiste la categoria { category_selection }")
   print("Escoge la receta \n")
   
   # Append files names to a list
   names = []
   for receipt in Path(directory_root / category_selection).glob("*.txt"):
      names.append(receipt.stem)
   
   # Show the list of receipts in the subfolder that has the same name as the user chose
   for name in names:
      print(f"{ names.index(name) + 1 }. { name }")

   # Ask the user to enter the correct name of the recipe
   user_recipe = ''

   while ( user_recipe not in names ):
      user_recipe = input("Escribe el nombre de la receta: ")

   return user_recipe

# Function Menu 1: Read the recipe
def read_recipe(directory_root, category, recipe_name):
   system('cls')
   print(f"Leyendo la receta: { category } / { recipe_name } \n")

   file = Path(directory_root / category / f"{ recipe_name }.txt")
   print(file.read_text() + "\n")

   input("Presione Enter para volver a mostrar el menu: ")

   return

# Functions Menu 4: Delete a recipe
def delete_recipe(directory_root, category, recipe_name):
   system('cls')
   print(f"Eliminando la receta: { category } / { recipe_name } \n")

   route = Path(directory_root / category / f"{ recipe_name }.txt")
   os.remove(route)

   input("Presione Enter para volver a mostrar el menu: ")

   return

# Execute functions
greet_user(username, directory_root, receipts_names)
user_selection = show_menu(user_selection)

# Loop while to show menu to user unless user decide to end algorithm
match user_selection:
   case 1:
      system('cls')
      print(f"Elegiste la opcion { user_selection }. Leer una receta \n")
      print("Escoge una categoria segun el numero de la par: ")
      category_selection = choose_category(directory_root)
      user_recipe = choose_receipt(directory_root, category_selection)
      read_recipe(directory_root, category_selection, user_recipe)
      system('cls')
      show_menu(user_selection)
   case 2:
      print("Hola mundo 2")
   case 3:
      print("Hola Mundo 3")
   case 4:
      system('cls')
      print(f"Elegiste la opcion { user_selection }. Eliminar una receta \n")
      print("Escoge una categoria segun el numero de la par: ")
      category_selection = choose_category(directory_root)
      user_recipe = choose_receipt(directory_root, category_selection)
      delete_recipe(directory_root, category_selection, user_recipe)
      system('cls')
      show_menu(user_selection)
   case 5:
      print("Hola Mundo 5")

""" while ( user_selection != 6 ):
else:
   print("\n¡Nos vemos luego!") """
   