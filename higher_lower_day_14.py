from higher_lower_dictionary import game_data, vs_logo,high_low_logo
from random import choice

def person_slector():
    return(choice(game_data)) 


no_of_count=0
cond=True
while cond:
    print(high_low_logo)
    person_1=person_slector()
    print(f"\nCompare a:  {person_1["name"]  }, a {person_1["description"]} ,from {person_1["country"]}\n ")
    print(vs_logo,"\n")
    person_2=person_slector()
    print(f"Against b : {person_2["name"]  } , a {person_2["description"]}, from { person_2["country"] }")
    user_choice=input("Who has more followers ? Guess  'A','B' : ").lower()
    if user_choice=='a'or user_choice=='b':
        if user_choice=='a' and  person_1["follower_count"]>=person_2["follower_count"]:
            no_of_count+=1
            print("\n",no_of_count)
        elif user_choice=='b'and person_2["follower_count"]>= person_1["follower_count"]:
            no_of_count+=1
            print("\n",no_of_count)
        else : 
            
            print(high_low_logo)
            print(f"Sorry ,That was Wrong . Final Score {no_of_count}")
            cond=False




  


