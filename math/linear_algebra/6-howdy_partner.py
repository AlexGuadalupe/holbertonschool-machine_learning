#!/usr/bin/env python3
"""
This module contains a function to concatenate two arrays.
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays.

    Args:
        arr1 (list): A list of ints/floats.
        arr2 (list): A list of ints/floats.

    Returns:
        list: A new list with the elements of arr1
        followed by the elements of arr2.
    """
    return arr1 + arr2


if __name__ == "__main__":
    # Test cases
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print(cat_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]

    arr1 = [1.5, 2.5]
    arr2 = [3.5, 4.5]
    print(cat_arrays(arr1, arr2))  # Output: [1.5, 2.5, 3.5, 4.5]
