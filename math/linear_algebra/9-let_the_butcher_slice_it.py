#!/usr/bin/env python3
"""
This module slices a given 5x5 matrix to extract specific submatrices.
"""


import numpy as np

# Define the 5x5 matrix
matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]])

# Extract the middle two rows of the matrix
mat1 = matrix[1:3, :]

# Extract the middle two columns of the matrix
mat2 = matrix[:, 1:3]

# Extract the bottom-right, square, 3x3 matrix of the matrix
mat3 = matrix[2:, 2:]

# Print the results
print("The middle two rows of the matrix are:\n", mat1)
print("The middle two columns of the matrix are:\n", mat2)
print("The bottom-right, square, 3x3 matrix of the matrix is:\n", mat3)
