from cal_function import *
while True:
    print("what do you want to do?? ")
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 subtraction")
    print("enter yes or no to exit")

    choice  = input("enter your choice: ")

    if choice =="yes" or choice == 'no':
        break

    num1 = float(input("enter number 1: "))
    num2 = float(input("enter number 2: "))

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        multiplication(num1,num2)
    elif choice == '4':
        division(num1,num2)
    else :
        print("invalid choice")
