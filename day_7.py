import random 
from hangmanart import stages
from hangmanwords import words
from logo import logo

chosen_word=random.choice(words)

placeholder=""

for spaces in chosen_word:
    placeholder+="_"

print(logo)
print(f"Guess the word  Save this Person to be Hang   :  {placeholder} ")
print(stages[6])

correct_letters=[]
no_of_lives=6
game_over=False
while not game_over:
    
    display=""
    guess_letter=input("Guess a letter : ").lower()
    if guess_letter in display:
        print(f"You allready Guessed this Word {guess_letter}")


    for letter in chosen_word:
        if letter==guess_letter:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter

        else:
            display+="_"
    if not guess_letter in chosen_word:
        no_of_lives-=1
        print(f"You guessed : {guess_letter} which is not this Word, You lose a Life")
           
    if no_of_lives==0:
        game_over=True
        print("You're out of lives . You lose the Game")
        print(f"This particular word was {chosen_word}")
    print(display)
   
    if not "_" in display:
        game_over=True
        print(" whooooo , You made it !! .You won the game")
    print(stages[no_of_lives]) 