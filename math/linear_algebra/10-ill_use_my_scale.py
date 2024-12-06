#!/usr/bin/env python3
"""
This module contains a function to calculate the shape of a numpy.ndarray.
"""


import numpy as np

def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray.

    Args:
        matrix (numpy.ndarray): The input numpy array.

    Returns:
        tuple: A tuple of integers representing the shape of the array.
    """
    return matrix.shape


if __name__ == "__main__":
    # Test cases
    mat1 = np.array([[1, 2, 3], [4, 5, 6]])
    print(np_shape(mat1))  # Output: (2, 3)

    mat2 = np.array([1, 2, 3, 4])
    print(np_shape(mat2))  # Output: (4,)

    mat3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(np_shape(mat3))  # Output: (2, 2, 2)
