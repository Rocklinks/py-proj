
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
    
total = None

    if choice == 1:
        total=add(a,b)
        print(f"The addition of {a} and {b} is {total}")
    elif choice == 2:
        total=sub(a,b)
        print(f"The subtraction of {a} from {b} is {total}")
    elif choice == 3:
        total=mul(a,b)
        print(f"The multiplication of {a} and {b} is {total}")
    elif choice == 4:
        totalt=div(a,b)
        print(f"The division of {a} by {b} is {total}")
    elif choice == 5:
        totalt=percentage(a,b)
        print(f"The {a} percentage of {b} is {total}")
    elif choice == 6:

        exit()
    else:
        print("Invalid Choice")
    next=input("Do you want to use operation Yy/Nn ")
    if next=='y' or next=='Y':
        continue
    elif next=='n' or next=="N":
        break
    else:
        print("Enter a valid input")
