a=0
b=1
c=a+b
num=int(input("How many terms to print? "))
i=1
if(num==1):
    print(a,b)
elif(num==2):
    print(b)
else:
    print(a)
    while(i<=num):
        print(c)
        a=b
        b=c
        c=a+b
        i+=1
