from random import randint
from random import choice 
from functions import draw_card,calculate_score,ace_case
___=True
while ___==True:
    permition=input("If you want to play game  type 'y'  or type 'n' to exit : ").lower()
    if permition=='y':
        users_cards=[]
        computer_cards=[]
        for i in range(2):
                users_cards.append(draw_card())
                computer_cards.append(draw_card())
        __=True
        while __==True:
            if calculate_score(computer_cards)<16:
                computer_cards.append(draw_card())
            computer_score=calculate_score(computer_cards)
            if 11 in computer_cards:
                computer_cards=ace_case(computer_cards)
            if calculate_score(computer_cards)>16:
                __=False

        _ =True
        while _==True  :   
            print(f"Your cards are : {users_cards}")
            print(f"Computer's first card is : {computer_cards[0]}")
            more_card=input("Do you want to draw more cards 'y' ,'n': ")
            if more_card=='y':
                        users_cards.append(draw_card())
            if calculate_score(computer_cards)<16:
                        computer_cards.append(draw_card())

            user_score=calculate_score(users_cards)

            
            if 11 in users_cards:
                computer_cards=ace_case(users_cards)
            if more_card=='n' :
                _=False
        if user_score>computer_score and user_score<=21:
                print(f" You have won the game with cards :{users_cards}")
                print(f" Computer's cards were :{computer_cards}")
        if user_score<computer_score and computer_score<=21:
                    print(f" You have lost the game with cards :{users_cards}")
                    print(f" Computer's cards were :{computer_cards}")
        if user_score==computer_score and user_score<=21 and computer_score<=21:
                print(f" Your game is draw in draw  with cards :{users_cards}")
                print(f" Computer's cards were :{computer_cards}")

        
                
                
            
            
                


        
            

 



   

