import random
print("number between different ranges\n")
print("A Decimal between 0 -> 1. Fraction always ")
number_between_0_1=random.random()

print(f"\t\trandom.random() : {number_between_0_1}")

print(" The the number above is totally random \n")
print("Now try some limiting gueses \n \t lets set some uper and lower limits(boundaries), and get a random number in between")
lower_limit=int(input("Enter lower limit : "))
upper_limit=int(input("Enter uper limit :  "))



bounded_guess_in_limits=random.randint(lower_limit,upper_limit)
print(f"The random number, which is actually in between {lower_limit}, and {upper_limit}  is:{bounded_guess_in_limits}")


