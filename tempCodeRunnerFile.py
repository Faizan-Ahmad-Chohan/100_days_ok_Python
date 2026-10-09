person_1=person_slector()
person_2=person_slector()
while person_1 !=person_2 and loop_variable:
    if no_of_count>=1:
        print(f"You are right, current score is: {no_of_count}")
    print(high_low_logo)
    print(f"\nCompare a:  {person_1['name']  }, a {person_1['description']} ,from {person_1['country']} ")
    print(vs_logo,"\n")

    print(f"Against b : {person_2['name']  } , a {person_2['description']}, from { person_2['country'] }")
    user_choice=input("Who has more followers ? Guess  'A','B' : ").lower()
    if user_choice=='a'or user_choice=='b':
        if user_choice=='a' and  person_1['follower_count']>=person_2['follower_count']:
            no_of_count+=1
            print("\n",no_of_count)
        elif user_choice=='b'and person_2['follower_count']>= person_1['follower_count']:
            no_of_count+=1
            print("your score is:",no_of_count)
        else : 

            print(high_low_logo)
            print(f"Sorry ,That was Wrong . Final Score {no_of_count}")
            loop_variable=False
            
            try_again=input("Do You want to restart 'y' , 'n' ? ").lower()
            if try_again=='y':
                loop_variable=True
                no_of_count=0

    break






