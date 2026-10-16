water=300
milk=200
coffee=100
total_cash=0.0

def capiccino(amount):
    price_cap=200
    if amount==price_cap or amount>price_cap :
        print("Here is your capiccino , enjoy ")
        amount=amount-price_cap
        print(f"Remainig money :{amount}")
    elif amount<price_cap:
        print("Not Enough money. ")


def latee(amount):
    price_lat=200
    if amount==price_lat or amount>price_lat :
            print("Here is your latee , enjoy ")
            amount=amount-price_lat
            print(f"Remainig money :{amount}")
    elif amount<price_lat:
            print("Not Enough money. ")
def espresso(amount):
    price_esp=200
    if amount==price_esp or amount>price_esp :
            print("Here is your espresso , enjoy ")
            amount=amount-price_esp
            print(f"Remainig money :{amount}")
    elif amount<price_esp:
            print("Not Enough money. ")
def report():
    print(f"water : {water}ml\nMilk : {milk}ml\ncoffee : {coffee}g\nTotal_c : ${total_cash}")
def turn_off():
    return False
order_dicctionary={
"capiccino" : capiccino,
"latee" : latee,
"espresso" : espresso,
"report" : report,
"off" : turn_off



}








def money_count():
    print("-----Enter how much tokens you have, 1,2,3,4...")
    fiftys=input("how much tokent of rupees'50' :")
    hundreds=input("how much tokent of rupees'100' :")
    hun_twenties=input("how much tokent of rupees '120' :").lower()
    result= (fiftys*50)+(hundreds*100)+(hun_twenties*120)
    return result


def terminal():
        