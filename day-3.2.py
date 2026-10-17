print(" --------- Welcome to Amusement Park---------")

hight=int(input(" What's Your Hight ? "))
if hight>=120:
    print("You can have ride of RollerCoster !")
    age=int(input(" Enter Your Age :"))
    if age<=12:
        print("Your ticket cost's  : 7$")
    elif age<=18:
        print("Your ticket cost's : 9$")
    elif age>18:
        print("Your ticket cost's : 12$")
    else:
        print("Please Provide valid Age.........")
else:
    print("You're not Enough Tall to have Ride.......")