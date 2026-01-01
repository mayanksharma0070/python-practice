# A python program to find the HCF of two number

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
hcf=1
small=min(num1,num2)
for i in range(1,small+1):
    if(num1%i == 0 and num2%i == 0):
        hcf=i

print(f"HCF of {num1},{num2} is:\n {hcf}")