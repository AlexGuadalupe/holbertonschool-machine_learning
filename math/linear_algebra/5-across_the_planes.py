#!/usr/bin/env python3
"""
This module contains a function to add two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list): A 2D list of ints/floats.
        mat2 (list): A 2D list of ints/floats.

    Returns:
        list: A new 2D list with the element-wise sum of mat1 and mat2.
        None: If mat1 and mat2 are not the same shape.
    """
    if len(mat1) != len(mat2) or any(
        len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)
    ):
        return None
    return [
        [elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
        for row1, row2 in zip(mat1, mat2)
    ]


if __name__ == "__main__":
    # Test cases
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[7, 8, 9], [10, 11, 12]]
    print(add_matrices2D(mat1, mat2))  # Output: [[8, 10, 12], [14, 16, 18]]

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6, 7], [8, 9, 10]]
    print(add_matrices2D(mat1, mat2))  # Output: None

    mat1 = [[1.5, 2.5], [3.5, 4.5]]
    mat2 = [[5.5, 6.5], [7.5, 8.5]]
    print(add_matrices2D(mat1, mat2))  # Output: [[7.0, 9.0], [11.0, 13.0]]
