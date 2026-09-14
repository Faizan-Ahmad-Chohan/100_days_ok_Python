from random import randint
from random import choice
def draw_card():
    """Draws a random card from Deck"""
    cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    card_drawn=choice(cards)
    return card_drawn
users_cards=[]
computer_cards=[]
loop=True
while loop==True:
    continue_or_cheak=input("Do You want to play Game . 'y' for continuing or 'n' for exit : ").lower()
    if continue_or_cheak=='y':
        users_cards.append(draw_card())
        computer_cards.append(draw_card())
        print(f" users cards are : {users_cards}")
        print(f" computer cards are : {computer_cards}")
    if continue_or_cheak=='n':
        loop=False

    
   

