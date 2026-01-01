# A python program to calculate the dot and cross products of two vectors
import numpy as np

#create two equal vectors
list1 = [4,5,6]
list2 = [1,2,3]
vector1 = np.array(list1)
vector2 = np.array(list2)
print("first vector: ",vector1)
print("second vector: ",vector2)
print("\n")

#calculate the dot and cross products of vectors
dot_product = np.dot(vector1,vector2)
cross_product = np.cross(vector1,vector2)
#print the result 
print("Dot product: ",dot_product)
print("Cross product: ",cross_product)
