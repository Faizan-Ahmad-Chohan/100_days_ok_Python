from logo_cofee import logo
water=300
milk=200
coffee=100
balance_money=0.0
def report():
    print(f"Water : {water}ml\nMilk : {milk}ml\nCoffee : {coffee}g\nAccount Balance : {balance_money}")
def money_input():
    print("Enter the cards. write no of cards, (i.e , 1,2,3 etc)")
    no_fifties=int(input("Enter cards of worth 50 here :"))
    no_hundreds=int(input("Enter cards of worth 100 here :"))
    no_twenties=int(input("Enter cards of worth 20  here :"))
    total_money=(no_fifties*50)+(no_hundreds*100)+(no_twenties*20)
    return total_money
print(money_input())
def coffee():
    input("Enter your choice for")