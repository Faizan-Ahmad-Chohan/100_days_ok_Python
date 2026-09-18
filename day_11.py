from random import randint
from random import choice 
from functions import draw_card , calculate_score


users_cards=[]
computer_cards=[]
loop=True
while True:
    users_cards.append(draw_card())
    computer_cards.append(draw_card())
    users_cards.append(draw_card())
    computer_cards.append(draw_card())
    print(f" users cards are : {users_cards}")
    print(f" computer cards are : {computer_cards}")
    print(f"total of user is  {calculate_score(users_cards)}")
    print(f"total of user is  {calculate_score(computer_cards)}")




   

