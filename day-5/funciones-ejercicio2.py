# Crear una funcion que retorne cada uno de sus letras en una lista no duplicada
word = input("Write a word to eliminate duplicated letter and organize them alphabetically: ")

def delete_duplicate(word):
   word_not_duplicate = []

   for letter in word:
      if ( letter not in word_not_duplicate ):
         word_not_duplicate.append(letter)
   
   return word_not_duplicate


def organize(word_list):
   word_list.sort()
   print(f"The word you introduced is here: { word_list }")

word_not_duplicate = delete_duplicate(word)
organize(word_not_duplicate)