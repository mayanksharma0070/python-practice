# A python program to calculate the inverse of a matrix
import numpy as np

#original matrix
mat = np.array([[0, 8, 6],
                [1, 5, 2],
                [6, 0, 3]])
print("original matrix:\n",mat)
print("\n")

#calculating inverse of matrix and printing the result
mat_inv = np.linalg.inv(mat)
print("Inverse of matrix is:\n", mat_inv)
