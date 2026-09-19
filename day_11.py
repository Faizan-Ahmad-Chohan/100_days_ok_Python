from random import randint
from random import choice 
from functions import draw_card,calculate_score,ace_case

permition=input("If you want to play game  type 'y'  or type 'n' to exit : ").lower()
if permition=='y':
    users_cards=[]
    computer_cards=[]
    for i in range(2):
            users_cards.append(draw_card())
            computer_cards.append(draw_card())
    while True  :   
        print(f"Your cards are : {users_cards}")
        print(f"Computer's first card is : {computer_cards[0]}")
        more_card=input("Do you want to draw more cards 'y' ,'n': ")
        user_score=calculate_score(users_cards)
        computer_score=calculate_score(computer_cards)
        if more_card=='y':
            users_cards.append(draw_card())
        if calculate_score(computer_cards)<16:
            computer_cards.append(draw_card())

       
             
              
        
        
              


       
        

 



   

