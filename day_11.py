from random import randint
from random import choice 
from functions import draw_card,calculate_score

permition=input("If you want to play game  type 'y'  or type 'n' to exit : ")
if permition=='y':
    users_cards=[]
    computer_cards=[]
    for i in range(2):
             users_cards.append(draw_card())
             computer_cards.append(draw_card())
             print(f"Your cards are: {users_cards}")
             print(f"Computer's first card is : {computer_cards[0]}")  
    while True:      
         
        more_card=input("If you want to draw more cards \" yes 'y',no 'n'\"")  
            
            
 


       
        

 



   

