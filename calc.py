
def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.percentage")
    print("6.Exit")

calculator()

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b 

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    
def percentage(a,b):
    try:
        return a/b*100
    except ZeroDivisionError:
        return "unable to find the percentage"
while True:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    choice = int(input("Enter your choice either 1 or 2 or 3 or 4 or 5 or 6: "))
    if choice == 1:
        print(f"The addition of {a} and {b} is {add(a,b)}")
    elif choice == 2:
        print(sub(a,b))
    elif choice == 3:
        print(mul(a,b))
    elif choice == 4:
        print(div(a,b))
    elif choice == 5:
        print(percentage(a,b))
    elif choice == 6:
        exit
    else:
        print("Invalid Choice")
    next=input("Do you want to use operation Yy/Nn ")
    if next=='y' or next=='Y':
        continue
    elif next=='n' or next=="N":
        exit()
    else:
        print("Enter a valid input")
