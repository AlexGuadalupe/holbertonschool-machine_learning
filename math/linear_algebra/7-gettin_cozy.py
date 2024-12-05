#!/usr/bin/env python3
"""
This module contains a function to concatenate
two 2D matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specific axis.

    Args:
        mat1 (list): A 2D list of ints/floats.
        mat2 (list): A 2D list of ints/floats.
        axis (int): The axis along which to concatenate
        (0 for rows, 1 for columns).

    Returns:
        list: A new 2D list with the concatenated matrices.
        None: If the two matrices cannot be concatenated.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None


if __name__ == "__main__":
    # Test cases
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[7, 8, 9], [10, 11, 12]]
    print(cat_matrices2D(mat1, mat2))
    # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(cat_matrices2D(mat1, mat2, axis=1))
    # Output: [[1, 2, 5, 6], [3, 4, 7, 8]]

    mat1 = [[1, 2, 3]]
    mat2 = [[4, 5, 6], [7, 8, 9]]
    print(cat_matrices2D(mat1, mat2))  # Output: None
