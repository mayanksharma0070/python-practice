# A python program to generate pseudo random numbers

num=int(input("How many random terms are to be genearted? "))
seed=(0,1,2,3,4,5,6,7,8,9)
j=1
for i in range(0,num):
    if (j>9):
        j=0
    p=seed[j]*3+6-3
    p=p%10
    print(p)
    j+=1
    
    