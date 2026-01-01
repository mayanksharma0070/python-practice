def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

num=int(input("enter number: "))
ans=fact(num)
print("factorial of",num,"is: ",ans)