def rev_num(num):
    rev_no=0
    while num>0:
        last_digit=num%10
        rev_no=rev_no*10+last_digit
        num=num//10
    return rev_no

num=int(input("enter a number: "))
r_num=rev_num(num)
print("the reverse of",num,"is: ",r_num)