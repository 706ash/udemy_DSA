import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(f"Matrix: \n{matrix}")

#Transpose

transpose = matrix.T
print(f"Transpose: \n{transpose}")

another_matrix = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])

print(f"Addition: \n{matrix + another_matrix}")
print(f"Multiplication: \n{matrix * another_matrix}")