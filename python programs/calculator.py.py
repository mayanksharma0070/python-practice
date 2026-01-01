def calculate(choice):
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    if(num2!=0):
        
        div=num1/num2
        mod=num1%num2
        flag=1
    else:
        flag=0
    if(choice==1):
        return add
    elif(choice==2):
        return sub
    elif(choice==3):
        return mul
    elif(choice==4):
        if(flag==0):
            print("division by zero(0) is not define")
            return -1
        return div
    else:
        if(flag==0):
            print("modulus by zero(0) is not define")
            return -1
        return mod
while 1:
    print("\n\t\t\t***MENU***\n")
    print("\t\t1. Addition\n")
    print("\t\t2. Subtract\n")
    print("\t\t3. Multiply\n")
    print("\t\t4. Division\n")
    print("\t\t5. Modulus\n")
    print("\t\t6. Exit")
    choice=int(input("enter your choice here: "))
    if(choice>=1 and choice<=3):
        ans=calculate(choice)
        print(ans)
    elif(choice==4 or choice == 5):
        ans=calculate(choice)
        if(ans>=0):
            print(ans)
    elif(choice <= 0 or choice > 6 ):
        print("invalid choice try again")
    else:
        print("thank you!")
        break
    


    