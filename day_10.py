from logo import calculator

def sum(n1,n2):
    return  n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def diviion(n1,n2):
    return n1 / n2
function_dictionary={
    "+" : sum ,
    "-" : subtract ,
    "*" : multiply ,
    "/" : diviion ,

} 
print(calculator)
def calculator_function():
    n1=float(input("Enter  number : "))
    count=0
    while count==0:
        print("+\n-\n*\n/")
        operation=input(" Select any Operation : ")
        n2=float(input("Enter  Second number : "))
        print(n1 , operation , n2 , "=" , function_dictionary[operation](n1,n2))
        n1=function_dictionary[operation](n1,n2)
    
        further_calculations=input(f"Write 'y' for continuing calculating with {n1} or Type 'n'to stop  :  ")
        if further_calculations =='n':
            count+=1
            

            
calculator_function()
