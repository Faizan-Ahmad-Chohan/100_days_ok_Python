import random
def difficulty_selection():
    type=input("Chose a difficulty , 'easy' ,'difficult','hard' : ").lower()
    loop_exit=True
    no_of_attempts=0
    while loop_exit:
        if type=='hard':
            no_of_attempts=5
            loop_exit=False
            return no_of_attempts
        elif type=='difficult':
                no_of_attempts=8
                loop_exit=False
                return no_of_attempts
        elif type=="easy":
            no_of_attempts=10
            loop_exit=False
            return no_of_attempts
        else:
            print("Choose  avRelevant Option ")
            type=input("Chose a difficulty , 'easy' ,'difficult','hard'").lower()

def number_gusser(no_of_attempts):
    number=random.randint(1,100)
    print(number)
    while no_of_attempts>0:
        print(f" You have {no_of_attempts} attempts left to guess the number. ")
        guess=int(input("Guess a number : "))
        if guess==number:
            print(" You Nailed it \n Whoo You made it !!!!")
            break

        elif guess>number:
                print(f" Too high\n Guess again ")
                no_of_attempts -= 1

        elif guess<number:
            print(f" Too low\n Guess again ")
            no_of_attempts -= 1









