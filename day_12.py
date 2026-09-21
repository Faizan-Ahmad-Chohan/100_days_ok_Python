def difficulty_selection():
    type=input("Chose a difficulty , 'easy' ,'difficult','hard'").lower()
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

