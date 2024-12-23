#!/usr/bin/env python3
"""
This module contains a function to calculate the transpose of a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list): A 2D list representing the matrix.

    Returns:
        list: A new 2D list representing the transposed matrix.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
