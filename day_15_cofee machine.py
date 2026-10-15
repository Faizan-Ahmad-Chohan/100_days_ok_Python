water=300
milk=200
coffee=100
total_cash=0.0

def report():
    print(f"water : {water}ml\nMilk : {milk}ml\ncoffee : {coffee}g\nTotal_c : ${total_cash}")
def turn_off():
    return False
def money_count():
    print("-----Enter how much tokens you have, 1,2,3,4...")
    fiftys=input("how much tokent of rupees'50' :")
    hundreds=input("how much tokent of rupees'100' :")
    hun_twenties=input("how much tokent of rupees '120' :").lower()
    result= (fiftys*50)+(hundreds*100)+(hun_twenties*120)
    return result
def orders():
    ord=input(" What will you like to have :(capiccino,latee,espresso) :").lower()
    cappiccno=200
    latee=220
    espresso=150
    if ord=='capiccino':
        money_count()-cappiccno
    elif ord=='latee':
        money_count()-latee
    elif ord=='espresso':
        money_count()-espresso
def terminal(ped):
    orders()
    money_count()
    turn_off()
    report()
while True:
     ord=input(" What will you like to have :(capiccino,latee,espresso) :"). lower()
     terminal(ord)
