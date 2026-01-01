# A python program to find GCD of two numbers using recursive method

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("GCD is:\n",gcd(a,b))
