from alphabet import alphabets# cieser cifer
from logo import logo_ceaser_cypher

def ceasercyfer(text,shift,encode_or_decode):


    
    enc_or_dec_mesg=""
    if encode_or_decode == "decode":
        shift  *=-1
    elif encode_or_decode=="encode":
        shift *= 1
    else :
        print("     Please select a valid option    ")
    for letter in text:
       
        index_total=0
        if letter in alphabets:
            index_total=alphabets.index(letter) + shift 
            total_shift = index_total % len(alphabets)
            enc_or_dec_mesg += alphabets[total_shift]
        elif letter not in alphabets:
            enc_or_dec_mesg+=letter
    print(f"The {encode_or_decode}d reasult is : {enc_or_dec_mesg}")      
        


print(logo_ceaser_cypher)
first_attempt=True
while first_attempt:
    first_try=0
    messasge = input("Enter text : ").lower()
    shift_no = int(input("Enter shift number to start with : "))
    enc_or_dec = input("What do you want encode or decode  : ").lower()
    ceasercyfer(text=messasge , shift=shift_no ,encode_or_decode= enc_or_dec)
    choice_to_continue=input("Do you want more Encrypt or Decrypt ( yes or  no ) :  ")
    if choice_to_continue=='yes':
        first_attempt=True
    elif choice_to_continue=='no':
        first_attempt=False