#total numbers for rounds of operations

for i in range(6):
    print(f"/,round=5")

#input

    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))

    #choices for op

    print("1 for sum ")
    print("2 for multiply")
    print("3 for division")
    print("4 for modulus")
    print("5 for subtraction")
    choice=int(input("enter your choice"))

    #condition for choices
     
    if choice==1:
        print("sum is:", n1+n2)
    elif choice==2:
        print("multiply is:",n1*n2)
    elif choice==3:
        print("division is:",n1/n2)
    elif choice==4:
        print("modulus is :",n1%n2)
    elif choice==5:
        print("subtraction is:",n1-n2)

        #in case given choices are not entered by user
    
    else:
        ("invalid key")
