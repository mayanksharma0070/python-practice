# this program is to test random module and some operations on random module 
import random

#random.random()
#this will generate any random float value between 1 and 0
print("This will generate any random float value between 1 and 0:   ",random.random())
print("\n")

#random.randint(a,b)
#this will generate an int value between range a and b (both included)
print("a random integer value between 1 and 10: ",random.randint(1,10))
print("\n")


#random.uniform(a,b)
#this will generate any random float value between numbers a,b
print("a random value in float between 1 and 5: ",random.uniform(1,5))
print("\n")


#random.randrange(start, stop, range)
#this will generate any random number between range start and stop
#start  starting number(included)
#stop   ending number(not included)
#range  for how much the number will increase (optional)
print("random value between range 1 and 10(excluded) increasing with a set of 2:    ",random.randrange(1,10,2))
print("\n")


#random.choice(sequence)
#this will choose any item randomly from a given list,tuple..etc.
li=["stone","paper","scissor"]
print("this will choose an item from a given sequence:  ",random.choice(li))
print("\n")


#random.sample(sequence,k)
#this returns a random order of k from a given sequence (no repetation) of tuple, list,..etc
tu=(1,0.5,True,False,"banana")
print("this will choose k items from a given sequence:  ",random.sample(tu,3))
print("\n")


#random.shuffle(sequence)
#this will rearrange the order or sequence of a given tuple,list...etc
fruits=["banana","mango","apple","cherry"]
random.shuffle(fruits)
print(fruits)
print("\n")
