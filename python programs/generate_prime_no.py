# A python program to generate prime numbers 
num=int(input("How many prime numbers are to be generate? "))
i=1
while(num!=0):
    flag=0
    for j in range(2,i+1):
        if(i%j==0):
            flag=1
            break

    if(flag==0):
        print(i)
        num=num-1
    else:
        continue

    i+=1

        