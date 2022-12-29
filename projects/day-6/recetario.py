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
   categorie_selection = len(categories) + 1
   
   for categorie in categories:
      print(f"{ categories.index(categorie) + 1 }. { categorie }")
   
   while ( categorie_selection > len(categories) ):
      categorie_selection = int(input("Digite el numero de la categoria: "))
   
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

   if ( len(names) == 0 ):
      print("No hay recetas en esta categoria, te recomendamos que crees una nueva en esta categoria.")
      input("Presiona Enter para volver al menu principal: ")
      return

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

# Function Menu 2: Create a new recipe with name and content
def create_recipe(directory_root, category):
   system('cls')
   new_recipe_name = input("Escibre el nombre de la nueva receta: ")

   while ( Path(directory_root / category / f"{ new_recipe_name }.txt").exists() == True ):
      new_recipe_name = input("Ya existe una receta con ese nombre, intenta con uno diferente: ")

   new_recipe_content = input("Escribe el contenido de la nueva receta: ")

   # First, we need to create the file with the name provided by the user
   new_file = open(Path(directory_root / category / f"{ new_recipe_name }.txt"), 'x')
   new_file.close()

   # Finally, we need just to open the file with write mode and write the content user provided
   new_file = open(Path(directory_root / category / f"{ new_recipe_name }.txt"), 'w')
   new_file.write(new_recipe_content)
   new_file.close()
   
   # Validate if the new file was created successfully
   if ( Path(directory_root / category / f"{ new_recipe_name }.txt").exists() == False ):
      input("Ha ocurrido un error, presiona Enter para volver a intentarlo: ")
      return
   
   input("La receta se ha creado correctamente, presiona Enter para volver al menu principal: ")
   
   return

# Function Menu 3: Create a new category without any recipe inside, i mean, just the folder
def create_category(directory_root):
   system('cls')
   print(f"Elegiste la opcion { user_selection }. Crear una nueva categoria \n")
   new_directory_name = input("Escribe el nombre de la nueva categoria: ")

   while ( new_directory_name == '' ):
      new_directory_name = input("Escribe el nombre de la nueva categoria: ")

   # Create the new empty folder with the name that user provided
   os.makedirs(Path(directory_root / new_directory_name))

   if ( Path(directory_root / new_directory_name).exists() == False ):
      input("Ha ocurrido un error, presiona Enter para volver a intentalo: ")
      return
   
   system('cls')
   print(f"Se ha creado la nueva categoría, su ruta es: { Path(directory_root / new_directory_name) }")
   input("Presiona Enter para volver al menu principal: ")

   return

# Functions Menu 4: Delete a recipe
def delete_recipe(directory_root, category, recipe_name):
   system('cls')
   print(f"Eliminando la receta: { category } / { recipe_name } \n")

   route = Path(directory_root / category / f"{ recipe_name }.txt")
   os.remove(route)

   input("Presione Enter para volver a mostrar el menu: ")

   return

# Function Menu 5: Delete a category
def delete_category(directory_root, category):
   # To remove a completed directory, first we need to remove all files contained in that specific path
   route = Path(directory_root / category)
   
   # Loop on every file inside the route variable
   for file in os.listdir(route):
      print(f"Eliminando archivo: { file }")
      os.remove(Path(route / file))
   
   print(f"Todos los archivos de la categoria { category } han sido eliminados.")
   print(f"Eliminando categoria: { category }")

   # Now that directory is empty, we're allowed to remove the directory
   os.rmdir(route)

   input(f"Categoria { category } eliminada correctamente. Presione Enter para volver al menu principal: ")

   return

# Execute functions
greet_user(username, directory_root, receipts_names)
user_selection = show_menu(user_selection)

# Loop while to show menu to user unless user decide to end algorithm
while ( user_selection != 6 or user_selection == None ):
   match user_selection:
      case 1:
         system('cls')
         print(f"Elegiste la opcion { user_selection }. Leer una receta \n")
         print("Escoge una categoria segun el numero de la par: ")
         category_selection = choose_category(directory_root)
         user_recipe = choose_receipt(directory_root, category_selection)
         if ( user_recipe == None ):
            system('cls')
            user_selection = show_menu(user_selection)
         else:
            read_recipe(directory_root, category_selection, user_recipe)
            system('cls')
            user_selection = show_menu(user_selection)
      case 2:
         system('cls')
         print(f"Elegiste la opcion { user_selection }. Crear una receta en una categoria existente \n")
         print("Escoge una categoria segun el numero de la par: ")
         category_selection = choose_category(directory_root)
         create_recipe(directory_root, category_selection)
         system('cls')
         user_selection = show_menu(user_selection)
      case 3:
         system('cls')
         create_category(directory_root)
         system('cls')
         user_selection = show_menu(user_selection)
      case 4:
         system('cls')
         print(f"Elegiste la opcion { user_selection }. Eliminar una receta \n")
         print("Escoge una categoria segun el numero de la par: ")
         category_selection = choose_category(directory_root)
         user_recipe = choose_receipt(directory_root, category_selection)
         delete_recipe(directory_root, category_selection, user_recipe)
         system('cls')
         user_selection = show_menu(user_selection)
      case 5:
         system('cls')
         print(f"Elegiste la opcion { user_selection }. Eliminar una categoria. \n")
         print("Ten en cuenta que para eliminar una categoria todas las recetas de esa categoria seran eliminadas")
         print("Escoge una categoria segun el numero de la par: ")
         category_selection = choose_category(directory_root)
         delete_category(directory_root, category_selection)
         system('cls')
         user_selection = show_menu(user_selection)
else:
   print("\n¡Nos vemos luego!")