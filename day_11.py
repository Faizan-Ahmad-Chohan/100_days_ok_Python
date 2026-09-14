from random import randint
from random import choice
"""Black jack game 
A Man Against the Possibility"""

cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]


continue_or_cheak=input("Do You want to play Game . 'y' for continuing or 'n' for exit : ").lower()
users_cards=[]
computer_cards=[]
if continue_or_cheak=='y':
    
    users_cards.append(choice(cards))
    print(users_cards)


