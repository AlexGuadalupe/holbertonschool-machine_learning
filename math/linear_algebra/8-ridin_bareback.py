#!/usr/bin/env python3
"""
This module contains a function to perform matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication.

    Args:
        mat1 (list): A 2D list of ints/floats representing the first matrix.
        mat2 (list): A 2D list of ints/floats representing the second matrix.

    Returns:
        list: A new 2D list representing the product of mat1 and mat2.
        None: If the two matrices cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None

    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]
    return result


if __name__ == "__main__":
    # Test cases
    mat1 = [[1, 2], [3, 4], [5, 6]]
    mat2 = [[7, 8, 9], [10, 11, 12]]
    print(mat_mul(mat1, mat2))  # Output: [[27, 30, 33], [61, 68, 75], [95, 106, 117]]

    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[7, 8], [9, 10], [11, 12]]
    print(mat_mul(mat1, mat2))  # Output: [[58, 64], [139, 154]]

    mat1 = [[1, 2, 3]]
    mat2 = [[4], [5], [6]]
    print(mat_mul(mat1, mat2))  # Output: [[32]]

    mat1 = [[1, 2]]
    mat2 = [[3, 4], [5, 6], [7, 8]]
    print(mat_mul(mat1, mat2))  # Output: None
