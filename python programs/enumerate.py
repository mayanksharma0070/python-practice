# enumerate() uses to loop over a sequence, such as list, tuple,or string and get the index and value of each element

fruits = ["banana","mango","papaya"]
for index,fruit in enumerate(fruits,start=1):
    print(f"{index}: {fruit}")

#enumerate over string of each character
string="hello world"
for index,c in enumerate(string):
    print(index,c)