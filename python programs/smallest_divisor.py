# A python program that input a number and find it's smallest divisor

num=int(input("Enter number: "))
i=2
flag=1
while(i*i<=num):
    flag=1
    if(num%i==0):
        print(f"{i} is the smallest divisor for {num}")
        flag=0
        break
    i +=1
    
if(flag == 0):
    print(f"{num} is a prime number")
