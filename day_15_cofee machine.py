water=300
milk=200
coffee=100
total_cash=0.0
mon=0
loop_breaker=True







def money_count():
    print("-----Enter how much tokens you have, 1,2,3,4...")
    fiftys=int(input("how much tokent of rupees'50' :"))
    hundreds=int(input("how much tokent of rupees'100' :"))
    hun_twenties=int(input("how much tokent of rupees '120' :").lower())
    result= (fiftys*50)+(hundreds*100)+(hun_twenties*120)
    print(f"You have a total of Rs {result} to order!!")
    return result

def cappiccino(amount):
    global milk,water,coffee,total_cash,loop_breaker
    price_cap=200
    if amount==price_cap or amount>price_cap :
        print("Here is your capiccino , enjoy ")
        milk-=50
        water-=20
        coffee-=30
        amount=amount-price_cap
        total_cash+=price_cap
        print(f"Remainig money :{amount}")
        print("if any more order just type any key and press enter, and n for no order anymore !")

        restart=input("Do you have any more order?'y','n' : ").lower()
        if restart=='n':
             loop_breaker=False
             print(f"Remaining Cash  Rs {mon} refunded !!")
             
    elif amount<price_cap:
        print("Not Enough money. ")


def latee(amount):
    global milk,water,coffee,total_cash,loop_breaker
    price_lat=210
    if amount==price_lat or amount>price_lat :
            print("Here is your latee , enjoy ")
            milk-=40
            water-=30
            coffee-=30
            amount=amount-price_lat
            total_cash+=price_lat
            print(f"Remainig money :{amount}")
            print("if any more order just type any key and press enter, and n for no order anymore !")
            
            restart=input("Do you have any more order?'y','n'").lower()
            if restart=='n':
                    loop_breaker=False
                    print(f"Remaining Cash  Rs {mon} refunded !!")
    elif amount<price_lat:
            print("Not Enough money. ")
def espresso(amount):
    global milk,water,coffee,total_cash,loop_breaker

    price_esp=80
    if amount==price_esp or amount>price_esp :
            print("Here is your espresso , enjoy ")
            milk-=40
            water-=30
            coffee-=20
            amount=amount-price_esp
            total_cash+=price_esp
            print(f"Remainig money :{amount}")
            print("if any more order just type any key and press enter, and n for no order anymore !")
                       
    
            restart=input("Do you have any more order?'y','n'").lower()
            if restart=='n':
                    loop_breaker=False
                    print(f"Remaining Cash  Rs {mon} refunded !!")
    elif amount<price_esp:
            print("Not Enough money. ")
def report():
    print(f"water : {water}ml\nMilk : {milk}ml\ncoffee : {coffee}g\nTotal_c : ${total_cash}")
def turn_off(mon):
    global loop_breaker
    loop_breaker= False







order_dicctionary={
"cappiccino" : cappiccino,
"latee" : latee,
"espresso" : espresso,
"report" : report,
"off" : turn_off,



}






def terminal():
        global mon
        prp=input("What would you like to have? (espresso/late/cappiccino):")
        if prp in order_dicctionary.keys():
            order_dicctionary[prp](mon)
        else:
              print("Please enter a valid command !!\n")



srt=input("Write 'start' to turn on machine :'").lower()
if srt=='start':
    global loop_braker
    mon=int(money_count())

    while loop_breaker:
        terminal()
