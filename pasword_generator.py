import random
#pasword generator
letters= ["a","b","c","d","e","f","g","h","i","j","k","l",
          "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


symbols=["@","!","#","%","&","*","(",")","\"","\'","?","/",">","<",",",".",]
numbers=["1","2","3","4","5","6","7","8","9"]
print("Welcome to Pasword Generator " \
"let me know what are Your choices  ")
letter_choice=int(input("How much letters :  "))
symbol_choice=int(input("How many Symbols :  " ))
numbers_choice=int(input("How ,many numbers :  "))
if letter_choice>len(letters):
    letter_choice=len(letters)
if symbol_choice>len(symbols):
    symbol_choice=len(symbols)
if numbers_choice>len(numbers):
   numbers_choice=len(numbers)


random_letters=list()
for selected_letter in range(1,letter_choice+1):
   random_letters+=random.choice(letters)

random_symbols=list()
for selected_symbols in range(1,symbol_choice+1):
   random_symbols+=random.choice(symbols)

random_numbers=list()
for selected_numbers in range(1,numbers_choice+1):
    random_numbers+=random.choice(numbers)

pasword=random_letters +random_symbols +random_numbers
random.shuffle(pasword)
pass_string=str()

for letr in pasword:
    pass_string+=letr

print(f"Here is your Pasword  : {pass_string}")
