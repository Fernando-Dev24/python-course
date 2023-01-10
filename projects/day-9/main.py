# Modules
import os
from datetime import *
import time
import math
import re

# Function to format the date
def format_date(date):
   return date.strftime("%d/%m/%Y")

# Variables
pattern = r'N\w{3}-\d{5}'
date = format_date(datetime.now())

# Function to iterate every folder, subfolder and file inside Mi_Gran_Directorio, this function need to complete the following requirements
# 1. Iterate every folder/subfolder/file to validate the regular expression

def get_serial_numbers(pattern):
   os.system('cls')
   start = time.time()
   serial_numbers = []

   # Iterate over all folder, subfolders, and files
   route = f"{ os.getcwd() }\\Mi_Gran_Directorio"

   for folder, subfolder, archive in os.walk(route):
      for arch in archive:
         file = open(f"{ folder }\\{ arch }", 'r')
         file_content = file.read()

         # Validate file content includes the serial number. If it's included then it'll be added to a list.
         has_serial_number = re.search(pattern, file_content)

         if( has_serial_number != None ):
            file_name = os.path.basename(f"{ route }\\{ folder }\\{ arch }")
            file_serial_number = has_serial_number.group()
            serial_numbers.append((file_name, file_serial_number))
            continue
   
   return serial_numbers, start

# Function to show information on console. At the end, the console needs to show the following:
# 1. Show search date in this format: dd/mm/yyyy
# 2. The file name that has the serial number and serial number on that document
# 3. How many documents has a serial number
# 4. How long this software takes to finish

def output_function(date, serial_numbers, started_time):
   # Clear console
   os.system('cls')
   print("-"*30)

   # Show today date
   print(f"Fecha de búsqueda: { date } \n")

   # Show serial numbers: file - serial number
   for file_name, number in serial_numbers:
      print(file_name, number)

serial_numbers, started_time = get_serial_numbers(pattern)
output_function(date, serial_numbers, started_time)