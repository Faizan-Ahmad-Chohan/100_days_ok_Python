from random import choice
def sum(n1,n2):
    num1=input("enter first number")
    n1=int(num1)
    num2=input("enter second number")
    n2=int(num2)
    sm=int(n1+n2)
    print(sm)


def draw_card():
    
    """Draws a random card from Deck"""
    cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    card_drawn=choice(cards)
    return card_drawn
def calculate_score(cards):
    """ print Total of persons cards"""
    sum=0
    for elements in cards:

        sum+=elements

    return sum
def ace_case(input_cards ):
    for crd in input_cards:
        if crd==11 and calculate_score(input_cards)>21:
            crd=1
            return crd 

            





