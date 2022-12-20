# Input, user input a txt and three letters to make the analize
txt = input("Digite el texto a su eleccion, puede ser un articulo, un parrafo, o un poema: ").lower()
letters = [
   input("Digite la primera letra ").lower(),
   input("Digite la segunda letra ").lower(),
   input("Digite la segunda letra ").lower(),
]

result = {}

# Process the txt variable
# 1. Count how many times appear each letter into the txt

countLetter1 = txt.count(letters[0])
countLetter2 = txt.count(letters[1])
countLetter3 = txt.count(letters[2])

result['countLetter1'] = countLetter1
result['countLetter2'] = countLetter2
result['countLetter3'] = countLetter3

# 2. Count how many letter are in the txt
txtList = len(txt.split())
result['txtList'] = txtList

# 3. Get the first and last letter of the txt
firstLetter = txt[0].upper()
lastLetter = txt[-1]

result['firstLetter'] = firstLetter
result['lastLetter'] = lastLetter

# 4. Reverse the txt and show it to the user
txtSplit = txt.split()
txtSplit.reverse()
txtSplit = " ".join(txtSplit)

result['txtSplit'] = txtSplit

# 5. Validate if txt includes Python word or not
validatePyWord = 'python' in txt
result['isPythonWord'] = validatePyWord

# Output
print(f"En el texto ingresado la letra { letters[0] } se repetió { result['countLetter1'] } veces; \nLa letra { letters[1] } se repetió { result['countLetter2'] } veces; \ny la letra { letters[2] } se repetió { result['countLetter3'] } veces. \nSe detectaron { result['txtList'] } palabras. \nLa primera letra del texto fue { result['firstLetter'] } y la ultima fue { result['lastLetter'] } \nTu texto al reves da un resultado asi: { result['txtSplit'] }. \nLa validacion de la palabra 'Python' da como resultado { result['isPythonWord'] }")