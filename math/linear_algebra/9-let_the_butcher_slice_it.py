#!/usr/bin/env python3
import numpy as np
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]])
mat1, mat2, mat3 = matrix[1:3, :], matrix[:, 1:3], matrix[2:5, 2:5]
print("The middle two rows of the matrix are:\n", mat1, "\nThe middle two columns of the matrix are:\n", mat2, "\nThe bottom-right, square, 3x3 matrix is:\n", mat3)
