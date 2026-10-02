from higher_lower_dictionary import game_data, vs_logo,high_low_logo
from random import choice

def person_slector():
    return(choice(game_data)) 



print(high_low_logo)
person_1=person_slector()
print(f"\nCompare a:  {person_1["name"]  }, a {person_1["description"]} ,from {person_1["country"]}\n ")
print(vs_logo,"\n")
person_2=person_slector()
print(f"Against b : {person_2["name"]  } , a {person_2["description"]}, from { person_2["country"] }")







 