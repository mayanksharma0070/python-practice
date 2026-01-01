# A python program to find square root of a number
from math import sqrt


"""num=int(input("enter number:"))
for i in range(0,int(num/2+1)):
    if(i*i==num):
        print(f"{i} is square root of {num}")
    
if(i==int(num/2)):
    print(f"{num} does not have a integer square root")"""

num=int(input("Enter a number: "))
s_rt=sqrt(num)
print(f"Square root of {num}: {s_rt}")