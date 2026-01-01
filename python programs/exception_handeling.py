
try:
    a=int(input("enter a number: "))
    s=(6,4)
    print(f"enterd number:{a} ")
    print(s[a])

except ValueError:
    print("entered input is not an integer")
except IndexError:
    print("index error occuerd")

finally:
    print("this statement has been written in finally clause. So this statement will alaways execute no matter what!")
    print(f"code has been executed")
