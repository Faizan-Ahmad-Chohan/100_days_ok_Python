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
          

    while True:     
        print(f"Your cards are: {users_cards}")
        print(f"Computer's first card is : {computer_cards[0]}")  
        more_card=input("If you want to draw more cards \" yes 'y',no 'n'\"").lower()
        if more_card=='y': 
            users_cards.append(draw_card()) 
        
        computers_total=calculate_score(computer_cards)
        while  computers_total <=16:
            computer_cards.append(draw_card())
            if ace_case(computer_cards):
                computers_total=ace_case(computer_cards)
        print(computers_total)
       
             
              
        
        
              


       
        

 



   

