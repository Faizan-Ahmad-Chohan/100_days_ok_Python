from random import choice 
from logo import blackjack_logo


def ace_case(input_cards ):
    for crd in input_cards:
        
        if calculate_score(input_cards)<=21:
            return input_cards
            
        
        if calculate_score>22 : 
            crd=1
            return  input_cards



def calculate_score(cards):
    """ print Total of persons cards"""
    sum=0
    for elements in cards:

        sum+=elements

    return sum


def draw_card():
    
    """Draws a random card from Deck"""
    cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    card_drawn=choice(cards)
    return card_drawn

def winner(u_cards,c_cards):
    if user_score>computer_score and user_score<=21:
            print(f" You have won the game with cards :{u_cards}")
            print(f" Computer's cards were :{c_cards}")
    if user_score<computer_score and computer_score<=21:
                print(f" You have lost the game with cards :{u_cards}")
                print(f" Computer's cards were :{c_cards}")
    if user_score==computer_score and user_score<=21 and computer_score<=21:
            print(f" Your game is draw in draw  with cards :{u_cards}")
            print(f" Computer's cards were :{c_cards}")



print(blackjack_logo)

replay_loop=True

while replay_loop==True:
    permition=input("If you want to play game  type 'y'  or type 'n' to exit : ").lower()
    if permition not in ('y','n'):
             print("Please enter Valid input to Proceed. 'y' or 'n'")
             permition=input("If you want to play game  type 'y'  or type 'n' to exit : ").lower()

         
    if permition=='y':
        users_cards=[]
        computer_cards=[]
        for i in range(2):
                users_cards.append(draw_card())
                computer_cards.append(draw_card())
        c_loop=True
        while c_loop==True:
            if calculate_score(computer_cards)<16:
                computer_cards.append(draw_card())
            computer_score=calculate_score(computer_cards)
            if 11 in computer_cards:
                computer_cards=ace_case(computer_cards)
            if calculate_score(computer_cards)>16:
                c_loop=False

        u_loop =True
        while u_loop==True  :   
            print(f"Your cards are : {users_cards}")
            print(f"Computer's first card is : {computer_cards[0]}")
            more_card=input("Do you want to draw more cards 'y' ,'n': ")

            if more_card not in ('y','n'):
                print(" Kindly type a Valid  key 'y','n'")
                more_card=input("Do you want to draw more cards 'y' ,'n': ")

            if more_card=='y':
                        users_cards.append(draw_card())
            

            user_score=calculate_score(users_cards)
            if user_score>21:
                  break

            
            if 11 in users_cards:
                computer_cards=ace_case(users_cards)
            if more_card=='n' :
                u_loop=False
        
        print(winner(users_cards,computer_cards))
        
                
                
            
            
                


        
            

 



   

